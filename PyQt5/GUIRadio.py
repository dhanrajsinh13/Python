import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift Card", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.initUI()


        self.message_label1 = QLabel("Enter payment method: ",self)
        self.message_label1.setGeometry(0, 0, 500, 50)
        self.message_label1.setStyleSheet("font-size: 40px; font-family: Arial; color: darkred;")
        self.message_label2 = QLabel("Enter service type: ",self)
        self.message_label2.setGeometry(0, 200, 500, 50)
        self.message_label2.setStyleSheet("font-size: 40px; font-family: Arial; color: darkgreen;")


    def initUI(self):
        self.radio1.setGeometry(0, 50, 300, 50)
        self.radio2.setGeometry(0, 100, 300, 50)
        self.radio3.setGeometry(0, 150, 300, 50)
        self.radio4.setGeometry(0, 250, 300, 50)
        self.radio5.setGeometry(0, 300, 300, 50)

        self.setStyleSheet("QRadioButton{"
                                         "font-size: 40px;"
                                         "font-family: Arial;"
                                         "padding: 10px;"
                                         "}")


        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(lambda checked: self.radio_button_changed(self.radio1, checked))
        self.radio2.toggled.connect(lambda checked: self.radio_button_changed(self.radio2, checked))
        self.radio3.toggled.connect(lambda checked: self.radio_button_changed(self.radio3, checked))
        self.radio4.toggled.connect(lambda checked: self.radio_button_changed(self.radio4, checked))
        self.radio5.toggled.connect(lambda checked: self.radio_button_changed(self.radio5, checked))

    def radio_button_changed(self, radio_button, checked):
        if checked:
            print(f"{radio_button.text()} is selected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
