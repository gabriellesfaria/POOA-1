from datetime import datetime
import codecs

class File:
    def __init__(self, titles, urls, filename=datetime.now().strftime("news-%Y-%m-%d-%H-%M.csv")):
        self.filename = filename
        self.titles = titles
        self.urls = urls

    def writeFile(self):
        file = codecs.open(self.filename, "w", encoding='utf-8')
        file.write('TITULOS E LINKS: \n\n')
        for i, u in zip(self.titles, self.urls):
            file.write(i + "\n")
            file.write(u + "\n\n")
        file.close()