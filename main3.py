import forma3
from forma3 import llenar_forma
from alimentar import datos
import time, random
from selenium import webdriver

#nombres = ['AARON GARCIA', 'EDEL SAID PABLO BIBIANO', 'ANA SOFIA RODRIGUEZ LUNA']
#pos = ['14', '15', '23']
nombres = ['AARON GARCIA', 'EDEL SAID PABLO BIBIANO']
pos = ['14', '15']
espera = 60
cooldown = 2

def cooldown():
    print("\nCooldown:")
    espera_query = cooldown + random.randrange(0,4)
    for l in range(espera_query):
        print(str(espera_query-l), end=" ", flush=True)
        time.sleep(1)  

def init_rank():
    rank_browser = webdriver.Chrome('/home/mr/Documents/corona/chromedriver')
    rank_browser.get('https://coronacapital10.com.mx/sites/all/themes/bootstrap_barrio/img/logo.png')
    rank_browser.add_cookie({'name' : 'OptanonAlertBoxClosed',
                        'value' : '2019-10-31T06:37:07.575Z',
                        'domain' : '.coronacapital10.com.mx',
                        'path':'/'})
    rank_browser.get('https://coronacapital10.com.mx/ranking')

    try:
        elem = rank_browser.find_element_by_id('age_checker_day')
        elem.send_keys('12')

        elem = rank_browser.find_element_by_id('age_checker_month')
        elem.send_keys('02')

        elem = rank_browser.find_element_by_id('age_checker_year')
        elem.send_keys('1996')

        elem = rank_browser.find_element_by_id('edit-submit')
        elem.click()

        print("sí se pudo qué")

        return rank_browser
    except:
        print("chale")

def main():

#    rank_browser = init_rank()
    
    while True:
        k=0
        for i in range(len(nombres)):
#            p=0
            p=1
            while p==0:
                try:
                    rank = rank_browser.find_element_by_xpath('/html/body[1]/div[2]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div['+ pos[i] + ']/p[1]').text
                    p=1
                except:
                    try:
                        print("\nERROR: REINICIANDO RANKING\n")
                        rank_browser.quit()
                        rank_browser = init_rank()
                    except:
                        print("\nERROR: REABRIENDO RANKING\n")
                        rank_browser = init_rank()


#            if nombres[i]==rank:
#                print('\n' + nombres[i] + ' EN ' + pos[i] + 'AVA POSICIÓN')
#                k=k+1
#            else:
#                print('\nRankeando a ' + nombres[i] + ' a la posición ' + pos[i])
#                par = datos()
#                llenar_forma(par[0], par[1], par[2], i)
            print('\n\nRankeando a ' + nombres[i] + ' a la posición ' + pos[i])
            par=datos()
            try:
                llenar_forma(par[0], par[1], par[2], i)
            except:
                print("NO JAJAJAJAJALOLOLOLOLO")
                None

#            cooldown()

        if k==len(nombres):
            print('\nTodos rankeados, checando otra vez en ', espera, ' segundos')
            time.sleep(espera)

#        n=0
        n=1
        while n==0:
            try:
                rank_browser.refresh()
                n=1
            except:
                None

if __name__ == "__main__":
    main()