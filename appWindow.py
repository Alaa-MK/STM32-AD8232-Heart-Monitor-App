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
        self.MAX_SIZE = 40
        self.timeData = []
        self.data = []
        self.canvas = FigureCanvas(Figure(figsize=(6.4, 2.3)))
        self.ax = self.canvas.figure.subplots()

    def append(self, value):
        self.ax.clear()
        self.data.append(value)
        self.timeData.append(time.time()-self.startingTime)
        if len(self.data) > self.MAX_SIZE:
            self.data.pop(0)
            self.timeData.pop(0)
        self.ax.set_ylim(0, 1)
        self.ax.plot(self.timeData, self.data)
        self.ax.figure.canvas.draw()
        

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        gwidget = QtWidgets.QWidget(self.ui.graphGroupBox)
        self.graph = Graph()        
        layout = QtWidgets.QVBoxLayout(gwidget)
        layout.addWidget(self.graph.canvas)
        

    def updateGraph(self, value):
        self.graph.append(value)
