.. testsetup:: *

   from pwn import *

:mod:`pwnlib.args` --- 魔术命令行参数
=====================================================

进行`from pwn import *`导入操作时，Pwntools会暴露出多种神奇的命令行参数和环境变量。

参数从命令行提取并将其从``sys.argv``中删除。

参数的设定不光可以从命令行附加，还可以通过以``PWNLIB_``为前缀的环境变量设定。

以启用更详细的调试输出这一最简单的例子为例，也就是设定``DEBUG``参数。
.. code-block:: bash
    $ PWNLIB_DEBUG=1 python exploit.py
    $ python exploit.py DEBUG

这些参数是自动提取的，而无须关心其名称如何，并通过:mod:`pwnlib.args.args`以全局变量:data:`args`的方式暴露出来。但``pwntools``内部保留的参数并不会以这种方式暴露。
.. code-block:: bash
    $ python -c 'from pwn import *; print args' A=1 B=Hello HOST=1.2.3.4 DEBUG
    defaultdict(<type 'str'>, {'A': '1', 'HOST': '1.2.3.4', 'B': 'Hello'})

这对于条件编码非常有用，例如用于判定此漏洞利用是用于本地还是连接的远程服务器。如果参数未定义则认为其为空。
.. code-block:: python
    if args['REMOTE']:
        io = remote('exploitme.com', 4141)
    else:
        io = process('./pwnable')
所有支持的“魔术参数”及其功用列表如下：

``pwnlib.args.DEBUG(x)``
将日志输出的详细级别设定为``debug``，此级别能显示包括`tubes`发送的每一字节内容在内的更多信息。


``pwnlib.args.LOG_FILE(x)``
通过``context.log_file``设定日志记录文件，如``LOG_FILE=./log.txt``。

``pwnlib.args.LOG_LEVEL(x)``
通过``context.log_level``设定日志详细级别，如``LOG_LEVEL=debug``。

``pwnlib.args.NOASLR(v)``
通过``context.aslr``禁用ASLR。

``pwnlib.args.NOPTRACE(v)``
通过``context.noptrace``禁用依赖``ptrace``的工具，如``gdb.attach()``语句。

``pwnlib.args.NOTERM(v)``
禁用终端的优雅输出设置及动画。

``pwnlib.args.RANDOMIZE(v)``
通过``context.randomize``启用各区段随机化
Enables randomization of various pieces via ``context.randomize``

``pwnlib.args.SILENT(x)``
将日志级别设定为``error``，静默大部分输出。

``pwnlib.args.STDERR(v)``
将日志的默认输出目标从``stdout``更改到``stderr``。 

``pwnlib.args.TIMEOUT(v)``
通过``context.timeout``设置`tube`各操作的超时时间，以秒为单位，如``TIMEOUT=30``。

``pwnlib.args.asbool(s)``
 将一个字符串转换为布尔值。

 ``pwnlib.args.isident(s)``
 检查命令行传递的字符串是否为有效标识符的辅助类函数。
 