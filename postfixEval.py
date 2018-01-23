# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:53:44 2017

@author: Mateusz
"""
from struktury_danych.Stack import *

def infix_to_postfix(infix):
    opstack = Stack()
    result = []
    operands_priority = {'*':'3','/':'3','+':'2','-':'2','(':'1'}
    infix = infix.split()
    
    for item in infix:
        if (item in "0123456789" or item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            result.append(item)
        elif (item == '('):
            opstack.push('(')
        elif (item ==')'):
            pop_item = opstack.pop()
            while (pop_item!='(' ):
                result.append(pop_item)
                pop_item = opstack.pop()
        else:
            while(not opstack.isEmpty()) and (operands_priority[opstack.peek()] >= operands_priority[item]):
                result.append(opstack.pop())
            opstack.push(item)                          

    while(not opstack.isEmpty()):
        result.append(opstack.pop())
                 
    result = " ". join(result)
    result = result.replace(" ","")
    return result

def calculate(postfix):
    operandStack = Stack()
    postfix_list = list(postfix)
    " ".join(postfix_list)
    operands = '0123456789'
    operators = '+-*/'
    try:
        for item in postfix_list:
            if (item in operands):
                operandStack.push(int(item))
            elif(item in operators):
                op1 = operandStack.pop()
                op2 = operandStack.pop()
                operandStack.push(do_math(item,op1,op2))
        return operandStack.pop() 
    except IndexError:
        return 'Niepoprawne wyrażenie'
        
        
def do_math(operator,op1,op2):
    try:
        if (operator == "+"):
            return op1+op2
        elif(operator == "-"):
            return op1 - op2
        elif(operator=="*"):
            return op1*op2
        elif(operator=="/"):
            return op2/op1
            
    except TypeError as err:
        return ('Niepoprawne wyrażenie',err)
        
if __name__=="__main__":
    postfix = infix_to_postfix(' 4 + ( 4 * 2 / 2 ) * 3')
    print(calculate(postfix))