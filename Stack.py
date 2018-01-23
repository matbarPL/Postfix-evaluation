# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:13:47 2017

@author: Mateusz
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def pop_item(self,index):
        index_to_pop = self.items.index(index)
        self.items.pop(index_to_pop)
            
    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return (len(self.items)==0)
        
    def size(self):
        return len(self.items)
        
    def __contains__(self,item):
        return item in self.items
        
    def __str__(self):
        arr = []
        for item in self.items:
            arr.append(str(item))
        return str(arr)