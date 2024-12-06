from .unsplash_scraper import UnsplashScraper
from .pexels_scraper import PexelsScraper


class ScraperFactory:
    scrapers = [UnsplashScraper(), PexelsScraper()]

    def execute(self):
        for scraper in self.scrapers:
            scraper.run()


if __name__ == "__main__":
    ScraperFactory().execute()
