# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:21:24 2021

@author: herrm
"""

class ListKeeper:
    #Deklaration und Initalisierung des Dictionaries
    dic = {}
    dic["example"] = [1,2,3,4,5]
    
    #Gibt alle Namen des Dictionary aus 
    def show(self):
        return self.dic.keys()
    
    #Hinzufügen eines neuen Eintrages
    def add(self,name,list):
        self.dic[name] = list
    
    #Löscht einen Eintrag anhand dem Namen des Indexes
    def delete(self,name):
        self.dic.pop(name)
    
    #Sortiert die gewünschte Liste eines bestimmten Indexes
    def sort(self,name):
        unsorted = self.dic[name]
        sorted = unsorted.sort()
        return sorted
    
    #Fügt eine Liste einer bestehenden Liste hinzu
    #Mit append als Liste, mit extend die Werte
    def append(self,name,list):
        #self.dic[name].append(list)
        self.dic[name].extend(list)