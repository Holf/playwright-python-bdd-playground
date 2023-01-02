from playwright.sync_api import Page
from .base_page import IsomorphicLabsWebPage


class IsomorphicLabsHomePage(IsomorphicLabsWebPage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.workWithUs_link = page.get_by_role(
            "link", name="work with us").first
