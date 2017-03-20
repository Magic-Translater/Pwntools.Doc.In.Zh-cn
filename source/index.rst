pwntools
====================================

``pwntools`` 是一个 CTF 框架和进行漏洞利用的开发库。

本框架使用 Python 编写，是为了拥有更快的开发速度， 也是为了让漏洞利用更加容易。

我们使用了 readthedocs_ ， 而本项目的文档在 docs.pwntools.com_ ，有以下三个分支：

- Stable_
- Beta_
- Dev_

.. _readthedocs: https://readthedocs.org
.. _docs.pwntools.com: https://docs.pwntools.com
.. _Stable: https://docs.pwntools.com/en/stable
.. _Beta: https://docs.pwntools.com/en/beta
.. _Dev: https://docs.pwntools.com/en/dev


开始
---------------

.. toctree::
   :maxdepth: 3
   :glob:

   about
   install
   intro
   globals
   commandline


Module Index
------------

 ``pwntools`` 每一个模块的文档都在这里。

.. toctree::
   :maxdepth: 1
   :glob:

   adb
   args
   asm
   atexception
   atexit
   constants
   context
   dynelf
   encoders
   elf
   exception
   flag
   fmtstr
   gdb
   log
   memleak
   replacements
   rop
   rop/*
   runner
   shellcraft
   shellcraft/*
   term
   timeout
   tubes
   tubes/*
   ui
   update
   useragents
   util/*

.. toctree::
   :hidden:

   testexample

.. only:: not dash

   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
