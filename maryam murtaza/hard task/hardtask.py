#                                  #task 1
          ##palindrome words are those when you read them from forward or backward direction, it read as one word

list=["bat","tab","cat"]
ind=[]
for i in list:
    for x in range(len(list)):
        num1=list[x]
        add=i+num1
            #negative slicing used to reverse the list
        rev=add[::-1]
             #apply condition to check reverse and original list is same
        if add==rev:
            print(f"{add}  it's palindrome pair  {rev}")
            ind.append([list.index(i), list.index(num1)])
print("indexes of words that make palindrome pairs are ",ind)





