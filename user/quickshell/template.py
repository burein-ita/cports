pkgname = "quickshell"
pkgver = "0.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DDISTRIBUTOR='Chimera Linux user/quickshell'",
    "-DCMAKE_BUILD_TYPE=Release",
    "-DINSTALL_QML_PREFIX=lib/qt6/qml",
    "-DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES",
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
    "qt6-qtsvg-devel",
    "pipewire-devel",
    "jemalloc-devel",
    "libxcb-devel",
    "wayland",
    "wayland-devel",
    "libdrm-devel",
    "mesa-gbm-devel",
    "wayland-protocols",
    "cli11",
]
pkgdesc = "Flexbile QtQuick based desktop shell toolkit"
license = "LGPL-3.0-only"
#url = "https://github.com/quickshell-mirror/quickshell"
#source = f"{url}/archive/refs/heads/master.zip"
url = "https://github.com/burein-ita/quickshell"
source = f"{url}/archive/refs/heads/musl.zip"
sha256 = "e27cbc5eb5441a55323b94eb530c2c0d6d4f64da42afacc670dd420757d5563b"
