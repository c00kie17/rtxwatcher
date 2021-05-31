from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


cards = [
    {"name": "3080", "url": "https://rptechindia.in/nvidia-geforce-rtx-3080.html"},
    {"name": "3090", "url": "https://rptechindia.in/nvidia-geforce-rtx-3090.html"},
]


if __name__ == "__main__":
    while 1:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome("./chromedriver", options=chrome_options)
        for card in cards:
            try:
                driver.get(card["url"])
            except:
                print("tried to fetch " + card["name"] + " but an error occoured")

            elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[1]/main/div[3]/div/section/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/i",
                    )
                )
            )

            elem.click()
            elem2 = driver.find_element_by_xpath(
                "/html/body/div[1]/main/div[3]/div/section/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/ul/li[1]/div[3]"
            )
            print(card["name"] + ":" + elem2.get_attribute("innerHTML"))
        driver.quit()
        sleep(10)