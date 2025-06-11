inFp = None
inStr = ""
count = 1

inFp = open("C:\\Users\\TaeHyun\\Desktop\\새 폴더\\week10\\CookBook 파이썬을 공부합니다..txt","r", encoding='UTF8')

while True:
    inStr = inFp.readline()
    if inStr =="":
        break
    print("%d : %s" % (count, inStr), end="")
    count +=1
    
inFp.close()