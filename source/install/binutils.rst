二进制工具
-------------

对国外的系统架构的汇编（比如在Mac OS X上汇编Sparc shellcode），我们需要安装交叉编译版本的binutils，我们尽可能使得这个安装过程流畅一点。

在下列的例子中，使用你的系统架构代替$ARCH(例如arm, mips64, vax等等)。

在一个现代化的8核计算机上编译binutils大约花费60秒。

Ubuntu
^^^^^^^^^^^^^^^^

对于Ubuntu 12.04到15.10的发行版，你需要添加pwntools的 `个人包存档库 <http://binutils.pwntools.com>`__。

Ubuntu Xenial (16.04) 已经拥有官方的包，不需要做下面的步骤。

.. code-block:: bash

    $ apt-get install software-properties-common
    $ apt-add-repository ppa:pwntools/binutils
    $ apt-get update

接着，针对于你的系统架构安装binutils。

.. code-block:: bash

    $ apt-get install binutils-$ARCH-linux-gnu

Mac OS X
^^^^^^^^^^^^^^^^

在Mac OS X上安装binutils非常简单，但是需要源码编译安装。然而，既然我们已经有了homebrew，我们就可以使用一条命令来解决。安装 `brew <http://brew.sh>`__  之后, 我们只需要从binutils中获取我们的二进制工具：  `binutils
repo <https://github.com/Gallopsled/pwntools-binutils/>`__.

.. code-block:: bash

    $ brew install https://raw.githubusercontent.com/Gallopsled/pwntools-binutils/master/osx/binutils-$ARCH.rb

其他系统
^^^^^^^^^^^^^^^^

如果你想通过自己的手动编译安装，并且不是上面两个系统之一，编译binutils也非常简单，运行下面的脚本即可。

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
