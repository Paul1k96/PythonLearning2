access_dict = {'write': 'W', 'read': 'R', 'execute': 'X'}
request_ans = ['Access denied', 'OK']

files = {}
for _ in range(int(input())):
    tmp_name = input().split()
    files[tmp_name[0]] = tmp_name[1:]

for _ in range(int(input())):
    request = input().split()
    print(request_ans[access_dict[request[0]] in files[request[1]]])

# for example
# 5
# my_pycode.exe W X
# log_n X W R
# ave R
# lucky_m W R
# dnsss.py W
# 6
# execute ave
# read dnsss.py
# write log_n
# execute log_n
# read ave
# write my_pycode.exe