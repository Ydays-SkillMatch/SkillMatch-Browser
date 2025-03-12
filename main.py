from PyQt5.QtWidgets import QApplication
from browser import Browser

def main():
    app = QApplication([])
    browser = Browser()  
    browser.show()  
    app.exec_() 

if __name__ == "__main__":
    main()
