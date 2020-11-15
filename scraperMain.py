# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:53:47 2020

@author: Michael
"""
import bs4
from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

url = "https://www.newegg.ca/g-skill-8gb-240-pin-ddr3-sdram/p/N82E16820231314?Description=F3-12800CL9D-8GBRL&cm_re=F3-12800CL9D-8GBRL-_-20-231-314-_-Product"

uClient = uReq(url)
pageHTML = uClient.read()
uClient.close()

pageSoup = soup(pageHTML, "html.parser")

print(pageSoup)