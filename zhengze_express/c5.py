# import re
# qq = '1910329063'
# #4~8
# r = re.findall('^\d{4,8}$',qq)
# print(r)

import re
qq = '00000000'
#4~8
r = re.findall('000$',qq)#^表示开头是000，$表示末尾是000
print(r)