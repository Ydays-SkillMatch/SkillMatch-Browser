import datetime
import os
import json
import requests

class Logger:
    def __init__(self):
        self.log_file = "browser_logs.json"
        self.logs = self.load_logs()

    def send_request(self, data):
        with open(self.log_file, "w") as file:
            json.dump(self.logs, file, indent=4)
        
        r = requests.post(url="http://localhost:8080/api/navdata/", data=data)
        print(r.text)


    def load_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as file:
                return json.load(file)
        return []

    def log_paste(self, shortcut):
        data = {
            "type": "pasted_data",
            "data": shortcut,
            "user": {
                "id": 1,
            },
            "timestamp": datetime.datetime.now(datetime.timezone.utc).timestamp()
        }
        self.logs.append(data)
        self.send_request(data=data)

    def log_navigation(self, url):
        data = {
            "type": "url",
            "data": url,
            "user": {
                "id": 1,
            },
            "timestamp": datetime.datetime.now(datetime.timezone.utc).timestamp()
        }
        self.logs.append(data)
        self.send_request(data=data)

    def log_download(self, download_item):
        data = {
            "type": "download",
            "data": download_item.url().toString(),
            "user": {
                "id": 1,
            },
            "timestamp": datetime.datetime.now(datetime.timezone.utc).timestamp()
        }
        self.logs.append(data)
        self.send_request(data=data)