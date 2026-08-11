import requests
from bs4 import BeautifulSoup




def get_soup(url):

    headers={"User-Agent": "Mozilla/5.0"} #to prevent me being blocked

    response=requests.get(url,headers=headers)  #send HTTP request
    response.raise_for_status()
    html=response.text   #store the server's reply 
    soup=BeautifulSoup(html, "html.parser")
   
    return soup