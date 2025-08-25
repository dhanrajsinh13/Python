import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QPixmap, QPainter, QPainterPath
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    """
    Main application window that displays an image and a styled text label.
    """
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("Pookie!")
        self.setGeometry(300, 200, 600, 600)
        self.setStyleSheet("background-color: rgb(252, 3, 103);")

        # Create and configure the image label
        self.setup_image_label()

        # Create and configure the text label
        self.setup_text_label()

    def setup_image_label(self):
        """
        Creates a QLabel to display an image with rounded upper corners.
        """
        image_label = QLabel(self)
        image_label.setGeometry(100, 50, 400, 400)

        # Load and resize the image
        pixmap = QPixmap("../Data/pookie.jpg").scaled(400, 400, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        # Create a rounded mask for upper corners
        mask = QPixmap(pixmap.size())
        mask.fill(Qt.transparent)

        painter = QPainter(mask)
        path = QPainterPath()
        path.moveTo(0, 50)
        path.lineTo(0, pixmap.height())
        path.lineTo(pixmap.width(), pixmap.height())
        path.lineTo(pixmap.width(), 50)
        path.quadTo(pixmap.width(), 0, pixmap.width() - 50, 0)
        path.lineTo(50, 0)
        path.quadTo(0, 0, 0, 50)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillPath(path, Qt.white)
        painter.end()

        pixmap.setMask(mask.createMaskFromColor(Qt.transparent))
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)

    def setup_text_label(self):
        """
        Creates a QLabel to display styled text with rounded bottom corners.
        """
        text_label = QLabel("Hey, Pookie!", self)
        text_label.setGeometry(100, 450, 400, 100)

        text_label.setFont(QFont("Arial", 32))
        text_label.setStyleSheet("""
            color: rgb(252, 3, 103);
            background-color: #e0ce98;
            font-weight: bold;
            font-style: italic;
            text-decoration: underline;
            border-bottom-left-radius: 30px;
            border-bottom-right-radius: 30px;
        """)
        text_label.setAlignment(Qt.AlignCenter)

def main():
    """
    Entry point for the application.
    Initializes the QApplication and shows the main window.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()