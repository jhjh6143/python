import re
html='html0'
pattern=re.compile('<dic><p>.*</p></div>',re.S)
r_list=pattern.findall(html)


print(r_list)

pattern=re.compile('<dic><p>(.*?)</p></div>',re.S)
r_list=pattern.findall(html)