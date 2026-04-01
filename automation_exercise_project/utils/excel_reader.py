import openpyxl


def get_search_data():

    file = "test_data.xlsx"

    workbook = openpyxl.load_workbook(file)

    sheet = workbook["Sheet1"]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):

        data.append(row[1])

    return data