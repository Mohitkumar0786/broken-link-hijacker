print("""
██████╗ ██████╗  ██████╗ ██╗  ██╗███████╗███╗   ██╗    ██╗     ██╗███╗   ██╗██╗  ██╗    ██╗  ██╗██╗     ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██║     ██║████╗  ██║██║ ██╔╝    ██║  ██║██║     ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝██████╔╝██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ██║██╔██╗ ██║█████╔╝     ███████║██║     ██║███████║██║     █████╔╝ 
██╔══██╗██╔══██╗██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██║██║╚██╗██║██╔═██╗     ██╔══██║██║██   ██║██╔══██║██║     ██╔═██╗ 
██████╔╝██║  ██║╚██████╔╝██║  ██╗███████╗██║ ╚████║    ███████╗██║██║ ╚████║██║  ██╗    ██║  ██║██║╚█████╔╝██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
 """) 
import requests
import os
from bs4 import BeautifulSoup
 
def brokenLinkHijack(Find_links,all_links,Find_links_present):
    for Find_link in Find_links:
        for link in all_links:
            if Find_link in link.attrs['href']:
                Find_links_present.Find_links_presentappend(link.attrs['href'])
    for link in Find_links_present:
        print(link, file=open('sociallinks.txt', 'a'))
    os.system("cat sociallinks.txt| sudo httpx -silent -status-code -title -follow-redirects -content-length")
 
if __name__== '__main__':
    try:
        url = input("Enter your URL: ")
        r = requests.get(url)
        Find_links = ['twitter.com','facebook.com', 'instagram.com']
        Find_links_present = []
 
        soup = BeautifulSoup(r.content, 'html5lib')
        all_links = soup.find_all('a', href = True)
        brokenLinkHijack(Find_links, all_links, Find_links_present)
    except:
        pass
        