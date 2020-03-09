"""
Interface utilisateur
"""

#import de la bibliothèque wx
#initialisation de l'interface graphique
#création de la fenêtre
#affichage de la fenêtre

import wx

class Menu(wx.Frame):
    def _init_(self) :
        super()._init_(parent=None, Title="Jeu du super-morpion")
        bouton1 = wx.Button(self, id=1000, label='X', pos=(30, 30), size=(50, 20))
        self.Bind(wx.EVT_BUTTON, self.OnBouton, bouton1)
    def _installer_menu_(self) :
        barre_Menu=wx.MenuBar()
        menu_fichier=wx.Menu
        article_quitter=menu.fichier.Append(wx.ID_EXIT, 'Quitter', 'Quitter le jeu')
        barre_menu.Append(menu_fichier, '&fichier')
        self.SetMenuBar(barre_menu)
        self.Bind(wx.EVT_Menu, self.OnQuit, article_quitter)
        
    def OnQuit(self, e) :
        print('aticle :', e.GetId() )
        print("Je quitte")
            
        self.Close()

if __name__ == '__main__' :
    app = wx.App()
    frame = wx.Frame(parent=None, title="Jeu du super-morpion")
    frame.Show()
    app.MainLoop()
