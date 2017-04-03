# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:41:47 2017

@author: evlil
"""

try:
    import AD_Classes
except:
    err="AD_Classes.py missing"
    raise ImportError(err)
try:
    from pyad import *
except:
    err="Please read the requirements. Install the correct modules first."
    raise ImportError(err)
    
test=AD_Classes.UserName("evlil")
print(test.get_attributes())
