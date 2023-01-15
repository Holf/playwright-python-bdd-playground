from pages.home_page import IsomorphicLabsHomePage
from pages.work_with_us_page import IsomorphicLabsWorkWithUsPage
from playwright.sync_api import expect, Page
from pytest_bdd import scenario, given, when, then


@scenario('navigation.feature',
          'user can navigate from the Home page to the Work With Us page')
def test_is_starting():

    print('Starting')


@given("the Isomorphic Labs home page is displayed")
def load_home_page(
        home_page: IsomorphicLabsHomePage) -> None:

    home_page.load()


@when("the user clicks on Work With Us")
def click_on_work_with_us(
        home_page: IsomorphicLabsHomePage) -> None:

    home_page.click_on_workWithUs()

@then("they should be taken to the Work With Us page")
def check_page_title(
        work_with_us_page: IsomorphicLabsWorkWithUsPage) -> None:

    work_with_us_page.verify_page_title()
