from pyproj import Proj

from View.PanelUas import MyFrame
import wx
import tkinter as tk
from tkinter import filedialog
from osgeo import gdal_array
from osgeo import gdal
from PIL import Image
from View.PanelUas import AlertDialog
from bs4 import BeautifulSoup
import bs4
import os

# PATH
root_path = os.getcwd()
print("ROOT PATH : " + root_path)

helper_path = os.getcwd() + "\Helper"
print("HELPER PATH : " + helper_path)

storage_path = os.getcwd() + "\Storage"
print("STORAGE PATH : " + storage_path)

result_path = os.getcwd() + "\Result"
print("RESULT PATH : " + result_path)

temp_4 = "\\temp_band_4.tif"
temp_5 = "\\temp_band_5.tif"
temp_result_ndvi = "\\temp_result_ndvi.tif"
temp_mask = "\\temp_mask.tif"


class ChildPanelUas(MyFrame):
    TAG = "ChildPanelUas.class = "

    # ATRIBUTE INPUT
    file_path4 = None
    file_path5 = None
    array_band4 = None
    array_band5 = None
    image_band4 = None
    image_band5 = None
    gdal_band4 = None
    gdal_band5 = None
    # AKHIR

    # ATRIBUTE CROP
    long_start = None
    long_end = None
    lat_start = None
    lat_end = None
    image = None
    cols = None
    rows = None
    # ATRIBUTE CROP

    # PROSES LOAD FILE
    file_load_path = None
    load_doc = None
    # PROSES LOAD FILE

    # PROSES CREATE NDVI
    open_process = False
    process_finished = False
    image_ndvi = None
    image_mark = None
    temp_array_ndvi = None
    temp_array_mark = None
    # PROCES CREATE NDVI

    # PROSES SAVE
    file_path_png = None
    file_path_jpg = None
    file_path_tif = None

    # PROSES INPUT CITRA=======================================================
    def ChildInit(self):
        self.m_gridPerkiraanLuas.SetColLabelValue(0, "PIXEL")
        self.m_gridPerkiraanLuas.SetColLabelValue(1, "PERKIRAAN")
        self.m_gridPerkiraanLuas.SetCellValue(0, 0, "?")
        self.m_gridPerkiraanLuas.SetCellValue(0, 1, "?")

    def m_buttonBand4OnButtonClick(self, event):
        self.m_textCtrlBand4.Clear()
        root = tk.Tk()
        root.withdraw()
        self.file_path4 = filedialog.askopenfilename()
        self.array_band4 = gdal_array.LoadFile(self.file_path4)
        self.image_band4 = self.convertToImage(self.array_band4, True)
        self.gdal_band4 = gdal.Open(self.file_path4, gdal.GA_ReadOnly)
        #   MEMBERIKAN PATH KE TEXTCTRL BAND 4
        self.m_textCtrlBand4.SetValue(self.file_path4)

    def m_buttonBand5OnButtonClick(self, event):
        self.m_textCtrlBand5.Clear()
        root = tk.Tk()
        root.withdraw()
        self.file_path5 = filedialog.askopenfilename()
        self.array_band5 = gdal_array.LoadFile(self.file_path5)
        self.image_band5 = self.convertToImage(self.array_band5, True)
        self.gdal_band5 = gdal.Open(self.file_path5, gdal.GA_ReadOnly)
        #     MEMBERIKAN PATH KE TEXTCTRL BAND 5
        self.m_textCtrlBand5.SetValue(self.file_path5)

    def m_buttonOpenOnButtonClick(self, event):
        error = ""
        if self.image_band4 is None:
            error = error + "Tambahkan Band 4 \n"
        if self.image_band5 is None:
            error = error + "Tambahkan Band 5 \n"

        if error == "":
            self.m_bitmapBand4.SetBitmap(wx.Bitmap(self.image_band4))
            self.m_bitmapBand5.SetBitmap(wx.Bitmap(self.image_band5))

            driverTiff = gdal.GetDriverByName("GTiff")
            cloneImg = driverTiff.Create(storage_path + "\\temp_band_4.tif",
                                         self.gdal_band4.RasterXSize, self.gdal_band4.RasterYSize, 1,
                                         gdal.GDT_Float32)
            cloneImg.SetGeoTransform(self.gdal_band4.GetGeoTransform())
            cloneImg.SetProjection(self.gdal_band4.GetProjection())
            cloneImg.GetRasterBand(1).SetNoDataValue(255)
            cloneImg.GetRasterBand(1).WriteArray(self.array_band4)
            cloneImg = None

            driverTiff = gdal.GetDriverByName("GTiff")
            cloneImg = driverTiff.Create(storage_path + "\\temp_band_5.tif",
                                         self.gdal_band5.RasterXSize, self.gdal_band5.RasterYSize, 1,
                                         gdal.GDT_Float32)
            cloneImg.SetGeoTransform(self.gdal_band5.GetGeoTransform())
            cloneImg.SetProjection(self.gdal_band5.GetProjection())
            cloneImg.GetRasterBand(1).SetNoDataValue(255)
            cloneImg.GetRasterBand(1).WriteArray(self.array_band5)
            cloneImg = None

            self.m_staticTextTotalPixel4.SetLabelText(str(len(self.array_band4) * len(self.array_band4[0])))
            ukuran4 = str(len(self.array_band4)) + " X " + str(len(self.array_band4[0]))
            self.m_staticTextUkuran4.SetLabelText(ukuran4)

            self.m_staticTextTotalPixel5.SetLabelText(str(len(self.array_band5) * len(self.array_band5[0])))
            ukuran5 = str(len(self.array_band5)) + " X " + str(len(self.array_band5[0]))
            self.m_staticTextUkuran5.SetLabelText(ukuran5)

            self.open_process = True
            self.Refresh()
            self.Layout()
        else:
            alert = AlertDialog(None)
            alert.m_staticTextErrorMessage.SetLabelText(error)
            alert.Show()

    def m_buttonExecuteCropOnButtonClick(self, event):
        error = ""
        if self.image_band4 == None:
            error += "Tambahkan Band 4 !\n"
        if self.image_band5 == None:
            error += "Tambahkan Band 5 !\n"

        if error == "":
            self.CropCoordinate()
            self.array_band4 = self.CropImage(self.gdal_band4)
            self.array_band5 = self.CropImage(self.gdal_band5)

            self.image_band4 = self.convertToImage(self.array_band4, True)
            self.m_bitmapBand4.SetBitmap(wx.Bitmap(self.image_band4))

            self.image_band5 = self.convertToImage(self.array_band5, True)
            self.m_bitmapBand5.SetBitmap(wx.Bitmap(self.image_band5))

            driverTiff = gdal.GetDriverByName("GTiff")
            cloneImg = driverTiff.Create(storage_path + temp_4,
                                         len(self.array_band4[0]), len(self.array_band4), 1,
                                         gdal.GDT_Float32)
            cloneImg.SetGeoTransform(self.gdal_band4.GetGeoTransform())
            cloneImg.SetProjection(self.gdal_band4.GetProjection())
            cloneImg.GetRasterBand(1).SetNoDataValue(255)
            cloneImg.GetRasterBand(1).WriteArray(self.array_band4)
            cloneImg = None

            driverTiff = gdal.GetDriverByName("GTiff")
            cloneImg = driverTiff.Create(storage_path + temp_5,
                                         len(self.array_band5[0]), len(self.array_band5), 1,
                                         gdal.GDT_Float32)
            cloneImg.SetGeoTransform(self.gdal_band5.GetGeoTransform())
            cloneImg.SetProjection(self.gdal_band5.GetProjection())
            cloneImg.GetRasterBand(1).SetNoDataValue(255)
            cloneImg.GetRasterBand(1).WriteArray(self.array_band5)
            cloneImg = None

            self.m_staticTextTotalPixel4.SetLabelText(str(len(self.array_band4) * len(self.array_band4[0])))
            ukuran = str(len(self.array_band4)) + " X " + str(len(self.array_band4[0]))
            self.m_staticTextUkuran4.SetLabelText(ukuran)

            self.m_staticTextTotalPixel5.SetLabelText(str(len(self.array_band5) * len(self.array_band5[0])))
            ukuran5 = str(len(self.array_band5)) + " X " + str(len(self.array_band5[0]))
            self.m_staticTextUkuran5.SetLabelText(ukuran5)

            self.Refresh()
            self.Layout()
        else:
            alert = AlertDialog(None)
            alert.m_staticTextErrorMessage.SetLabelText(error)
            alert.Show()

    def m_buttonLoadCropOnButtonClick(self, event):
        root = tk.Tk()
        root.withdraw()
        self.file_load_path = filedialog.askopenfilename()
        if "sprm" not in self.file_load_path:
            print(self.TAG, "SALAH FILE")
            alert = AlertDialog(None)
            alert.m_staticTextErrorMessage.SetLabelText("FORMAT FILE SALAH\nRequired : .sprm")
            alert.Show()
        else:
            self.load_doc = open(self.file_load_path)
            soup = BeautifulSoup(self.load_doc, "xml")
            self.long_start = soup.find("OPTION", {"id": "XMIN"}).text
            self.long_end = soup.find("OPTION", {"id": "XMAX"}).text
            self.lat_start = soup.find("OPTION", {"id": "YMAX"}).text
            self.lat_end = soup.find("OPTION", {"id": "YMIN"}).text

            self.m_textCtrlLongStart.SetLabelText(self.long_start)
            self.m_textCtrlLongEnd.SetLabelText(self.long_end)
            self.m_textCtrlLatStart.SetLabelText(self.lat_start)
            self.m_textCtrlLatEnd.SetLabelText(self.lat_end)

    def m_buttonCreateNdviOnButtonClick(self, event):
        self.createNDVI()
        self.Refresh()
        self.Layout()

    def m_buttonPNGOnButtonClick(self, event):
        if self.process_finished:
            try:
                root = tk.Tk()
                root.withdraw()
                files = [('png', '.png')]
                self.file_path_png = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
                print(self.file_path_png.name)

                self.saveImage(self.file_path_png.name, "png")
            except:
                print(self.TAG, "ERROR")
        else:
            alert = AlertDialog(None)
            alert.m_staticTextErrorMessage.SetLabelText("Apa yang akan anda save ?")
            alert.Show()

    def m_buttonJPGOnButtonClick(self, event):
        if self.process_finished:
            try:
                root = tk.Tk()
                root.withdraw()
                files = [('jpg bos', '.jpg')]
                self.file_path_jpg = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
                print(self.file_path_jpg.name)

                self.saveImage(self.file_path_jpg.name, "jpg")
            except:
                print(self.TAG, "ERROR")
        else:
            alert = AlertDialog(None)
            alert.m_staticTextErrorMessage.SetLabelText("Apa yang akan anda save ?")
            alert.Show()

    def m_buttonTIFOnButtonClick(self, event):
        if self.process_finished:
            try :
                root = tk.Tk()
                root.withdraw()
                files = [('tif bos', '.tif')]
                self.file_path_tif = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
                print(self.file_path_tif.name)

                self.saveImage(self.file_path_tif.name, "tif")
            except:
                print(self.TAG,"ERROR")
        else:
            alert = AlertDialog(None)
            alert.m_staticTextErrorMessage.SetLabelText("Apa yang akan anda save ?")
            alert.Show()

    # PROSES DILUAR GUI ==============================================================================================

    # FUNGSI ARRAY 2 IMAGE
    def convertToImage(self, array, isfloat):
        if isfloat:
            rgb = array * 255
        else:
            rgb = array / 255
        pilImage = Image.fromarray(rgb).convert('RGB')
        image = wx.Image(pilImage.size[0], pilImage.size[1])
        image.SetData(pilImage.tobytes())
        H = image.GetHeight()
        W = image.GetWidth()
        newH = 250
        newW = 250
        if (W > H):
            newH = 250 * H / W
        else:
            newW = 250 * W / H
        image = image.Scale(newW, newH)
        return image

    # PROSES INPUT CITRA=======================================================

    # PROSES CROP COORDINATE
    def CropCoordinate(self):
        error = ""
        if self.m_textCtrlLongStart.GetValue() == "":
            error += "Tambahkan Longtitude Start \n"
        if self.m_textCtrlLongEnd.GetValue() == "":
            error += "Tambahkan Longtitude End \n"
        if self.m_textCtrlLatStart.GetValue() == "":
            error += "Tambahkan Latitude Start \n"
        if self.m_textCtrlLatEnd.GetValue() == "":
            error += "Tambahkan Latitude End \n"

        if error == "":
            self.long_start = self.m_textCtrlLongStart.GetValue()
            self.long_end = self.m_textCtrlLongEnd.GetValue()
            self.lat_start = self.m_textCtrlLatStart.GetValue()
            self.lat_end = self.m_textCtrlLatEnd.GetValue()

            print(self.TAG, "lonStart: ", self.long_start)
            print(self.TAG, "lonEnd: ", self.long_end)
            print(self.TAG, "latStart: ", self.lat_start)
            print(self.TAG, "latEnd: ", self.lat_end)
        else:
            alert = AlertDialog(None)
            alert.m_staticTextErrorMessage.SetLabelText(error)
            alert.Show()

    def CropImage(self, image):
        self.cols = image.RasterXSize
        self.rows = image.RasterYSize
        bands = image.RasterCount
        print("cols: ", self.cols, "\nrows: ", self.rows, "\nbands: ", bands)

        gt = image.GetGeoTransform()
        print("GeoTransform: ", gt)
        x0 = gt[0]
        y0 = gt[3]
        pwidth = gt[1]
        pheight = gt[5]
        x_end = self.cols * pwidth + x0
        y_end = self.cols * pheight + y0

        myProj = Proj("+proj=longlat +a=6378137 +rf=298.257223600004 +no_defs")
        lon, lat = myProj(x0, y0, inverse=True)
        x_utm, y_utm = myProj(lon, lat)
        print("lon: ", lon, "\nlat: ", lat)
        print("x_utm", x_utm, "\ny_utm", y_utm)

        x_mulai_crop_utm, y_mulai_crop_utm = myProj(
            self.long_start, self.lat_start)
        x_akhir_crop_utm, y_akhir_crop_utm = myProj(
            self.long_end, self.lat_end)
        print("x_mulai_crop_utm: ", x_mulai_crop_utm, "\ny_mulai_crop_utm: ", y_mulai_crop_utm, "\nx_akhir_crop_utm: ",
              x_akhir_crop_utm, "\ny_akhir_crop_utm: ", y_akhir_crop_utm)

        xoff = int((x_mulai_crop_utm - x0) / pwidth)
        yoff = int((y_mulai_crop_utm - y0) / pheight)
        print("xoff: ", xoff, "\nyoff: ", yoff)

        self.output_cols = int((x_akhir_crop_utm - x_mulai_crop_utm) / pwidth)
        self.output_rows = int((y_akhir_crop_utm - y_mulai_crop_utm) / pheight)

        print("output_cols: ", self.output_cols)
        print("output_rows: ", self.output_rows)

        band_image = image.GetRasterBand(1)

        crop_band = band_image.ReadAsArray(xoff, yoff, self.output_cols, self.output_rows)
        return crop_band

    def CreateImage(self, filename, image):
        driverTiff = gdal.GetDriverByName("GTiff")
        cloneImg = driverTiff.Create(storage_path + filename,
                                     image.RasterYSize, image.RasterXSize, 1,
                                     gdal.GDT_Float32)
        cloneImg.SetGeoTransform(image.GetGeoTransform())
        cloneImg.SetProjection(image.GetProjection())
        cloneImg.GetRasterBand(1).SetNoDataValue(255)
        cloneImg.GetRasterBand(1).WriteArray(self.crop_band)
        cloneImg = None

    def openImage(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, gdal.GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath = path
            self.image = openImage
            return True

    def createNDVI(self):
        error = ""
        if not self.open_process:
            error += "Mohon Selesaikan Form Persiapan !"

        if error != "":
            alert = AlertDialog(None)
            alert.m_staticTextErrorMessage.SetLabelText(error)
            alert.Show()
        else:
            os.chdir(helper_path)
            A = storage_path + temp_4
            B = storage_path + temp_5
            O = storage_path + temp_result_ndvi
            OM = storage_path + temp_mask

            command_ndvi = "gdal_calc.py -A \"" + A + "\" -B \"" + B + "\" --calc=(B-A)/(B+A) --outfile=\"" + O + "\" --overwrite"
            os.system(command_ndvi)
            self.image_ndvi = self.convertToImage(gdal_array.LoadFile(O), True)
            print(self.TAG, command_ndvi)

            command_threshold = "gdal_calc.py -A \"" + O + "\" --calc=\"A>=0.65\" --outfile=\"" + OM + "\" --overwrite"
            os.system(command_threshold)
            self.image_mark = self.convertToImage(gdal_array.LoadFile(OM), True)
            print(self.TAG, command_threshold)

            self.areaCounter(gdal_array.LoadFile(OM))

            self.temp_array_ndvi = gdal_array.LoadFile(O)
            image_ndvi = self.convertToImage(self.temp_array_ndvi, True)
            self.m_bitmapNdvi.SetBitmap(wx.Bitmap(image_ndvi))

            self.temp_array_mark = gdal_array.LoadFile(OM)
            image_mangrove = self.convertToImage(self.temp_array_mark, True)
            self.m_bitmapMangrove.SetBitmap(wx.Bitmap(image_mangrove))

            self.process_finished = True

    def areaCounter(self, rasterArray):
        xSize = len(rasterArray)
        ySize = len(rasterArray[0])
        tot = 0
        zero = 0
        one = 0
        for x in range(xSize):
            for y in range(ySize):
                if rasterArray[x][y] == 0:
                    zero += 1
                elif rasterArray[x][y] == 1:
                    one += 1
                tot += 1

        self.m_gridPerkiraanLuas.SetCellValue(0, 0, str(one))
        self.m_gridPerkiraanLuas.SetCellValue(0, 1, (str(one * 900 / 10000) + " HA"))

        print(self.TAG, "total cell zero : ", zero, "\ntotal cell one : ", one, "\n Total Meter Persegi :", one * 900)

    def saveImage(self, filename, type):
        if self.process_finished:
            if type == "tif":
                if ".tif" not in filename:
                    filename += ".tif"

                driverTiff = gdal.GetDriverByName("GTiff")
                cloneImg = driverTiff.Create(filename,
                                             len(self.temp_array_ndvi[0]), len(self.temp_array_ndvi), 1,
                                             gdal.GDT_Float32)
                cloneImg.SetGeoTransform(self.gdal_band5.GetGeoTransform())
                cloneImg.SetProjection(self.gdal_band5.GetProjection())
                cloneImg.GetRasterBand(1).SetNoDataValue(255)
                cloneImg.GetRasterBand(1).WriteArray(self.temp_array_ndvi)
                cloneImg = None

            elif type == "jpg":
                if ".jpg" not in filename:
                    filename += ".jpg"

                ndvi_save = Image.fromarray(self.temp_array_ndvi * 255).convert("RGB")
                ndvi_save.save(filename, format="jpeg")

            elif type == "png":
                if ".png" not in filename:
                    filename += ".png"

                ndvi_save = Image.fromarray(self.temp_array_ndvi * 255).convert("RGB")
                ndvi_save.save(filename, format="png")

        alert = AlertDialog(None)
        alert.SetTitle("Sukses Menyimpan")
        alert.m_staticTextErrorMessage.SetLabelText("IMAGE BERHASIL DISIMPAN")
        alert.Show()
