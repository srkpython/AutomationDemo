from pyjavaproperties3 import Properties
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote

class BaseSetup:
    @pytest.fixture(autouse=True)
    def precondition(self):
        print("Accessing properties file")
        pptobj=Properties()
        pptobj.load(open('config.properties'))
        
        self.xl_path=pptobj['XL_PATH']
        print("Excel PAth",self.xl_path)
        
        
        usegrid=pptobj['USEGRID'].lower()
        print("USE GRID",usegrid)
        
        gridurl=pptobj['GRIDURL']
        print("USE GRID",gridurl)
        
        appurl=pptobj['APPURL']
        browser=pptobj['BROWSER'].lower()
        print('browser',browser)
        
        ito=pptobj['IMPLICIT_TIME_OUT']
        print('ito',ito)
        
        eto=pptobj['IMPLICIT_TIME_OUT']
        print('eto',eto)
        
        if usegrid=="yes":
            print("Executing in remote system")
            if browser=='chrome':
                self.driver=Remote(gridurl,DesiredCapabilities.CHROME)
            
            elif browser=='firefox':
                self.driver=Remote(gridurl,DesiredCapabilities.FIREFOX)
                
            else:
                self.driver=Remote(gridurl,DesiredCapabilities.EDGE)
        else:
            print("Executing in local system")       
            if browser=='chrome':
                print("Open in chrome browser")
                self.driver=webdriver.Chrome()
                
            elif browser=='firefox':
                print("Open in Firefox browser")
                self.driver=webdriver.Firefox()
            
            else:
                print("Open in Edge browser")
                self.driver=webdriver.Edge()
        print("Print the URL",appurl)   
        self.driver.get(appurl)
        print("Maximize the browser")
        self.driver.maximize_window()
        print('set ito',ito,'seconds')
        self.driver.implicitly_wait(ito)
        print('set eto',eto,'seconds')
        self.wait=WebDriverWait(self.driver,eto)
        
    @pytest.fixture(autouse=True)    
    def postcondition(self):
        yield
        print("Close the browser")
        self.driver.quit()