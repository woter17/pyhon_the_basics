import csv
path = './test.csv'
row1 = ['name', 'age']
row2 = ['Bob', 17]
row3 = ['John', 71]
rows = [
    row1,
    row2,
    row3,
]
# with open(path, 'w') as f:
#     writer = csv.writer(f, delimiter=',')
#     # writer.writerow(row1) # 1 способ
#     # writer.writerow(row2)
#     # writer.writerow(row3)
#
#     writer.writerows(rows) # 2 способ
with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)