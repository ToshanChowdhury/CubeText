import sys
import time
import tkinter.messagebox as msg

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.path = ''

        self.texteditor = QTextEdit()
        self.texteditor.setFont(QFont("Times New Roman", 11))
        self.tabs.addTab(self.texteditor, "Main Editor")

        self.calendar = QCalendarWidget()
        self.calendar.setFont(QFont("Times New Roman", 15))
        self.tabs.addTab(self.calendar, "Calendar")

        webbrowser = QWebEngineView()
        webbrowser.setUrl(QUrl("https://www.google.com/en"))
        self.tabs.addTab(webbrowser, "Web Browser")

        menu_bar = QMenuBar()

        files = QMenu("Files", self)

        new_file = QAction(QIcon("icons/new-document.png"), "New File", self)
        new_file.triggered.connect(self.new_action)

        open_file = QAction(QIcon("icons/open-folder.png"), "Open File", self)
        open_file.setShortcut(QKeySequence("Ctrl+O"))
        open_file.triggered.connect(self.open_action)

        save_file = QAction(QIcon("icons/diskette.png"), "Save File", self)
        save_file.setShortcut(QKeySequence("Ctrl+S"))
        save_file.triggered.connect(self.save_file)

        save_as = QAction(QIcon("icons/folder.png"), "Save As File", self)
        save_as.setShortcut(QKeySequence("Ctrl+Shift+S"))
        save_as.triggered.connect(self.save_as)

        exit_program = QAction(QIcon("icons/logout.png"), "Exit Program", self)
        exit_program.setShortcut(QKeySequence("Ctrl+Q"))
        exit_program.triggered.connect(self.exit)

        files.addActions([new_file, open_file, save_file, save_as, exit_program])

        menu_bar.addMenu(files)

        edit = QMenu("Edit", self)

        undo = QAction(QIcon("icons/undo.png"), "Undo", self)
        undo.setShortcut(QKeySequence("Ctrl+Z"))
        undo.triggered.connect(self.undo)

        redo = QAction(QIcon("icons/redo.png"), "Redo", self)
        redo.setShortcut(QKeySequence("Ctrl+Y"))
        redo.triggered.connect(self.redo)

        cut = QAction(QIcon("icons/cut.png"), "Cut", self)
        cut.setShortcut(QKeySequence("Ctrl+X"))
        cut.triggered.connect(self.cut)

        copy = QAction(QIcon("icons/copy.png"), "Copy", self)
        copy.setShortcut(QKeySequence("Ctrl+C"))
        copy.triggered.connect(self.copy)

        paste = QAction(QIcon("icons/paste.png"), "Paste", self)
        paste.setShortcut(QKeySequence("Ctrl+V"))
        paste.triggered.connect(self.paste)

        edit.addActions([undo, redo])
        edit.addSeparator()

        edit.addActions([cut, copy, paste])
        edit.addSeparator()

        select_all = QAction(QIcon("icons/selection.png"), "Select All Text", self)

        edit.addActions([select_all])

        menu_bar.addMenu(edit)

        format = QMenu("Format", self)

        bold = QAction(QIcon("icons/bold.png"), "Bold", self)

        italic = QAction(QIcon("icons/italic.png"), "Italic", self)

        underline = QAction(QIcon("icons/underline.png"), "Underline", self)

        format.addActions([bold, italic, underline])
        format.addSeparator()

        left_align = QAction(QIcon("icons/align-left.png"), "Left Alignment", self)
        left_align.setShortcut(QKeySequence("Ctrl+L"))
        left_align.triggered.connect(self.left)

        right_align = QAction(QIcon("icons/align-right.png"), "Right Alignment", self)
        right_align.setShortcut(QKeySequence("Ctrl+R"))
        right_align.triggered.connect(self.right)

        center_align = QAction(QIcon("icons/center-align.png"), "Center Alignment", self)
        center_align.setShortcut(QKeySequence("Ctrl+E"))
        center_align.triggered.connect(self.center)

        justify_align = QAction(QIcon("icons/justify.png"), "Justify Alignment", self)
        justify_align.setShortcut(QKeySequence("Ctrl+J"))
        justify_align.triggered.connect(self.justify)

        format.addActions([left_align, right_align, center_align, justify_align])
        format.addSeparator()

        image = QAction(QIcon("icons/images.png"), "Insert Image", self)
        image.setShortcut(QKeySequence("Ctrl+I"))
        image.triggered.connect(self.insert_image)

        date = QAction(QIcon("icons/date.png"), "Insert Date", self)
        date.setShortcut(QKeySequence("Ctrl+D"))
        date.triggered.connect(self.insert_date)

        time = QAction(QIcon("icons/clock.png"), "Insert Time", self)
        time.setShortcut(QKeySequence("Ctrl+M"))
        time.triggered.connect(self.insert_time)

        dateandtime = QAction(QIcon("icons/calendar.png"), "Insert Date and Time", self)
        dateandtime.setShortcut(QKeySequence("Ctrl+T"))
        dateandtime.triggered.connect(self.insert_date_time)

        format.addActions([image, date, time, dateandtime])

        menu_bar.addMenu(format)

        self.setMenuBar(menu_bar)

        self.toolbar = QToolBar("Toolbar")

        new_file = QAction(QIcon("icons/new-document.png"), "New File", self)
        new_file.triggered.connect(self.new_action)

        open_file = QAction(QIcon("icons/open-folder.png"), "Open File", self)
        open_file.triggered.connect(self.open_action)

        save_file = QAction(QIcon("icons/diskette.png"), "Save File", self)
        save_file.triggered.connect(self.save_file)

        save_as = QAction(QIcon("icons/folder.png"), "Save As File", self)
        save_as.triggered.connect(self.save_as)

        exit_program = QAction(QIcon("icons/logout.png"), "Exit Program", self)
        exit_program.triggered.connect(self.exit)

        self.toolbar.addActions([new_file, open_file, save_file, save_as, exit_program])
        self.toolbar.addSeparator()

        undo = QAction(QIcon("icons/undo.png"), "Undo", self)
        undo.setShortcut(QKeySequence("Ctrl+Z"))
        undo.triggered.connect(self.undo)

        redo = QAction(QIcon("icons/redo.png"), "Redo", self)
        redo.setShortcut(QKeySequence("Ctrl+Y"))
        redo.triggered.connect(self.redo)

        cut = QAction(QIcon("icons/cut.png"), "Cut", self)
        cut.triggered.connect(self.cut)

        copy = QAction(QIcon("icons/copy.png"), "Copy", self)
        copy.triggered.connect(self.copy)

        paste = QAction(QIcon("icons/paste.png"), "Paste", self)
        paste.triggered.connect(self.paste)

        self.toolbar.addActions([undo, redo, cut, copy, paste])
        self.toolbar.addSeparator()

        self.font = QFontComboBox()
        self.font.setCurrentFont(QFont("Times New Roman"))
        self.font.currentFontChanged.connect(self.texteditor.setCurrentFont)
        self.toolbar.addWidget(self.font)

        self.font_size = QSpinBox()
        self.font_size.setValue(11)
        self.font_size.valueChanged.connect(self.set_font_size)
        self.toolbar.addWidget(self.font_size)

        self.toolbar.addSeparator()

        bold = QAction(QIcon("icons/bold.png"), "Bold", self)
        bold.triggered.connect(self.bold)

        italic = QAction(QIcon("icons/italic.png"), "Italic", self)
        italic.triggered.connect(self.italic)

        underline = QAction(QIcon("icons/underline.png"), "Underline", self)
        underline.triggered.connect(self.underline)

        self.toolbar.addActions([bold, italic, underline])
        self.toolbar.addSeparator()

        left_align = QAction(QIcon("icons/align-left.png"), "Left Alignment", self)
        left_align.triggered.connect(self.left)

        right_align = QAction(QIcon("icons/align-right.png"), "Right Alignment", self)
        right_align.triggered.connect(self.right)

        center_align = QAction(QIcon("icons/center-align.png"), "Center Alignment", self)
        center_align.triggered.connect(self.center)

        justify_align = QAction(QIcon("icons/justify.png"), "Justify Alignment", self)
        justify_align.triggered.connect(self.justify)

        self.toolbar.addActions([left_align, right_align, center_align, justify_align])
        self.toolbar.addSeparator()

        image = QAction(QIcon("icons/images.png"), "Insert Image", self)
        image.triggered.connect(self.insert_image)

        date = QAction(QIcon("icons/date.png"), "Insert Date", self)
        date.triggered.connect(self.insert_date)

        time = QAction(QIcon("icons/clock.png"), "Insert Time", self)
        time.triggered.connect(self.insert_time)

        dateandtime = QAction(QIcon("icons/calendar.png"), "Insert Date and Time", self)
        dateandtime.triggered.connect(self.insert_date_time)

        self.toolbar.addActions([image, date, time, dateandtime])

        self.addToolBar(self.toolbar)

        self.showMaximized()

    def new_action(self):
        try:
            self.texteditor.clear()
            self.path = ''
            self.texteditor.setWindowTitle("CubeText")
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def open_action(self):
        try:
            self.path, _ = QFileDialog.getOpenFileName(self, "Open File", "*.cbtxt",
                                                       "CubeText Files (*.cbtxt)")

            with open(self.path, "r") as f:
                document = f.read()
        except Exception as e:
            msg.showerror(title="CubeText", message=e)
        else:
            self.texteditor.setText(document)
            self.texteditor.setWindowTitle("CubeText: " + self.path)

    def save_file(self):
        if self.path == "":
            self.save_as()

        text = self.texteditor.toPlainText()

        try:
            with open(self.path, "w") as f:
                f.write(text)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def save_as(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save As", "*.cbtxt",
                                                   "CubeText Files (*.cbtxt)")

        text = self.texteditor.toPlainText()

        try:
            with open(self.path, "w") as f:
                f.write(text)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def exit(self):
        try:
            exit()
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def cut(self):
        try:
            self.texteditor.cut()
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def copy(self):
        try:
            self.texteditor.copy()
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def paste(self):
        try:
            self.texteditor.paste()
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def select_all(self):
        try:
            self.texteditor.selectAll()
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def bold(self):
        try:
            self.texteditor.setFontWeight(QFont.Bold)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def italic(self):
        try:
            if self.texteditor.fontItalic() != True:
                self.texteditor.setFontItalic(True)
            else:
                self.texteditor.setFontItalic(False)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def underline(self):
        try:
            if self.texteditor.fontUnderline() != True:
                self.texteditor.setFontUnderline(True)
            else:
                self.texteditor.setFontUnderline(False)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def undo(self):
        try:
            self.texteditor.undo()
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def redo(self):
        try:
            self.texteditor.redo()
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def left(self):
        try:
            self.texteditor.setAlignment(Qt.AlignLeft)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def right(self):
        try:
            self.texteditor.setAlignment(Qt.AlignRight)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def center(self):
        try:
            self.texteditor.setAlignment(Qt.AlignCenter)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def justify(self):
        try:
            self.texteditor.setAlignment(Qt.AlignJustify)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def insert_image(self):
        try:
            self.image_path, _ = QFileDialog.getOpenFileName(self, "Insert Image", "",
                                                          "all files (*.*)")

            document = self.texteditor.document()
            cursor = QTextCursor(document)

            cursor.insertImage(self.image_path)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def insert_date(self):
        try:
            get_time = time.strftime("%d/%m/%Y")
            self.texteditor.insertPlainText(get_time)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def insert_time(self):
        try:
            get_time = time.strftime("%I:%M %p")
            self.texteditor.insertPlainText(get_time)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def insert_date_time(self):
        try:
            get_time = time.strftime("%d/%m/%Y %I:%M %p")
            self.texteditor.insertPlainText(get_time)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)

    def set_font_size(self):
        try:
            value = self.font_size.value()
            self.texteditor.setFontPointSize(value)
        except Exception as e:
            msg.showerror(title="CubeText", message=e)


app = QApplication(sys.argv)
app.setApplicationName("CubeText")
app.setWindowIcon(QIcon("icons/cube.png"))
window = MainWindow()
window.show()
sys.exit(app.exec_())