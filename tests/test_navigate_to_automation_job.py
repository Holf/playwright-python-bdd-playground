from pages.home_page import IsomorphicLabsHomePage
from pages.work_with_us_page import IsomorphicLabsWorkWithUsPage
from playwright.sync_api import expect, Page


def test_navigate_to_workWithUs_page(
        page: Page,
        home_page: IsomorphicLabsHomePage) -> None:

    # Given the Isomorphic Labs home page is displayed
    home_page.load()

    # When the user clicks on 'Work With Us'
    home_page.click_on_workWithUs()

    # Then they should be taken to the 'Work With Us' page
    expect(page).to_have_title('Work With Us - Isomorphic Labs')


def test_navigate_to_automation_job(
        page: Page,
        work_with_us_page: IsomorphicLabsWorkWithUsPage) -> None:

    # Given the Isomorphic Labs home page is displayed
    work_with_us_page.load()

    # Then they should be taken to the 'Work With Us' page
    expect(page).to_have_title('Work With Us - Isomorphic Labs')
