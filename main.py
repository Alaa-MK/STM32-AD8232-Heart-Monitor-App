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
        # print(val)
        try:
            val = app.serial.readline().decode()[3:-1]
            val = int(val) / 4096
            appWindow.appendValue(val)
        except:
            print("Not a valid number!")

        if app.isCollecting:
            if (time.time() > app.startTime + app.duration):
                with open('data.csv', 'w', newline='') as myfile:
                    wr = csv.writer(myfile)
                    wr.writerows(app.collectedData)
                app.isCollecting = False
            else:
                app.collectedData.append([time.ctime(), val])
                
class App():
    def __init__(self):   

        #data collection
        self.isCollecting = False
        self.duration = 10
        self.startTime = None
        self.collectedData = []

        #communicaation
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

    def _startCollectingHandler(self, duration):
        if duration.isnumeric():
            print("starting collection..")
            self.duration = int(duration)
            self.isCollecting = True
            self.startTime = time.time()
            self.collectedData.clear()
        else:   
            print("invalid duration!")

    def _communicationHandler(self, port, baudRate):
        if baudRate.isnumeric():
            print("changing communication settings..")
            try:
                self.serial.close()
            except:
                "Opening a new port.."
            self.serial = serial.Serial(port=port, baudrate=baudRate)
            print(self.serial)
        else:
            print("invalid communication settings!")

    def _refreshPortHandler(self):
        ports = list(list_ports.comports())
        port = '' if (len(ports) == 0) else ports[0][0]
        self.appWindow.ui.portLineEdit.setText(port)

    def _setSamplingRateHandler(self, rate):
        self.serial.write(f's{rate}\n'.encode())

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
