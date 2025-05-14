import json
import os

class Favorites:
    def __init__(self):
        self.favorites_file = "favorites.json"
        self.favorites = self.load_favorites()

    def load_favorites(self):
        if os.path.exists(self.favorites_file):
            with open(self.favorites_file, "r") as file:
                return json.load(file)
        return []

    def save_favorites(self):
        with open(self.favorites_file, "w") as file:
            json.dump(self.favorites, file, indent=4)

    def add_favorite(self, title, url):
        if not any(fav["url"] == url for fav in self.favorites):
            self.favorites.append({"title": title, "url": url})
            self.save_favorites()

    def remove_favorite(self, url):
        self.favorites = [fav for fav in self.favorites if fav["url"] != url]
        self.save_favorites()

    def get_favorites(self):
        return self.favorites
    
    def is_favorite(self, url):
        return any(fav["url"] == url for fav in self.favorites)
