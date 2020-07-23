# import re
# s = 'ada213892543756qweqqw332'

# def convert(value):
#     matched = value.group()
#     if int(matched) >= 6:
#         return '9'
#     else:
#         return '0'
# r = re.sub('\d',convert,s)
# print(r) 

# 关于match和search的区别


import re
s = '9ada21hh38jj92543756qweqqw332'
r = re.match('\d',s)
print(r.span())
r1 = re.search('\d',s)
print(r1.group())
r2 = re.findall('\d',s) 
print(r2)