from PyQt5.QtCore import QUrl
import re

def is_valid_domain(domain):
    """
    Checks if the input is a valid domain (e.g., 'example.com').
    """
    domain_regex = re.compile(
        r'^(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,6}$'  # Domain format check
    )
    return bool(domain_regex.match(domain))

def validate_url(input_text: str):
    """
    Ensures a valid URL format. If the input isn't a URL or domain, it converts it into a Google Search.
    """
    input_text = input_text.strip()

    # Check if input starts with http/https
    if input_text.startswith(("http://", "https://")):
        return QUrl(input_text)

    # Check if input is a valid domain (e.g., "example.com")
    if is_valid_domain(input_text):
        return QUrl(f"https://{input_text}")
    
    if "chrome" in input_text :
        return QUrl(f"https://www.google.com/")

    # If input isn't a valid URL or domain, treat it as a Google search
    search_query = input_text.replace(" ", "+")  # Convert spaces to "+"
    return QUrl(f"https://www.google.com/search?q={search_query}")
