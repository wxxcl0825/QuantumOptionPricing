import sys

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from view.MainWindow import MainWindow


def load_fonts():
    QFontDatabase().addApplicationFont(":fonts/fonts/hitmo.ttf")
    QFontDatabase().addApplicationFont(":fonts/fonts/rostov.ttf")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    load_fonts()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
