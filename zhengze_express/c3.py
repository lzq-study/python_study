import re
s='abd,avd,akd,ajd,and,aid'
r = re.findall('a[^bvi]d',s)#[[]]表示字符集  ^表示取反
print(r)