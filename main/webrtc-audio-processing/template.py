pkgname = "webrtc-audio-processing"
pkgver = "1.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "cmake"]
makedepends = ["abseil-cpp-devel", "linux-headers"]
pkgdesc = "Packaging-friendly copy of WebRTC AudioProcessing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://freedesktop.org/software/pulseaudio/webrtc-audio-processing"
source = f"{url}/{pkgname}-{pkgver}.tar.gz"
sha256 = "441a30d2717b2eb4145c6eb96c2d5a270fe0b4bc71aebf76716750c47be1936f"
# unmarked api
hardening = ["!vis"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("webrtc-audio-processing-devel")
def _devel(self):
    return self.default_devel()
