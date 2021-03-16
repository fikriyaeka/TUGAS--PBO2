# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class FrameTugas
###########################################################################

class FrameTugas ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 648,443 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		wSizer1 = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.text_hello = wx.StaticText( self, wx.ID_ANY, u"\"HELLO WX\"", wx.DefaultPosition, wx.Size( 180,50 ), 0 )
		self.text_hello.Wrap( -1 )

		self.text_hello.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Century751 No2 BT" ) )

		wSizer1.Add( self.text_hello, 0, wx.ALL, 5 )

		self.text_nama = wx.StaticText( self, wx.ID_ANY, u"NAMA : FIKRIYA EKA WAHYUNI", wx.Point( 20,20 ), wx.DefaultSize, 0 )
		self.text_nama.Wrap( -1 )

		self.text_nama.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.text_nama.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		wSizer1.Add( self.text_nama, 0, wx.ALL, 5 )

		self.text_nim = wx.StaticText( self, wx.ID_ANY, u"NIM      : 192410101003", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_nim.Wrap( -1 )

		self.text_nim.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.text_nim.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		wSizer1.Add( self.text_nim, 0, wx.ALL, 5 )

		self.icon = wx.adv.AnimationCtrl( self, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.Size( 180,180 ), wx.adv.AC_DEFAULT_STYLE )

		self.icon.SetInactiveBitmap( wx.Bitmap( u"Maskot BITS.png", wx.BITMAP_TYPE_ANY ) )
		self.icon.Play()
		wSizer1.Add( self.icon, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Ayo Daftar BITS 2021 ya kawan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )
		self.m_checkBox2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		wSizer1.Add( self.m_checkBox2, 0, wx.ALL, 5 )


		self.SetSizer( wSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


