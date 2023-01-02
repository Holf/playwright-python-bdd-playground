from playwright.sync_api import Page


class IsomorphicLabsWebPage:
    domain = 'www.isomorphiclabs.com'
    baseUrl = 'https://' + domain
    path = ''

    def __init__(self, page: Page) -> None:
        self.page = page
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

    def click_on_workWithUs(self) -> None:
        self.page.get_by_role(
            "link", name="work with us").first.click()
