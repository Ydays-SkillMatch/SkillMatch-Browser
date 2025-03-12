from PyQt5.QtWidgets import QToolBar, QLineEdit, QAction
from PyQt5.QtCore import QUrl
from utils import validate_url


class Controls:
    def __init__(self, main_window):
        """
        Initializes the navigation toolbar with Back, Forward, Reload buttons and a URL bar.
        """
        self.main_window = main_window  # Reference to the main browser window

        # Create the toolbar
        self.toolbar = QToolBar("Navigation")

        # Back Button
        back_action = QAction("Back", main_window)
        back_action.triggered.connect(self.go_back)
        self.toolbar.addAction(back_action)

        # Forward Button
        forward_action = QAction("Forward", main_window)
        forward_action.triggered.connect(self.go_forward)
        self.toolbar.addAction(forward_action)

        # Reload Button
        reload_action = QAction("Reload", main_window)
        reload_action.triggered.connect(self.reload_page)
        self.toolbar.addAction(reload_action)

        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL and press Enter")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.url_bar)

    def update_url_bar(self, url):
        """
        Updates the URL bar when the user navigates to a new page.
        """
        self.url_bar.setText(url)

    def navigate_to_url(self):
        """
        Navigates to the URL entered in the address bar.
        """
        url = self.url_bar.text().strip()  # Remove any accidental spaces
        validated_url = validate_url(url)  # Ensure proper format
        browser = self.main_window.current_browser()
        if browser:
            browser.setUrl(validated_url)


    def go_back(self):
        """
        Navigates back in the browser history.
        """
        if self.main_window.current_browser():
            self.main_window.current_browser().back()

    def go_forward(self):
        """
        Navigates forward in the browser history.
        """
        if self.main_window.current_browser():
            self.main_window.current_browser().forward()

    def reload_page(self):
        """
        Reloads the current page.
        """
        if self.main_window.current_browser():
            self.main_window.current_browser().reload()
