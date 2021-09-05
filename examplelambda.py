# l=[1,2,3,4]

# f=lambda x:x+10
# print(f(5))
# print(f(10))

# f1=lambda x,y:x*y

# print(f1(5,10))

# def myfunc(n):
#     return lambda x:x*n

# doubler=myfunc(2)
# print(doubler(6))


#sorting

# points2d=[(2,3),(4,1),(5,3),(10,2)]
# sortedby=sorted(points2d,key=lambda x:x[0])
# print(sortedby)

# mylist1=[-1,-4,-2,-3,1,2,3,4]
# mylist=[1,2,3,-8,-9,-1]
# sortedabs=sorted(mylist,key=lambda x:abs(x))
# print(sortedabs)


# b=list(map(lambda x:x*2,mylist))
# print(b)

# c=[x*2 for x in mylist]
# print(c)


# l1=[1,2,6,7,8,9,3,4,5]
# b=list(filter(lambda x:(x%2==0),l1))
# print(b)

# c1=[x for x in l1 if (x%2==0)]
# print(c1)

# from functools import reduce
# l2=[1,2,3,4,5,6]
# product_a=reduce(lambda x,y : x*y,l2)
# print (product_a)




# if x<0:
#     raise Exception("x shoubld be postive value")

# assert (x>=0),'x is not positive value'



# try:
#     a=int(input("enter number"))
#     b=int(input("enter number"))
#     c=a+b 
#     d=a/b
#     e=a+'k'
# except ZeroDivisionError:
#     print('cant divide by 0')
# except ValueError:
#     print('Trying convert string to in number')
# except TypeError:
#     print("cannot add str and number")
# except Exception as e:
#     print(e.with_traceback)

# else:
#     print('good no error')
#     print(a)
#     print(b)
#     print(c)
#     print(d)

# finally:
#     print('I will surely execute if exception occured or not')



#from _typeshed import HasFileno


class Error(Exception):
    pass
class AgeException(Error):
    pass

try:
    a=int(input("enter Year"))
    a=2021-a
    if(a<18 or a>30):
        raise AgeException
    else:
        print("age is valid")
except AgeException:
    print("Age ahould greater than 18 and less than 30")
