import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

# This window will display the text entered by the user.
class DisplayWindow(QWidget):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Display Text")
        self.setGeometry(150, 150, 400, 200)
        self.setup_ui(text)

    def setup_ui(self, text):
        layout = QVBoxLayout()
        # Create a label to show the text with a colorful style.
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        # Apply a style sheet to set text color and font properties.
        label.setStyleSheet("color: blue; font-size: 20px;")
        layout.addWidget(label)
        self.setLayout(layout)

# Main window to collect the user’s text.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Collector")
        self.setGeometry(100, 100, 400, 200)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background-color: blue;")
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Text input widget.
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Enter your text here")
        self.input_text.setStyleSheet("""
            background-color: #f0f0f0;
            color: black;
            font-size: 20px;
            padding: 10px;
            border: 2px solid #ccc;
        """)
        layout.addWidget(self.input_text)
        
        # Submit button.
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: red; color: white; font-size: 18px;")
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.show_text_window)

    # When the button is clicked, open a new window displaying the text.
    def show_text_window(self):
        text = self.input_text.text()
        if text.strip():
            self.display_window = DisplayWindow(text)
            self.display_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
