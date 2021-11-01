def checKeyInDictionary(nameFile,key):
	file=open(nameFile,mode='r',encoding='utf-8')
	doc=file.read()
	doc=doc.split()
	dic={key:1} 
	i=0
	for word in doc:
		if(word in dic):
			i=i+1
	if i>0:
		return True
	else:
		return False
# def changeToDictionary(nameFile):
# 	file=open(nameFile,mode='r',encoding='utf-8')
# 	doc=file.read()
# 	doc=doc.split()
# 	dic={}

# 	for word in doc:
# 		for i in files:
# 			if(word not in dic):
# 				dic[word]=1
# 			else:
# 				i=dic[word]
# 				i=i+1
# 				dic.update({word:i})
# 		print(dic)
# 		for key in dic:
# 			print(key," : ",dic[key])
# 		file.close()	
def changeToDictionary(nameFile):
	file=open(nameFile,mode='r',encoding='utf-8')
	files={'doc2.txt','doc3.txt','doc4.txt','doc5.txt','doc6.txt'}
	doc=file.read()
	doc=doc.split()
	dic={}

	for word in doc:
		if word not in dic:
			dic[word]=1
		k=1
		for i in files:
			
			fileCursor=i
			if checKeyInDictionary(fileCursor,word) == True:
				k=dic[word]
				k=k+1
				dic.update({word:k})
				break

	print(dic)
	file.close()	
file1='doc1.txt'
file2='doc2.txt'
file3='doc3.txt'
file4='doc4.txt'
file5='doc5.txt'
file6='doc6.txt'
files={'doc1.txt','doc2.txt','doc3.txt','doc4.txt','doc5.txt','doc6.txt'}
changeToDictionary(file1)
# changeToDictionary(file2)
# changeToDictionary(file3)
# changeToDictionary(file4)
# changeToDictionary(file5)
# changeToDictionary(file6)
toi='với'



