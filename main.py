from time import sleep
from selenium import webdriver

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        self.driver.maximize_window()
        sleep(3)
        #self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(1)

    def commentSpam(self, targetName, comment):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(targetName)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]").click()
        sleep(3)
        numPost = int(self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").text)

        for x in range(1,numPost):
            num = x%3
            if num == 0:
                num = 3
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div/div/div["+str(round(x/3)+1)+"]/div["+str(num)+"]").click()
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form").click()
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea").send_keys(comment)
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button").click()
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()

bot = InstaBot('UsernameLogin', 'PasswordLogin')
bot.commentSpam('Target Username', "Spam Message")
