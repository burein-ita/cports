pkgname = "kpimtextedit"
pkgver = "24.12.3"
pkgrel = 0
build_style = "cmake"
# hangs
make_check_args = ["-E", "richtextcomposertest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "ktextaddons-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE PIM textedit class"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/kdepim/kpimtextedit/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kpimtextedit-{pkgver}.tar.xz"
)
sha256 = "2f3239d612b7617815fa1748fadce28110814047db2bab7c6ec2b760b1eebc2e"


@subpackage("kpimtextedit-devel")
def _(self):
    return self.default_devel()
