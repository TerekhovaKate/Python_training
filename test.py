
dic = {}

with open("text.txt", 'r') as f:
    for line in f:
        for st in line.split(" "):
            if st in dic:
                dic[st]=dic[st]+1
            else:
                dic[st]=1

print(dic)




import operator

sorted_x = sorted(dic.items(), key=operator.itemgetter(1))
print sorted_x.reverse()



