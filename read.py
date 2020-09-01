
count = 0
data = []
with open ('reviews.txt', 'r') as f:#r讀取 w 寫入(會自己建立一個新檔)
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案已讀取完畢，總共', len(data), '筆資料')

#文字計數器
word_count = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1 #新增key進字典

for word in word_count:
	if word_count[word] > 1000:
		print(word, word_count[word])

		print(len(words))
		print(word_count['Tim'])

while True:
	word = input('請輸入你要查的字: ')
	if word == 'q':
		break
	if word in word_count:

			print(word, '出現次數為:', word_count[word])
	else:
		print('查無此字')
print('感謝使用~')


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