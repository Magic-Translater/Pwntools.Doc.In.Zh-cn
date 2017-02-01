# pwntools translate

**请使用`git feth; git merge origin/master`进行同步更新.**

**重要工作请使用分支和GitHub RP**

## 0x00 说明

这是一个为[Pwntools](https://github.com/Gallopsled/pwntools)进行本地化的项目。

* participator : passexcel, DrimTuer, iphan, swing
* pwntools offical docs : [http://docs.pwntools.com/en/stable/](http://docs.pwntools.com/en/stable/)

## 0x01 markdown规范

为了后期整理方便，需要大家统一markdown的写作规范。

**markdown默认不分段，所以段落和段落之间一定要多一个回车**

其余的在下面这个链接参考：[markdown简明中文文档](http://wowubuntu.com/markdown/basic.html)

## 0x02 编辑环境配置

推荐sublime text（插件简直太爽）。有这么几个markdown的插件：

* `Markdown Preview`，可以在浏览器中预览当前编辑的markdown文件。

* `Markdown Editing`，编辑markdown的皮肤？（应该是吧，可以补全括号引号什么的）

* `Markdown Extended`，支持markdown语法高亮。

其它现代编辑器以及远古神级编辑器都有对Markdown的原生支持(如Atom)或者插件支持.

## 0x03 版本 & 命名规范

文档版本采用release. 定期维护一份Index目录, 一切变动以Index为准.

命名规范:

每一章对应一份文件, 存放在source下, 文件名为`标号.章节名`.

章节名称只截取`--`后的部分.

eg:

```
05. Command Line Tools
=>
05.Command_Line_Tools

15. pwnlib.elf -- Working with ELF binaries
=>
15.Working_with_ELF_binaries
```
