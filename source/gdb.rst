:mod:`pwnlib.gdb` --- Working with GDB
======================================

``attach(target, execute = None, exe = None, arch = None, ssh = None) -> None``

在新的终端中启动终端，并将其attach到 `target` 上。除了 `target` 是 ``(host, port)`` 外，:func:`pwnlib.util.proc.pidof` 用来寻找 `target` 的PID。在那种情况下， `target` 应该为 一个GDB Server。

如果在本地运行，并且没有提供 `exe` ，那么我们就尝试分析运行
GDB Server(qemu,gdbserver) 命令的程序，寻找目标二进制文件的路径。注意，如果PID 是一
个已知的(当目标不是GDB Server), `exe` 将会从 ``/proc/<pid>/exe`` 中读取。

如果安装了gdb-multiarch, 我们就使用它，否则就使用gdb。参数如下

     - **target** - 要被attach到的target。
     - **execute** (str or file) - attach 之后，GDB 要运行的脚本。
     - **exe** (str) - 目标二进制程序的路径
     - **arch** (str) - 目标二进制程序的架构，如果 `exe` 已知的话，GDB 将会进行自动检测（如果支持的话）。

返回值为None。

``pwnlib.gdb.debug(args) -> tube``

使用给定的命令行启动GDB Server，然后启动GDB，并将其attach到GDB Server上。

参数如下：

     - **args** - 与传给 :mod:`pwnlib.tubes.process` 的参数一致。
     - **ssh** - 用于启动进程的远程ssh会话。这样的话，就会自动启动端口转发，然后gdb就可以在本地运行了。

返回值为连接到目标进程的tube。

``pwnlib.gdb.debug_shellcode(*a,**kw)``

创建一个ELF文件，并且使用GDB启动它。

参数如下：

      - **data** (str) - 经过汇编的shellcode。
      - **kwargs** (dict) -  传给context的参数(e.g arch='arm')。

返回一个管道，这个管道会和stdin/stdout/stderr连接在一起。


``pwnlib.gdb.debug_assembly(*a,**kw)``

创建一个ELF文件，并且使用GDB启动它。

这和debug_shellcode一样，不仅可以使用所有已经定义在GDB里的符号，而且它还省去了我们对asm的显式调用。

``pwnlib.gdb.find_module_addresses(binary,ssh=None,ulimit=False)``

通过使用gdb来查找模块。

由于一些服务器会禁止 ``proc/$pid/map`` ，所以我们不能够使用这个。这个虽然阻断了GDB中的 ``info proc`` ，但是 ``info sharedlibrary`` 仍然可以执行。
除此之外， ``info sharedlibrary`` 也在FreeBSD上工作，但是，这上面可能没有启动procfs或者说它不可用。

输出的结果就像这个一样::

    info proc mapping
    process 13961
    warning: unable to open /proc file '/proc/13961/maps'

    info sharedlibrary
    From        To          Syms Read   Shared Object Library
    0xf7c820    0xf7ff505f  Yes (*)     /lib/ld-linux.so.2
    0xf7fbb650  0xf7fc79f8  Yes         /lib32/libpthread.so.0
    0xf7e26f10  0xf7f5b51c  Yes (*)     /lib32/libc.so.6
    (*): Shared library is missing debugging information.


注意由 ``info sharedlibrary`` 提供的最初始的地址就是 ``.text`` 段的地址，并不是镜像基地址。

这个方法自动化了下面的流程：

   1. 从远程下载二进制文件。
   2. 爬取GDB的信息。
   3. 为ELF文件加载每一个库。
   4. 修复基地址 vs ``.text`` 段地址

参数如下：

   - **binary** (str) - 远程服务器上二进制文件的路径。
   - **ssh** (pwnlib.tubes.tube) - 通过该种方式加载二进制文件的方式，如果什么也不填的话，将会使用 ``pwnlib.tubes.process.process``
   - **ulimit** (bool) - 如果设置为真的话，将会在启动GDB之前执行 ``ulimit -s unlimited``

返回值一个列表，其中每个元素都具有正确的基地址。
::
OB
   >>> with context.local(log_level=9999):
   ...     shell = ssh(host='bandit.labs.overthewire.org',user='bandit0',password='bandit0')
   ...     bash_libs = gdb.find_module_addresses('/bin/bash', shell)
   >>> os.path.basename(bash_libs[0].path)
   'libc.so.6'
   >>> hex(bash_libs[0].symbols['system'])
   '0x7ffff7634660'

