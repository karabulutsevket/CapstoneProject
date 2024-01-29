import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QStackedWidget,
    QPageWidget,
)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # QStackedWidget widget'ı oluştur
        self.stackedWidget = QStackedWidget()

        # Page Widget oluştur
        self.page1 = QPageWidget()

        # Page Widget'ı QStackedWidget'a ekle
        self.stackedWidget.addWidget(self.page1)

        # Page Widget'ı pencerenin içeriğine ekle
        self.layout().addWidget(self.stackedWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Pencereyi oluştur
    window = MyWindow()

    # Pencereyi göster
    window.show()

    sys.exit(app.exec_())
