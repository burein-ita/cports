pkgname = "quickshell"
pkgver = "git"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DDISTRIBUTOR='Chimera Linux user/quickshell'",
    "-DCMAKE_BUILD_TYPE=Release",
    "-DINSTALL_QML_PREFIX=lib/qt6/qml",
    "-DDISTRIBUTOR_DEBUGINFO_AVAILABLE=NO",
    "-DNO_PCH=ON",
    "-DCRASH_REPORTER=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "spirv-tools-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtshadertools-devel",
    "qt6-qtwayland-devel",
    "pipewire-devel",
    "jemalloc-devel",
    "libxcb-devel",
    "wayland-devel",
    "libdrm-devel",
    "mesa-gbm-devel",
    "wayland-protocols",
    "linux-pam-devel",
    "cli11",
]
depends = ["qt6-qtsvg", "qt6-qtmultimedia",]
pkgdesc = "Flexbile QtQuick based desktop shell toolkit"
license = "LGPL-3.0-only"
url = "https://github.com/quickshell-mirror/quickshell"
source = f"{url}/archive/refs/heads/master.zip"
sha256 = "bae0cb090c2b1d72fa94aadb4c55b012e639cebc0b46f6a3edc8adc5524b7f75"
