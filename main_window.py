from PySide6.QtWidgets import QApplication, QToolBar, QWidget, QMainWindow, QWidgetAction, QMenu, QMenuBar, QPushButton, QVBoxLayout, QHBoxLayout, QStatusBar, QLabel, QLineEdit, QMessageBox, QTextEdit
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import QSize
import sys
import os.path

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Save File")

        self.path = '/Users/nahalhz/Documents'
        self.fileName = ''
        self.content = ''
        w_layout = QVBoxLayout()

        label = QLabel("File Name:")
        self.line_edit = QLineEdit()
        label_layout = QHBoxLayout()
        label_layout.addWidget(label)
        label_layout.addWidget(self.line_edit)


        button1 = QPushButton("Save")
        button1.clicked.connect(self.save_file2)
        button2 = QPushButton("Cancel")
        button2.clicked.connect(self.close)
        b_layout = QHBoxLayout()
        b_layout.addWidget(button1)
        b_layout.addWidget(button2)

        w_layout.addLayout(label_layout)
        w_layout.addLayout(b_layout)

        self.setLayout(w_layout)

    def save_file2(self):
        if self.line_edit.textEdited:
            self.fileName = self.line_edit.text() + '.txt'
        myPath = os.path.join(self.path, self.fileName)
        myFile = open(myPath, 'w')
        myFile.write(self.content)
        myFile.close()
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.app = app #declare an app member(application instance that the main window belong to
        self.setWindowTitle("Note APP")
        self.popUp = None


        self.text_edit = QTextEdit()
        exit_action = QAction(QIcon("quit.png"), "&App Exit", self)
        #button_action.setStatusTip("This is your button")
        exit_action.triggered.connect(self.quit_app)

        save_action = QAction( "&Save File", self)
        save_action.triggered.connect(self.save_file)


        copy_action =QAction("&Copy", self)
        copy_action.triggered.connect(self.text_edit.copy)
        copy_action.setShortcut(QKeySequence("Ctrl+c"))

        cut_action = QAction("&Cut", self)
        cut_action.triggered.connect(self.text_edit.cut)
        cut_action.setShortcut(QKeySequence("Ctrl+x"))

        paste_action = QAction("&Paste", self)
        paste_action.triggered.connect(self.text_edit.paste)
        paste_action.setShortcut(QKeySequence("Ctrl+v"))

        redo_action = QAction("&Redo", self)
        redo_action.triggered.connect(self.text_edit.redo)
        redo_action.setShortcut(QKeySequence("Ctrl+y"))

        undo_action = QAction("&Undo", self)
        undo_action.triggered.connect(self.text_edit.undo)
        undo_action.setShortcut(QKeySequence("Ctrl+z"))

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(exit_action)
        file_menu.addAction(save_action)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction(copy_action)
        edit_menu.addAction(cut_action)
        edit_menu.addAction(paste_action)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

        #more menu options:(NEED TO ADD ACTION FOR IT TO SHOW UP)
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Help")



        #Button as a central widget
        self.setCentralWidget(self.text_edit)


        #self.setCentralWidget(button)

    def toolbar_button_clicked(self):
        self.statusBar().showMessage(
            ("Message from my app", 3000))  # message pops from status bar and stays for 3 sec

    def button_clicked(self):
        print("Clicked")

    def button_pressed(self):
        print("Pressed")

    def button_released(self):
        print("Released")

    def button_toggled(self, data):
        print("click state:", data)


    def quit_app(self):
        ret = QMessageBox.question(self, "Exit", "Is it Okay to quit?",
                                  QMessageBox.Ok | QMessageBox.Cancel  )

        if ret == QMessageBox.Ok:
            sys.exit()
        else:
            print("User chose cancel!")

    def save_file(self):
        self.popUp = AnotherWindow()
        self.popUp.content = self.text_edit.toPlainText()
       # self.popUp.setGeometry(QRect(100, 100, 400, 200))
        self.popUp.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
