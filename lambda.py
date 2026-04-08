#what is lambda:
#lambda is anomours functions means function without name and 
# its a keyword, 
# return values of the expresion , 
# lambda is one expression 
# lambda can have any no of arguments

# write a code to give integer is even or odd with two integer
"""
n = lambda x : 'even' if x %2 == 0 else 'odd'
print(n(1))
"""
"""
n= lambda x,y : (('even' if x %2 == 0 else 'odd'),('even' if y %2 ==0 else 'odd'))
print(n(1,2))
"""
#what is MAP function?
#MAP is used to apply the function to each element of an iterable (ex:list,tuple) return a new iterable(map objects)
list1 = [1,2,3,4,5]
n = list(map(lambda x : x **2, list1))
print(n)

#what is filter?
#filter is used to apply the function only element which satisfy the given condition ,return a new iterable(filter objects)
list1 = [1,2,3,4,5]
n = list(filter(lambda x : x % 2 ==0 ,list1))
print(n)

d = {'a':1,'b':2,'c':3,'d':4}
output = {'b':2,'d':4}
n = dict(filter(lambda x : x[1]%2 == 0,d.items()))
print(n)