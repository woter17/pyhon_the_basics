# import json
# path = './log_100.json'
# with open(path) as f:
#     d = json.load(f)
# ip_dict ={}
# for row in d:
#     if row['ip'] not in ip_dict:
#         ip_dict[row['ip']] = 1
#     else:
#         ip_dict[row['ip']] += 1
# tmp_lst = []
# for val in ip_dict.values():
#     tmp_lst.append(val)
# tmp_lst.sort()
# print(tmp_lst)
# print(str(sum(tmp_lst[-3:]) / sum(tmp_lst) * 100) + '%')
# k = 0
# for i in tmp_lst:
#     if i == 1:
#         k+=1
# print(k)

#задача 2
# import csv
# min = 999999
# path ='./log_cereals.csv'
# with open(path) as f:
#     reader = csv.reader(f)
#     i = 0
#     sum = 0
#     k = -1
#     for row in reader:
#         k+=1
#         if i == 0:
#             i+=1
#             continue
#         sum += float(row[2])
#         if float(row[1]) < min:
#             min = float(row[1])
# print(min,sum/k)

#Zadacha 3

# import csv
# ip_dict = {}
# path = 'log_full.csv'
# with open(path) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         ip = row[1]
#         if ip not in ip_dict:
#             ip_dict[ip] = 1
#         else:
#             ip_dict[ip] += 1
# max_val = 0
# result_ip = ''
# for ip in ip_dict:
#     if ip_dict[ip] > max_val:
#         max_val = ip_dict[ip]
#         result_ip = ip
# print(max_val,ip)
#i td

