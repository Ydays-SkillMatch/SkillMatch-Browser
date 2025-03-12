import json
import os

class Favorites:
    def __init__(self):
        """
        Initializes the favorites system.
        Loads favorites from a JSON file.
        """
        self.favorites_file = "favorites.json"
        self.favorites = self.load_favorites()

    def load_favorites(self):
        """
        Loads favorites from a file if it exists; otherwise, returns an empty list.
        """
        if os.path.exists(self.favorites_file):
            with open(self.favorites_file, "r") as file:
                return json.load(file)
        return []

    def save_favorites(self):
        """
        Saves the favorites list to a JSON file.
        """
        with open(self.favorites_file, "w") as file:
            json.dump(self.favorites, file, indent=4)

    def add_favorite(self, title, url):
        """
        Adds a new favorite if it's not already in the list.
        """
        if not any(fav["url"] == url for fav in self.favorites):  # Avoid duplicates
            self.favorites.append({"title": title, "url": url})
            self.save_favorites()
            print(f"Added to favorites: {title} - {url}")

    def remove_favorite(self, url):
        """
        Removes a favorite by URL.
        """
        self.favorites = [fav for fav in self.favorites if fav["url"] != url]
        self.save_favorites()
        print(f"Removed from favorites: {url}")

    def get_favorites(self):
        """
        Returns the list of saved favorites.
        """
        return self.favorites
