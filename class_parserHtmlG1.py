from bs4 import BeautifulSoup
from class_parserHtml import ParserHtml
import re

class ParserHtmlG1(ParserHtml):

    def getTitles(self, htmlString):
        htmlParsed = BeautifulSoup(htmlString, 'html.parser')
        return [item.get_text() for item in htmlParsed.find_all("a", class_="feed-post-link")]

    def getUrls(self, htmlString):
        htmlParsed = BeautifulSoup(htmlString, 'html.parser')
        return [item['href'] for item in htmlParsed.find_all("a", class_="feed-post-link", href=True)]