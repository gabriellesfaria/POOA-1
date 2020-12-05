from bs4 import BeautifulSoup
from class_parserHtml import ParserHtml

class ParserHtmlElse(ParserHtml):
    def __init__(self, classname):
        self.classname = classname

    def getTitles(self, htmlString):
        htmlParsed = BeautifulSoup(htmlString, 'html.parser')
        return [item.get_text() for item in htmlParsed.find_all("a", class_=self.classname)]

    def getUrls(self, htmlString):
        htmlParsed = BeautifulSoup(htmlString, 'html.parser')
        return [item['href'] for item in htmlParsed.find_all("a", class_=self.classname, href=True)]