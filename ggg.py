from bs4 import BeautifulSoup
import requests
import re
import random

def getVal(arr):
    rand = random.randrange(0,len(arr))
    error = ['or','a','the','in','out','above','it','he','she','there','of']
    flag = False
    for a in  range(len(arr)):
        val = arr[rand]
        for er in error:
            if(val == er):
                flag = True
                break
        if(flag == True):
            flag = False 
            continue
        else:          
            return val    
    dic = base()
    return getVal(dic)            
def getDict(st):
    dic = st.split()
    return dic
def getSource(html):
    prefics = 'https://en.wikipedia.org'
    res = BeautifulSoup(html.text,'lxml')
    out = res.find_all('a')
    a= 0
    rand1 = random.randrange(1, 50)
    rand2 = random.randrange(1, 3)
    d = 'f'
    st = 'f'
    for o in out:        
        li = str(o.get('href'))        
        if (re.match(r"^/wiki",li) and not re.match(r"^/wiki/List_of",li) and not re.match(r"^/wiki/Main_Page",li)):
            # print("good")
            a+=1
            if(a == rand2):
                st = li
            if(a == rand1):
                html = requests.get(prefics+li)
                resp = BeautifulSoup(html.text,'lxml')
                #kon = resp.find('h1',id='firstHeading').text
                kon = resp.find('div',id='bodyContent').text
                return kon 
        if(a == 50):
            d = li
        # print(li)
    html = requests.get(prefics+st)
    resp = BeautifulSoup(html.text,'lxml')
    kon = resp.find('h1',id='firstHeading').text            
    return kon
def getUrl(url):
    prefics = 'https://en.wikipedia.org'
    # r = requests.get(url)
    # s = BeautifulSoup(r.text,'lxml')
    # r = s.find('a',class_="mw-redirect",title="Index of poets").get('href')
    #report = prefics+r
    html = requests.get(url)
    return html
def Url(url):
    prefics = 'https://en.wikipedia.org'
    rand1 = random.randrange(1, 30)
    r = requests.get(url)
    prefics = 'https://en.wikipedia.org'
    s = BeautifulSoup(r.text,'lxml')
    res = s.find_all('a')
    a = 66
    it = 0
    for r in res:
        li = str(r.get('href'))
        it+=1
        if(it==a+rand1):
            st = prefics+li
            html = requests.get(st)
            return html
    
def base():
    url = 'https://en.wikipedia.org/wiki/Wikipedia:Contents/Indices'
    html = Url(url)
    html = getSource(html)   
    dic = getDict(html)
    return dic
def main():
    dic = base()
    resoult = getVal(dic)
    print(resoult)

if __name__ == "__main__":
    main()