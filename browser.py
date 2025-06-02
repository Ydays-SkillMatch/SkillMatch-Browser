from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QToolButton, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings 
from PyQt5.QtWebEngineCore import QWebEngineCookieStore
from PyQt5.QtNetwork import QNetworkCookie
from PyQt5.QtGui import QKeyEvent
from controls import Controls
from logger import Logger
from utils import is_blocked_url


class Browser(QMainWindow):
    def __init__(self, user_id, access_token):
        super().__init__()
        self.user_id = user_id
        self.access_token = access_token
        self.last_pasted = ""

        self.setWindowTitle("Modular Browser")
        self.resize(1024, 768)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.add_new_tab_button()

        self.setCentralWidget(self.tabs)

        self.logger = Logger(user_id=user_id, access_token=access_token)

        self.controls = Controls(main_window=self)
        self.addToolBar(self.controls.toolbar)

        self.add_new_tab("https://www.google.com", "SkillMatch")

        QApplication.instance().installEventFilter(self)

    def eventFilter(self, obj, event):
        if isinstance(event, QKeyEvent):
            if event.key() == Qt.Key_V and event.modifiers() & Qt.ControlModifier:
                pasted_text = QApplication.clipboard().text()
                if pasted_text != self.last_pasted:
                    self.logger.log_paste(pasted_text)
                    self.last_pasted = pasted_text
        return super().eventFilter(obj, event)

    def add_new_tab_button(self):
        new_tab_button = QToolButton()
        new_tab_button.setText("+")
        new_tab_button.setToolTip("New Tab")
        new_tab_button.clicked.connect(self.open_new_tab)
        self.tabs.setCornerWidget(new_tab_button)

    def add_new_tab(self, url, label):
        browser = QWebEngineView()
        browser.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        browser.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        browser.setUrl(QUrl(url))
        # profile = browser.page().profile()
        # cookie_store = profile.cookieStore()
        
        # cookie = QNetworkCookie()
        # cookie.setName(b"SkillMatchToken")
        # cookie.setValue(self.access_token.encode()) 
        # cookie.setDomain("localhost") 
        # cookie.setPath("/")
        # cookie.setHttpOnly(True)
        # cookie.setSecure(False) 

        # cookie_store.setCookie(cookie, QUrl("https://skillmatch.albanagisa.fr"))
        
        

        browser.urlChanged.connect(lambda url, browser=browser: self.check_blocked_url(url, browser))
        browser.titleChanged.connect(lambda title, browser=browser: self.update_tab_title(title, browser))
        browser.urlChanged.connect(lambda url, browser=browser: self.logger.log_navigation(url.toString()))
        browser.urlChanged.connect(lambda url, browser=browser: self.update_url_bar(url, browser))

        index = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(index)

    def check_blocked_url(self, url, browser):
        if is_blocked_url(url.toString()):
            browser.setUrl(QUrl("about:blank")) 

    def update_tab_title(self, title, browser):
        index = self.tabs.indexOf(browser)
        if index != -1: 
            self.tabs.setTabText(index, title)

    def update_url_bar(self, url, browser):
        if browser == self.current_browser():
            formatted_url = url.toString()
            if formatted_url.startswith("https://"):
                formatted_url = formatted_url.replace("https://", "")
            elif formatted_url.startswith("http://"):
                formatted_url = formatted_url.replace("http://", "")
            self.controls.update_url_bar(formatted_url)


    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def current_browser(self):
        return self.tabs.currentWidget()
    
    def open_new_tab(self):
        self.add_new_tab("https://www.google.com", "New Tab")
