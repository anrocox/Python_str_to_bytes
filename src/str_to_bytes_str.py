#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2014

@author: anroco

How to convert a string to bytes in python?

¿Como convertir un string a bytes en python?
'''

#create a str
s = 'string to bytes'
print(s)

#return an encoded version of the string as a bytes object. Default encoding
#is 'utf-8'.
b = s.encode()
print(type(b))
print(b)

#create a str
s = 'montaña canción'

#return byte encoding ascii and replace by '?' the chars not found
b = s.encode('ascii', 'replace')
print(b)
