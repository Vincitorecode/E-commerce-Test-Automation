from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")  # ID del campo de usuario en Sauce Demo
        self.password_field = (By.ID, "password")  # ID del campo de contraseña
        self.login_button = (By.ID, "login-button")  # ID del botón de login

    def login(self, username, password):
        """Rellena los campos de usuario y contraseña y hace clic en el botón de login"""
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        """Verifica si el login fue exitoso verificando si la página tiene un elemento específico"""
        return "PRODUCTS" in self.driver.page_source  # Verifica que se cargue la página de productos
