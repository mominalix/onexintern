# -*- coding: utf-8 -*-
"""easy task  1 new

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tcu8I4XoSwifecyqezvFSb1pFb6SNynK
"""

#easy task
list_1 = [1,2,3]
list_2 = [4,5,6]
print ("The original list 1 is : " + str(list_1))
print ("The original list 2 is : " + str(list_2))
size_1 = len(list_1)
size_2 = len(list_2)
res = []
i , j = 0 ,0
while i < size_1 and j < size_2:
   if list_1[i] < list_2[j]:
     res.append(list_1[i])
     i=i+1
   else: 
       res.append(list_2[j])
       j=j+1
res = res + list_1[i:] + list_2[j:]
print (" The sorted list is : " + str(res))