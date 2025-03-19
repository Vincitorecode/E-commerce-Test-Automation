from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Config:
    BASE_URL = "https://www.saucedemo.com"  # URL de la tienda ficticia
    DRIVER_PATH = r"C:\webdriver\chromedriver.exe"  # Ruta de tu chromedriver

    @staticmethod
    def get_driver():
        """Obtiene el driver de Chrome configurado"""
        service = Service(Config.DRIVER_PATH)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # Maximiza la ventana del navegador
        return webdriver.Chrome(service=service, options=options)

