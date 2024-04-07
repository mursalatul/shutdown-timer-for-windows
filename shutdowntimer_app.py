from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import sys

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('shutdown_timer_gui.ui', self)
        # find start button
        self.start_bnt = self.findChild(QtWidgets.QPushButton, 'start_button')
        self.start_bnt.clicked.connect(self.start_button_event)
    
    def start_button_event(self):
        """
        handle start button
        """
        print("start button pressed")
        tm = 1
        per_increase_delay = (tm * 60) / 100
        self.start_progress_bar(10)

    def start_progress_bar(self, per_increase_delay):
        """
        trigger the progress bar
        """
        # find progress barr
        self.progress_bar = self.findChild(QtWidgets.QProgressBar, 'progressBar')
        
        # start the progressBar
        while self.progress_bar.value() < 100:
            QtCore.QTimer(self).start(per_increase_delay * 1000)
            self.progress_bar.setValue(self.progress_bar.value() + 1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()