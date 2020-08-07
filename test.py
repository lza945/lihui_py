# coding:utf-8
# data = 'hello,world'
# f = open('login.yaml','w')
# f.write(data)
# f = open('scores.txt')
# data = f.readlines()
# f.close()
# #print(data)
# for i in data:
#     datas = i.split()
#     #print(datas)
#     score_list = datas[1:]
#     #print(score_list)
#     sum = 0
#     for score in score_list:
#
#         sum += int(score)
#     print(sum)

i = 0
while i < 5:
   i += 1
   for j in range(3):
       print ('j=%d'%j)
       if j == 2:
           break
   for k in range(3):
       if k == 2:
           continue
       print ('k=%d'%k)
   if i > 3:
       break
   print ('i=%d'%i)



