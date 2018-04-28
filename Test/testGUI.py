import wx

app = wx.App()
window = wx.Frame(None, title="wxPython Frame", size=(300,200))
window.Center()
panel=wx.Panel(window)
label=wx.StaticText(panel, label="Hello World", pos=(100,50))
button = wx.Button(panel, label = "Press Me")
window.Show(True)
app.MainLoop()