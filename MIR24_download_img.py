import requests


def download_img(url):
    try:
        pattern = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

        r = requests.get(url=url)

        res = r.text[r.text.index('<!-- meta -->') + 22:r.text.index('jpg" />') + 3]
        pic_name = res[res.index('<title>') + 7:res.index('</title>')]
        pic_name = ''.join(map(lambda x: x.strip(pattern), pic_name)) + '.jpg'

        try:
            pic_url = res[res.index('https://'):].split('" />\n')[0]
            pic = requests.get(url=pic_url)

            with open(pic_name, 'wb') as out:
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
