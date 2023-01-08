from typing import Dict, Generator

import pytest

from pages.home_page import IsomorphicLabsHomePage
from pages.work_with_us_page import IsomorphicLabsWorkWithUsPage
from playwright.sync_api import BrowserType, Browser, Page


@pytest.fixture
def home_page(page: Page) -> IsomorphicLabsHomePage:
    return IsomorphicLabsHomePage(page)


@pytest.fixture
def work_with_us_page(page: Page) -> IsomorphicLabsWorkWithUsPage:
    return IsomorphicLabsWorkWithUsPage(page)


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):

    print(browser_type_launch_args)
    return {**browser_type_launch_args, "executable_path": "/usr/bin/chromium-browser"}
