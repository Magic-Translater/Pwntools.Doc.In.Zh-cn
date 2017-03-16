.. testsetup:: *

   from pwn import *
   old = context.defaults.copy()

.. testcleanup:: *

    context.defaults.copy = old

命令行工具
========================

pwntools附带一些有用的命令行工具，作为内部功能的封装器。

.. toctree::

.. autoprogram:: pwnlib.commandline.main:parser
   :prog: pwn
