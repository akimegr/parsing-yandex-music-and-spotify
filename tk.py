import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from tkinter import *
import lxml
import matplotlib.pyplot as plt


root = Tk()
root["height"] = 800
root["width"] = 800

headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

webUrl = requests.get("https://music.yandex.ru/chart", headers = headers).text
soup = BeautifulSoup(webUrl, "lxml")
dictSaNs = {}
dictAll = {}
sounds = soup.find_all("div", class_="d-track__name")
names = soup.find_all("span", class_="d-track__artists")
timeSounds = soup.find_all("span", class_="typo-track deco-typo-secondary")
data = []
takeLinks = []
allGenre = []
masGenre = {}
labeles = {}
artistInLabels = {}
basLinks = "https://music.yandex.ru/"
endLinks = "/artists"


def wrFile():
    f = open("Ress.txt", "wb")
    for i,v in artistInLabels.items():
        f.write(str(i).encode("utf-8") + ":".encode("utf-8") + str(v).encode("utf-8")+"\n".encode("utf-8"))

def save_to_csv(data, file_name):
    with open(file_name, mode = "w", encoding="utf-8") as f:
        wrt = csv.writer(f,delimiter = ";", lineterminator = "\r")
        wrt.writerow(["Song_title","Song_writer", "Listening", "Genre"])

        for item in data:
            print([str(item["song_title"]), str(item["song_writer"]), str(item["listening"]), str(item["genre"])])
            wrt.writerow([item["song_title"], item["song_writer"], item["listening"], item["genre"]])



def parseSoundAndName():

    for i in range(len(names)):

        listName = []
        now = names[i].find_all("a", class_ = "deco-link deco-link_muted")
        for a in now:
            listName.append(a.get_text().strip(" "))

        dictSaNs.update({sounds[i].get_text().strip(" ") : listName})
    z = 0

    for i,v in dictSaNs.items():
        data.append({"song_title":str(i), "song_writer":str(v).strip("[").strip("]"), "listening":timeSounds[z].get_text(), "genre":allGenre[z]})
        z+=1
        # dictAll.update({str(i) + "$" +str(v) : timeSounds[z].get_text()})
        # z+=1
    print(data)

def checkgenre():
    links = soup.find_all("a", class_ = "d-track__title deco-link deco-link_stronger")

    for link in links:
        takeLinks.append("https://music.yandex.ru/" + link.get("href"))
    counter = 0
    for link in takeLinks:
        newWebUrl = requests.get(str(link), headers=headers).text
        newSoup = BeautifulSoup(newWebUrl, "lxml")
        gnr = newSoup.find_all("a", class_="d-link deco-link deco-link_mimic typo")
        allGenre.append(gnr[0].get_text())
        afaterLbl = newSoup.find_all("div", class_="page-album__label")
    for i in allGenre:
            if (i not in labeles):
                masGenre.update({str(i):1})
            else:
                labeles[str(i)]+=1
    lab = []
    size = []
    for x,y in labeles.items():
        lab.append(x)
        size.append(y)
    plt.pie(size, labels=lab, rotatelabels = True)

    plt.axis('equal')
    plt.show()

def checkLabeles():
    links = soup.find_all("a", class_ = "d-track__title deco-link deco-link_stronger")

    for link in links:
        takeLinks.append("https://music.yandex.ru/" + link.get("href"))
    counter = 0
    for link in takeLinks:
        newWebUrl = requests.get(str(link), headers=headers).text
        newSoup = BeautifulSoup(newWebUrl, "lxml")
        gnr = newSoup.find_all("a", class_="d-link deco-link deco-link_mimic typo")
        allGenre.append(gnr[0].get_text())
        afaterLbl = newSoup.find_all("div", class_="page-album__label")
        for i in afaterLbl:
            lbl = i.find_all("a", class_="d-link deco-link")
            lbl2 = lbl[0].get_text()                          #???????????????? ??????????
            midle = lbl[0].get("href")                      #???????????????? ????????????????

            if (lbl2 not in labeles):
                labeles.update({str(lbl2):1})
            else:
                labeles[str(lbl2)]+=1

            allArtistLink = basLinks + midle + endLinks
            artWebUrl = requests.get(str(allArtistLink), headers=headers).text
            artSoup = BeautifulSoup(artWebUrl, "lxml")
            artLabels = artSoup.find_all("span", class_="d-artists")
            listArtist = []
            for artLabel in artLabels:
                artists = artLabel.find_all("a", class_="d-link deco-link")
                for artist in artists:
                    listArtist.append(str(artist.get_text()))
            if (lbl2 not in artistInLabels):
                artistInLabels.update({str(lbl2):str(listArtist)})

    lab = []
    size = []
    for x,y in labeles.items():
        lab.append(x)
        size.append(y)
    plt.pie(size, labels=lab, rotatelabels = True)

    plt.axis('equal')
    plt.show()

def allVoice():

    for link in takeLinks:
        newWebUrl = requests.get(str(link), headers=headers).text
        newSoup = BeautifulSoup(newWebUrl, "lxml")
        gnr = newSoup.find_all("a", class_="d-link deco-link deco-link_mimic typo")
        allGenre.append(gnr[0].get_text())
        afaterLbl = newSoup.find_all("div", class_="page-album__label")
        for i in afaterLbl:
            lbl = i.find_all("a", class_="d-link deco-link")
            lbl2 = lbl[0].get_text()                          #???????????????? ??????????
            midle = lbl[0].get("href")                      #???????????????? ????????????????

            allArtistLink = basLinks + midle + endLinks
            artWebUrl = requests.get(str(allArtistLink), headers=headers).text
            artSoup = BeautifulSoup(artWebUrl, "lxml")
            artLabels = artSoup.find_all("span", class_="d-artists")
            listArtist = []
            for artLabel in artLabels:
                artists = artLabel.find_all("a", class_="d-link deco-link")
                for artist in artists:
                    listArtist.append(str(artist.get_text()))
            if (lbl2 not in artistInLabels):
                artistInLabels.update({str(lbl2):str(listArtist)})
    print(artistInLabels)





btnTag = Button(root,text="???????????????? ??????????, ???????????????????????? ?? ???????????????????????? ???? ?????????? YM ", bg = "black", fg="white", command = parseSoundAndName)
btnTag.place(x=70,y=50)
btnDate = Button(root, text="???????????????? ???????????????????????? ??????????????", bg = "black", fg="white", command = checkLabeles )
btnDate.place(x=70, y = 80)
btnDiscription = Button(root, text  = "???????????????? ???????????????? ??????????????", bg = "black", fg = "white", command = allVoice)
btnDiscription.place(x=70, y = 110)
btnDiscription = Button(root, text  = "???????????? ???????????????????? ????????????", bg = "black", fg = "white", command = checkgenre)
btnDiscription.place(x=70, y = 140)



root.mainloop()