from playwright.sync_api import Page
from .base_page import IsomorphicLabsBasePage


class IsomorphicLabsHomePage(IsomorphicLabsBasePage):
    page_title = 'Reimagining Drug Discovery Process with AI - Isomorphic Labs'

    def __init__(self, page: Page, assert_snapshot) -> None:
        super().__init__(page, assert_snapshot)
