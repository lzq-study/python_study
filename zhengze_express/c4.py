""" #数量词
import re
a = 'python 1111java678php'

r = re.findall('[a-z]{3,6}',a)
print(r)
#输出结果 ['python', 'java', 'php']
#其实取三个字母就可以结束了，这涉及到贪婪与非贪婪

#非贪婪模式是在数量集的后面加一个问号 """

import re
a = 'python 1111java678php'

r = re.findall('[a-z]{3,6}?', a)
print(r)

#输出结果 ['pyt', 'hon', 'jav', 'php']