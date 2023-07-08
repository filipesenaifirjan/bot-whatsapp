from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import keys
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(50)

contatos = ['Filipe']
mensagem = 'Olá, sou um robô!'

def buscar_contato(contato):
  campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
time.sleep(3)
campo_pesquisa.click()
campo_pesquisa.send_keys(contato)
campo_pesquisa.send_keys(keys.ENTER)
time.sleep(5)

def enviar_mensagem(mensagem):
  campo_mensagem = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
  campo_mensagem[1].click()
  time.sleep(3)
  campo_mensagem[1].send_keys(mensagem)
  campo_mensagem[1].send_keys(keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    #enviar_mensagem(mensagem)    
