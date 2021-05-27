# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import datetime

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, QTimer


class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.setTime())
        self.timer.start(1000)

    # Signal Set name
    setName = Signal(str)

    # Signal Set Date
    printTime = Signal(str)

    # Signal Show / Hide Rectangle
    isVisible = Signal(bool)

    # Function Show / Hide Rectangle
    @Slot(bool)
    def showHideRactangle(self, isChecked):
        # print("Is Rectangle visible: ",  isChecked)
        self.isVisible.emit(isChecked)

    # Set Timer Function
    def setTime(self):
        now = datetime.datetime.now()
        formatDate = now.strftime("Now is %H:%M:%S %p of %Y/%m/%d")
        self.printTime.emit(formatDate)

    # Function: set name to label
    @Slot(str)
    def welcomeText(self, name):
        self.setName.emit("Welcome, " + name)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Get Context
    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)

    # Load QML file
    engine.load(os.fspath(Path(__file__).resolve().parent / "qml/main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
