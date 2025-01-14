import re

import pytest
from playwright.sync_api import Page, expect


# Using fixtures: https://playwright.dev/python/docs/writing-tests#using-fixtures
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("after the test runs")


def test_has_title(page: Page):
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
