from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Configuração do WebDriver com opções de cabeçalho (opcional)
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Descomente se quiser o modo headless
driver = webdriver.Chrome(options=options)

# Lista de URLs e termos de pesquisa
pesquisas = [
    ("https://www.kabum.com.br", "Notebook Dell G15"),
    ("https://www.kabum.com.br", "Samsung S23 FE"),
    ("https://www.kabum.com.br", "Positivo Vision R15")
]

# Função para buscar o preço
def buscar_preco(url, termo):
    driver.get(url)
    try:
        search_box = driver.find_element(By.ID, "input-busca")
        search_box.send_keys(termo)
        search_box.send_keys(Keys.RETURN)


        preco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-e5003a21-2.jfrbst.priceCard")))
        return preco.text
    except Exception as e:
        print(f"Error while fetching price for {termo} from {url}: {e}")
        return None


precos = []
for url, termo in pesquisas:
    preco = buscar_preco(url, termo)
    if preco:
        precos.append(f"{termo} ({url}): {preco}")
    else:
        precos.append(f"{termo} ({url}): Erro ao buscar preço")


for preco in precos:
    print(preco)

# Função para abrir o Bloco de Notas e anotar os preços
def anotar_precos(precos):


    with open("precos.txt", "w") as file:
        for preco in precos:
            file.write(preco + "\n")


    os.system("notepad.exe precos.txt")


anotar_precos(precos)


driver.quit()

