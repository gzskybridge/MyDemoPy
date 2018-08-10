from urllib import request

response=request.urlopen('http://www.baidu.com/')
fi=open('/tmp/baidu.txt','w')
page=fi.write(repr(response.read()))
print(page)
fi.close()
