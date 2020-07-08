import csv

with open('test.csv','w',newline='',encoding='utf-8') as f:
    riter=csv.writer(f)
    riter.writerow(['啊',20])
    riter.writerow(['是',22])

with open('test.csv','a',newline='',encoding='utf-8') as f:
    riter=csv.writer(f)
    data_list=[('的',23),('发',24)]
    riter.writerows(data_list)
