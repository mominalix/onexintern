                                #TASK1
def returnindexes(list):
    target = int(input("enter values bet 3,6,9"))
    a = None
    # loop used to iterate from 0 to 1
    for i in range(len(list)):
        try:
            # add value of "i" in  list indexes
            a = list[0 + i]
            # value of list index remain "1" at each time
            # but bcz of adding value of "i" the list index value chage according to it
            b = list[1 + i]
            # after adding value of "i", the list index =list[0][list[1]
            # now add both indexex values of list. it add values which place on given indexes of list
            c = a + b
            # condition apply
            if c == target:
                print([list.index(a), list.index(b)])
                break
        except:
            print("invalid target")
                # return indices of the two numbers such that they add up to target.
returnindexes(list=[1,2,4,5])




