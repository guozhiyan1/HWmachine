#1计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000
a=input().split()
print(len(a[-1]))
#2写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数
a=input().lower()
b=input().lower()
print(a.count(b))
#3明明生成了N个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。
n=int(input())
a=[]
for i in range(n):
    b=int(input())
    if b not in a:
        a.append(b)
a.sort()
for i in range(len(a)):
    print(a[i])
#4输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
a=input()
while a:
    if len(a)>=8:
        print(a[0:8])
        a=a[8:]
    else:
        print(a+"0"*(8-len(a)))
        break
#5进制转换
print(int(a,16))
print(eval(a))
#6.输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
import math
a = int(input())
i=2
while i<=int(math.sqrt(a)):
    while a % i == 0:
        print(i,end=" ")
        a=a//i
    i+=1
if a!=1:
    print(a)
#7.受一个正浮点数值，输出该数值的近似整数值 四舍五入
import math

a = float(input())
b = a - math.floor(a)
if b<0.5:
    print(math.floor(a))
else:
    print(math.ceil(a))
#8.数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出
n=int(input())
dic={}
for i in range(n):
    read=input().split()
    key=int(read[0])
    value=int(read[1])
    if key in dic:
        dic[key]=dic[key]+value
    else:
        dic[key]=value
likey=sorted(dic.keys())
for i in range(len(likey)):
    print(likey[i],dic[likey[i]])
#9输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
a=list(input())
a.reverse()
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print("".join("%s" %id for id in b))
#10计算字符串中含有的不同字符的个数
a=set(input())
print(len(a))
#11 数字颠倒
print(input()[::-1])
#12 字符串反转
print(''.join(reversed(input())))
print(input()[::-1])
#13HJ13 句子逆序
s=input().split()  #接收输入内容
s1=s[::-1]  #把输入内容倒序排列
for x in s1:
    print(x,end=" ")  #输出元素之间用空格分隔