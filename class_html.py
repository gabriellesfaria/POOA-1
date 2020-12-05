import urllib.request

class Html:
    def __init__(self, siteUrl="https://g1.globo.com/"):
        self.siteUrl = siteUrl

    def getHtml(self):
        f = urllib.request.urlopen(self.siteUrl)
        htmlString = f.read().decode("utf8")
        f.close()
        return htmlString
