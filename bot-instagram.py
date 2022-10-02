from xml.etree.ElementTree import Comment
from selenium import webdriver
from seleniun.webdriver.common.keys import keys
from time import sleep
from ramdom import randint

chromedrive_path = "C:\Users\Delfim dos Anjos\Downloads\Compressed\chromedriver/chromedriver.exe"
webdriver = webdriver.Chrome(executable_path=chromedrive_path)
sleep(3)
webdriver.get('https://www.instagram.com/accounts/login/')
sleep(3)

usuario = webdriver.find_element_by_name('usernanme')
usuario.send_keys('delfim_dos_anjos')
senha = webdriver.find_element_by_name('password')
senha.send_keys('kkkkkkkk...')

button_login = webdriver.find_element_by_css_selector(
    '#loginForm > div > div:nth-child(3)')
button_login.click()
sleep(3)

agora_nao = webdriver.find_element_by_css_selector(
    '#mount_0_0_P5 > div > div > div > div.bdao358l.om3e55n1.g4tp4svg > div > div > div > div.alzwoclg.cqf1kptm.p1t2w4gn.fawcizw8.om3e55n1.g4tp4svg > section > main > div > div > div > div > button')
agora_nao.click()

hashtag_list = ['programming', 'python', 'setup', 'football', 'programmer', 'web', 'webdesign',
                'webdeveloper', 'game', 'gamer', 'rust', 'html', 'css', 'javascript', 'tecnologia']

novos_users_seguidos = []

tag = -1  # A tag pode iniciar em zero(0)
seguindo = 0
likes = 0
Comments = 0


for hashtag in hashtag_list:
    tag = +1
    webdriver.get('https://www.instagram.com/explore/tags/' +
                  hashtag_list[tag] + '/')
    sleep(3)
    primeira_thumb = webdriver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    primeira_thumb.click()
    sleep(randint(2, 3))
    try:
        for _ in range(1, 6):

        except:
            continue
