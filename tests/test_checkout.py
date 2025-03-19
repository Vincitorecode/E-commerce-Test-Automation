from selenium.webdriver.common.by import By
from config import Config

def test_checkout():
    driver = Config.get_driver()
    driver.get("https://www.saucedemo.com/")  # URL de la página de prueba
    print("Página de checkout abierta")

    # Login para realizar el checkout
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Agregar un producto al carrito
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()

    # Ir al carrito y proceder al checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Ingresar información del checkout
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Finalizar compra
    driver.find_element(By.ID, "finish").click()

    print("Compra completada")

    driver.quit()

if __name__ == "__main__":
    test_checkout()
