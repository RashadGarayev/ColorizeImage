from PyQt5.QtWidgets import QApplication,QDialog,QWidget
from PyQt5.uic import loadUi
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import cv2,sys,os,datetime,time
import numpy as np
from PyQt5.QtWidgets import *
import imageio,helper
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
class Window(QWidget):
    def __init__(self):
        """-----------------------------"""
        super(Window,self).__init__()
        loadUi('ui/gui.ui',self)
        self.setFixedSize(733,432)
        self.pushButton_3.clicked.connect(self.Photo)
        self.pushButton.clicked.connect(self.About)
        self.pushButton_2.clicked.connect(self.Video)
    def Photo(self):
        self.colorizePhoto = ColorizePhotoWindow()
        self.colorizePhoto.show()
    def Video(self):
        self.colorizeVideo = ColorizeVideoWindow()
        self.colorizeVideo.show()
    def About(self):
        self.win = QWidget()
        self.win.setWindowTitle('About')
        self.win.setGeometry(100,100,450,400)
        self.win.setFixedSize(450,400)
        self.win.show()
class ColorizePhotoWindow( QWidget ) :
    def __init__ ( self) :
        super( ColorizePhotoWindow, self ).__init__()
        loadUi('ui/photo.ui',self)
        self.setWindowTitle('Colorization Image')
        self.pushButton_2.clicked.connect(self.ChooseFile)
    def ChooseFile(self):
        try:
            filename, _ = QFileDialog.getOpenFileName(None, 'Image', '.', 'Image Files(*.jpg *.png)')
            if filename:
                with open(filename, 'rb') as file:
                    data = np.array(bytearray(file.read()))
                    self.f = filename.rstrip(os.sep)
                    self.gray = cv2.imdecode(data, cv2.IMREAD_GRAYSCALE)
                    img = self.gray
                    img = cv2.resize(img, (281,281))
                    start = datetime.datetime.now()
                    size = img.shape
                    step = img.size / size[0]
                    qformat = QImage.Format_Indexed8
                    if len(size) == 3:
                        if size[2] == 4:
                            qformat = QImage.Format_RGBA8888
                        else:
                            qformat = QImage.Format_RGB888
                    img = QImage(img, size[1], size[0], step, qformat)
                    img = img.rgbSwapped()
                    self.pixmapgray = QPixmap(img)
                    self.label.setPixmap(self.pixmapgray)
                    self.listWidget.addItem(f'Original image: {self.gray.shape}')
                    helper.Image(self.f)
                    end = datetime.datetime.now()
                    elapsed = end - start
                    self.listWidget.addItem(f'Total seconds:{elapsed.total_seconds()}')
                    self.pixmapcolorize = QPixmap(r'tmp/colorized.jpg')
                    self.label_2.setPixmap(self.pixmapcolorize)
                    hsv = cv2.imread(r'tmp/colorized.jpg')
                    hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
                    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
                    hist = cv2.imwrite(r'tmp/histogram.jpg',hist)
                    self.pixmaphistogram = QPixmap(r'tmp/histogram.jpg')
                    self.label_3.setPixmap(self.pixmaphistogram)
                    self.listWidget.addItem('Image saved : tmp/colorized.jpg')
        except AttributeError:
            self.listWidget.addItem('Please choose image')
class ColorizeVideoWindow( QWidget ) :
    def __init__ ( self) :
        super( ColorizeVideoWindow, self ).__init__()
        loadUi('ui/video.ui',self)
        self.setWindowTitle('Colorization')
        self.setFixedSize(780,335)
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.ChooseVideoFile)


    def ChooseVideoFile(self):
        try:
            filename, _ = QFileDialog.getOpenFileName(None, 'Video', '.', 'Video Files(*.mp4 )')
            if filename:
                with open(filename, 'rb') as file:
                    self.f = filename.rstrip(os.sep)
                    reader = imageio.get_reader(self.f)
                    fps = reader.get_meta_data()['fps']
                    writer = imageio.get_writer('tmp/output.mp4', fps=fps)
                    counter = 0
                    for iteration, frame in enumerate(reader):
                        frame = helper.ColorizeVideo(frame)
                        writer.append_data(frame)
                        self.listWidget.addItem(u'Emal olunur...')
                        while counter < iteration:
                            counter += 1
                            if counter > iteration:
                                self.progressBar.setFormat(u'Emal olunur...')

                            else:
                                time.sleep(2)
                                self.progressBar.setValue(counter)
                    
                    writer.close()
                    self.progressBar.setFormat(u'Succesfully')
                    
        except AttributeError:
            self.listWidget.addItem('Please choose file')




if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Window()
    window.setWindowTitle("Colorization")
    window.show()
    sys.exit(app.exec_())