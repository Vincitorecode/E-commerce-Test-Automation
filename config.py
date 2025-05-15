from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Config:
    BASE_URL = "https://www.saucedemo.com"  # URL de la tienda ficticia

    @staticmethod
    def get_driver():
        """Obtiene el driver de Chrome usando webdriver-manager"""
        options = Options()
        options.add_argument("--start-maximized")  # Maximiza la ventana del navegador
        # Puedes agregar más opciones aquí si necesitas
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)


