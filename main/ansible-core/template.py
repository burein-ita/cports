pkgname = "ansible-core"
pkgver = "2.18.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-cryptography",
    "python-jinja2",
    "python-packaging",
    "python-passlib",
    "python-pyyaml",
    "python-resolvelib",
]
checkdepends = [
    "git",
    "openssh",
    "python-bcrypt",
    "python-pytest",
    "python-pytest-mock",
    "python-pytest-xdist",
    "util-linux-mount",
    *depends,
]
pkgdesc = "Configuration management and multinode orchestration framework"
subdesc = "core components"
license = "GPL-3.0-or-later"
url = "https://ansible.com"
# pypi does not ship some files
source = (
    f"https://github.com/ansible/ansible/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "90820d73f124fe8b842e2471b09da2e389931217157b02e2d96dc0b1f0ff782a"


def check(self):
    self.do(
        "./bin/ansible-test",
        "units",
    )
