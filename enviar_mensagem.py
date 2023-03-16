import time
import pandas as pd
from selenium import webdriver
import urllib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

contatos_df = pd.read_excel('Enviar.xlsx')

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")


while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)


for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(1)

    navegador.find_element(
        By.XPATH, './/*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span'
    ).send_keys(Keys.ENTER)

