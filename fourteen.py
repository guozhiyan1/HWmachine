#字符串排序
n=int(input())
a=[]
for i in range(n):
    a.append(input())
a.sort()
for i in range(n):
    print(a[i])
#15输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数
a=int(input())
b=bin(a)[2:]
print(b.count("1"))