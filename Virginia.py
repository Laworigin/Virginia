# !/bin/usr/
# conding:utf-8
# author:Wisdom_Tree
# get key and decode Virginia

import re
import math

c=str(input("请输入密文:"))
c=c.replace(" ","")
# print(c[0])
c_len=len(c)
# print(c_len)
c_list=list(c)
# print(len(c_list))
# for i in c_list:
# 	print(i)
c_list_gro={}  #创建空子典
c_column_gro=[]
avg=[]  #存储每一长度的距0.065的差值
decode_list=[]


# 算法公式：每个字母出现次数乘以出现次数减一，
# 将26个字母的乘积相加得到A
# 当前列的所有字母数量乘以字母数量减一得到B
# A/B得到最终的重合指数，越接近0.065表示越正确


def get_coincidence(c_column): #计算重合指数
	c_column=c_column.lower()
	# print(c_column)
	total_len=len(c_column)
	result1=0
	src_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	# print(len(src_list))
	for i in src_list:
		pre_time=c_column.count(i)	#统计出现次数
		# print(i,pre_time)
		result1=result1+(pre_time*(pre_time-1))
	result2=total_len*(total_len-1)
	result=result1/result2
	return result



def key_len(c_str,key_length):  #提取每一列中的所有字母
	c_str_len=len(c_str)
	pre_list=[]
	if c_str[c_str_len-1]=="*":   #删除最后一个*号
		c_str=c_str[:c_str_len-1]
	print(c_str)
	c_str_list=c_str.split("*")

	for j in range(0,key_length):  
		# print(j)
		pre_list_tmp=[]
		for i in c_str_list:
			try:   #捕获异常，以防超出合法范围
				pre_list_tmp.append(i[int(j)])
				# print(i[int(j)])
			except Exception:
				continue
		pre_list_str_tmp=""
		pre_list_str=pre_list_str_tmp.join(pre_list_tmp)
		pre_list.append(pre_list_str)

	for i in pre_list:
		print(i)

	prob=0
	for evr_list in pre_list:  #取每一列的字母
		column_prob=get_coincidence(evr_list)  #保留小数点后三位
		c_column_gro.append(evr_list)
		prob=prob+(column_prob)
	to_avg=prob/key_length
	# avg.append(to_avg)
	num_diff=abs(to_avg-0.065)
	avg.append(num_diff)
	# print(str(key_length)+": "+prob)
	print(str(key_length)+": "+str(to_avg))
	print("--------------------")


def stat_freq(n,c_column_gro):  #统计真实key长度的每一列的每一个字母出现频率 
	start=Factorial(n)	 #对列表进行切片，获取指定长度的column
	# for i in c_column_gro:
	# 	print(i)
	# print("**********************")
	src_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	c_column_gro=c_column_gro[start:start+n]
	key=""
	for column in c_column_gro:
		column=column.lower()
		decode_list.append(column)
		print(column)
		key_part=displace(column)
		key=key+str(key_part)
		print("***************************")
		# column_len=len(column)
		# column=column.lower()
		# result1=0
		# for src in src_list:
		# 	occur_time=column.count(src) #计算出现次数
		# 	result1=result1+occur_time*(occur_time-1)
		# 	occur_prob=occur_time/column_len
		# 	print(src+"出现的概率为"+str(round(occur_prob,3)))
		# result2=column_len*(column_len-1)
		# result=result1/result2
		# print("-------------------")
		# print(column)
		# print(result)
		# print("*******************")
	print("key is:"+key)
	return key

def displace(column): #26位位移
	# column2=column
	# print(column)
	# print(".................................")
	coin=[]  #重合指数列表
	coin2=[]
	for j in range(0,26):
		# column2=column
		change_str=""
		for i in column:
			i=ord(i)+j
			if i>122:
				i=96+(i-122)
				change_str=change_str+chr(i)
			else:
				change_str=change_str+chr(i)
		# print(change_str)
		quasi_coin(change_str,coin2)
		# result=get_coincidence(change_str) #计算每一次位移之后的重合指数
		# print(change_str+"\n")
		# coin.append(abs(result-0.065))
	# mini=coin.index(min(coin))  #获取列表中最小值的下标
	mini2=coin2.index(min(coin2))
	# print(chr(97+mini2))
	# print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
	# mini=97+i
	# if mini>122:
	# 	mini=97+(mini-122)
	# key_part=chr(int(mini)+97)
	key_part=chr(97+mini2)
	return key_part

