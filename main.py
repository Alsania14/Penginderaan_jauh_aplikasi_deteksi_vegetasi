from osgeo import gdal
from View.ChildMyFrame import ChildPanelUas
import wx

class MainApp(wx.App):
    def OnInit(self):
        Panel = ChildPanelUas(None)
        Panel.ChildInit()
        Panel.Show(True)
        return True


if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()