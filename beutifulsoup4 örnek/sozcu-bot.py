import bs4
import urllib3 as url

http = url.PoolManager()
r = http.request('GET','http://www.sozcu.com.tr/kategori/gundem/')
if(r.status == 200):
    bs = bs4.BeautifulSoup(r.data, "html.parser")
    bs.prettify()

    baslik = bs.findAll("span", {"class": "the-title"})
    icerik = bs.findAll("span", {"class": "the-spot"})

    basliklar = []
    icerikler = []
    for i in baslik:
        basliklar.append(i.text)
    for j in icerik:
        icerikler.append(j.text)

    b = zip(basliklar, icerikler)
    for i, j in b:
        print("Başlık: {}\nİçerik: {}\n".format(i, j))
else:
    exit()