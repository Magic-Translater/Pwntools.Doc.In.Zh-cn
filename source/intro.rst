.. testsetup:: *

   from pwn import *

开始使用
========================

为了能够让你亲身实践一下pwntools，首先，我们来看几个简单的例子。

当在编写自己的exp时，我们一般会采用下面的方法，这样的话，pwntools就会将会它的所有功能都导入进来。


    >>> from pwn import *

显然，这样的话，你将在全局空间里引用pwntools的所有函数。你现在可以用一些简单函数进行汇编，反汇编，pack，unpack等等其他操作。

整个pwntools的使用文档在这里查看： :doc:`globals`.


连接
------------------

如果你想要pwn一个程序的话，你肯定需要和它进行交互，对吧？pwntools使用它的模块 :mod:`pwnlib.tubes` 使这个变得相当简单。

这个模块会建立一个与进程、socket、端口和其他相关的连接。例如，远程操作连接可以通过 :mod:`pwnlib.tubes.remote` 来实现。

    >>> conn = remote('ftp.debian.org',21)
    >>> conn.recvline() # doctest: +ELLIPSIS
    '220 ...'
    >>> conn.send('USER anonymous\r\n')
    >>> conn.recvuntil(' ', drop=True)
    '331'
    >>> conn.recvline()
    'Please specify the password.\r\n'
    >>> conn.close()

它也可以很容易地使得一个监听者处于等待状态：

    >>> l = listen()
    >>> r = remote('localhost', l.lport)
    >>> c = l.wait_for_connection()
    >>> r.send('hello')
    >>> c.recv()
    'hello'

此外，我们也可以利用 :mod:`pwnlib.tubes.process` 来简单地和进程进程交互。

::

    >>> sh = process('/bin/sh')
    >>> sh.sendline('sleep 3; echo hello world;')
    >>> sh.recvline(timeout=1)
    ''
    >>> sh.recvline(timeout=5)
    'hello world\n'
    >>> sh.close()

当然，你不仅可以利用程序来和进程进行通信，也可以直接与之 **交互** ：

    >>> sh.interactive() # doctest: +SKIP
    $ whoami
    user

当你通过ssh方式进行漏洞利用的时候，可以使用 :mod:`pwnlib.tubes.ssh`.

::

    >>> shell = ssh('bandit0', 'bandit.labs.overthewire.org', password='bandit0')
    >>> shell['whoami']
    'bandit0'
    >>> shell.download_file('/etc/motd')
    >>> sh = shell.run('sh')
    >>> sh.sendline('sleep 3; echo hello world;') # doctest: +SKIP
    >>> sh.recvline(timeout=1)
    ''
    >>> sh.recvline(timeout=5)
    'hello world\n'
    >>> shell.close()

包装整数
------------------

在编写exp时，最常见的工作就是在整数之间转换，而且转换后，它们的表现形式就是一个字节序列。通常情况下，我们使用 ``struct`` 这个模块。

pwntools通过 :mod:`pwnlib.util.packing` 使之十分简单。这样我们就不需要再记住解包装的代码, 只需要看着说明文档编写代码就行.

    >>> import struct
    >>> p32(0xdeadbeef) == struct.pack('I', 0xdeadbeef)
    True
    >>> leet = '37130000'.decode('hex')
    >>> u32('abcd') == struct.unpack('I', 'abcd')[0]
    True

此外，pack和unpack的操作也支持其它字长，比如8位字长：

    >>> u8('A') == 0x41
    True

设置目标系统架构及操作系统
--------------------------------------

我们在操作中特别指定目标机器的系统架构：

    >>> asm('nop')
    '\x90'
    >>> asm('nop', arch='arm')
    '\x00\xf0 \xe3'

此外，我们也可以通过一次性地在全局的参数 ``context``中设置，操作系统，字节序，大小端，位宽都可以在那里设定。
    >>> context.arch      = 'i386'
    >>> context.os        = 'linux'
    >>> context.endian    = 'little'
    >>> context.word_size = 32

当然，你也可以一次性设置好这些变量：

    >>> asm('nop')
    '\x90'
    >>> context(arch='arm', os='linux', endian='big', word_size=32)
    >>> asm('nop')
    '\xe3 \xf0\x00'

.. doctest::
   :hide:

    >>> context.clear()

设置日志记录级别
-------------------------

你可以通过context来控制日志记录的级别：

例如，这样设置：

    >>> context.log_level = 'debug'

这样，通过管道发送和接收的数据都会被打印在屏幕上。

.. doctest::
   :hide:

    >>> context.clear()

汇编和反汇编
------------------------

有时候，你可能需要从互联网上下载一些shellcode，这时你可以使用 :mod:`pwnlib.asm` 模块。

    >>> asm('mov eax, 0').encode('hex')
    'b800000000'

如果你按照下面的方式来做，会更加容易：

    >>> print disasm('6a0258cd80ebf9'.decode('hex'))
       0:   6a 02                   push   0x2
       2:   58                      pop    eax
       3:   cd 80                   int    0x80
       5:   eb f9                   jmp    0x0

而且，你甚至不需要大部分时间去写shellcode。pwntools提供了 :mod:`pwnlib.shellcraft` ，可以在你编写shellcode的时候提供帮助。

如果说我们想执行 `setreuid(getuid(), getuid())`，之后复制文件描述符4到 `stdin`, `stdout` 以及 `stderr`, 然后弹出一个shell!，那我们就可以这么做

    >>> asm(shellcraft.setreuid() + shellcraft.dupsh(4)).encode('hex') # doctest: +ELLIPSIS
    '6a3158cd80...'


杂项工具
----------------------
多亏有了 :mod:`pwnlib.util.fiddling` 这个模块，我们不需要写另外的hexdump。

我们可以通过使用模块 :mod:`pwnlib.cyclic` 在触发的崩溃中寻找偏移量或缓冲区大小。

    >>> print cyclic(20)
    aaaabaaacaaadaaaeaaa
    >>> # Assume EIP = 0x62616166 ('faab' which is pack(0x62616166))  at crash time
    >>> print cyclic_find('faab')
    120

操纵ELF文件
----------------

我们也不需要进行硬编码了，因为我们可以使用 :mod:`pwnlib.elf` 来在运行时查看对应的参数。

    >>> e = ELF('/bin/cat')
    >>> print hex(e.address) #doctest: +SKIP
    0x400000
    >>> print hex(e.symbols['write']) #doctest: +SKIP
    0x401680
    >>> print hex(e.got['write']) #doctest: +SKIP
    0x60b070
    >>> print hex(e.plt['write']) #doctest: +SKIP
    0x401680

你也可以给ELF文件打补丁或是保存。

    >>> e = ELF('/bin/cat')
    >>> e.read(e.address+1, 3)
    'ELF'
    >>> e.asm(e.address, 'ret')
    >>> e.save('/tmp/quiet-cat')
    >>> disasm(file('/tmp/quiet-cat','rb').read(1))
    '   0:   c3                      ret'
