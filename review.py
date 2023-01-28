data = [] #增加空列表
count = 0 #次數
with open('reviews.txt','r') as f: #讀取'reviews'檔 並且定義為'F'
	for line in f: #將'F逐筆取出並定義每次每筆為'line'
		data.append(line) #將'line'新增至'data'列表
		count += 1 #每讀取一次+1
		if count % 1000 == 0: #當'count'除以1000餘數=0時 
			print(len(data)) #列印'data'長度

print('檔案總共有',len(data),'筆資料')

sum_len = 0 #總長度
for d in data: #把'data'檔定義為'd'
	sum_len += len(d) #將每次讀取'd後的長度 存入'sum_len'

print('留言的平均長度是',sum_len/len(data)) #總長度/data長度

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'筆留言字數小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆留言提到"good"')		
