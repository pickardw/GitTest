import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.createFirstGroup(),0,0)
        grid.addWidget(self.createSecondGroup(),0,1)
        self.setLayout(grid)

        self.setWindowTitle('Tau Beta Assassins')
        self.resize(500,500)

    def createFirstGroup(self):
        gBox = QtWidgets.QGroupBox('Game Initialization Functions')
        createWorkbook = QPushButton('Create Assassins Spreadsheet')
        randomizeTargets = QPushButton('Randomize Targets in Spreadsheet')

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(createWorkbook)
        vbox.addStretch(1)
        vbox.addWidget(randomizeTargets)
        vbox.addStretch(1)
        gBox.setLayout(vbox)

        return gBox

    def createSecondGroup(self):
        gBox = QtWidgets.QGroupBox('Record a Kill')
        killer = QPushButton('Killer Name')
        menu = QtWidgets.QMenu(self)

        #NEED TO MAKE EXCEL FUNCTION TO GET ALL NAMES
        #RETURNS LIST OF NAMES - listNames
        # for name in listNames:
        #   menu.addAction(name)

        killer.setMenu(menu)


        pointsGained, okPressed = QtWidgets.QInputDialog.getDouble(self, "Input Point Number")
        playerInfo = QPushButton('Get Info on a Player')

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(killer)
        hbox.addStretch(1)
        hbox.addWidget()
        hbox.addStretch(1)



        gBox.setLayout(hbox)

        return gBox


""" def init_UI(self):
        #Create first window buttons
        self.create_workbook = QPushButton('Create Workbook')
        self.randomize_targets = QPushButton('Randomize Targets')
        self.record_kill = QPushButton('Log Kill')
        self.game_info = QPushButton('Game Info')

        #create home window labels
        self.top_label = QtWidgets.QButtonGroup

        # layout directions
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.top_horizontal = QtWidgets.QHBoxLayout()
        self.bottom_horizontal = QtWidgets.QHBoxLayout()

        self.top_horizontal.addStretch()
        self.top_horizontal.addWidget(self.create_workbook)
        self.top_horizontal.addStretch()
        self.top_horizontal.addWidget(self.randomize_targets)
        self.top_horizontal.addStretch()

        self.bottom_horizontal.addStretch()
        self.bottom_horizontal.addWidget(self.record_kill)
        self.bottom_horizontal.addStretch()
        self.bottom_horizontal.addWidget(self.game_info)
        self.bottom_horizontal.addStretch()

        self.vertical_layout.addLayout(self.top_horizontal)
        self.vertical_layout.addLayout(self.bottom_horizontal)

        self.setLayout(self.vertical_layout)
        self.setWindowTitle('Theta Tau Assassins')
        self.show() """


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    home_window = Window()
    home_window.show()

    sys.exit(app.exec_())