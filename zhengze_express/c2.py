#概括子母集
# \d 数字字符
# \D  非数字字符
# \w(只能匹配单词字符--数字、子母、下划线)  
# \W(非单词字符)
# \s空白字符
# \S非空白字符
import re

a='C0C++t7Java5C#69PythonhgJavacript'

r = re.findall('\W',a)

print(r)