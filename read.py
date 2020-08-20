
count = 0
data = []
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案已讀取完畢，總共', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度', sum_len/len(data))



