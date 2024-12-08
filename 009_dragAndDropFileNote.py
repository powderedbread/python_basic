# these are notes, not a program.
# add new custom frame class anywhere before the end if using a frame widget

class CustomFrame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.acceptProposedAction()

            urls = event.mimeData().urls()
            if urls:
                image_path = urls[0].toLocalFile()
                print(f"Image dropped: {image_path}")
        else:
            event.ignore()

# then replace this line if using a frame, whever and whatever its named 
self.frame_dropArea = QtWidgets.QFrame(self.centralwidget)
# with this line 
self.frame_dropArea = CustomFrame(self.centralwidget)
