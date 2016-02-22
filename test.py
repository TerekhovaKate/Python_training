from math import sqrt
import operator
dic = {}

with open("text.txt", 'r') as f:
    for line in f:
        for st in line.split(" "):
            if st in dic:
                dic[st]=dic[st]+1
            else:
                dic[st]=1

print(dic)
sorted_x = sorted(dic.items(), key=operator.itemgetter(1))
print sorted_x.reverse()


def solve(a,b,c):
    d = b*b-4*a*c
    if d<0:
        print ("No solution")
    elif d == 0:
        x= -b/(2*a)
        print ("Solution one" + str(x))
    else:
        x1 = (-b+sqrt(d)/(2*a))
        x2 = (-b-sqrt(d)/(2*a))
        print ("Solution two" + str(x1)+ "and" +str(x2))

solve(1,1,1)
solve(1,2,1)
solve(1,5,6)





