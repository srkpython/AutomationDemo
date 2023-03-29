from generic.base_setup import BaseSetup
from generic.excel import Excel

class TestScript1(BaseSetup):
    def test_script1(self):
        print("This is test script1")
        print(self.driver.title)
        Excel.get_data(self.xl_path, "TestValidLogin", 1, 1)