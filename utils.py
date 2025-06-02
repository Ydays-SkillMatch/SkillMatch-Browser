from PyQt5.QtCore import QUrl
import re

BLOCKED_URLS = [
    "https://chrome.google.com/webstore",
    "https://microsoftedge.microsoft.com/addons",
    "https://addons.mozilla.org",
    "chromewebstore.google.com"
]

def is_blocked_url(url):
    for blocked in BLOCKED_URLS:
        if url.startswith(blocked):
            return True
    return False

def is_valid_domain(domain):
    domain_regex = re.compile(
        r'^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,6}$' 
    )
    return bool(domain_regex.match(domain))

def validate_url(input_text: str):
    input_text = input_text.strip()

    if input_text.startswith(("http://", "https://")):
        return QUrl(input_text)

    if is_valid_domain(input_text):
        return QUrl(f"https://{input_text}")
    

    search_query = input_text.replace(" ", "+") 
    return QUrl(f"https://www.google.com/search?q={search_query}")
