print("Hello World!")

print(1+2) #4
print(5/3) #1.666666
print(2*5) #10
print(2**5) #32
print(9//2) #4.0
print(9%2) #1

print(True) #True
print(False) #False
print(True and False) #False
print(True or False) #True
print(not False) #True

myStr = 'Kia'
myInt = 5
myFloat = 5.0
myBool = True

myList = [1,2,3,4,5]

print(myStr, myInt, myFloat, myBool, myList)

myList = (myList + [6])* 2

print(myList)
print(7 in myList) #False
print(len(myList)) #12

#list methods
  # append(item), adds item to end
  # insert(index, item), adds item to index
  # pop([index]), removes item from end or optional index
  # sort(), sorts list
  # reverse(), reverses list
  # del list[i], removes item from ith position
  # index(item), returns first occurence of item
  # remove(item), removes first occurence of item

#range

myRange = range(10, 16, 2) #defaults to 0, 2nd number is exclusive upper bound
print(list(myRange)) #[10,12,14]

#string methods
  #count(item)
  #lower()
  #upper
  #find(item), returns index of first occurence
  #split(char), splits string on char

#tuples
  #immutable lists, (items)

#sets

mySet = {1,2,3,4,5, 'a', 'b', 'c'}

  #sets have unique membership
    #can check with in
    #can check with len
    #can | sets, combine 2 sets 
    #can & sets, and operator, think bitwise &
    #can diff sets with -, set1 - set2
    #can ask whether all elements of set are in the second, set1 <= set2

  #setmethods
    #set.union(otherset), returns new set of their union
    #set.intersection(otherset), returns a new set with their commonality
    #set.difference(otherset), items only in first set
    #set.isssubset(otherset), returns whether elements of one set are in otherset
    #set.add(item), adds item to set
    #set.remove(item), removes item from the set
    #set.pop(), removes arbitrary element from set
    #set.clear(), removes all elements from the set


#Dictionaries

myDict = {'kia': 'awesome', 'america': 'f yeah'}

print('kia' in myDict) #True
del myDict['kia']
print('kia' in myDict) #False