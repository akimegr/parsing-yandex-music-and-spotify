# import requests
# from bs4 import BeautifulSoup
# import re
# import lxml
#
# headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
#
# webUrl = requests.get("https://spotifycharts.com/regional").text
# soup = BeautifulSoup(webUrl, "lxml")
# print(soup)
# #allSounds = soup.find_all("td", class_="chart-table-track")
# allSounds = soup.find_all("tr")
# print(allSounds)
# dictMusic = {}
# for i in range(len( allSounds)):
#     sound = allSounds[i].find_all("strong")
#     name = allSounds[i].find_all("span")
#     dictMusic.update({str(name[0].get_text()):str(sound[0].get_text())})
# print(dictMusic)
#
#
#
#
# firstLinks = soup.find_all("td", "chart-table-image")
# allSite = []
# for firstLink in firstLinks:
#     allSite.append(firstLink.find("a").get("href"))
#
# allSaNs = {}
# for n in allSite:
#     print(n)
#     newWebUrl =  requests.get(str(n), headers = headers).text
#     newSoup = BeautifulSoup(newWebUrl, "lxml")
#     name = newSoup.find_all("head")
#     print(name)
#
#
# def wrFile():
#     f = open("Result.txt", "wb")
#     for i,v in dictAll.items():
#         f.write(str(i).encode("utf-8") + "%$".encode("utf-8") + str(v).encode("utf-8")+"\n".encode("utf-8"))
#
#
#
# def parseSoundAndName():
#
#     for i in range(len(names)):
#
#         listName = []
#         now = names[i].find_all("a", class_ = "deco-link deco-link_muted")
#         for a in now:
#             listName.append(a.get_text().strip(" "))
#
#         dictSaNs.update({sounds[i].get_text().strip(" ") : listName})
#     z = 0
#     for i,v in dictSaNs.items():
#         dictAll.update({str(i) + "$%" +str(v) : timeSounds[z].get_text()})
#         z+=1
#     print(dictSaNs)
#
#
#
#     print(dictAll)
# parseSoundAndName()
# wrFile()
#
#
#
#
#
#
#
