pkgname = "cli11"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=None",
    "-DCLI11_BUILD_TESTS=OFF",
    "-DCLI11_BUILD_EXAMPLES=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "catch2-devel",
]
pkgdesc = "Command line parser for C++11"
license = "BSD-3-Clause"
url = "https://github.com/CLIUtils/CLI11"
source = f"{url}/archive/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "17e02b4cddc2fa348e5dbdbb582c59a3486fa2b2433e70a0c3bacb871334fd55"


def post_install(self):
    self.install_license("LICENSE")
