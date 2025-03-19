from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config
import time

def test_add_to_cart():
    # Inicializar el WebDriver
    driver = Config.get_driver()
    
    # Abrir la página de prueba
    driver.get("https://www.saucedemo.com/")  # URL de la página de prueba
    print("Página de carrito abierta")

    # Login para poder agregar productos al carrito
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Espera explícita para asegurarse de que la página haya cargado
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inventory_container"))
    )
    print("Login exitoso")

    # Agregar un producto al carrito
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    print("Producto agregado al carrito")

    # Espera explícita para que el icono del carrito aparezca
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    
    # Verificar si el carrito tiene el producto
    try:
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1", f"El carrito no tiene 1 producto, tiene {cart_badge.text}"
        print("Producto agregado al carrito correctamente")
    except Exception as e:
        print("Error al agregar el producto al carrito:", e)

    # Cerrar el navegador
    driver.quit()

if __name__ == "__main__":
    test_add_to_cart()
