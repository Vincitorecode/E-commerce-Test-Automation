import pytest
from selenium.common.exceptions import NoSuchElementException
from config import Config
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = Config.get_driver()
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Validar que el login fue exitoso
    try:
        assert login_page.is_logged_in(), "No se encontró el logo, login fallido"
    except NoSuchElementException:
        pytest.fail("Login fallido: Elemento no encontrado")

