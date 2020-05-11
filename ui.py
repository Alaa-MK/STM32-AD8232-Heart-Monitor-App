# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(681, 407)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.communicationGroupBox = QtWidgets.QGroupBox(Dialog)
        self.communicationGroupBox.setGeometry(QtCore.QRect(10, 260, 211, 141))
        self.communicationGroupBox.setObjectName("communicationGroupBox")
        self.portLineEdit = QtWidgets.QLineEdit(self.communicationGroupBox)
        self.portLineEdit.setGeometry(QtCore.QRect(80, 30, 91, 21))
        self.portLineEdit.setObjectName("portLineEdit")
        self.portRefreshButton = QtWidgets.QPushButton(
            self.communicationGroupBox)
        self.portRefreshButton.setGeometry(QtCore.QRect(180, 30, 21, 21))
        self.portRefreshButton.setObjectName("portRefreshButton")
        self.portLabel = QtWidgets.QLabel(self.communicationGroupBox)
        self.portLabel.setGeometry(QtCore.QRect(8, 30, 55, 16))
        self.portLabel.setObjectName("portLabel")
        self.communicationApplyButton = QtWidgets.QPushButton(
            self.communicationGroupBox)
        self.communicationApplyButton.setGeometry(
            QtCore.QRect(10, 110, 191, 28))
        self.communicationApplyButton.setObjectName("communicationApplyButton")
        self.baudRateLineEdit = QtWidgets.QLineEdit(self.communicationGroupBox)
        self.baudRateLineEdit.setGeometry(QtCore.QRect(80, 60, 121, 22))
        self.baudRateLineEdit.setObjectName("baudRateLineEdit")
        self.baudRateLineEdit.setText("250000")
        self.baudRateLabel = QtWidgets.QLabel(self.communicationGroupBox)
        self.baudRateLabel.setGeometry(QtCore.QRect(8, 60, 61, 16))
        self.baudRateLabel.setObjectName("baudRateLabel")
        self.communicationErrorLabel = QtWidgets.QLabel(
            self.communicationGroupBox)
        self.communicationErrorLabel.setGeometry(QtCore.QRect(10, 90, 191, 16))
        self.communicationErrorLabel.setText("")
        self.communicationErrorLabel.setObjectName("communicationErrorLabel")
        self.samplingGroupBox = QtWidgets.QGroupBox(Dialog)
        self.samplingGroupBox.setGeometry(QtCore.QRect(230, 261, 231, 141))
        self.samplingGroupBox.setObjectName("samplingGroupBox")
        self.samplingRateLineEdit = QtWidgets.QLineEdit(self.samplingGroupBox)
        self.samplingRateLineEdit.setGeometry(QtCore.QRect(110, 60, 111, 22))
        self.samplingRateLineEdit.setObjectName("samplingRateLineEdit")
        self.samplingRateLabel = QtWidgets.QLabel(self.samplingGroupBox)
        self.samplingRateLabel.setGeometry(QtCore.QRect(8, 60, 91, 16))
        self.samplingRateLabel.setObjectName("samplingRateLabel")
        self.samplingApplyButton = QtWidgets.QPushButton(self.samplingGroupBox)
        self.samplingApplyButton.setGeometry(QtCore.QRect(10, 110, 211, 28))
        self.samplingApplyButton.setObjectName("samplingApplyButton")
        self.BPMlabel = QtWidgets.QLabel(self.samplingGroupBox)
        self.BPMlabel.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.BPMlabel.setObjectName("BPMlabel")
        self.BPMValue = QtWidgets.QLabel(self.samplingGroupBox)
        self.BPMValue.setGeometry(QtCore.QRect(110, 30, 91, 16))
        self.BPMValue.setObjectName("BPMValue")
        self.samplingErrorLabel = QtWidgets.QLabel(self.samplingGroupBox)
        self.samplingErrorLabel.setGeometry(QtCore.QRect(10, 90, 211, 16))
        self.samplingErrorLabel.setText("")
        self.samplingErrorLabel.setObjectName("samplingErrorLabel")
        self.dataCollectionGroupBox = QtWidgets.QGroupBox(Dialog)
        self.dataCollectionGroupBox.setGeometry(
            QtCore.QRect(470, 261, 201, 141))
        self.dataCollectionGroupBox.setObjectName("dataCollectionGroupBox")
        self.durationLineEdit = QtWidgets.QLineEdit(
            self.dataCollectionGroupBox)
        self.durationLineEdit.setGeometry(QtCore.QRect(140, 60, 51, 22))
        self.durationLineEdit.setObjectName("durationLineEdit")
        self.durationLabel = QtWidgets.QLabel(self.dataCollectionGroupBox)
        self.durationLabel.setGeometry(QtCore.QRect(8, 60, 121, 16))
        self.durationLabel.setObjectName("durationLabel")
        self.dataCollectionStartButton = QtWidgets.QPushButton(
            self.dataCollectionGroupBox)
        self.dataCollectionStartButton.setGeometry(
            QtCore.QRect(10, 110, 181, 28))
        self.dataCollectionStartButton.setObjectName(
            "dataCollectionStartButton")
        self.dataCollectionErrorLabel = QtWidgets.QLabel(
            self.dataCollectionGroupBox)
        self.dataCollectionErrorLabel.setGeometry(
            QtCore.QRect(10, 90, 181, 16))
        self.dataCollectionErrorLabel.setText("")
        self.dataCollectionErrorLabel.setObjectName("dataCollectionErrorLabel")
        self.graphGroupBox = QtWidgets.QGroupBox(Dialog)
        self.graphGroupBox.setGeometry(QtCore.QRect(9, 9, 661, 251))
        self.graphGroupBox.setTitle("")
        self.graphGroupBox.setObjectName("graphGroupBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        Dialog.setWindowIcon(QtGui.QIcon('icon.ico'))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Heart Monitor"))
        self.communicationGroupBox.setTitle(
            _translate("Dialog", "Communication"))
        self.portLabel.setText(_translate("Dialog", "COM Port"))
        self.portRefreshButton.setText(_translate("Dialog", "⟳"))
        self.communicationApplyButton.setText(_translate("Dialog", "Apply"))
        self.baudRateLabel.setText(_translate("Dialog", "Baud Rate"))
        self.portRefreshButton.setText(_translate("Dialog", "⟳"))
        self.samplingGroupBox.setTitle(_translate("Dialog", "Sampling"))
        self.samplingRateLabel.setText(_translate("Dialog", "Sampling Rate"))
        self.samplingApplyButton.setText(_translate("Dialog", "Apply"))
        self.BPMlabel.setText(_translate("Dialog", "BPM"))
        self.BPMValue.setText(_translate("Dialog", "20.6"))
        self.dataCollectionGroupBox.setTitle(
            _translate("Dialog", "Data Collection"))
        self.durationLabel.setText(_translate("Dialog", "Duration (seconds)"))
        self.dataCollectionStartButton.setText(_translate("Dialog", "Start"))
