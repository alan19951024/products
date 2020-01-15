import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename,'r',encoding='utf-8') as f: #encoding='utf-8'
			for line in f:
				if '商品,價格' in line:
					continue #繼續 跳到下一迴
				name,price = line.strip().split(',')
				products.append([name,price])
	return products

#讓使用者輸入
def user_input (products):
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
	return products

#印出購買紀錄
def print_products(products):
	for p in products:
		print(p[0],'的價格是',p[1])
	
#寫入檔案
def write_file(filename,products):
	with open(filename,'w',encoding='utf-8') as f: #encoding='utf-8'
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ','+ p[1] + '\n')

#為程式進入點
def main():	
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案有沒有存在
			print('YES,有找到')
			products = read_file (filename)
	else:
		print('no,找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv',products)

main()