# pwntools.translate

<!-- MarkdownTOC -->

- [0x00 说明](#0x00-说明)
- [0x01 markdown规范](#0x01-markdown规范)
- [0x02 编辑环境配置](#0x02-编辑环境配置)
- [0x03 分工&版本](#0x03-分工&版本)

<!-- /MarkdownTOC -->

* **重要说明：使用git时一定要先使用`git pull`将软件仓库的代码到pull到本地才开始自己的工作！否组很可能所有人的工作前功尽弃！**

* participator : passexcel, DrimTuer, iphan, swing

* pwntools offical docs : [http://docs.pwntools.com/en/stable/](http://docs.pwntools.com/en/stable/)

## 0x00 说明

这是一个为[Pwntools](https://github.com/Gallopsled/pwntools)进行本地化的项目。

## 0x01 markdown规范

为了后期整理方便，需要大家统一markdown的写作规范。

**markdown默认不分段，所以段落和段落之间一定要多一个回车**

其余的在下面这个链接参考：[markdown简明中文文档](http://wowubuntu.com/markdown/basic.html)

## 0x02 编辑环境配置

推荐sublime text（插件简直太爽）。有这么几个markdown的插件：

* `Markdown Preview`，可以在浏览器中预览当前编辑的markdown文件。

* `Markdown Editing`，编辑markdown的皮肤？（应该是吧，可以补全括号引号什么的）

* `Markdown Extended`，支持markdown语法高亮。

## 0x03 分工&版本

鉴于Pwntools更新频繁，组员均为业余时间进行翻译，翻译原本采用stable版。之后正式提交时再校对为latest。

* 前五章以由众人共同完成
* 每人自行选取感觉适合的**一整个章节**进行翻译。
* 文件命名方式：同Index文件的命名。特殊字符如\*可替换为下划线等等。

**翻译前的准备工作：**

* 首先commit一个空文件。
* 在Index文件处添加自己的ID
* 在Index文件更新时，自行更新对应的文件名。

**关于更新Index**

* Pwntools自身一直在不断更新，对应的文档也会发生变动，一但docs源被更新，Index文件也需同步更新。
* 每次Index更新之后，请**以显著的方式提醒所有成员**，如issue/群消息。
