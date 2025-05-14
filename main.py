from PyQt5.QtWidgets import QApplication, QDialog
from browser import Browser
from login_dialog import LoginDialog
from auth import AuthManager

def main():
    app = QApplication([])
    auth = AuthManager()
    login_dialog = LoginDialog(auth_manager=auth)
    if login_dialog.exec_() == QDialog.Accepted:
        browser = Browser(user_id=auth.id, access_token=auth.access_token)
        browser.show()
        app.exec_()
    else:
        print("Login failed. Exiting application.")
    

if __name__ == "__main__":
    main()
