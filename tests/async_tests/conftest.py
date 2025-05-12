from pytest_playwright_asyncio.pytest_playwright import pytest_addoption
from pytest_playwright_asyncio.pytest_playwright import *  # noqa: F403

del pytest_addoption  # delete so it's unified on the upper conftest
