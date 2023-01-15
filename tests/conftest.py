import pytest

from playwright.sync_api import Page
from pages.home_page import IsomorphicLabsHomePage
from pages.work_with_us_page import IsomorphicLabsWorkWithUsPage

from colab_utils.setup_non_playwright_chromium_option import *


@pytest.fixture
def home_page(page: Page, assert_snapshot) -> IsomorphicLabsHomePage:
    return IsomorphicLabsHomePage(page, assert_snapshot)


@pytest.fixture
def work_with_us_page(page: Page, assert_snapshot) -> IsomorphicLabsWorkWithUsPage:
    return IsomorphicLabsWorkWithUsPage(page, assert_snapshot)
