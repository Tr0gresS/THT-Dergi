from colorama import init , Fore
import requests
from bs4 import BeautifulSoup as bs
import os

init()

def THT_DERGI():
    try:
        path = os.path.expanduser("~")
        os.chdir(path)
        os.mkdir("THT-Dergi")
        a = os.path.join(path, "THT-Dergi")
        os.chdir(a)

    except FileExistsError:
        pass

    response = requests.get("https://dergi.turkhackteam.org")
    content = bs(response.content, "lxml")
    for item in content.find_all("div", attrs={"class": "item"}):
        for j in item.findAll("a"):
            r = requests.get(j["href"])
            resCon = bs(r.content, "lxml")
            for i in resCon.find_all("li", attrs={"class": "nav-pdf"}):
                for k in i.findAll("a"):
                    url = ((j["href"]+k["href"]))
                    if str(url).find("/"):
                        p = requests.get(url)
                        if p.status_code == 200:
                            open(str(url.rsplit("/",1)[1]), "wb").write(p.content)
                            print(Fore.LIGHTBLUE_EX+str(url.rsplit("/",1)[1])+" İndi")







if __name__ == "__main__":THT_DERGI()
