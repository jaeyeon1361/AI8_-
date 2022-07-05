#!/usr/bin/env python
# coding: utf-8

# In[3]:


PI = 3.14

def number_input():
    output = input('숫자 입력 : ')
    return float(output)

def get_circum(radius):
    return radius * 2 * PI

def get_circle_area(radius):
    return PI * radius * radius

print("모듈의 __name__ : ", __name__)
if __name__ == '__main__' :                          #메인 이
    print("get_circum(5) : ", get_circum(5))
    print("get_circle_area(5)) : ", get_circle_area(5))


# In[ ]:




