list01=[]
user = int(input("enter no of element:  "))
for i in range(0, user):
    ele = int(input())
    list01.append(ele)
print(list01)
def swaplist(list01):
    start,* middle,last=list01
    list01=last,*middle,start
    return list01

print(swaplist(list01))

#end of quesion 1

def swappositions(list20,pos1,pos2):
    list20[pos1], list20[pos2] = list20[pos2],list20[pos1]
    return list20

list20=[23,65,19,90]
pos1,pos2=1,3
print(swappositions(list20,pos1-1,pos2-1))

#end of quesion 2

list23=[15,6,7,10,12,20,10,28,10]
x=int(input("enter num: "))
y= list23.count(x)
print("The num you input is",y,"times in this list")

#end of quesion 3

list12=[4,5,1,2,9,7,10,8]
Sum = sum(list12)
print(Sum)
a=sum(list12) / len(list12)
print(a)

#end of quesion 4

def multiplyList(myList) :
    res = 1
    for x in myList:
         res = res* x
    return res
     
list11 = [1, 2, 3]
print(multiplyList(list11))
#end of quesion 5

list24=[2,7,5,64,14]
for i in list24:
    if i%2==0:
        print(i)

#end of quesion 6

list29=[12,14,95,3,73]
for i in list29:
    if i%2==1:
        print(i)

#end of quesion 7

list29=[2,7,5,64,14]
even_num , odd_num =0,0
for i in list29:
    if i%2==0:
        even_num+=1
    else:
        odd_num+=1
    
print("even number is: ", even_num)
print("odd number is: ",odd_num)

#end of quesion 8

list18=[12,-7,5,64,-14]
for i in list18:
    if i>0:
        print(i)

#end of quesion 9

list70 = [12,14,-95,3]
  
for num in list70:
    if num > 0:
       print(num, end = " ")

#end of quesion 10