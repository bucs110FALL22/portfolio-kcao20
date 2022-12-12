import requests


class AnimeChan:
    def __init__(self):
        """
        Creates an AnimeChan API proxy class
        """
        self.url = "https://animechan.vercel.app/api/random"

    def get(self):
        """
        Queries the API for a response and returns it
        return: dict response
        """
        r = requests.get(self.url)
        if r.status_code != 404:
            response = r.json()
            return response
        else:
            return None

    def findCharacter(self, character):
        """
        Changes the api to search for characters
        args: str character
        """
        self.url = f"https://animechan.vercel.app/api/random/character?name={character}"

    def findAnime(self, anime):
        """
        Changes the api to search for anime titles
        args: str anime
        """
        self.url = f"https://animechan.vercel.app/api/random/anime?title={anime}"

    def __str__(self) -> str:
        """
        Replaces the __str__ magic method to print information about the class
        return: str self.url
        """
        return f"AnimeChan({self.url})"
