from PyQt6.QtWidgets import QMainWindow, QApplication,QFileDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PIL import Image, ImageFilter
from ui import Ui_MainWindow
import os

app = QApplication([])
win = QMainWindow()
ui = Ui_MainWindow()

ui.setupUi(win)

workdir = ""
extensions = [".png", ".jpg", ".jpeg", ".bmp", ".gif"]

def filter(files: list[str]):
    filtered_files = []

    for fole in files:
        for ext in extensions:
            if fole.endswith(ext):
                filtered_files.append(fole)
    return filtered_files

def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files_list = os.listdir(workdir)

    files_list = filter(files_list)

    ui.files_list.addItems(files_list)


ui.choose_dir_btn.clicked.connect(choose_workdir) 

class ImageProcessor():
    def init(self):
        self.image: Image.Image = None
        self.filename: str = ""
        self.modified_subfolder = "modified"

    def openImage(self, filename: str):
        self.filename = filename
        self.full_path = os.path.join(workdir, filename)
        self.image = Image.open(self.full_path)

    def showImage(self):
        if self.image is not None:
            ui.image_lb.hide()
            pixmap = QPixmap(self.full_path)
            w, h = ui.image_lb.width(), ui.image_lb.height()

            pixmapimage = pixmap.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio)
            ui.image_lb.setPixmap(pixmapimage)

            ui.image_lb.show()

def saveImage(self):
    save_dir_path = os.path.join(workdir, self.modified_subfolder)
    if not os.path.isdir(save_dir_path):
        os.mkdir(save_dir_path)

    full_path = os.path.join(save_dir_path, self.filename)
    self.image.save(full_path)

def makeBW(self):
    self.image = self.image.convert("L")
    self.saveImage()
    modified_path = os.path.join(workdir, self.modified_subfolder, self.filename)
    ...
    ...
    ...
ip = ImageProcessor()

def show_choosen_image():
    if ui.files_list.selectedItems():
        choosen_filename = ui.files_list.currentItem().text()
        ip.openImage(choosen_filename)
        ip.showImage()

ui.files_list.currentItemChanged.connect(show_choosen_image)


win.show()
app.exec()