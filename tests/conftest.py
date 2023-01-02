import pytest

from pages.home_page import IsomorphicLabsHomePage
from pages.work_with_us_page import IsomorphicLabsWorkWithUsPage
from playwright.sync_api import Page

@pytest.fixture
def home_page(page: Page) -> IsomorphicLabsHomePage:
    return IsomorphicLabsHomePage(page)

@pytest.fixture
def work_with_us_page(page: Page) -> IsomorphicLabsWorkWithUsPage:
    return IsomorphicLabsWorkWithUsPage(page)