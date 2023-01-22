from pages.work_with_us_page import IsomorphicLabsWorkWithUsPage
from pytest_bdd import scenario, when, then


@scenario('workWithUs_page_layout.feature',
          'user can see the Work With Us page')
def test_workWithUs_page_layout():
    pass

@when("the user is on the Work With Us page")
def click_on_work_with_us(
        work_with_us_page: IsomorphicLabsWorkWithUsPage) -> None:

    work_with_us_page.load()


@then("they should see the expected page layout")
def verify_snapshot(
        work_with_us_page: IsomorphicLabsWorkWithUsPage) -> None:

    work_with_us_page.verify_visual_snapshot("work_with_us")
