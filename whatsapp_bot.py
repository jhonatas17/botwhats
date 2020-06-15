from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class WhatsappBot:
    def __init__(self):
        # Parte 5 - A mensagem que você quer enviar
        self.mensagem = "BINO não é cilada não, vamos fazer uma jornada financeira sim. https://www.youtube.com/watch?v=u-ohv2XchFs"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Hackathon CCR"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver', chrome_options=options)

    def EnviarMensagens(self):
	    self.driver.get('https://web.whatsapp.com')
	    time.sleep(5)
	    for grupo_ou_pessoa in self.grupos_ou_pessoas:
	        campo_grupo = self.driver.find_element_by_xpath(
	            f"//span[@title='{grupo_ou_pessoa}']")
	        time.sleep(5)
	        campo_grupo.click()
	        chat_box = self.driver.find_element_by_class_name('_2FVVk._2UL8j')
	        time.sleep(5)
	        chat_box.click()
	        chat_box.send_keys(self.mensagem)
	        botao_enviar = self.driver.find_element_by_xpath(
	            "//span[@data-icon='send']")
	        time.sleep(5)
	        botao_enviar.click()
	        time.sleep(30)

bot = WhatsappBot()
bot.EnviarMensagens()