from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import subprocess
import requests

#chrome_options = Options()
#chrome_options.add_extension('/home/mr/Documents/corona/buster.crx')
#chrome_options.add_argument('start-maximized')
#chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#chrome_options.add_experimental_option('useAutomationExtension', False)
#browser = TorBrowserDriver("/home/mr/Documents/corona/chromedriver", options = chrome_options)
#browser.get("https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php")

#profile = FirefoxProfile()
#profile.add_extension(extension="/home/mr/Documents/corona/buster.xpi")
#browser = Firefox(executable_path='/home/mr/Documents/corona/geckodriver', firefox_profile=profile)

#PROXY = "127.0.0.1:9999"

#options = Options()
#options.add_extension("/home/mr/Documents/corona/buster.crx")
#options.add_argument('--proxy-server=%s' % PROXY)
#options.add_extension("/home/mr/Documents/corona/kronymous.crx")
#driver = Chrome("/home/mr/Documents/corona/chromedriver", options=options)
#driver.get("http://whatismyipaddress.com")

wifi = ['INFINITUMC69A_5', 'TP-Link_29E0_5G', 'INFINITUMC69A_2.4', 'TP-Link_29E0', 'Edge']

#def cambiar_ip():
  #  print("\nCONEXIONES AGOTADAS, CAMBIANDO IP")
  #  disconnect_bash = "sudo pvpn -d"
 #   randomip_bash = "sudo pvpn -r"
 #   subprocess.call(disconnect_bash, shell=True)
 #   subprocess.call("qseft123", shell=True)
#    subprocess.call(randomip_bash, shell=True)
#    print("\n")

#cambiar_ip()

#browser = Chrome("/home/mr/Documents/corona/chromedriver")
#browser.get("https://www.google.com")
#browser.set_window_size(900, 500)
#size = browser.get_window_size()
#print(size['width'], size['height'])

def internet_on():
    try:
        _ = requests.get('http://www.google.com/', timeout=1)
        print("EXITO")
    except requests.ConnectionError:
        print("FRACASO.")

internet_on()

time.sleep(300)