# def new_coincidence(column_str):  #计算重合指数
# 	p = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056,0.02758, 0.00978, 0.02360, 0.00150,0.01974, 0.00074]
# 	len_column=len(column_str)
# 	column_coin=[]
# 	sum_column=0
# 	for i in range(0,26):
# 		column_coin.append(column_str.count(chr(97+i),0,len_column)/len_column)
# 	for i in range(0,26):
# 		f=(column_coin[i]*p[i])
# 		sum_column=sum_column+f
# 	return sum_column

def quasi_coin(column,coin2):  #拟重合指数 计算key的值
	p = [0.08167,0.01492,0.02782,0.04253,0.12705,0.02228,0.02015,0.06094,0.06996,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.0009,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.0015,0.01974,0.00074]
	q = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	total_coin=0
	column_len=int(len(column))
	for i in range(0,26):
		# print(((column.count(q[i])/column_len)*p[i])/column_len)
		# part_coin=(((column.count(q[i])/column_len)*p[i])/column_len)*100
		# part_coin=column.count(q[i])*(column.count(q[i])-1)/(column_len*(column_len-1))
		# part_coin=((column.count(q[i])*p[i])/column_len)
		part_coin=(column.count(q[i])/column_len)*p[i]  #频率*频率表
		# part_coin=
		total_coin=total_coin+part_coin
	print(total_coin)
	coin_avg=abs(total_coin-0.065)
	coin2.append(coin_avg)
	print("##############################")

def Factorial(n):	#计算阶乘
	result=0
	for i in range(1,n):
		result=result+i
	return result

def decode(key,c_list):
	p_list=[]
	p_str_p=""
	for i,j in zip(c_list,key):
		print(i,j)
		p_line=""
		for c_str in i:
			p_str=ord(c_str)+(ord(j)-97)
			# print(p_str)
			if p_str>122:
				p_str=chr(96+(p_str-122))
				p_line=p_line+p_str
			else:
				p_str=chr(p_str)
				p_line=p_line+p_str
		print(p_line)
		p_list.append(p_line)
	
	# for pp in p_list:
	# 	print("*************************")
	# 	print(pp)
	# 	print("**********")

	for i in range(0,100):
		try:
			for p in p_list:
				# print(p[i])
				p_str_p=p_str_p+p[i]
		except Exception:
			continue
	# print(p_str)
	return p_str_p


# 循环遍历K的长度，将密文转换为列表，每隔k个列表元素插入一个*号作为标记
# 最后使用join方法将插入标识符的列表转化为字符串
# 将k的值存入字典的key中，将标记过flag的值存入字典value中

for i in range(1,10):
	c_list2=c_list.copy()  #复制列表
	list_len=len(c_list)
	for list_lens in range(1,list_len+1):
		if list_lens%i==0:
			# print(list_lens-1)
			c_list2[list_lens-1]=c_list2[list_lens-1]+"*"
	# print(c_list2)
	c_list2_str_tmp=""
	c_list2_str=c_list2_str_tmp.join(c_list2)
	# c_list_gro.append(c_list2_str)
	c_list_gro[str(i)]=c_list2_str
	key_len(c_list2_str,i)

mini=avg.index(min(avg))
print("秘钥长度为:"+str(mini+1))

# real_key_len=input('stop-------------')
key=stat_freq(mini+1,c_column_gro)
p=decode(key,decode_list)
print("-------------------------------------")
print("result:")
print("key is:"+key)
print("Plaintext is:"+p)


# print("----------------------")
# # print(c_list)
# for c_str_key in c_list_gro.keys():
# 	print(c_str_key)


# 统计每个字母的出现频率，和概率表进行比较，获取偏移量，进行还原，最后获得秘钥

