#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:25:48 2020

@author: pierre
Script de récuperation des categories
"""

import requests
from bs4 import BeautifulSoup
import json
import pickle
import pandas as pd
import re
from ScrapFunc import GetPage

from selenium import webdriver
from selenium.webdriver.common.by import By

def GetTitle(Soup):
    return Soup.find('h1',{'id':'firstHeading'}).text


def ScrapCategories(Soup):
    Items=set()
    Mainlist=Soup.find_all('div',{'class':'sub-menu'})
    print([item for item in Mainlist])
    # divs=Mainlist.find_all('div',{'class':'mCSB_container'})
    # for currdiv in divs:
    #     for li in currdiv.find_all('li'):
    #         item={}
    #         item['name']=li.find('a').attrs['title']
    #         item['category_id']=li.find('a').attrs['categoryid']
    #         Items.add(item)
    return Items

# def save_liste(title,liste):
#     with open(f'{title}.txt','w')
# def RecurScrap(entryURL,Depth):
#     for i in range(Depth):
                


entryURL="https://artlist.io/category/93&5/sexy&uplifting/"



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"

opts = webdriver.FirefoxOptions()
opts.headless = True
driver = webdriver.Firefox(options=opts)
driver.get('https://artlist.io/')

element=driver.find_elements_by_xpath('//*[@id="menu-main-list"]//mCSB_container')
listeit=[]

for li in driver.find_elements_by_xpath('//li[@class="art-music-category"]'):
# for item in element.find_elements(By.CLASS_NAME,"mCSB_container"):
    it={}
    it['categoryid']=li.get_attribute("categoryid")
    it['title']=li.get_attribute("title")
    listeit.append(it)

driver.close()

# Liste_Linked_URL=ScrapCategories(GetPage(entryURL))
# print(Liste_Linked_URL)

# for url in Liste_Linked_URL:
#     Liste_Linked_URL=ScrapLink(GetPage(url))
#     save_liste

