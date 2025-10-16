"""
Example GUI in Python
Lightning Talks Vortrag am 17.10.2025    
"""

from PySide6.QtWidgets import QApplication
import sys

from gui.mainwindow import MainWindow


def main():
    print("Hello from python-gui!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
