import requests
import bs4

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
           'accept': '*/*'}


def get_html(url, param=None):
    r = requests.get(url, headers=HEADERS, params=param)
    html = r
    return html


if __name__ == '__main__':
    test_list = [{'Название': 'Насосная станция Optima TPS60 Mini', 'Бренд': 'Optima',
                  'Ссылка КТУ': 'https://kty.com.ua/ru/nasosnaya-stanciya-optima-tps60-mini-037-kvt.html',
                  'Цена КТУ': None, 'Конкурент 1': 'AquaTools',
                  'Ссылка конкурента 1': 'https://aquatools.com.ua/nasosnaya-stanciya-optima-tps-60-mini.html',
                  'Цена конкурента 1': None, 'Конкурент 2': '3 метра',
                  'Ссылка конкурента 2': 'https://3metra.com/catalog/nasosnye-stantsii/nasosnaya-stantsiya-optima-tps60-mini-8400/',
                  'Цена конкурента 2': None, 'Конкурент 3': 'Заслонка',
                  'Ссылка конкурента 3': 'https://zaslonka.com.ua/nasosnaya-stanciya-optima-tps60-mini/',
                  'Цена конкурента 3': None}, {'Название': 'Optima PC59', 'Бренд': 'Optima',
                                               'Ссылка КТУ': 'https://kty.com.ua/ru/zashhita-sukhogo-khoda-optima-pc59-c-reguliruemym-diapazonom-davleniya.html',
                                               'Цена КТУ': None, 'Конкурент 1': '3 метра',
                                               'Ссылка конкурента 1': 'https://3metra.com/catalog/avtomatika_dlya_nasosov/zashchita-sukhogo-khoda-optima-pc59-n-c-reguliruemym-diapazonom-davleniya/',
                                               'Цена конкурента 1': None, 'Конкурент 2': 'Заслонка',
                                               'Ссылка конкурента 2': 'https://zaslonka.com.ua/rele-davleniya-optima-pc59-n-c-reguliruemym-diapazonom-davleniya/',
                                               'Цена конкурента 2': None, 'Конкурент 3': None,
                                               'Ссылка конкурента 3': None, 'Цена конкурента 3': None}]

    for i in test_list:
        if i['Ссылка КТУ']:
            print('Ссылка КТУ', get_html(i['Ссылка КТУ']).status_code)
        if i['Ссылка конкурента 1']:
            print('Ссылка конкурента 1', get_html(i['Ссылка конкурента 1']).status_code)
        if i['Ссылка конкурента 2']:
            print('Ссылка конкурента 2', get_html(i['Ссылка конкурента 2']).status_code)
        if i['Ссылка конкурента 3']:
            print('Ссылка конкурента 3', get_html(i['Ссылка конкурента 3']).status_code)

