from selenium import webdriver
from config import Config
from pages.login_page import LoginPage
import pytest

# Test de Login
def test_login():
    # Crear una instancia del WebDriver desde la configuración
    driver = Config.get_driver()

    # Abrir la página de login (utilizamos la URL de Sauce Demo para este ejemplo)
    driver.get(Config.BASE_URL)  # Esto tomará la URL que hayas configurado en config.py

    # Crear una instancia de la página de login
    login_page = LoginPage(driver)

    # Realizar el login con usuario y contraseña de prueba
    login_page.login("standard_user", "secret_sauce")  # Usamos un usuario y contraseña válidos

    # Verificar que la página cargó correctamente después de iniciar sesión
    assert login_page.is_login_successful(), "El login falló o no se redirige correctamente después de iniciar sesión."

    # Cerrar el navegador después de la prueba
    driver.quit()

