import openpyxl


def read_file(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    rows = sheet.max_row
    cols = sheet.max_column

    name_cols = ['Название', 'Бренд', 'Ссылка КТУ', 'Цена КТУ',
                 'Конкурент 1', 'Ссылка конкурента 1', 'Цена конкурента 1',
                 'Конкурент 2', 'Ссылка конкурента 2', 'Цена конкурента 2',
                 'Конкурент 3', 'Ссылка конкурента 3', 'Цена конкурента 3',
                 'Конкурент 4', 'Ссылка конкурента 4', 'Цена конкурента 4',
                 'Конкурент 5', 'Ссылка конкурента 5', 'Цена конкурента 5']

    contents = []
    for row in sheet.iter_rows(min_row=2, max_col=sheet.max_column, max_row=sheet.max_row):
        items = {}
        j = 0
        for cell in row:
            item = cell.value
            items[name_cols[j]] = item
            j += 1
        contents.append(items)
    return contents


if __name__ == '__main__':
    file = 'test/prods.xlsx'
    print(read_file(file))
