from PyQt5.QtWidgets import QApplication
from browser import Browser

def main():
    """
    Main function to start the browser application.
    """
    app = QApplication([])
    browser = Browser()  # Create browser instance
    browser.show()  # Display the browser window
    app.exec_()  # Start the Qt event loop

if __name__ == "__main__":
    main()
