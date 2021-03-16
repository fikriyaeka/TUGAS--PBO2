import wx
from noname import FrameTugas

class tampilan(FrameTugas):
    def __init__(self, parent):
        FrameTugas.__init__(self, parent)

app = wx.App()
frame = tampilan(parent=None)
frame.Show()
app.MainLoop()