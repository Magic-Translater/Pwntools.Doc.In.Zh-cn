.. testsetup:: *

   from pwn import *
   import logging
   log = pwnlib.log.getLogger('pwnlib.context')

:mod:`pwnlib.context` --- 设定运行时变量
=====================================================

.. autodata:: pwnlib.context.context

.. autoclass:: pwnlib.context.ContextType
    :members:

.. autoclass:: pwnlib.context.Thread
