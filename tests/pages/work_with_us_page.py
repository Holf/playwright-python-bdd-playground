from playwright.sync_api import Page
from .base_page import IsomorphicLabsWebPage


class IsomorphicLabsWorkWithUsPage(IsomorphicLabsWebPage):
    path = 'work-with-us'

    def __init__(self, page: Page) -> None:
        super().__init__(page)

