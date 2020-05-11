from appWindow import ApplicationWindow
import sys, time, serial
from matplotlib.backends.qt_compat import QtWidgets, QtGui
from threading import Thread, Event
import csv
from serial.tools import list_ports

def backgroundThread(app, appWindow):
    while True:
        if app.serial is None:
            continue
        try:
            val = app.serial.readline().decode()[3:-1]
            val = int(val) / 4096
            appWindow.appendValue(val)
            print(val)
        except:
            print("Not a valid number!")
                
class App():
    def __init__(self):   
        
        #communication
        self.serial = None

        qapp = QtWidgets.QApplication(sys.argv)
        self.appWindow = ApplicationWindow()

        self._setupEventHandlers()
        self._refreshPortHandler()

        thread = Thread(target=backgroundThread, args=(self, self.appWindow,))
        thread.daemon = True
        thread.start()

        self.appWindow.show()
        sys.exit(qapp.exec_())

    def _communicationHandler(self, port, baudRate):
        val = 0
        try:
            val = int(baudRate)
        except:
            self.appWindow.ui.communicationErrorLabel.setText(
                "ERROR: Non numerical value!")
            return
        if val <= 0:
            self.appWindow.ui.communicationErrorLabel.setText(
                "ERROR: Non positive value!")
            return
        try:
            self.serial.close()
        except:
            "Opening a new port.."
        self.serial = serial.Serial(port=port, baudrate=baudRate)
        self.appWindow.ui.communicationErrorLabel.setText("")
        print('Communication settings changed!')

    def _refreshPortHandler(self):
        ports = list(list_ports.comports())
        port = '' if (len(ports) == 0) else ports[0][0]
        self.appWindow.ui.portLineEdit.setText(port)

    def _setSamplingRateHandler(self, rate):
        val = 0
        try:
            val = int(rate)
        except:
            self.appWindow.ui.samplingErrorLabel.setText("ERROR: Non numerical value!")
            return
        if val <= 0:
            self.appWindow.ui.samplingErrorLabel.setText(
                "ERROR: Non positive value!")
            return
        self.serial.write(f's{rate}\n'.encode())
        self.appWindow.ui.samplingErrorLabel.setText("")
        print('Command for setting sampling rate sent!')

    def _startCollectingHandler(self, duration):
        val = 0
        try:
            val = int(duration)
        except:
            self.appWindow.ui.dataCollectionErrorLabel.setText(
                "ERROR: Non numerical value!")
            return
        if val <= 0:
            self.appWindow.ui.dataCollectionErrorLabel.setText(
                "ERROR: Non positive value!")
            return
        self.serial.write(f'c{duration}\n'.encode())
        self.appWindow.ui.dataCollectionErrorLabel.setText("")
        print('Command for collecting data sent!')
        

    # def _getSelectedBaudRate(self):

    def _setupEventHandlers(self):
        self.appWindow.ui.dataCollectionStartButton.clicked.connect(
            lambda : self._startCollectingHandler(self.appWindow.ui.durationLineEdit.text())
        )
        self.appWindow.ui.communicationApplyButton.clicked.connect(
            lambda : self._communicationHandler(self.appWindow.ui.portLineEdit.text(), self.appWindow.ui.baudRateLineEdit.text())
        )
        self.appWindow.ui.portRefreshButton.clicked.connect(
            self._refreshPortHandler
        )
        self.appWindow.ui.samplingApplyButton.clicked.connect(
            lambda : self._setSamplingRateHandler(self.appWindow.ui.samplingRateLineEdit.text())
        )


if __name__ == "__main__":
    App()
