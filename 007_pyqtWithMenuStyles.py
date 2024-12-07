
# type  "pip install pyqt"  
# in a terminal to use modules
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("pb_qt")
        # start-x, start-y, width, height
        self.setGeometry(100, 100, 500, 500)

        #main menu bar
        MM_menubar = self.menuBar()
        MM_file_menu = MM_menubar.addMenu("&File")

        # add quit
        MM_file_menu_quit = QAction("Quit", self)
        MM_file_menu_quit.triggered.connect(self.close)
        MM_file_menu.addAction(MM_file_menu_quit)
        
        #style for main window
        self.setStyleSheet("background-color: #34414e;")

        #stylesheet menubar
        MM_menubar.setStyleSheet(
            """ 
            /* menu bar */ 
            QMenuBar {
            background-color: #303030;
            }

            /* top level menu items */
            QMenuBar::item {
            color : white;
            margin-top:0px;
            spacing: 0px;
            padding: 5px 5px;  
            background-color: transparent;
            border-radius: 0px;
            }
            
            /* Top-level menu items hover */
            QMenuBar::item:selected { 
            background-color: #707070;
            }
            
            /* sub menu items regular */
            QMenu{ 
            background-color: #303030;
            color:#ffffff;
            margin: 0px
            }
            
            /* sub menu items hover */
            QMenu::item:selected { 
            background-color: #707070;
           
            
            
            }
            
        """)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
