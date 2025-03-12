import datetime
import os
import json

class Logger:
    def __init__(self):
        self.log_file = "browser_logs.json"
        self.logs = self.load_logs()

    def save_logs(self):
        with open(self.log_file, "w") as file:
            json.dump(self.logs, file, indent=4)

    def load_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as file:
                return json.load(file)
        return []

    def log_paste(self, shortcut):
        data = {
            "pasted_data": shortcut,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        self.logs.append(data)
        self.save_logs()

    def log_navigation(self, url):
        data = {
            "url": url,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        self.logs.append(data)
        self.save_logs()

    def log_download(self, download_item):
        data = {
            "download": download_item.url().toString(),
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        self.logs.append(data)
        self.save_logs()