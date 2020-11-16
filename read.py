data = [] #建立一個空清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1
		if count % 1000 == 0:
			print(len(data)) #每1000筆印出一次長度,透過count計數
#print(len(data)) #印出清單的長度
print(data[0])
print('....................................')
print(data[1])


