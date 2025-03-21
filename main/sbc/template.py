pkgname = "sbc"
pkgver = "2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-pie"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["libsndfile-devel", "linux-headers"]
pkgdesc = "Bluetooth Subband Codec (SBC) library"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "http://www.bluez.org"
source = f"$(KERNEL_SITE)/bluetooth/sbc-{pkgver}.tar.xz"
sha256 = "8f12368e1dbbf55e14536520473cfb338c84b392939cc9b64298360fd4a07992"


@subpackage("sbc-devel")
def _(self):
    return self.default_devel()
