from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

REDDIT_EMAIL = "mihai.minascurta3@gmail.com"
REDDIT_PASSWORD = "SpectrumM2012"

class InternetSpeedRedditBot:
    def __init__(self):

        self.options = webdriver.ChromeOptions()
        self.prefs = {
            "profile.default_content_setting_values.geolocation": 2,  # 1 = allow, 2 = block
            "profile.default_content_setting_values.notifications": 2
        }
        self.options.add_experimental_option("prefs", self.prefs)
    
    def get_internet_speed(self):

        speed_options = webdriver.ChromeOptions()
        speed_options.add_experimental_option("prefs", self.prefs)
        speed_driver = webdriver.Chrome(options=speed_options)
        
        speed_driver.get("https://www.speedtest.net/")
        speed_driver.maximize_window()
        time.sleep(5)
        
        try:
            go_button = WebDriverWait(speed_driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "s-start-test")]')))
            go_button.click()
            print("A fost găsit butonul GO")
        except Exception as e:
            print(f"Eroare la găsirea butonului GO: {e}")
        
        time.sleep(60)

        try:
            download_elem = WebDriverWait(speed_driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(@class, "download-speed")]')))
            upload_elem = WebDriverWait(speed_driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(@class, "upload-speed")]')))
            downloads_text = download_elem.text
            upload_text = upload_elem.text
            print(f"Download: {downloads_text}, Upload: {upload_text}")
        except Exception as e:
            print(f"Nu s-au găsit valorile de viteză: {e}")
            downloads_text = upload_text = "0"

        speed_driver.quit()  # închidem fereastra de speedtest
        return downloads_text, upload_text


    def reddit_at_provider(self, downloads_mbps, upload_mbps):

        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://www.reddit.com/")
        self.driver.maximize_window()
        time.sleep(5)
        
        try:
            self.login_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@id="login-button"]')))
            self.login_button.click()
            time.sleep(3)

            self.username = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,'username')))
            self.username.send_keys(REDDIT_EMAIL)
            time.sleep(3)

            self.password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME,'password')))
            self.password.send_keys(REDDIT_PASSWORD)
            time.sleep(3)

            submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker')))
            submit_button.click()
            time.sleep(3)
            print("Logarea a fost cu succes")
        except Exception as e:
            print(f"Eroare la logare {e}")
        
        try:
            self.driver.get("https://www.reddit.com/user/Independent-Tip-1376/submit/?type=TEXT")
            time.sleep(3)

            

            self.title_post = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, 'title')))
            self.title_post.send_keys("Test")
            time.sleep(3)

            self.body_text = WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p[class='first:mt-0 last:mb-0']")))
            self.body_text.send_keys(f"Acest mesaj este automat,viteza internetului meu este {downloads_mbps}  la downloads mbps ,{upload_mbps}  la upload mbps")
            time.sleep(3)

            self.post_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submit-post-button"]')))
            self.post_button.click()
            time.sleep(10)
            print("Postarea a fost facuta cu succes!!!")
        except Exception as e:
            print(f"Postarea nu a fost facuta , {e}")
        time.sleep(5)
        self.driver.close()


bot = InternetSpeedRedditBot()
downloads_mbps,upload_mbps = bot.get_internet_speed()
bot.reddit_at_provider(downloads_mbps, upload_mbps)
