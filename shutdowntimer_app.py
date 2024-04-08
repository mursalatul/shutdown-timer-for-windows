from pkgutil import get_data
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi
import sys

class MainUI(QtWidgets.QMainWindow):
    # true when start button is clicked
    process_started = True
    
    # time
    shutdown_after_minutes = 1 #default value

    def __init__(self):
        super(MainUI, self).__init__()
        loadUi('shutdown_timer_gui.ui', self)

        # resize the window in raw code cause in .ui the size can conflict with the system
        self.resize(400, 400)

        # find start button
        self.start_btn = self.findChild(QtWidgets.QPushButton, 'start_button')
        self.start_btn.clicked.connect(self.start_button_event)

        #find At & After radio buttons
        self.at_btn = self.findChild(QtWidgets.QRadioButton, 'radioButton_At')
        self.after_btn = self.findChild(QtWidgets.QRadioButton, 'radioButton_After')

        #find spinbox and clock
        self.spinbox = self.findChild(QtWidgets.QSpinBox, 'spinBox')
        self.timeedit = self.findChild(QtWidgets.QTimeEdit, 'timeEdit')

    def start_button_event(self):
        """
        handle start button
        """
        # start button
        if self.process_started:
            # setting Stop button
            self.process_started = False
            self.start_btn.setText("Stop")
            self.start_btn.setStyleSheet("background-color: #ff5454;") # semi-red

            # disable the After & At buttons
            self.button_status_change([self.at_btn, self.after_btn], False)

            # get_data will refresh shutdown_after_minutes
            self.get_data()

            # calculating the time need for increase 1% in the progress bar
            per_increase_delay = (self.shutdown_after_minutes * 60) / 100

            # starting progress bar
            self.start_progress_bar(per_increase_delay)
        
        # stop button
        else:
            # setting start button
            self.process_started = True
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

    def get_data(self):
        """
        get used inputed data from spinbox / timeedit
        """
        if self.after_btn.isChecked():
            self.shutdown_after_minutes = self.spinbox.value()
        else:
            self.shutdown_after_minutes = round(self.minutes_left_to_time(self.timeedit))
            
    def minutes_left_to_time(self, time_edit):
        # Get the current time
        current_time = QtCore.QTime.currentTime()
        # Get the time set in the QTimeEdit widget
        selected_time = time_edit.time()
        # Calculate the difference in minutes between the current time and the selected time
        minutes_difference = current_time.secsTo(selected_time) / 60
        return minutes_difference

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec_())
