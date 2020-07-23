
import re
lanuage = 'PythonC#JavaPHP'
r = re.sub('C#','Go',lanuage,0)
#表示字符串的替换
#上面0的位置--count表示被替换的最大次数，0表示无数次，1表示一次
print(r)


import re
lanuage = 'PythonC#JavaPHP'
r = lanuage.replace('C#','Go')
#表示字符串的替换
#上面0的位置--count表示被替换的最大次数，0表示无数次，1表示一次
print(r)