import datetime
import json

class Logger:
    def __init__(self):
        self.log_file = "browser_logs.json"

    def log_paste(self, shortcut):
        data = {
            "pasted_data": shortcut,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        jsondata = json.dumps(data, indent=4)
        with open(self.log_file, "a") as f:
            f.write(jsondata + ", \n")
        print(jsondata.__str__())

    def log_navigation(self, url):
        data = {
            "url": url,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        jsondata = json.dumps(data, indent=4)
        with open(self.log_file, "a") as f:
            f.write(jsondata + ", \n")
        print(jsondata.__str__())

    def log_download(self, download_item):
        data = {
            "download": download_item.url().toString(),
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        jsondata = json.dumps(data, indent=4)
        with open(self.log_file, "a") as f:
            f.write(jsondata + ", \n")
        print(jsondata.__str__())