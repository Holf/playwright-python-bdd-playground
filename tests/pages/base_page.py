from playwright.sync_api import Page, expect
import time


class IsomorphicLabsBasePage:
    domain = 'www.isomorphiclabs.com'
    baseUrl = 'https://' + domain
    path = ''
    page_title = ''

    def __init__(self, page: Page, assert_snapshot) -> None:
        self.page = page
        self.assert_snapshot = assert_snapshot
        self.__set_cookieBannerDismissed_state()

        self.url = self.__get_url()

    def __set_cookieBannerDismissed_state(self) -> None:
        self.page.context.add_cookies(
            [{'domain': self.domain,
             'path': '/',
              'name': 'CookieConsent',
              'value': '{stamp:%27PkEKxWD2rmtylS/JL2c09GB6n9jWO7PfXW17YxKg1OzCF8D2a1rdow==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1672612493420%2Cregion:%27gb%27}'}])

    def __get_url(self) -> str:
        return self.baseUrl + '/' + self.path

    def load(self) -> None:
        self.page.goto(self.url)

    def verify_page_title(self) -> None:
        expect(self.page).to_have_title(self.page_title)

    def verify_visual_snapshot(self) -> None:
        # TODO: Sleeps are evil. With more time I'd find a
        # way to know when the page is ready for snapshotting.
        time.sleep(3)
        self.assert_snapshot(self.page.screenshot(path="goob.png"))

    def click_on_workWithUs(self) -> None:
        self.page.get_by_role(
            "link", name="work with us").first.click()
