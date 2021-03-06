# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview
import wx.richtext

###########################################################################
## Class AppConfiguration
###########################################################################

class AppConfiguration ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MSD Configuration", pos = wx.DefaultPosition, size = wx.Size( 523,872 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 219, 237, 255 ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_Title = wx.StaticText( self, wx.ID_ANY, u"MSD Config params", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_Title.Wrap( -1 )
		self.m_Title.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_Title, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer1.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Data Filename (eg AllROI-D.txt)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer1.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl15, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"MSD Filename (eg AllROI-MSD.txt)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer1.Add( self.m_staticText19, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl16, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Histogram Filename (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Filtered Filename (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Filtered MSD (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, u"All Statistics Filename (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )
		fgSizer1.Add( self.m_staticText181, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl161 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl161, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Avg MSD Filename (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer1.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl18, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"MSD points", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer1.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Time Interval", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer1.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"D column label (exact match)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer1.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Log column label (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer1.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Min limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer1.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Max limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer1.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Binwidth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl12, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Mobile Threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer1.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl13, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Group 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_tcGroup1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_tcGroup1, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Group 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer1.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_tcGroup2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_tcGroup2, 0, wx.ALL, 5 )
		
		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnSave, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnSave.Bind( wx.EVT_BUTTON, self.OnSaveConfig )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSaveConfig( self, event ):
		event.Skip()
	

###########################################################################
## Class StatsDialog
###########################################################################

class StatsDialog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"MSD Statistics: t-tests", pos = wx.DefaultPosition, size = wx.Size( 500,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 247, 247, 247 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Comparison of Group Statistics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetFont( wx.Font( 12, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText18, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Group 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer2.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_textCtrlGp1 = wx.TextCtrl( self, wx.ID_ANY, u"STIM", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlGp1, 0, wx.ALL, 5 )
		
		self.m_tcRatioFile1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.m_tcRatioFile1, 0, wx.ALL, 5 )
		
		self.m_btnGp1 = wx.Button( self, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_btnGp1, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Group 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer2.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_textCtrlGp2 = wx.TextCtrl( self, wx.ID_ANY, u"NOSTIM", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		fgSizer2.Add( self.m_textCtrlGp2, 0, wx.ALL, 5 )
		
		self.m_tcRatioFile2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.m_tcRatioFile2, 0, wx.ALL, 5 )
		
		self.m_btnGp2 = wx.Button( self, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_btnGp2, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_tcResults = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,100 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP|wx.SIMPLE_BORDER|wx.VSCROLL )
		bSizer2.Add( self.m_tcResults, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_btnRatioRun = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_btnRatioRun, 0, wx.ALL, 5 )
		
		self.m_btnRatioClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_btnRatioClose, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.ALL|wx.RIGHT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_btnRatioClose.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class ConfigPanel
###########################################################################

class ConfigPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.VERTICAL )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_Title = wx.StaticText( self, wx.ID_ANY, u"Configuration", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_Title.Wrap( -1 )
		self.m_Title.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		fgSizer1.Add( self.m_Title, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.m_status = wx.StaticText( self, wx.ID_ANY, u"Settings for processing scripts", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_status.Wrap( -1 )
		self.m_status.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_status, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Data Filename (eg AllROI-D.txt)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer1.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl15, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"MSD Filename (eg AllROI-MSD.txt)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		fgSizer1.Add( self.m_staticText19, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl16, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Histogram Filename (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Filtered Filename (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Filtered MSD (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, u"All Statistics Filename (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )
		fgSizer1.Add( self.m_staticText181, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl161 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl161, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Avg MSD Filename (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer1.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_textCtrl18, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"MSD points", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		fgSizer1.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Time Interval", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer1.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"D column label (exact match)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer1.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Log column label (generated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer1.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Min limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer1.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Max limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer1.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Binwidth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl12, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Mobile Threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer1.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl13, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Group 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_tcGroup1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_tcGroup1, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Group 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer1.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_tcGroup2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_tcGroup2, 0, wx.ALL, 5 )
		
		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Cell ID (number of subfolders)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		fgSizer1.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.m_tcCellid = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_tcCellid, 0, wx.ALL, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnLoadConfig = wx.Button( self, wx.ID_ANY, u"Load From File", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.btnLoadConfig, 0, wx.ALL, 5 )
		
		self.btnSave = wx.Button( self, wx.ID_ANY, u"Save Changes", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.btnSave, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer22, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		fgSizer1.Fit( self )
		
		# Connect Events
		self.btnLoadConfig.Bind( wx.EVT_BUTTON, self.OnLoadConfig )
		self.btnSave.Bind( wx.EVT_BUTTON, self.OnSaveConfig )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnLoadConfig( self, event ):
		event.Skip()
	
	def OnSaveConfig( self, event ):
		event.Skip()
	

###########################################################################
## Class ProcessPanel
###########################################################################

class ProcessPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 508,919 ), style = wx.TAB_TRAVERSAL )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, u"Run Selected Processes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )
		self.m_staticText85.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer19.Add( self.m_staticText85, 0, wx.ALL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer19.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_checkListProcessChoices = [ u"None", u"QSM", u"Atlas" ]
		self.m_checkListProcess = wx.RadioBox( self, wx.ID_ANY, u"Processing options", wx.DefaultPosition, wx.DefaultSize, m_checkListProcessChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_checkListProcess.SetSelection( 0 )
		bSizer20.Add( self.m_checkListProcess, 0, wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_stTitle = wx.StaticText( self, wx.ID_ANY, u"TITLE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_stTitle.Wrap( -1 )
		self.m_stTitle.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		
		bSizer15.Add( self.m_stTitle, 0, wx.ALL, 5 )
		
		self.m_stDescription = wx.StaticText( self, wx.ID_ANY, u"Process Description", wx.DefaultPosition, wx.Size( -1,80 ), 0|wx.FULL_REPAINT_ON_RESIZE|wx.VSCROLL )
		self.m_stDescription.Wrap( -1 )
		self.m_stDescription.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		bSizer15.Add( self.m_stDescription, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_btnRunProcess = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnRunProcess.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.m_btnRunProcess.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer16.Add( self.m_btnRunProcess, 0, wx.ALL, 5 )
		
		self.m_btnStopProcess = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnStopProcess.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.m_btnStopProcess.Enable( False )
		
		bSizer16.Add( self.m_btnStopProcess, 0, wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer16, 1, wx.ALIGN_BOTTOM, 5 )
		
		
		bSizer20.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_dataViewListCtrlRunning = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_ROW_LINES|wx.FULL_REPAINT_ON_RESIZE|wx.VSCROLL )
		self.m_dataViewListCtrlRunning.SetMinSize( wx.Size( -1,400 ) )
		
		self.m_dataViewListColumnProcess = self.m_dataViewListCtrlRunning.AppendTextColumn( u"Process" )
		self.m_dataViewListColumnSeries = self.m_dataViewListCtrlRunning.AppendTextColumn( u"Series ID" )
		self.m_dataViewListColumnStatus = self.m_dataViewListCtrlRunning.AppendProgressColumn( u"Status" )
		self.m_dataViewListColumnOutput = self.m_dataViewListCtrlRunning.AppendTextColumn( u"Output" )
		bSizer21.Add( self.m_dataViewListCtrlRunning, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		self.m_stOutputlog = wx.StaticText( self, wx.ID_ANY, u"View processing output in log file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_stOutputlog.Wrap( -1 )
		bSizer19.Add( self.m_stOutputlog, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer19 )
		self.Layout()
		
		# Connect Events
		self.m_checkListProcess.Bind( wx.EVT_RADIOBOX, self.OnShowDescription )
		self.m_btnRunProcess.Bind( wx.EVT_BUTTON, self.OnRunScripts )
		self.m_btnStopProcess.Bind( wx.EVT_BUTTON, self.OnCancelScripts )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnShowDescription( self, event ):
		event.Skip()
	
	def OnRunScripts( self, event ):
		event.Skip()
	
	def OnCancelScripts( self, event ):
		event.Skip()
	

###########################################################################
## Class ComparePanel
###########################################################################

class ComparePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Cloud Processing Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer1.Add( self.m_staticText18, 0, wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND, 5 )
		
		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Click update to refresh status of files processing in the cloud", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText58.Wrap( 650 )
		self.m_staticText58.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_staticText58, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_tcResults = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,400 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP|wx.SIMPLE_BORDER|wx.VSCROLL )
		bSizer1.Add( self.m_tcResults, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_btnCompareRun = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_btnCompareRun.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.m_btnCompareRun.SetBackgroundColour( wx.Colour( 0, 128, 64 ) )
		
		bSizer1.Add( self.m_btnCompareRun, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_btnCompareRun.Bind( wx.EVT_BUTTON, self.OnCompareRun )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCompareRun( self, event ):
		event.Skip()
	

###########################################################################
## Class WelcomePanel
###########################################################################

class WelcomePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Clinic 2 Cloud", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		self.m_staticText23.SetFont( wx.Font( 14, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		bSizer18.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer18.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.NO_BORDER|wx.VSCROLL|wx.WANTS_CHARS, wx.DefaultValidator, u"welcome" )
		bSizer18.Add( self.m_richText1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer18 )
		self.Layout()
		bSizer18.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class FilesPanel
###########################################################################

class FilesPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.TAB_TRAVERSAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Select Folder for analysis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		self.m_staticText23.SetFont( wx.Font( 14, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		bSizer5.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Browse and/or Drag N Drop to select folder containing patient DICOM files then click select the required series. ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		
		bSizer5.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Patient DICOM directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer4.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.txtInputdir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer4.Add( self.txtInputdir, 0, wx.ALL, 5 )
		
		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button18, 0, wx.ALL, 5 )
		
		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Upload directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )
		fgSizer4.Add( self.m_staticText56, 0, wx.ALL, 5 )
		
		self.txtOutputdir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer4.Add( self.txtOutputdir, 0, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button16, 0, wx.ALL, 5 )
		
		self.m_cbSelectall = wx.CheckBox( self, wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cbSelectall.SetValue(True) 
		fgSizer4.Add( self.m_cbSelectall, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_tcDragdrop = wx.TextCtrl( self, wx.ID_ANY, u"Drag data folder here !", wx.DefaultPosition, wx.Size( 200,100 ), wx.TE_CENTRE|wx.TE_READONLY )
		self.m_tcDragdrop.SetBackgroundColour( wx.Colour( 191, 191, 255 ) )
		
		fgSizer4.Add( self.m_tcDragdrop, 0, wx.ALIGN_CENTER, 5 )
		
		self.btnClearlist = wx.Button( self, wx.ID_ANY, u"Clear List", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnClearlist, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer5.Add( fgSizer4, 1, wx.ALIGN_TOP|wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.dataview.DV_MULTIPLE|wx.HSCROLL|wx.VSCROLL )
		self.m_dataViewListCtrl1.SetMinSize( wx.Size( -1,300 ) )
		
		self.col_selected = self.m_dataViewListCtrl1.AppendToggleColumn( u"Select" )
		self.col_patient = self.m_dataViewListCtrl1.AppendTextColumn( u"PatientID" )
		self.col_sequence = self.m_dataViewListCtrl1.AppendTextColumn( u"Sequence" )
		self.col_protocol = self.m_dataViewListCtrl1.AppendTextColumn( u"Protocol" )
		self.col_imagetype = self.m_dataViewListCtrl1.AppendTextColumn( u"Image Type" )
		self.col_num = self.m_dataViewListCtrl1.AppendTextColumn( u"Num Files" )
		self.col_series = self.m_dataViewListCtrl1.AppendTextColumn( u"Series ID" )
		bSizer18.Add( self.m_dataViewListCtrl1, 0, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		self.m_status = wx.StaticText( self, wx.ID_ANY, u"Select required files then go to Run Processes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_status.Wrap( -1 )
		bSizer18.Add( self.m_status, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		# Connect Events
		self.m_button18.Bind( wx.EVT_BUTTON, self.OnInputdir )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnOutputdir )
		self.m_cbSelectall.Bind( wx.EVT_CHECKBOX, self.OnSelectall )
		self.btnClearlist.Bind( wx.EVT_BUTTON, self.OnClearlist )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnInputdir( self, event ):
		event.Skip()
	
	def OnOutputdir( self, event ):
		event.Skip()
	
	def OnSelectall( self, event ):
		event.Skip()
	
	def OnClearlist( self, event ):
		event.Skip()
	

