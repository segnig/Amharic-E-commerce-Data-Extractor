import unittest
from src.scraper import scrape_data

class TestScraper(unittest.TestCase):
    def test_scrape_data(self):
        # This is a placeholder test.
        # TODO: Add a real test with a mock URL and expected data.
        url = "http://example.com"
        data = scrape_data(url)
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main() 