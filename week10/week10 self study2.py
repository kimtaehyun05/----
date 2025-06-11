inFp = None
inList, inStr = [],""
count = 1

inFp = open("C:\\Users\\TaeHyun\\Desktop\\새 폴더\\week10\\CookBook 파이썬을 공부합니다..txt", "r", encoding='UTF8')

inList = inFp.readlines()
for inStr in inList:
    print(f"{count} : {inStr}", end="")
    count +=1
    
inFp.close()