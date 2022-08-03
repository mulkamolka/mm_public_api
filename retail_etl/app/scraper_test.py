import unittest
import pytest
import pytest_check as check
from app.scraper import PublicApiScraper

class PublicApiScraperTest(unittest.TestCase):

    @pytest.fixture
    def get_scraper(self):
        scraper = PublicApiScraper()
        return scraper

    
    def test_url(get_scraper):
        print(get_scraper)
        test_url = "http://openapi.seoul.go.kr:8088/4c63564f71726c6136384147526f4d/json/ListNecessariesPricesService/"
        assert  get_scraper._url == test_url

    
    def test_prev_lastitem_idx(get_scraper):
        
        assert get_scraper._prev_lastitem_idx == "0"
        