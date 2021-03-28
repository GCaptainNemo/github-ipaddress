# ipaddress-github
国内上github常出现打不开界面情况，这时需要去查询github的ip地址并添加到电脑hosts文件中(Windows系统下)。反复的手动查找效率太低，因此写了一个自动从[ipaddress](https://www.ipaddress.com/)
上爬取github网站ip地址的脚本，在不删改hosts文件中其它内容的情况下，添加github的ip地址，然后调取命令行刷新dns(ipconfig /flushdns)。

## 使用说明
1. 更改etc/hosts下的文件权限，改为可读写模式，不然代码运行会报PermissionError错误。修改权限参考[网站](https://blog.csdn.net/weixin_42664622/article/details/104310511)
2. 查找浏览器的headers，参考[网站](https://blog.csdn.net/xiezhiming1234/article/details/83592290)
3. 将src/main.py中的headers变量改为自己浏览器的headers
4. 登不上github时，运行代码main.py

**附**：少数情况下，使用该方法仍登不上github。

## 参考
1. [https://zhuanlan.zhihu.com/p/353522535](https://zhuanlan.zhihu.com/p/353522535)










