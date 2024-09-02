from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Solicitar ao usuário que insira seu nome
nome = input("Por favor, insira o nome da cidade desejada: ")

# site desejado
url = "https://www.google.com.br/maps"

# id da caixa de pesquisa
id_input = "searchboxinput"

# id para pesquisar
id_pesquisar = "searchbox-searchbutton"

# navegador desejado
nav = webdriver.Chrome()

# entra no site
nav.get(url)

# encontra os elementos necessários
input = nav.find_element(By.ID, id_input)

# qual cidade você quer?
print(input.send_keys(nome))

# escreve a cidade
pesquisar = nav.find_element(By.ID, id_pesquisar)

# clica para pesquisar
pesquisar.click()

sleep(30)
