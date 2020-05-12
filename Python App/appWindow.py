from matplotlib.figure import Figure
import time
import numpy as np
from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from ui import Ui_Dialog


class Graph():
    def __init__(self):
        self.startingTime = time.time()
        self.timeData = []
        self.data = []
        self.canvas = FigureCanvas(Figure(figsize=(6.4, 2.3)))
        self.ax = self.canvas.figure.subplots()
        self.line, = self.ax.plot(self.timeData, self.data)
        self.ax.set_ylim(0, 1)
        self.updateRate = 24
        self.lastUpdate = time.time()
        self.timeRange = 5      #shows only the last 5 seconds

    def append(self, value):
        self.data.append(value)
        self.timeData.append(time.time()-self.startingTime)
        if time.time() - self.startingTime - self.timeData[0] > self.timeRange:
            self.data.pop(0)
            self.timeData.pop(0)
        if (time.time() - self.lastUpdate > 1/self.updateRate):
            self.updateGraph()
            self.lastUpdate = time.time()
    
    def updateGraph(self):
        self.line.set_xdata(self.timeData)
        self.line.set_ydata(self.data)
        self.ax.set_xlim(self.timeData[-1] - self.timeRange, self.timeData[-1] + self.timeRange)
        self.canvas.figure.canvas.draw()

        

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        gwidget = QtWidgets.QWidget(self.ui.graphGroupBox)
        self.graph = Graph()        
        layout = QtWidgets.QVBoxLayout(gwidget)
        layout.addWidget(self.graph.canvas)
        

    def appendValue(self, value):
        self.graph.append(value)
