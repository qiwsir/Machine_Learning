#####  Mac OS - python、Anaconda安装配置过程

## 1 Python 安装

1.1 Python安装包下载

     Python 官网：https://www.python.org/
![](https://imgkr2.cn-bj.ufileos.com/35a5b305-5113-44d5-a205-24111eefead2.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=yKbikW48gkrwg389DpPKvkns34Y%253D&Expires=1603675924)

     然后选择电脑适用的版本
![](https://imgkr2.cn-bj.ufileos.com/c1be4a5d-a4e9-4491-b087-de5bfb665229.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=FqNddlARnq%252FK6vWZ0X0cuOCq9C0%253D&Expires=1603676005)

1.2 安装Python文件

       打开下载的安装文件，按照提示信息不断点击“继续”
    安装，直至安装完成。

![](https://imgkr2.cn-bj.ufileos.com/5919dcff-f30d-48f8-912d-b1321ef789d7.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=WUEH1v2teTHwApe%252Bt14zOmpkJJ8%253D&Expires=1603676439)

![](https://imgkr2.cn-bj.ufileos.com/00428e76-f1b9-4f37-ab53-f7009c48e326.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=j2e6SBpLaCXS2ZHRM98mtI9EXmM%253D&Expires=1603676451)


1.3 配置mac默认版本是python
    
    打开终端，输入命令where python和where python3.9，
    查看python的安装目录。
    
![](https://imgkr2.cn-bj.ufileos.com/9b774809-4b24-4361-95ec-e6fca651fd9a.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=nVe2%252F5cT5E%252BfIo8gdHn4QNW%252FFSk%253D&Expires=1603676568)

1.4 将路径配入环境变量 

    输入vi .bash_profile 进行编译，然后再输入source .bash_profile即可配置成功。这样就可以在终端直接进行python编译。

![](https://imgkr2.cn-bj.ufileos.com/ce9341b7-b5ca-403e-ae8c-1a28e4dc78c4.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=jwHuw1%252FeHMQ6EzbIf7Kt50iXD6k%253D&Expires=1603679744)

1.5 查看python的版本

    查看python的版本是3.9版本
![](https://imgkr2.cn-bj.ufileos.com/0d44522f-52c3-4eea-8dc1-91e1b5c6433a.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=plRpwfDoNBzLUdLZwQFlfzhsbzI%253D&Expires=1603676682)

    
### 2 Anaconda安装和配置

2.1 Anaconda下载 

    官网地址：
    https://www.anaconda.com/distribution/
![](https://imgkr2.cn-bj.ufileos.com/29598c77-4db5-43f0-8f3d-b77b813b4cfe.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=S2jEO%252BgXqyTRg8ueniA3Fek6tGk%253D&Expires=1603676861)

2.2 Anaconda安装
  
    安装包下载好之后，双击安装包进入安装过程，不断点击继续，默认安装路径，
    直到安装完毕。然后在mac终端命令行输入conda list，列出所有安装的工具包。

![](https://imgkr2.cn-bj.ufileos.com/f71dd4d6-ca14-410f-bdc0-2f5fe0020a2d.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=hNjw19cEg2kO7%252FaK66oYVSOeuKQ%253D&Expires=1603677472)


2.3 Anaconda 环境配置
    
    找到Anaconda的下载路径/Users/cheneylu/opt/anaconda3，
    然后在终端输入vi .bash_profile,跳出编辑模式后，再输入
    export PATH=/Users/cheneylu/opt/anaconda3/bin后退出，
    最后输入source .bash_profile就配置完成了。
    
![](https://imgkr2.cn-bj.ufileos.com/978e54f2-e9fe-493e-8fcf-874183e9d162.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=7WpFNRLkdW1apIjydZhoKMJKJTE%253D&Expires=1603679325)

    配置完成后，可以在终端输入python -V查看Anaconda下
    python的版本，在输入python3进入编译模式。
    
![](https://imgkr2.cn-bj.ufileos.com/b500940a-03c0-4271-b586-56a0906a8bd6.png?UCloudPublicKey=TOKEN_8d8b72be-579a-4e83-bfd0-5f6ce1546f13&Signature=A5%252BKQ9vE%252FGqlx81BzOrAzOmc2B8%253D&Expires=1603679991)

