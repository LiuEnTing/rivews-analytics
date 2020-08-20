
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

#篩選
new = []
for d in data:
	if len(d) < 200:
		new.append(d)
print('一共有', len(new), '筆留言長度小於200')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆當中有說到good')