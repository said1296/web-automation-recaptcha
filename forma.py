#from selenium import webdriver
from selenium.webdriver.support.ui import Select
#from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver import Chrome as TorBrowserDriver
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random, time
from pynput.mouse import Controller, Button
from fake_useragent import UserAgent
import subprocess
import requests

cooldown = 2
cooldown_grande = 1800
reintentos = 1
intentos_ip = 2

dimx=900
dimy=500
posx=[0, 950, 0, 950]
posy=[0, 0, 550, 550]
captchax=[320, 1270, 320, 1270]
captchay=[415, 415, 930, 930]
solvex=[450, 1430, 470, 1430]
solvey=[500, 495, 1000, 1000]

wifi = ['INFINITUMC69A_5', 'TP-Link_29E0_5G', 'INFINITUMC69A_2.4', 'TP-Link_29E0', 'Edge']

preg1 = ['edit-answers-0-walk-on-the-walk-side', 'edit-answers-0-perfect-day', 'edit-answers-0-satellite-of-love']
preg2 = ['edit-answers-1-verdadero', 'edit-answers-1-falso']
preg3 = ['edit-answers-2-laid', 'edit-answers-2-say-something', 'edit-answers-2-shes-a-star']
preg4 = ['edit-answers-3-chemical-brothers', 'edit-answers-3-pixies', 'edit-answers-3-interpol']
preg5 = ['edit-answers-4-delphic', 'edit-answers-4-the-soft-pack', 'edit-answers-4-foals-']

#referral = ['https://coronacapital10.com.mx/register/referred/d2B7_Aq_vNrWAaoZdZlos1e1DNT8I8M2D52OeEJFVEI/1253/14',
#            'https://coronacapital10.com.mx/register/referred/GPTUqyI90Ar0iMBR49d3YEx0afu6rwTXHY2QE3OJ8pc/126922/61']

#referral = ['https://coronacapital10.com.mx/register/referred/Wkq-a0klgoITnzMedET19BZf1TbotKnUejmXFHNdgw4/135017/14'] sofia

referral=['https://www.coronacapital10vip.com.mx/register/referred/av-lh5_IDPwLeDjj-Kz6b3kxGM9LTfTo7f3HV1aFt5k/234322/61']

def rotate_wifi():
    r=wifi.index(get_ssid())
    g=0
    while g==0:
        try: 
            f=f+1
            if f==(len(wifi)-1):
                print("Todas las redes agotadas, intentando otra vez en:")
                for l in range(cooldown_grande):
                    print(str(cooldown_grande-l) + "\n")
                    time.sleep(1) 
                bash = "nmcli c up " + wifi[r]
                print("\nCambiando red a SSID: " + wifi[r] + "\n")
                process = subprocess.check_output(bash, shell=True)
                r=r+1
                f=0
            else:
                bash = "nmcli c up " + wifi[r]
                print("\nCambiando red a SSID: " + wifi[r] + "\n")
                process = subprocess.check_output(bash, shell=True)
                r=r+1
            if r == (len(wifi)-1):
                r=0
            g = 1
        except subprocess.CalledProcessError as e:
            print("ERROR, REINTENTANDO CONEXIÓN")
            r=r+1
            if r == (len(wifi)-1):
                r=0 

def get_ssid():
    bash = "nmcli c show --active"
    hilo = str(subprocess.check_output(bash, shell=True))
    lista=str.split(hilo)
    ssid=lista[4][2:]
    return ssid

def cambiar_ip():
    print("\nIP LENTA Ó DETECTADA, GENERANDO NUEVA")
    disconnect_bash = "sudo pvpn -d"
    randomip_bash = "sudo pvpn -r"
    subprocess.call(disconnect_bash, shell=True)
    subprocess.call(randomip_bash, shell=True)
    print("\n")

def init_chrome(num_cuenta, clone):
    chrome_options = Options()
    try:
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_extension('/home/mr/Documents/corona/buster.crx')
        chrome_options.add_argument('start-minimized')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        browser = TorBrowserDriver("/home/mr/Documents/corona/chromedriver", options = chrome_options)
        browser.set_page_load_timeout(10)
        browser.set_window_size(dimx, dimy)
        browser.set_window_position(posx[clone], posy[clone])
        browser.delete_all_cookies()
        size = browser.get_window_size()
        if size['width']!=900 and size['height']!=500:
            raise Exception
        browser.get(referral[num_cuenta])
    except:
        None
    return browser

