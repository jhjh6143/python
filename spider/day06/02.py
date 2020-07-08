#pip install pyexecjs
import execjs

with open('01.js','r') as f:
    js_data=f.read()

exec_obj=execjs.compile(js_data)
sign=exec_obj.eval('e("hello")')
print(sign)