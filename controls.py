from PyQt5.QtWidgets import QToolBar, QLineEdit, QAction, QMenu, QPushButton
from PyQt5.QtCore import QUrl
from utils import validate_url
from favorites import Favorites


class Controls:
    def __init__(self, main_window):
        self.main_window = main_window 
        self.favorites_manager = Favorites()

        self.toolbar = QToolBar("Navigation")
        self.toolbar.setContextMenuPolicy(0)

        back_action = QAction("Back", main_window)
        back_action.triggered.connect(self.go_back)
        self.toolbar.addAction(back_action)

        forward_action = QAction("Forward", main_window)
        forward_action.triggered.connect(self.go_forward)
        self.toolbar.addAction(forward_action)

        reload_action = QAction("Reload", main_window)
        reload_action.triggered.connect(self.reload_page)
        self.toolbar.addAction(reload_action)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL and press Enter")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.url_bar)
        
        favorite_button = QPushButton("★")
        favorite_button.setToolTip("Add to Favorites")
        favorite_button.clicked.connect(self.add_to_favorites)
        self.toolbar.addWidget(favorite_button)

        self.favorites_menu = QMenu("Favorites", main_window)
        favorites_button = QPushButton("📂") 
        favorites_button.setMenu(self.favorites_menu)
        self.toolbar.addWidget(favorites_button)
        self.load_favorites_menu()

    def contextMenuEvent(self, event):
        event.ignore()

    def update_url_bar(self, url):
        self.url_bar.setText(url)

    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        validated_url = validate_url(url)
        browser = self.main_window.current_browser()
        if browser:
            browser.setUrl(validated_url)


    def go_back(self):
        if self.main_window.current_browser():
            self.main_window.current_browser().back()

    def go_forward(self):
        if self.main_window.current_browser():
            self.main_window.current_browser().forward()

    def reload_page(self):
        if self.main_window.current_browser():
            self.main_window.current_browser().reload()

    def add_to_favorites(self):
        browser = self.main_window.current_browser()
        if browser:
            url = browser.url().toString()
            title = browser.page().title()
            self.favorites_manager.add_favorite(title, url)
            self.load_favorites_menu()  # Update the menu

    def load_favorites_menu(self):
        self.favorites_menu.clear()
        for fav in self.favorites_manager.get_favorites():
            action = QAction(fav["title"], self.main_window)
            action.triggered.connect(lambda checked, url=fav["url"]: self.open_favorite(url))
            self.favorites_menu.addAction(action)

    def open_favorite(self, url):
        browser = self.main_window.current_browser()
        if browser:
            browser.setUrl(validate_url(url))

    def remove_favorite(self, url):
        self.favorites_manager.remove_favorite(url)
        self.load_favorites_menu() 
