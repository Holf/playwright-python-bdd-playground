from playwright.sync_api import Page
from .base_page import IsomorphicLabsBasePage


class IsomorphicLabsWorkWithUsPage(IsomorphicLabsBasePage):
    path = 'work-with-us'
    page_title = 'Work With Us - Isomorphic Labs'

    def __init__(self, page: Page, assert_snapshot, browser_type) -> None:
        super().__init__(page, assert_snapshot, browser_type)

