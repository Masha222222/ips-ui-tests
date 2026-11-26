from uuid import uuid4

import pytest
from playwright.sync_api import sync_playwright

from pages.dashboard_page import DashboardPage


UI_TIMEOUT_MS = 30_000


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    page.set_default_timeout(UI_TIMEOUT_MS)
    return page


@pytest.fixture
def test_pump_id():
    return f"ui-test-{uuid4().hex[:12]}"


@pytest.fixture
def dashboard(page):
    return DashboardPage(page)