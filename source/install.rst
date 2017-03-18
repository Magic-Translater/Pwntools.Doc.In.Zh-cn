安装
============

pwntools对ubuntu 12.04和 14.04系统支持地最好，但大多数功能在符合Posix标准的系统上（Debian, Arch, FreeBSD, OSX等等）应该也可以正常使用。

准备
-------------

为了能够充分利用 `pwntools` 的功能，你应该安装下列的系统库。

.. toctree::
   :maxdepth: 3
   :glob:

   install/*

最新发行版
-----------------

你可以利用 ``pip`` 安装pwntools。

.. code-block:: bash

    $ apt-get update
    $ apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev
    $ pip install --upgrade pwntools

开发版
--------------

如果你要在本地定制自己的pwntools，你应该这样做：

.. code-block:: bash

    $ git clone https://github.com/Gallopsled/pwntools
    $ pip install --upgrade --editable ./pwntools

.. _Ubuntu: https://launchpad.net/~pwntools/+archive/ubuntu/binutils
