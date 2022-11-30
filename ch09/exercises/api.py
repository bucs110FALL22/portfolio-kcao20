import requests


def main():
    api_url = "https://animechan.vercel.app/api/random"
    response = requests.get(api_url).json()
    print(
        f'{response["character"]} from {response["anime"]} says, "{response["quote"]}"'
    )


if __name__ == "__main__":
    main()
