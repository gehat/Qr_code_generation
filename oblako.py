import yadisk
from openpyxl import load_workbook
from qr import qrsearch

def edit_oblako(name, author, url):


    y = yadisk.YaDisk(token="AQAAAAAzOwnEAAf56nUrxnY-s0QdhKan9z7tgzE")

    y.download("/Полка/Database.txt", "file.txt")
    with open("file.txt", "a+", encoding='utf-8') as f:
        f.write(f'{author}         {name}         {url}\n')
    y.remove("/Полка/Database.txt", permanently=True)
    y.upload("file.txt", "/Полка/Database.txt")
    k = qrsearch(name, url)
