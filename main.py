from selenium import webdriver
import time

class Check:
    def __init__(self,name):
        self.bot=webdriver.Firefox()
        self.name=name

    def openSite(self):
        bot=self.bot
        bot.get("https://crackwatch.com/search")
        time.sleep(3)

        #Removing the Overlay window
        noads=bot.find_element_by_class_name("overlay-button")
        noads.click()

    def checkGame(self):
        bot=self.bot
        name=bot.find_element_by_class_name("bar-search")
        name.send_keys(self.name)


cbc=Check("FIFA")
cbc.openSite()
cbc.checkGame()
