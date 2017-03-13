安装
============

pwntools在ubuntu 12.04和 14.04系统上支持的最好，但在功能上讲也可以在Posix系的系统上工作（Debian, Arch, FreeBSD, OSX, 等等）。

先决条件
-------------

为了能使`pwntools`发挥的更棒，你应该安装下列的系统库。

.. toctree::
   :maxdepth: 3
   :glob:

   install/*

最新发行版
-----------------

现在pwntools是一个``pip``包。

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
