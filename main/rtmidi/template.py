pkgname = "rtmidi"
pkgver = "6.0.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["pipewire-jack-devel", "alsa-lib-devel"]
pkgdesc = "Common API for realtime MIDI input/output"
license = "MIT"
url = "https://github.com/thestk/rtmidi"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ef7bcda27fee6936b651c29ebe9544c74959d0b1583b716ce80a1c6fea7617f0"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("rtmidi-devel")
def _(self):
    return self.default_devel()