def llenar_forma(nombre, apellido, correo, num_cuenta, clone):
    mouse = Controller()
    def registro():
            elem = browser.find_element_by_id("edit-field-nombres-und-0-value")
            elem.clear()
            elem.send_keys(nombre)
            print('Llenando forma')
            elem = browser.find_element_by_id("edit-field-apellidos-und-0-value")
            elem.clear()
            elem.send_keys(apellido)
            elem = browser.find_element_by_id("edit-field-celular-und-0-value")
            rand = random.randrange(11111111, 99999999)
            elem.clear()
            elem.send_keys("55"+str(rand))
            elem = browser.find_element_by_id("email")
            elem.clear()
            elem.send_keys(correo)

            elem = browser.find_element_by_id("edit-field-fecha-de-nacimiento-und-0-value-month")
            drp = Select(elem)
            rand = random.randrange(1,13)
            drp.select_by_value(str(rand))

            elem = browser.find_element_by_id("edit-field-fecha-de-nacimiento-und-0-value-day")
            drp = Select(elem)
            rand = random.randrange(1,32)
            drp.select_by_value(str(rand))

            elem = browser.find_element_by_id("edit-field-fecha-de-nacimiento-und-0-value-year")
            drp = Select(elem)
            rand = random.randrange(1988,2001)
            drp.select_by_value(str(rand))


            elem = browser.find_element_by_id("edit-field-ciudad-und")
            drp = Select(elem)
            drp.select_by_value('233')

            elem = browser.find_element_by_id('edit-pass-pass1')
            elem.clear()
            elem.send_keys('qseft123')

            ActionChains(browser).move_to_element(browser.find_element_by_id('submit')).perform()

#            time.sleep(3600)

            try:
                elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/div/button")
                elem.click()
                time.sleep(1)
            except:
                None

            mouse.position = (captchax[clone],captchay[clone])
            mouse.click(Button.left, 1)

            time.sleep(3)

            mouse.position = (solvex[clone], solvey[clone])
            mouse.click(Button.left, 1)

            time.sleep(9)
        
            elem = browser.find_elements_by_id("check")
            elem[0].click()
            elem[1].click()

            elem = browser.find_element_by_id("submit")
            elem.click()

    k=0
    f=0
    b=0
    while k==0:
        j=0
        n=0
        try:
            if b>=intentos_ip and clone==1:
                raise Exception
            else:
                browser = init_chrome(num_cuenta, clone)
        except:
            browser.quit()
            b=b+1

        while n==0 and j==0:
            try:
                if b>=intentos_ip:
                    raise Exception
                registro()
                n=1
            except:
                try:
                    time.sleep(1)
                    elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/div/button")
                    elem.click()
                except:
                    browser.quit()
                    b=b+1
                    j=1
                    if b>=intentos_ip:
                        if clone==1:
                            g=0
                            b=0
                            while g==0:
                                try:
                                    cambiar_ip()
                                    g=1
                                    n=1
                                    k=1
                                except:
                                    None
                        else:
                            k=1
                            n=1

        if j==1:
            n=1
        else:
            n=0
        c=0  
        while n==0 and c<=(reintentos-1):
            try:
#                elem = browser.find_element_by_xpath('//a[@href="'+"/trivia/14"+'"]')
                elem = browser.find_element_by_xpath('//a[@href="'+"/trivia/55"+'"]')
                print("EXITO")
#                elem.click()
                k=1
                n=1
                b=0
            except:
                c=c+1
                print('FRACASO')
            
            if c==reintentos:
                n=1
                b=b+1
                browser.quit()
                print("REINICIANDO PROGRAMA")
        
        if clone==1 and b>=intentos_ip:
            g=0
            b=0
            while g==0:
                try:
                    cambiar_ip()
                    g=1
                    n=1
                    k=1
                except:
                    None
                

        # try:
        #     rand=random.randrange(0,3)
        #     elem = browser.find_element_by_id(preg1[rand])
        #     elem.click()
        #     print('Contestando trivia al azar')
        #     elem = browser.find_element_by_id('next-question')
        #     elem.click()

        #     rand=random.randrange(0,2)
        #     elem = browser.find_element_by_id(preg2[rand])
        #     elem.click()
        #     elem = browser.find_element_by_id('next-question')
        #     elem.click()

        #     rand=random.randrange(0,3)
        #     elem = browser.find_element_by_id(preg3[rand])
        #     elem.click()
        #     elem = browser.find_element_by_id('next-question')
        #     elem.click()

        #     rand=random.randrange(0,3)
        #     elem = browser.find_element_by_id(preg4[rand])
        #     elem.click()
        #     elem = browser.find_element_by_id('next-question')
        #     elem.click()

        #     rand=random.randrange(0,3)
        #     elem = browser.find_element_by_id(preg5[rand])
        #     elem.click()
        #     elem = browser.find_element_by_id('next-question')
        #     elem.click()

        #     n=0  
        #     c=0      
        #     while n==0 and c<11:
        #         try:
        #             elem = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/section/div/div[2]/div/div/div[3]/button')
        #             elem.click()
        #             k=1
        #             n=1
        #         except:
        #             try:
        #                 elem = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/section/div/div[2]/div/div/div[3]/button')
        #                 elem.click()
        #                 k=1
        #                 n=1
        #             except:
        #                 c=c+1
        #                 print('2',c)
        #                 time.sleep(1)
        #     print("CERRANDO SESIÓN")
        #     elem = browser.find_element_by_xpath('//a[@href="'+"/user/logout"+'"]')
        #     elem.click()

        #     k=1
        # except:
        #     browser.quit()

    browser.quit()