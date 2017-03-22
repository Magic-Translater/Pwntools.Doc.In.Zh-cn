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
     - **arch** (str) - 目标二进制程序的架构，如果 `exe` 已知的话，GDB 将会进行自动
检测（如果支持的话）。
