from typing import Dict
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--use-non-playwright-chromium",
        action="store",
        default="false",
        help="Use preinstalled Chromium instead of the the Playwright-bundled version")


def __get_is_non_playwright_chromium_specified(request):
    return request.config.getoption("--use-non-playwright-chromium").lower() == "true"


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: Dict, request) -> Dict:
    if __get_is_non_playwright_chromium_specified(request):
        return {**browser_type_launch_args, "executable_path": "/usr/bin/chromium-browser"}

    return browser_type_launch_args
