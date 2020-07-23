import re
lanuage = 'PythonC#JavaC#PHP'
r = re.sub('C#','Go',lanuage,0)
#表示字符串的替换
#上面0的位置--count表示被替换的最大次数，0表示无数次，1表示一次
print(r) 


import re
lanuage = 'PythonC#JavaC#PHP'

def convert(value):
    #convert的返回结果替换着里面的C#
    print(value)
r = re.sub('C#',convert,lanuage,0)
# 表示字符串的替换 
# 上面0的位置--count表示被替换的最大次数，0表示无数次，1表示一次
print(r) 


import re
lanuage = 'PythonC#JavaC#PHP'
def convert(value):
    matched = value.group()
    return '!!'+ matched +'!!'
r = re.sub('C#',convert,lanuage)
# 表示字符串的替换 
# 上面0的位置--count表示被替换的最大次数，0表示无数次，1表示一次
print(r) 

