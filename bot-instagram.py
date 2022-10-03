from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.common.keys import keys
from time import sleep
from random import randint

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
    sleep(randint(3, 4))

    #iniciio do programa
    try:
        for _ in range(1, 6): #usei o `_` no lugar da var  porque ñ vou usar a var, porque eu só quero que faça o for pela quantidade de seguidores
            usuario = webdriver.find_element_by_xpath('//*[@id="mount_0_0_pA"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a').text

            if usuario not in novos_users_seguidos:
                if webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').text == 'seguir':
                    webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').click()
                    novos_users_seguidos.append(usuario)
                    seguindo = seguindo + 1

                    #like
                    button_like = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button/div[2]/span/svg')
                    button_like.click()
                    likes = likes + 1
                    sleep(randint(3, 4))

                    #comentario
                    webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button').click()
                    comment_box = webdriver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')

                    com = randint(1, 10)
                    if com < 6:
                        comment_box.send_keys('Nice!')
                        sleep(3)
                    elif com > 5 and com < 9:
                        comment_box.send_keys('Muito boomm!')
                        sleep(3)
                    elif com == 9:
                        comment_box.send_keys('Bom trabalho')
                        sleep(3)
                    elif com == 10:
                        comment_box.send_keys('Soft!!')
                        sleep(3)

                        comment_box.send_keys(keys.ENTER)
                        comentarios = comentarios +1
                        sleep(randint(2, 4))

                        webdriver.find_element_by_link_text('Seguinte').click()
                        sleep(randint(2, 4))
                    else:
                        webdriver.find_element_by_link_text('Seguinte').click()
                        
    except:
        continue

print('Liked {} fotos.'.format(likes))
print('Comentarios {} fotos.'.format(comentarios))
print('Seguindo {} novas pessoas.'.format(seguindo))