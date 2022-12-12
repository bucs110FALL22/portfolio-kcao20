import requests

API_KEY = "k_e9nq7rzk"


class IMDb:
    def __init__(self, action="search", expression="naruto"):
        """
        Creates a IMDb API proxy class
        args: str action, str expression
        """
        self.url = f"https://imdb-api.com/en/API/{action}/{API_KEY}/{expression}"

    def get(self):
        """
        Queries the API for a response and returns it
        return: dict response
        """
        r = requests.get(self.url)
        response = r.json()
        return response

    def search_series(self, title):
        """
        Changes the requestt url to search for a title
        args: str title
        """
        self.url = f"https://imdb-api.com/en/API/Search/{API_KEY}/{title}"

    def series_info(self, id):
        """
        Changes the request url to grab data on a show id
        args: str id
        """
        self.url = f"https://imdb-api.com/en/API/Title/{API_KEY}/{id}"

    def __str__(self) -> str:
        """
        Replaces the __str__ magic method to print information about the class
        return: str self.url
        """
        return f"IMDbAPI({self.url})"
