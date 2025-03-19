from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import Config

def test_login():
    driver = Config.get_driver()
    driver.get("https://www.saucedemo.com/")  # URL de la página de prueba
    print("Página de login abierta")

    # Encontrar los campos de usuario y contraseña
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Ingresar usuario y contraseña válidos
    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button.click()

    # Verificar si el login fue exitoso (se debe ver el logo de Sauce Labs)
    try:
        driver.find_element(By.CLASS_NAME, "app_logo")
        print("Login exitoso")
    except:
        print("Login fallido")

    driver.quit()

if __name__ == "__main__":
    test_login()
