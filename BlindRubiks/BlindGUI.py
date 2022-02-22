import wx
import Blind


newCube = Blind.Cube([[i,i,i,i,i,i,i,i,i] for i in range (6)])
scramble = newCube.randomScramble()
colorPattern = {0 : 'white', 1 : 'yellow', 2 : 'red', 3 : '#ff8000', 4 : 'green', 5 : 'blue' }
class Mywindow(wx.Frame):

    def __init__(self, parent, title):
      super(Mywindow, self).__init__(parent, title = title,size = (300,500))
      self.InitUI()
      self.Center()
      self.timerRunning = False

    def InitUI(self):

      menubar = wx.MenuBar()
      menu = wx.Menu()
      menu.Append(wx.ID_EXIT, "&Quit")
      menu.Append(wx.ID_ABOUT, "&About")
      self.tglNmode = menu.Append(wx.ID_ANY, "Toggle &Night Mode", kind = wx.ITEM_CHECK)
      menubar.Append(menu, "&Menu")
      self.panel = wx.Panel(self)
      vbox = wx.BoxSizer(wx.VERTICAL)
      scrambleText = wx.StaticText(self.panel, label= 'Scramble')
      global scrambleDisplay
      scrambleDisplay = wx.StaticText(self.panel, label=scramble)
      scrambleButton = wx.Button(self.panel, label = 'Scramble !')
      vbox.Add(scrambleText, flag = wx.ALL, border = 5)
      vbox.Add(scrambleDisplay, flag = wx.ALL, border = 5)
      vbox.Add(scrambleButton, flag = wx.ALL, border = 5)
      self.panel.SetSizer(vbox)


      self.SetMenuBar(menubar)
      self.Bind(wx.EVT_BUTTON, self.OnScramble, scrambleButton)
      self.Bind(wx.EVT_MENU, self.ToggleNightMode, self.tglNmode)
      self.panel.Bind(wx.EVT_PAINT, self.OnPaint)

      self.Centre()
      self.Show(True)
    def ToggleNightMode(self, e):
        if self.tglNmode.IsChecked():
            self.SetBackgroundColour("black")
        else :
            self.SetBackgroundColour((0,25,255))

    def OnPaint(self,e):
      def drawFace(face , x0 , y0 , sizeSquare=30):
          i=0
          for k in range (len(face)):
              dc.SetBrush(wx.Brush(colorPattern[face[i]]))
              y = sizeSquare * (i // 3)
              x = sizeSquare * (i % 3)
              dc.DrawRectangle( x0 + x, y0 + y, sizeSquare, sizeSquare)
              i += 1
    
      def drawCube (cube, sizeSquare = 30):
          sizeFace = sizeSquare*3
          drawFace(cube.u, sizeFace, 0, sizeSquare)
          drawFace(cube.f, sizeFace, sizeFace, sizeSquare)
          drawFace(cube.l, 0, sizeFace, sizeSquare)
          drawFace(cube.r, sizeFace*2, sizeFace, sizeSquare)
          drawFace(cube.d, sizeFace, sizeFace*2, sizeSquare)
          drawFace(cube.b, sizeFace, sizeFace*3.5, sizeSquare)
      dc = wx.PaintDC(self.panel)
      brush = wx.Brush("white")
      dc.SetBackground(brush)
      dc.Clear()
      drawCube(newCube)

    def OnScramble(self, e):
      print("scramble")
      newScramb = newCube.randomScramble()
      scrambleDisplay.SetLabel(newScramb)
      self.Refresh()

ex = wx.App()
Mywindow(None,"Rubik's Cube")
ex.MainLoop()
