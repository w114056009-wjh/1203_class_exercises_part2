
import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    all_movies = []
    for page in range(1, 11):
        url = f"https://ssr1.scrape.center/page/{page}"
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")
        for item in soup.find_all("div", class_="el-card__body"):
            title = item.find("h2", class_="m-b-sm").text.strip()
            image_url = item.find("img", class_="cover")["src"]
            score = item.find("p", class_="score").text.strip()
            genres = [g.text for g in item.find_all("div", class_="categories")[0].find_all("span")]
            all_movies.append({
                "電影名稱": title,
                "電影圖片 URL": image_url,
                "評分": score,
                "類型": ", ".join(genres)
            })
    df = pd.DataFrame(all_movies)
    df.to_csv("movie.csv", index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    main()
