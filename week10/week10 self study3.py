outFp = None
outStr = ""
fName = ""

fName = input("저장할 파일명을 입력하세요 : ")
outFp = open(fName, "w", encoding='UTF8')

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print(f"---정상적으로 '{fName}' 파일에 씀---")