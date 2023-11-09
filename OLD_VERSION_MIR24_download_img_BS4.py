import requests
from bs4 import BeautifulSoup


def download_img(url):
    try:
        pattern = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

        responce = requests.get(url=url)

        soup = BeautifulSoup(responce.content, 'html.parser')

        try:
            # Обрабатываем имя картинки
            image_name = soup.find('h1', class_="post-title").text
            image_name = ''.join(map(lambda x: x.strip(pattern), image_name)) + '.jpg'

            # Получаем ссылку на картинку (картинка на сайте)
            image_url = soup = list(soup.findAll('meta')[1])[1]['content']

            # Получаем данные со ссылки на картинку
            pic = requests.get(url=image_url)
            with open(image_name, 'wb') as out:
                out.write(pic.content)

            print('Картинка скачана')

        except:
            print('Ошибка получения ссылки на картинку')

    except:
        print('Ошибка обработки ссылки на сайт')


def main():
    print('Введите ссылку на сайте mir24.tv, где лежит картинка:')

    while True:
        url_input = input(':  ')
        download_img(url=url_input)


if __name__ == '__main__':
    main()
