class WebExtractor(object):

    def __init__(self, driver, link):
        self.driver = driver
        self.driver.get(link)

    def get_first_element_of_tag(self, tagname):
        element = self.driver.find_element_by_tag_name(tagname)
        return element

    def get_tagged_elements(self, tagname):
        elements = self.driver.find_elements_by_tag_name(tagname)
        return elements

    def get_first_element_of_class(self, classname):
        element = self.driver.find_element_by_class_name(classname)
        return element

    def get_class_elements(self, classname):
        elements = self.driver.find_elements_by_class_name(classname)
        return elements
