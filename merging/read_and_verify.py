#!/usr/bin/python

import csv, os, glob

def mdy_2_ymd(str):
    t = str.split('/')
    if len(t) > 2:
        t = list(map(int,t))
        if (t[0]) <= 12:
            return "{:04d}-{:02d}-{:02d}".format(t[2],t[0],t[1])
        elif (t[0]) >= 100:
            return "{:04d}-{:02d}-{:02d}".format(t[0],t[1],t[2])
        else :
            return "SHIT"
    else :
        return str

def coverage_check():
    coverage_count = {}
    # date
    for i in glob.glob('*.csv'):
        with open(i) as csvfile:
            reader = csv.DictReader(csvfile,fieldnames=['date','loc','number','time'])
            next(reader)
            for row in reader:
                key = (mdy_2_ymd(row['date']), row['loc'], row['time'])
                # coverage_count[key] = i
                if key in coverage_count:
                    coverage_count[key] += 1
                else:
                    coverage_count[key] = 1
                # coverage_count[(row['Date'], row['Địa danh'], row['Buổi'])] = (i, row['Số ca'])
    a =list(coverage_count.keys())
    a.sort()



    for i in a:
        print(i,coverage_count[i])

    return coverage_count

def conflict_data_check():
    conflict_check = {}
    # date
    for i in glob.glob('*.csv'):
        with open(i) as csvfile:
            reader = csv.DictReader(csvfile,fieldnames=['date','loc','number','time'])
            next(reader)
            for row in reader:
                key = (mdy_2_ymd(row['date']), row['loc'], row['time'])
                # conflict_check[key] = i
                if key in conflict_check:
                    conflict_check[key] += [(i, row['number'])]
                else:
                    conflict_check[key] = [(i, row['number'])]
                # conflict_check[(row['Date'], row['Địa danh'], row['Buổi'])] = (i, row['Số ca'])

    for i in conflict_check:
        l = conflict_check[i]
        if (len(l)) > 1:
            unanimous = True
            for k in range (1,len(l)):
                if l[k][1] != l[0][1]:
                    unanimous = False
                    break
            if unanimous == True:
                print(*i, l[0][1], sep = ', ')

    return conflict_check

conflict = conflict_data_check()
# # print(conflict)
# # quit()
# count_date = {}
# for i in conflict:
#     date = i[0]
#     # print(conflict[i])
#     files = set([i[0] for i  in conflict[i]])
#     # print (date, files)
#     # break
#     if date in count_date:
#         count_date[date].update(files)
#     else:
#         count_date[date] = files

# b = list(count_date.keys())
# b.sort()
# for i in b:
#     print(i, *list(count_date[i]))
# # print (count_date, sep='\n')
# # from datetime import date, timedelta
# # sdate = date(*map(int, a[0][0].split('-')) )
# # edate = date(*map(int, a[-1][0].split('-')) )
# # # print (sdate, edate)

# # while(sdate != edate):
# #     print(sdate)
# #     sdate += timedelta(days=1)

# # conflict_data_check()