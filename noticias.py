#importando classes
from class_html import Html
from class_file import File
from class_parserHtmlG1 import ParserHtmlG1
from class_parserHtmlElse import ParserHtmlElse

import argparse

def argParser(listArgs):
    parser = argparse.ArgumentParser()
    for arg in listArgs:
        parser.add_argument("--" + arg)
    return parser.parse_args()


def printData(data):
    for item in data:
        print(item)

#o que pode ser passado pela linha de comando:
# OPCIONAIS
    # SITEURL = site em que será buscada as noticias, tem como padrão o G1
        # por exemplo, https://www.globo.com/

    # FILENAME = nome em que o arquivo csv será salvo, tem como
    # padrão o nome "news-ANO-MES-DIA-HORA-MINUTO.csv"
        # por exemplo, noticia.csv

# OBRIGATÓRIO SE PASSADO O SITE - ele buscará class="feed-post-link" em um
# site que não do G1, portanto gerará um arquivo vazio
    # CLASSNAME = a classe que está no codigo fonte da pagina, de onde se
    # quer retirar a noticia, tem como padrão "feed-post-link"
        # por exemplo feed-post-link
listArgs = ["siteUrl", "filename", "classname"]
args = argParser(listArgs)
titles = []
urls = []

if args.siteUrl is None:
    html = Html()
else:
    html = Html(args.siteUrl)

#implementacao para o G1
if html.siteUrl == "https://g1.globo.com/":
    dataG1 = ParserHtmlG1()
    titles.extend(dataG1.getTitles(html.getHtml()))
    urls.extend(dataG1.getUrls(html.getHtml()))
    if args.filename is None:
        fileCsv = File(titles, urls)
    else:
        fileCsv = File(titles, urls, args.filename)
    fileCsv.writeFile()
#implementacao para qualquer site de noticia
else:
    dataSite = ParserHtmlElse(args.classname)
    titles.extend(dataSite.getTitles(html.getHtml()))
    urls.extend(dataSite.getUrls(html.getHtml()))
    if (args.filename) is None:
        fileCsv = File(titles, urls)
    else:
        fileCsv = File(titles, urls, args.filename)
        fileCsv.writeFile()