import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Window")
        self.setGeometry(100, 100, 500, 500)

        # Create the menu bar and menu
        MM_menubar = self.menuBar()
        MM_file_menu = MM_menubar.addMenu("&File")

        # Create a Quit action
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        MM_file_menu.addAction(quit_action)

        # stylesheet for main window
        self.setStyleSheet("background-color: orange;")
        # stylesheet for  menu bar
        MM_menubar.setStyleSheet("""
            background-color: #303030;
            color: white;
        """)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
