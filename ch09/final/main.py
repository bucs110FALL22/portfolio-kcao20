from AnimeChanAPI import AnimeChan  # Proxy Class
from IMDbAPI import IMDb  # Proxy Class


def main():
    ac_api = AnimeChan()
    response = int(
        input(
            "Enter 0 for a random anime \nEnter 1 to search by anime \nEnter 2 to search by character\n"
        )
    )
    if response == 1:
        while True:
            anime = input("Enter the name of the anime: ")
            ac_api.findAnime(anime)
            results = ac_api.get()
            if results == None:
                print("The anime could not be found.")
            else:
                break
    elif response == 2:
        while True:
            character = input("Enter the name of the character: ")
            ac_api.findCharacter(character)
            results = ac_api.get()
            if results == None:
                print("The character could not be found.")
            else:
                break
    else:
        results = ac_api.get()
    anime = results["anime"]
    character = results["character"]
    quote = results["quote"]
    id = get_show_id(anime)
    if id == None:
        print(f"IMDb does not have any data on {anime}")
    else:
        print(show_description(id))
    print(f'{character} from {anime} says, "{quote}"')


def show_description(id):
    """
    Returns a formatted description of show information
    args: str id
    return: str description
    """
    rating, title, genres, plot = get_show_info(id)
    description = (
        f"{title} has a score of {rating} on IMDb\nGenres: {genres}\nPlot: {plot}"
    )
    return description


def get_show_id(anime="naruto"):
    """
    Grabs the IMDb show id using a search function and grabbing the first result
    agrs: str anime
    return: str id
    """
    imdb_api = IMDb()
    imdb_api.search_series(anime)
    results = imdb_api.get()
    if len(results["results"]) == 0:
        id = None
    else:
        id = results["results"][0]["id"]
    return id


def get_show_info(id):
    """
    Grabs info about the show from IMDb using an IMDb id
    args: str id
    return: str rating, str title, str genres, str plot
    """
    imdb_api = IMDb()
    imdb_api.series_info(id)
    info = imdb_api.get()
    rating = info["imDbRating"]
    title = info["fullTitle"]
    genres = info["genres"]
    plot = info["plot"]
    return rating, title, genres, plot


if __name__ == "__main__":
    main()
