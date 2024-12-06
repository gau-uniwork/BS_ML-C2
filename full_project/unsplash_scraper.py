import requests
from .base import Scraper

search_url = (
    "https://unsplash.com/napi/search/photos?page={page}&per_page=20"
    + "&plus=none&query={query}&xp=search-region-awareness%3Aexperiment"
)
total_pages = 5


class UnsplashScraper(Scraper):
    def get_image_urls(self):
        images = []

        for query in ["happy person", "sad person"]:
            for page in range(total_pages):
                print(f"scraped pages: {page + 1} - {total_pages}")
                url = search_url.format(page=page + 1, query=query)
                response = requests.get(url)
                for image in response.json()["results"]:
                    images.append({"url": image["urls"]["small"], "slug": image["slug"], "query": query.split()[0]})
        return images

    def dowload_images(self, images):
        for idx, image in enumerate(images):
            print(f"downloading {idx + 1} - {len(images)}")
            response = requests.get(image["url"])
            with open(f"./images/{image["query"]}/{image["slug"]}", "wb") as f:
                f.write(response.content)

    def run(self):
        print("running unsplash scraper")
        images = self.get_image_urls()
        self.dowload_images(images)


if __name__ == "__main__":
    scraper = UnsplashScraper()
    scraper.run()
