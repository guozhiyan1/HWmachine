def check_ip(ip):
    ip=ip.split(".")
    for i in range(len(ip)):
        if int(ip[0])>255:
            return False
def check_mask(mask):
    mask=mask.split(".")
    for i in range(len(mask)):
        if int(mask[i])>255:
            return False
        mask[i]=bin(int(mask[i]))[2:]
    a=mask.find("1")
    b=mask.rfind("1")
    if a-b==1:
        return True
    else:
        return False

dic={"a":1,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}
while True:
    try:
        a=input().split("~")
        ip=a[0]
        mask=a[1]
        if check_ip(ip) and check_mask(mask):
            ip=ip.split(".")
            if int(ip[0])>=1 and int(ip[0])<=126:
                dic["a"]+=1
            elif int(ip[0])>=128 and int(ip[0])<=191:
                dic["b"]+=1
            elif int(ip[0])>=192 and int(ip[0])<=223:
                dic["c"]+=1
            elif int(ip[0])>=224 and int(ip[0])<=239:
                dic["d"]+=1
            elif int(ip[0])>=240 and int(ip[0])<=255:
                dic["e"]+=1
            if int(ip[0])==10:
                dic["g"]+=1
            elif int(ip[0])==172 and int(ip[1])>=16 and int(ip[1])<=31:
                dic["g"]+=1
            elif int(ip[0])==192 and int(ip[1])==168:
                dic["g"]+=1
        else:
            dic["f"]+=1
    except:
        print(dic.values())