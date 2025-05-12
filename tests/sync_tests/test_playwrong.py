from playwright.sync_api import Browser as SyncBrowser


def test_sync_browser(browser: SyncBrowser) -> None:
    assert isinstance(browser, SyncBrowser)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.close()
