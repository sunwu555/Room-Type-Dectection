import fileinput
import os

def main():
	# index_img = os.walk('JPEGImages/')
	index_lab = os.walk('Annotations/')
	f = open('train.txt', 'w')
	for a, b, c in index_lab:
		# for a1, b1, c1 in index_img:
		for filename in c:
				# if filename.strip('.xml') + '.jpg' not in c1:
				# 	print(filename)
			# if 'FR' in filename:
			# 	print(filename)
			# 	print(filename.split(' ')[0] + '.jpg')
			k = f.write(filename.strip('.xml') + '\n')
			print('successfuly write ', filename)
	# f.close()
			# print(l.strip('.xml'))
			# for l in fileinput.input('Annotations/' + filename, inplace = True):
			# 	print(l.replace('SDE', 'SDB'), end = '')
				# print(l)
				# if 'SDE' in l:
				# 	print(l.replace('SDE', 'SDB'))
				# print(l.replace('SDE', 'SDB'))
	return

main()