from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from xtractors.webxtractor import WebExtractor
from xtractors.docxtractor import DocExtractor
from xtractors.dirxtractor import DirExtractor
from xtractors.jsonxtractor import JsonExtractor
from xtractors.awsxtractor import AWSExtractor


# usage: x = Extractor(servicetype=str).mechanism
# b/c it's been instantiated this way, an IDE will display every functionality
class Extractor(object):

    def __init__(self, **kwargs):
        for key, value in kwargs:
            if key == 'link':
                my_webdriver = webdriver.Chrome(ChromeDriverManager().install())
                my_webdriver.minimize_window()
                self.mechanism = WebExtractor(my_webdriver, value)
                my_webdriver.close()
            elif key == 'breadcrumbs':
                # NYI: way to navigate through a 'variable' webpage directory
                pass
            # returns
            elif key == 'directory':
                self.mechanism = DirExtractor(value)
            elif key == 'json':
                self.mechanism = JsonExtractor(value)
            elif key == 'bucket':
                self.mechanism = AWSExtractor(value)
            else:
                self.mechanism = DocExtractor(value)


class Inserter:

    @staticmethod
    def write_to_txt(filepath, text):
        with open(filepath, 'w+') as file:
            if type(text) == 'list':
                for element in text:
                    file.write(element)
            else:
                file.write(text)

