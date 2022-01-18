import requests
from  bs4 import BeautifulSoup
import os
url='https://www.yetusacco.co.ke/'
def imagedown(url,folder):
    try:
       os.mkdir(os.path.join(os.getcwd(),folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(),folder))
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    print(soup.title.text)
    images=soup.find_all('img') 
    print(images)
    for image  in images:
        name= image['alt']
        link=image['src']
        with open(name.replace('','-').replace('/',',')+ '.jpg','wb') as f:
            im=requests.get(link)
            f.write(im.content)
            print('downloading the image:',name)
imagedown('https://www.yetusacco.co.ke/','yetusacco')
    
    