import openpyxl


def try_save(sheet, i, j, cols_name, price):
    try:
        if i[price]:
            sheet[f'{cols_name}{j}'] = i[price]
    except KeyError:
        pass


def save_file(data, file):
    wb = openpyxl.load_workbook(filename=file)
    sheet = wb.active

    j = 2
    for i in data:
        try_save(sheet, i, j, 'D', 'Цена КТУ')
        try_save(sheet, i, j, 'G', 'Цена конкурента 1')
        try_save(sheet, i, j, 'J', 'Цена конкурента 2')
        try_save(sheet, i, j, 'M', 'Цена конкурента 3')
        try_save(sheet, i, j, 'P', 'Цена конкурента 4')
        try_save(sheet, i, j, 'S', 'Цена конкурента 5')
        # if i['Цена КТУ']:
        #     sheet[f'D{j}'] = i['Цена КТУ']
        #
        # if i['Цена конкурента 1']:
        #     sheet[f'G{j}'] = i['Цена конкурента 1']
        #
        # if i['Ссылка конкурента 2']:
        #     sheet[f'J{j}'] = i['Цена конкурента 2']
        #
        # if i['Ссылка конкурента 3']:
        #     sheet[f'M{j}'] = i['Цена конкурента 3']
        #
        # if i['Ссылка конкурента 4']:
        #     sheet[f'P{j}'] = i['Цена конкурента 4']
        #
        # if i['Ссылка конкурента 5']:
        #     sheet[f'S{j}'] = i['Цена конкурента 5']
        j += 1
    wb.save('Проверен.xlsx')
    print('Файл сохранен')
