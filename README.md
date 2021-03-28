# ipaddress-github
在国内上github.com常常会出现打不开界面的情况，这时需要去查询github.com的ip地址并添加到电脑hosts文件中(Windows系统下)。反复的手动查找效率太低，因此写了一个自动从[ipaddress](https://www.ipaddress.com/)
上爬取github网站ip地址的脚本，并在不删改hosts文件中其它内容的情况下，添加github.com的ip地址，然后调取命令行flushdns。

## 使用说明
1. 改动etc/hosts下的文件读写权限，改为可以读写的模式，不然会报PermissionError错误。修改权限参考[网站](https://blog.csdn.net/weixin_42664622/article/details/104310511)
2. 查找自己浏览器的headers，参考[网站](https://blog.csdn.net/xiezhiming1234/article/details/83592290)
3. 将src/main.py中的headers变量改为自己浏览器的headers
4. 每次登不上github.com运行代码

**注意**：少数情况下，使用该方法仍登不上github.com

## 参考
1. [https://zhuanlan.zhihu.com/p/353522535](https://zhuanlan.zhihu.com/p/353522535)










