# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""\
import pandas as pd 
import numpy as np
import datetime
s = pd.Series(np.random.randn(4))
print(s.ndim)

d=pd.date_range(''"2021-01-dewesh 01"'', periods = 3 , freq = "H")
a1=np.array([1,2])
a2 = np.array([4,6])
a3= np.array(np.meshgrid(a1,a2)).T.reshape(-1,2)
print(a3)
