from PySide6.QtWidgets import QLabel, QMainWindow, QTextEdit, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._setup_ui()

    def onClicked(self):
        num1 = int(self.textbox1.toPlainText())
        num2 = int(self.textbox2.toPlainText())
        result = num1 + num2
        output = "<p style='color:blue'>The sum of " + str(num1) + " and " + str(num2) + " is " + str(result) + '</p>'
        self.lblResult.setText(output)
    
    def _setup_ui(self):
        self.setWindowTitle("Lightning Talks: Example GUI")
        self.setMinimumSize(800,700)
        # Create label for the first number
        self.lbl1 = QLabel('Number 1', self)
        self.lbl1.setGeometry(80, 20, 80, 50)
        # Create textbox for the first number
        self.textbox1 = QTextEdit(self)
        self.textbox1.setGeometry(80, 60, 70, 30)

        # Create label for the second number
        self.lbl2 = QLabel('Number 2', self)
        self.lbl2.setGeometry(200, 20, 80, 50)
        # Create textbox for the second number
        self.textbox2 = QTextEdit(self)
        self.textbox2.setGeometry(200, 60, 70, 30)

        # Create push button for calculate the sum
        self.submit = QPushButton('Calculate Sum', self)
        self.submit.setGeometry(80, 100, 190, 30)
        # Create label for show the result of summation
        self.lblResult = QLabel('', self)
        self.lblResult.setGeometry(80, 130, 200, 50)
        # Call function when the button is clicked
        self.submit.clicked.connect(self.onClicked)
