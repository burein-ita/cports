pkgname = "ncmpcpp"
pkgver = "0.10.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "BOOST_LIB_SUFFIX= ",
    "--enable-clock",
    "--enable-outputs",
    "--with-taglib",
    "--with-lto",
]
hostmakedepends = [
    "pkgconf",
    "autoconf",
    "automake",
    "libtool",
]
makedepends = [
    "boost-devel",
    "icu-devel",
    "curl-devel",
    "libmpdclient-devel",
    "readline-devel",
    "taglib-devel",
]
pkgdesc = "Ncurses mpd client inspired by ncmpc"
license = "GPL-2.0-only"
url = "https://github.com/ncmpcpp/ncmpcpp"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ddc89da86595d272282ae8726cc7913867b9517eec6e765e66e6da860b58e2f9"
