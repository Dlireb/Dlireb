# 案例2：msg='/etc/a.txt|365|get' 将该字符的文件名，文件大小，操作方法切割出来
msg='/etc/a.txt|365|get'
print(msg.split('|'))