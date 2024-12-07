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

        # Create the custom button on the right side of the menu bar
        button_widget = QWidget(self)
        button_layout = QHBoxLayout(button_widget)

        # Set the layout's margin to 0
        button_layout.setContentsMargins(0, 0, 0, 0)

        # Create the button
        button = QPushButton(self)
        button.setFixedSize(50, 50)  # Set button size to 50x50 pixels
        button.setStyleSheet("background-color: #707070; border: none")  # Remove button border and padding
        button.clicked.connect(self.on_button_click)

        # Add button to the layout and the menu bar
        button_layout.addWidget(button)
        MM_menubar.setCornerWidget(button_widget)

        #stylesheet for main window
        self.setStyleSheet("background-color: orange;")
        # Set the style of the menu bar
        MM_menubar.setStyleSheet("""
            background-color: #303030;
            color: white;
        """)

        self.show()

    @pyqtSlot()
    def on_button_click(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
