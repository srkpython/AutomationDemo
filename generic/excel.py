import openpyxl

class Excel:
    @staticmethod
    def get_data(xlpath,sheet,row,col):
        try:
            wb=openpyxl.load_workbook(xlpath)
            value=wb[sheet].cell(row,col).value
            print("Data from excel",value)
            wb.close()
            return value
        except:
            print("Exception while reading data from excel")
            return ""