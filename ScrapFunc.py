#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:32:22 2020
@author: pierre
"""
import requests
from bs4 import BeautifulSoup
import json
import pickle
import pandas as pd
import re

def GetPage(url='',params={},headers={}):
    try:
        requete = requests.get(url,params=params,headers=headers)
        html_file = requete.content
        soup = BeautifulSoup(html_file,features="lxml")
        if (requete.status_code==requests.codes.ok): return soup
        else: return('Il y a eu une erreur !')
    except requests.exceptions.ReadTimeout:
        print("Erreur")
        return('Il y a eu une erreur !')   
    
def exportdata(dict_data,name):
    with open(name, 'w',encoding='utf-8') as fp:
        json.dump(dict_data, fp,ensure_ascii=False,indent=1)
    return 'Exported'


def importJson(path):
    with open(path,'rb') as file :
        JSONFILE=json.load(file)
        return JSONFILE
    
def SaveFile(doc,name):
    with open(name, "wb") as pickFile:
        pickle.dump(doc, pickFile)
    return 'saved'

def Importfile(name):
    with open (name, 'rb') as pickFile:
        file = pickle.load(pickFile)
        return file
