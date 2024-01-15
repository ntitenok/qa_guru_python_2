import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    print("Настроить разрешение браузера 1920 на 1080")

    yield
    browser.quit()
    print("Закрыть браузер")
