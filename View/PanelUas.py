# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Penginderaan Jauh", pos = wx.DefaultPosition, size = wx.Size( 918,735 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"PENGINDERAAN JAUH", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetFont( wx.Font( 20, 71, 93, 92, False, wx.EmptyString ) )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer1.Add( self.m_staticText18, 0, wx.EXPAND, 0 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"INPUT" ), wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"BAND 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer7.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrlBand4 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrlBand4, 1, wx.ALL, 5 )
		
		self.m_buttonBand4 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_buttonBand4, 0, 0, 5 )
		
		
		sbSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText21 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"BAND 5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer71.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_textCtrlBand5 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_textCtrlBand5, 1, wx.ALL, 5 )
		
		self.m_buttonBand5 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_buttonBand5, 0, 0, 5 )
		
		
		sbSizer1.Add( bSizer71, 0, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonOpen = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"OPEN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_buttonOpen, 1, 0, 5 )
		
		
		sbSizer1.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		self.m_staticText211 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"BAND INFO", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		sbSizer1.Add( self.m_staticText211, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticTextNoData = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"BAND 4", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticTextNoData.Wrap( -1 )
		self.m_staticTextNoData.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer34.Add( self.m_staticTextNoData, 0, wx.EXPAND, 5 )
		
		self.m_staticTextNoDataVAlue = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextNoDataVAlue.Wrap( -1 )
		bSizer34.Add( self.m_staticTextNoDataVAlue, 0, wx.ALL, 5 )
		
		self.m_staticTextMin = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"TOTAL PIXEL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMin.Wrap( -1 )
		self.m_staticTextMin.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer34.Add( self.m_staticTextMin, 0, wx.EXPAND, 5 )
		
		self.m_staticTextTotalPixel4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextTotalPixel4.Wrap( -1 )
		bSizer34.Add( self.m_staticTextTotalPixel4, 0, wx.ALL, 5 )
		
		self.m_staticTextMax = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"UKURAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMax.Wrap( -1 )
		self.m_staticTextMax.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer34.Add( self.m_staticTextMax, 0, wx.EXPAND, 5 )
		
		self.m_staticTextUkuran4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUkuran4.Wrap( -1 )
		bSizer34.Add( self.m_staticTextUkuran4, 0, wx.ALL, 5 )
		
		
		bSizer33.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"BAND 5", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer35.Add( self.m_staticText15, 0, wx.EXPAND, 5 )
		
		self.m_staticText181 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )
		bSizer35.Add( self.m_staticText181, 0, wx.ALL, 5 )
		
		self.m_staticText191 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"TOTAL PIXEL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )
		self.m_staticText191.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer35.Add( self.m_staticText191, 0, wx.EXPAND, 5 )
		
		self.m_staticTextTotalPixel5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextTotalPixel5.Wrap( -1 )
		bSizer35.Add( self.m_staticTextTotalPixel5, 0, wx.ALL, 5 )
		
		self.m_staticText212 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"UKURAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		self.m_staticText212.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer35.Add( self.m_staticText212, 0, wx.EXPAND, 5 )
		
		self.m_staticTextUkuran5 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUkuran5.Wrap( -1 )
		bSizer35.Add( self.m_staticTextUkuran5, 0, wx.ALL, 5 )
		
		
		bSizer33.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		
		sbSizer1.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"BAND 4" ), wx.VERTICAL )
		
		self.m_bitmapBand4 = wx.StaticBitmap( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_bitmapBand4, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer4.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"BAND 5" ), wx.VERTICAL )
		
		self.m_bitmapBand5 = wx.StaticBitmap( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.m_bitmapBand5, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer4.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"CROP IMAGE" ), wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextCropLongStart = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Longtitude Start ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCropLongStart.Wrap( -1 )
		bSizer18.Add( self.m_staticTextCropLongStart, 0, wx.ALL, 5 )
		
		self.m_textCtrlLongStart = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_textCtrlLongStart, 1, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer18, 0, wx.EXPAND, 5 )
		
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextCropLongStart1 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Longtitude End  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCropLongStart1.Wrap( -1 )
		bSizer181.Add( self.m_staticTextCropLongStart1, 0, wx.ALL, 5 )
		
		self.m_textCtrlLongEnd = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.m_textCtrlLongEnd, 1, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer181, 0, wx.EXPAND, 5 )
		
		bSizer182 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextCropLongStart2 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Latitude Start     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCropLongStart2.Wrap( -1 )
		bSizer182.Add( self.m_staticTextCropLongStart2, 0, wx.ALL, 5 )
		
		self.m_textCtrlLatStart = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer182.Add( self.m_textCtrlLatStart, 1, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer182, 0, wx.EXPAND, 5 )
		
		bSizer183 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticTextCropLongStart3 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Latitude End      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextCropLongStart3.Wrap( -1 )
		bSizer183.Add( self.m_staticTextCropLongStart3, 0, wx.ALL, 5 )
		
		self.m_textCtrlLatEnd = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer183.Add( self.m_textCtrlLatEnd, 1, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer183, 0, wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonLoadCrop = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"LOAD SPRM", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_buttonLoadCrop, 1, 0, 5 )
		
		self.m_buttonExecuteCrop = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"CROP", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_buttonExecuteCrop, 1, 0, 5 )
		
		
		bSizer16.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_buttonCreateNdvi = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"CREATE NDVI", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_buttonCreateNdvi, 1, wx.EXPAND, 5 )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"SAVE AS" ), wx.HORIZONTAL )
		
		self.m_buttonPNG = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"PNG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonPNG.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_buttonPNG.SetBackgroundColour( wx.Colour( 184, 63, 63 ) )
		
		sbSizer10.Add( self.m_buttonPNG, 1, wx.ALL, 5 )
		
		self.m_buttonJPG = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"JPG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonJPG.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_buttonJPG.SetBackgroundColour( wx.Colour( 73, 193, 64 ) )
		
		sbSizer10.Add( self.m_buttonJPG, 1, wx.ALL, 5 )
		
		self.m_buttonTIF = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"TIF", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonTIF.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_buttonTIF.SetBackgroundColour( wx.Colour( 147, 85, 83 ) )
		
		sbSizer10.Add( self.m_buttonTIF, 1, wx.ALL, 5 )
		
		
		bSizer20.Add( sbSizer10, 1, wx.EXPAND, 5 )
		
		
		bSizer16.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		
		sbSizer8.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NDVI" ), wx.VERTICAL )
		
		self.m_bitmapNdvi = wx.StaticBitmap( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer51.Add( self.m_bitmapNdvi, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer22.Add( sbSizer51, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"MANGROVE" ), wx.VERTICAL )
		
		self.m_bitmapMangrove = wx.StaticBitmap( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer6.Add( self.m_bitmapMangrove, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer22.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer17.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"PERKIRAAN LUAS" ), wx.VERTICAL )
		
		self.m_gridPerkiraanLuas = wx.grid.Grid( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridPerkiraanLuas.CreateGrid( 1, 2 )
		self.m_gridPerkiraanLuas.EnableEditing( True )
		self.m_gridPerkiraanLuas.EnableGridLines( True )
		self.m_gridPerkiraanLuas.EnableDragGridSize( False )
		self.m_gridPerkiraanLuas.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridPerkiraanLuas.EnableDragColMove( False )
		self.m_gridPerkiraanLuas.EnableDragColSize( True )
		self.m_gridPerkiraanLuas.SetColLabelSize( 30 )
		self.m_gridPerkiraanLuas.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridPerkiraanLuas.EnableDragRowSize( True )
		self.m_gridPerkiraanLuas.SetRowLabelSize( 80 )
		self.m_gridPerkiraanLuas.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridPerkiraanLuas.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_gridPerkiraanLuas.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		
		sbSizer11.Add( self.m_gridPerkiraanLuas, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer17.Add( sbSizer11, 0, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"ALSANIA", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer1.Add( self.m_staticText19, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_buttonBand4.Bind( wx.EVT_BUTTON, self.m_buttonBand4OnButtonClick )
		self.m_buttonBand5.Bind( wx.EVT_BUTTON, self.m_buttonBand5OnButtonClick )
		self.m_buttonOpen.Bind( wx.EVT_BUTTON, self.m_buttonOpenOnButtonClick )
		self.m_buttonLoadCrop.Bind( wx.EVT_BUTTON, self.m_buttonLoadCropOnButtonClick )
		self.m_buttonExecuteCrop.Bind( wx.EVT_BUTTON, self.m_buttonExecuteCropOnButtonClick )
		self.m_buttonCreateNdvi.Bind( wx.EVT_BUTTON, self.m_buttonCreateNdviOnButtonClick )
		self.m_buttonPNG.Bind( wx.EVT_BUTTON, self.m_buttonPNGOnButtonClick )
		self.m_buttonJPG.Bind( wx.EVT_BUTTON, self.m_buttonJPGOnButtonClick )
		self.m_buttonTIF.Bind( wx.EVT_BUTTON, self.m_buttonTIFOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_buttonBand4OnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonBand5OnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonOpenOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonLoadCropOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonExecuteCropOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonCreateNdviOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonPNGOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonJPGOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonTIFOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class AlertDialog
###########################################################################

class AlertDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ERROR ?", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14.SetMinSize( wx.Size( 200,100 ) ) 
		self.m_staticTextErrorMessage = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.m_staticTextErrorMessage.Wrap( -1 )
		bSizer14.Add( self.m_staticTextErrorMessage, 1, wx.EXPAND, 5 )
		
		self.m_buttonAlertDialogBtn = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_buttonAlertDialogBtn, 0, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer13 )
		self.Layout()
		bSizer13.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.AlertDialog )
		self.m_buttonAlertDialogBtn.Bind( wx.EVT_BUTTON, self.m_buttonAlertDialogBtnOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def AlertDialog( self, event ):
		event.Skip()
	
	def m_buttonAlertDialogBtnOnButtonClick( self, event ):
		event.Skip()
	

