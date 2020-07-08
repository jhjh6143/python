from lxml import etree

html='''
jgkhk
'''
pares_html=etree.HTML(html)
r_list=pares_html.xpath('//a/text()')
print(r_list)
