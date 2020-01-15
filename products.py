import os #operating system
products = []#不管有沒有檔案都需使用到
#讀取檔案
if os.path.isfile('products.csv'): #檢查檔案有沒有存在
	print('YES,有找到')
	with open('products.csv','r',encoding='utf-8') as f: #encoding='utf-8'
		for line in f:
			if '商品,價格' in line:
				continue #繼續 跳到下一迴
			name,price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print('no,找不到檔案')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	#p = []
	# p.append(name)
	# p.append(price)
	#p = [ name,price]
	products.append([name,price])
print(products)

#印出購買紀錄
for p in products:
	print(p[0],'的價格是',p[1])
	
#寫入檔案
with open('products.csv','w',encoding='utf-8') as f: #encoding='utf-8'
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ','+ p[1] + '\n')
