import sys
from typing import Dict
import pytest

from playwright.sync_api import Page
from pages.home_page import IsomorphicLabsHomePage
from pages.work_with_us_page import IsomorphicLabsWorkWithUsPage


@pytest.fixture
def home_page(page: Page) -> IsomorphicLabsHomePage:
    return IsomorphicLabsHomePage(page)


@pytest.fixture
def work_with_us_page(page: Page) -> IsomorphicLabsWorkWithUsPage:
    return IsomorphicLabsWorkWithUsPage(page)


def pytest_addoption(parser):
    parser.addoption("--use-non-playwright-chromium",
                     action="store", default="false", help="Playwright will try to use installed Chromium instead of the the Playwright-bundled version")


def __get_is_non_playwright_chromium_specified(request):
    return request.config.getoption("--use-non-playwright-chromium").lower() == "true"


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict, request) -> Dict:
    if __get_is_non_playwright_chromium_specified(request):
        return {**browser_type_launch_args, "executable_path": "/usr/bin/chromium-browser"}

    return browser_type_launch_args
