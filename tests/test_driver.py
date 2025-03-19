import sys
import os

# Agregar el directorio raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import Config  # Ahora debería funcionar

driver = Config.get_driver()
driver.get(Config.BASE_URL)
print("Chrome se abrió correctamente")
driver.quit()
