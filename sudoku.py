

import random
import sys

temp = [ i for i in range(0,9)]
column, row = 9, 9
total = [[0 for _ in range(row)] for _ in range(column)]

for i in range(0,9) :
	temp[i] = input("input : ")


for i in range(9) :
	for j in range(9) :
		total[i][j] = int(temp[i][j])

def first_empty(total,x,y) : #找到第一個空的地方 直接使用next_empty 若第一個就為空則會造成省略
	for temp_y in range(y,9):
		if total[x][temp_y] == 0 : 
			return x,temp_y

	for temp_x in range(x+1,9):
		for temp_y in range(0,9) :
			if total[temp_x][temp_y] == 0 :
				return temp_x,temp_y

	return -1,-1 #代表全部找完

def next_empty(total,x,y) : #找到空的地方
	for temp_y in range(y+1,9):
		if total[x][temp_y] == 0 :
			return x,temp_y

	for temp_x in range(x+1,9):
		for temp_y in range(0,9) :
			if total[temp_x][temp_y] == 0 :
				return temp_x,temp_y

	return -1,-1 #代表全部找完

def find_list(total,x,y) : #找到可以填入的數字
	temp_a = x//3 *3
	temp_b = y//3 *3
	temp_nine =  set([total[a][b] for a in range(temp_a, temp_a+3) for b in range(temp_b, temp_b+3)]) #九宮格內出現過的數字
	temp_xlist = set([ total[x][i] for i in range(0,9) ]) # 找到同列出現過的數字
	temp_ylist = set([ total[i][y] for i in range(0,9) ]) # 找到同行出現過的數字
	temp_list = set([ i for i in range(1,10) ]) # 原本有1~9
	temp_list = temp_list - temp_xlist - temp_ylist - temp_nine #刪除已存在的數字
	
	return temp_list			


def sudoku(total,x,y) :
	temp_list = find_list(total,x,y) #刪除已存在行、列、九宮格中的數字
	for temp in temp_list :
		total[x][y] = temp 
		next_x,next_y = next_empty(total,x,y)
		if next_x == -1 : #若x和y都回傳-1 則代表找不到下一個空的位置
			if next_y == -1 :
				return True 
		else :
			is_finish = sudoku(total,next_x,next_y)
			
		if is_finish : #全部找完 所以結束
			return True  

		total[x][y] = 0 #未找到所以設回空

	return False


x,y = first_empty(total,0,0) #找到第一個為0的地方
sudoku(total,x,y)

print( "output:" )
for i in range(0,9) :
	for j in  range(0,9) :
		print(total[i][j], end='')

	print('\n', end='')



