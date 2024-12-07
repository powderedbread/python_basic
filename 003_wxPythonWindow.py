# to use wx modules
# type in terminal: pip install wxpython

import wx

class MyApp(wx.App):
    def OnInit(self):
        # Create the main window (frame) with a title and size
        self.mainFrame = wx.Frame(None, title="Basic wxPython Window", size=(500, 500))
        
        mainPanel = wx.Panel(self.mainFrame)
        mainPanel.SetBackgroundColour(wx.Colour(255, 165, 0))

        # Show the window
        self.mainFrame.Show(True)
        return True

# Run the wxPython application
if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
