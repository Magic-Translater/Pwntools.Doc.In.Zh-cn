二进制工具
-------------

对外来架构的汇编（比如在Mac OS X上汇编Sparc shellcode），需要各种跨版本的二进制工具的安装，我们已尽可能使安装过程流畅。

在下列的例子中，将你自己的目标架构代替$ARCH(例如arm, mips64, vax等等)。

编译二进制工具在现代8核计算机上大约花费60秒。

Ubuntu
^^^^^^^^^^^^^^^^

对于从Ubuntu 12.04到15.10的发行版，你首先需要添加pwntools的`个人包存档库 <http://binutils.pwntools.com>`__。

对于 Ubuntu Xenial (16.04) 已经拥有官方的包，不需要做下面的步骤。

.. code-block:: bash

    $ apt-get install software-properties-common
    $ apt-add-repository ppa:pwntools/binutils
    $ apt-get update

接着，安装符合自己计算机架构的二进制工具。

.. code-block:: bash

    $ apt-get install binutils-$ARCH-linux-gnu

Mac OS X
^^^^^^^^^^^^^^^^

Mac OS X的安装非常简单，但是需要源码编译安装，然而，我们已经有了homebrew，一条命令就可以解决。安装`brew <http://brew.sh>`__ 之后, 从这个链接获取我们的二进制工具： `binutils
repo <https://github.com/Gallopsled/pwntools-binutils/>`__.

.. code-block:: bash

    $ brew install https://raw.githubusercontent.com/Gallopsled/pwntools-binutils/master/osx/binutils-$ARCH.rb

其他系统
^^^^^^^^^^^^^^^^

如果你想通过自己的手动编译安装，并且不是上面两个系统之一，编译二进制工具也非常简单，运行下面的脚本即可。

.. code-block:: bash

    #!/usr/bin/env bash

    V=2.25   # Binutils Version
    ARCH=arm # Target architecture

    cd /tmp
    wget -nc https://ftp.gnu.org/gnu/binutils/binutils-$V.tar.gz
    wget -nc https://ftp.gnu.org/gnu/binutils/binutils-$V.tar.gz.sig

    gpg --keyserver keys.gnupg.net --recv-keys 4AE55E93
    gpg --verify binutils-$V.tar.gz.sig

    tar xf binutils-$V.tar.gz

    mkdir binutils-build
    cd binutils-build

    export AR=ar
    export AS=as

    ../binutils-$V/configure \
        --prefix=/usr/local \
        --target=$ARCH-unknown-linux-gnu \
        --disable-static \
        --disable-multilib \
        --disable-werror \
        --disable-nls

    MAKE=gmake
    hash gmake || MAKE=make

    $MAKE -j clean all
    sudo $MAKE install
