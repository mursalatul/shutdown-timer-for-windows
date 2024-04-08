from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import sys

class MainUI(QtWidgets.QMainWindow):
    # true when start button is clicked
    process_started = False
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('shutdown_timer_gui.ui', self)

        # find start button
        self.start_btn = self.findChild(QtWidgets.QPushButton, 'start_button')
        self.start_btn.clicked.connect(self.start_button_event)

        #find At & After radio buttons
        self.at_btn = self.findChild(QtWidgets.QRadioButton, 'radioButton_After')
        self.after_btn = self.findChild(QtWidgets.QRadioButton, 'radioButton_At')

    def start_button_event(self):
        """
        handle start button
        """
        # start button
        if not self.process_started:
            # setting Stop button
            self.process_started = True
            self.start_btn.setText("Stop")
            self.start_btn.setStyleSheet("background-color: #ff5454;") # semi-red

            # disable the After & At buttons
            self.button_status_change([self.at_btn, self.after_btn], False)

            tm = 1
            per_increase_delay = (tm * 60) / 100
            self.start_progress_bar(per_increase_delay)
        
        # stop button
        else:
            # setting start button
            self.process_started = False
            self.start_btn.setText("Start")
            self.start_btn.setStyleSheet("background-color: #ba8cff;") # semi-purple blue

            # disable the After & At buttons
            self.button_status_change([self.at_btn, self.after_btn], True)

            # stop to prograss bar
            self.timer.stop()

    def start_progress_bar(self, per_increase_delay):
        """
        trigger the progress bar
        """
        # find progress bar
        self.progress_bar = self.findChild(QtWidgets.QProgressBar, 'progressBar')

        # Create a timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.increment_progress)
        self.timer.start(per_increase_delay * 1000)  # Convert seconds to milliseconds

    def increment_progress(self):
        """
        Increment the progress bar value
        """
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 1)
        else:
            # Progress completed, stop the timer
            self.timer.stop()

    def button_status_change(self, list_of_buttons: list, status: bool) -> None:
        """
        disable all the buttons in the list_of_buttons.
        here list_of_buttons will be a list so that at
        a same time it can take multiple inputs and process
        it
        """
        for btn in list_of_buttons:
            btn.setEnabled(status)
            btn.setEnabled(status)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())
