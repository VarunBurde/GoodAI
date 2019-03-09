###################################task 3

ex = input()

#ex = 'QWEasd632541'
# b = sorted(ex)
# print(*b,sep='')
# c = sorted(ex ,key = lambda x:(x.isdigit(),x))
# print(*c,sep='')
# d = sorted(ex ,key = lambda x:(x.isdigit(),x.isupper(),x))
# print(*d,sep='')


def odd(x):
    if x.isdigit():
        if int(x)%2 !=0:
            return False
        else: return True


sortedlist = sorted(ex,key = lambda x:(x.isdigit(),odd(x),x.isupper(),x))

print(*sortedlist,sep='')



