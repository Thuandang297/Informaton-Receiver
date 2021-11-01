file=open('data/text1.txt',mode='r',encoding='utf-8')
lines=file.readlines()
for line in lines :
    print(line)
file.close()
print("Thuan")


