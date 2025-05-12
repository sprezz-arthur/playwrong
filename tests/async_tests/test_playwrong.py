from playwright.async_api import Browser as AsyncBrowser


async def test_async_browser(browser: AsyncBrowser) -> None:
    assert isinstance(browser, AsyncBrowser)
    page = await browser.new_page()
    await page.goto("https://www.google.com")
    await page.close()
