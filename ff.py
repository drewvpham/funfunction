def odd_even():

    for x in range(2001):
        if x % 2 == 0:
            print 'Number is {}. This is an even number'.format(x)
        elif x % 2 != 0:
            print 'Number is {}. This is an odd number'.format(x)
odd_even()


a = [2, 4, 10, 16]
def multiply(arr,num):
    for x in range(len(arr)):

        arr[x]=arr[x]*num
    return arr

b = multiply(a, 5)
print b




def layered_multiples(arg):
    print arg
    new_array=[]
    for x in arg:
        new_val=[]
        for y in range(0,x):
            new_val.append(1)
        new_array.append(new_val)
    return new_array





x = layered_multiples(multiply([2,4,5],3))
print x
