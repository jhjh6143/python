from django.http import HttpResponse

def shebao(request):
    html='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/shebao" method="post">
    <div>
        请输入基数<input type="input" name="POST">
    </div>
    <div>
        请输入选择户口
        <select name="is_city">
            <option value="1">城镇户口</option>
            <option value="0">农村户口</option>
        </select>
    </div>
    <input type="submit">
</form>
</body>
</html>
'''

    html_end='''
    '''

    if request.method=="GET":
        return HttpResponse(html)
    elif request.method=='POST':
        base=request.POST.get('income',0)
        base=base if base else '0'
        base=float(base)
        is_city=request.POST.get('is_city')
        html_table = '''
            <table>
            <thead>
            <tr>
                <th style="text-align: center">项目</th>
                <th style="text-align: center">个人缴纳</th>
                <th style="text-align: center">单位缴纳</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th style="text-align: center">项目</th>
                <th style="text-align: center">个人缴纳</th>
                <th style="text-align: center">单位缴纳</th>
            </tr>
            </tbody>
        </table>
            '''
    # else:
    #     return HttpResponse(html + html_table+html_end
