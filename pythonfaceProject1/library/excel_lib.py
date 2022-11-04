import xlrd
from library.config import Config


class ReadExcel:

    def read_test_data(self, sheetname):
        wb = xlrd.open_workbook(Config.TEST_EXCELDATA_PATH)
        ws = wb.sheet_by_name(sheetname)
        columns = ws.ncols
        rows = ws.get_rows()  # generator object
        header = next(rows)
        data = []

        for row in rows:
            values = ()
            for j in range (columns):
                values += (row[j].value,)
            data.append(values)

        return data

    def read_locators(self, sheetname):
        wb = xlrd.open_workbook(Config.LOCATOR_WEB_PATH)
        ws = wb.sheet_by_name(sheetname)
        rows = ws.get_rows()
        header = next(rows)

        dict_1 = {}
        for row in rows:
            dict_1[row[0].value] = (row[1].value, row[2].value)

        return dict_1
