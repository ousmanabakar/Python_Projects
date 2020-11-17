import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/chart/top/"

response = requests.get(URL)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

film_titles = soup.find_all("td", {"class": "titleColumn"})

film_ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})


wanted_rating = float(input("Enter a rating:"))

for title, rating in zip(film_titles, film_ratings):

    title = title.text
    rating = rating.text

    title = title.strip()
    title = title.replace("\n", "")

    rating = rating.strip()
    rating = rating.replace("\n", "")

    if float(rating) > wanted_rating:
        print(f"Title:{title}\nRating:{rating}")
