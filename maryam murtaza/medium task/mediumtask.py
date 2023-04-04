def first_last_occurrence(nums,target):
    ind = []
    # enumerate function used to give index no. and data in each iteration element
    for index, elements in enumerate(nums):
            if elements == target:
                ind.append(index)
            # min function used to identify the lowest index num
    try:
        print("first position of", (target), " is", min(ind))
            # max function used to identify the highest which is the last occurrence
        print("last position of", target, "is", max(ind))
    except:
        print("try new target")

nums = [8,5,7,8,7,8,10,5]
target = int(input("enter target"))
first_last_occurrence(nums,target)




