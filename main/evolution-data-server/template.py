pkgname = "evolution-data-server"
pkgver = "3.50.0"
pkgrel = 0
build_style = "cmake"
# TODO: libgdata
configure_args = [
    "-DENABLE_GOOGLE=OFF",
    "-DWITH_LIBDB=OFF",
    "-DSYSCONF_INSTALL_DIR=/etc",
    "-DENABLE_INTROSPECTION=ON",
    "-DENABLE_VALA_BINDINGS=ON",
    "-DWITH_OPENLDAP=OFF",  # don't depend on shit software
]
make_check_target = "test"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "flex",
    "glib-devel",
    "gperf",
    "gobject-introspection",
    "gettext",
    "vala",
    "perl",
]
makedepends = [
    "glib-devel",
    "libcanberra-devel",
    "libical-devel",
    "heimdal-devel",
    "webkitgtk-devel",
    "webkitgtk4-devel",
    "libsecret-devel",
    "nss-devel",
    "nspr-devel",
    "gnome-online-accounts-devel",
    "sqlite-devel",
    "libgweather-devel",
    "libsoup-devel",
    "json-glib-devel",
    "vala-devel",
]
checkdepends = ["dbus"]
pkgdesc = "Centralized access to appointments and contacts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/evolution-data-server"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c9f793d99ba188ef8cf2891b8062d7e570e3cba22b8cfc46eb561c6cecc81d3a"
# internally passes some stuff that only goes to linker
tool_flags = {"CFLAGS": ["-Wno-unused-command-line-argument"]}
options = ["!cross"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)


@subpackage("evolution-data-server-devel")
def _devel(self):
    return self.default_devel()
