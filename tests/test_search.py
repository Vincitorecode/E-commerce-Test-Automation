from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import Config

def test_search():
    driver = Config.get_driver()
    driver.get("https://www.saucedemo.com/")  # URL de la página de prueba
    print("Página de búsqueda abierta")

    # Login para poder buscar
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Buscar un producto
    search_box = driver.find_element(By.CLASS_NAME, "search_field")
    search_box.send_keys("Sauce Labs Backpack")
    search_box.send_keys(Keys.RETURN)

    # Verificar si el producto aparece en los resultados
    try:
        driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Backpack')]")
        print("Producto encontrado")
    except:
        print("Producto no encontrado")

    driver.quit()

if __name__ == "__main__":
    test_search()
