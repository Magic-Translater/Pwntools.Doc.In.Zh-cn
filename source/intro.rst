.. testsetup:: *

   from pwn import *

开始使用
========================

为了更直观的感受pwntools，我们通过几个例子来演示。

当你在写自己的exp时，pwntools会遵循“洗碗槽”的方法。


    >>> from pwn import *

这将引用pwntools进入当前的命名空间。你现在可以用一些简单函数进行汇编，反汇编，pack，unpack等等其他操作。

整个pwntools的使用文档在这里查看： :doc:`globals`.


取得连接
------------------

在pwn一个二进制挑战之前你是不是需要和相关的端口取得关联？引用 :mod:`pwnlib.tubes` 将会使它变得相当简单。

这个模块会建立一个与进程、socket、端口和其他相关的连接，例如，远程操作连接可以通过 :mod:`pwnlib.tubes.remote` 来实现。

    >>> conn = remote('ftp.debian.org',21)
    >>> conn.recvline() # doctest: +ELLIPSIS
    '220 ...'
    >>> conn.send('USER anonymous\r\n')
    >>> conn.recvuntil(' ', drop=True)
    '331'
    >>> conn.recvline()
    'Please specify the password.\r\n'
    >>> conn.close()

运转一个监听器也相当简单：

    >>> l = listen()
    >>> r = remote('localhost', l.lport)
    >>> c = l.wait_for_connection()
    >>> r.send('hello')
    >>> c.recv()
    'hello'

与一个进程进行交互你将用到 :mod:`pwnlib.tubes.process`.

::

    >>> sh = process('/bin/sh')
    >>> sh.sendline('sleep 3; echo hello world;')
    >>> sh.recvline(timeout=1)
    ''
    >>> sh.recvline(timeout=5)
    'hello world\n'
    >>> sh.close()

你现在不仅可以以编码的方式和进程通信，也可以与之 **交互** ：

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

在编写exp时最常见的工作就是再整数之间转换，和它们的在字节上的表现。通常情况下，人们使用 ``struct`` 这个模块。

pwntools通过 :mod:`pwnlib.util.packing` 这一模块使之实现十分简单。  不需要再记住解包装的代码, 只需要看着说明文档进行编码工作就好.

    >>> import struct
    >>> p32(0xdeadbeef) == struct.pack('I', 0xdeadbeef)
    True
    >>> leet = '37130000'.decode('hex')
    >>> u32('abcd') == struct.unpack('I', 'abcd')[0]
    True

包装和解包装的操作可以被定义为各种位宽：

    >>> u8('A') == 0x41
    True

设置目标系统及架构
--------------------------------------

目标的系统及架构可以在这里被简单定义为一个你需要的参数：

    >>> asm('nop')
    '\x90'
    >>> asm('nop', arch='arm')
    '\x00\xf0 \xe3'

然而，它只能在全局 ``context`` 设置一次，操作系统，字节序，位宽都可以在那里设定。
    >>> context.arch      = 'i386'
    >>> context.os        = 'linux'
    >>> context.endian    = 'little'
    >>> context.word_size = 32

另外，你也可以一次就设置好这些变量：

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

另外，你也可以一次就设置好这些变量：

例如，这样设置：

    >>> context.log_level = 'debug'

将接收到和发送到所有数据打印在屏幕上

.. doctest::
   :hide:

    >>> context.clear()

汇编和反汇编
------------------------

你总会运行从互联网上得来的shellcode，这时你也可以使用 :mod:`pwnlib.asm` 模块。

    >>> asm('mov eax, 0').encode('hex')
    'b800000000'

这样做，会更加容易：

    >>> print disasm('6a0258cd80ebf9'.decode('hex'))
       0:   6a 02                   push   0x2
       2:   58                      pop    eax
       3:   cd 80                   int    0x80
       5:   eb f9                   jmp    0x0

但是，你大多数情况下使用自己编写的shellcode，pwntools提供了 :mod:`pwnlib.shellcraft` 这个模块，可以在你编写自己的shellcode时提供帮助。

如果说我们想让 `setreuid(getuid(), getuid())` 在 复制文件描述符之后to `stdin`, `stdout`, 接着 `stderr`, 然后就可以弹出 shell!

    >>> asm(shellcraft.setreuid() + shellcraft.dupsh(4)).encode('hex') # doctest: +ELLIPSIS
    '6a3158cd80...'


杂项工具
----------------------
多亏有了 :mod:`pwnlib.util.fiddling` 这个模块，我们不需要写另外的hexdump。

在触发的崩溃中寻找偏移量或缓冲区大小，可以使用模块 :mod:`pwnlib.cyclic`.

    >>> print cyclic(20)
    aaaabaaacaaadaaaeaaa
    >>> # Assume EIP = 0x62616166 ('faab' which is pack(0x62616166))  at crash time
    >>> print cyclic_find('faab')
    120

操纵ELF文件
----------------

停止用手写代码的工作吧！看一看 :mod:`pwnlib.elf` 这个模块。

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
