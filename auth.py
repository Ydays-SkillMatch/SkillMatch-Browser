import requests
import json

class AuthManager:
    def __init__(self):
        self.login_url = "http://localhost:8080/api/auth/login/"
        self.refresh_url = "http://localhost:8080/api/auth/refresh/"
        self.access_token = None
        self.refresh_token = None
        self.id = None

    def login(self, email, password):
        response = requests.post(self.login_url, json={
            "email": email,
            "password": password
        })

        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access")
            self.refresh_token = data.get("refresh")
            self.id =  data.get("id")
            print(f"✅ Logged in as user {self.id}")
            return True
        else:
            print(f"❌ Login failed: {response.text}")
            return False

    def refresh(self):
        response = requests.post(self.refresh_url, json={
            "refresh": self.refresh_token
        })

        if response.status_code == 200:
            self.access_token = response.json().get("access")
            print("🔄 Token refreshed")
            return True
        else:
            print("❌ Refresh failed")
            return False
