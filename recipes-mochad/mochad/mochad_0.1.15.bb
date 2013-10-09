SUMMARY = "X10 Deamon manager"
HOMEPAGE = "freefr.dl.sourceforge.net"
LICENSE = "GPLv3"
LIC_FILES_CHKSUM = "file://COPYING;md5=d32239bcb673463ab874e80d47fae504"
DEPENDS = " libusb1 "
SRC_URI = "http://freefr.dl.sourceforge.net/mochad/mochad-${PV}.tar.gz \
		   file://FixInstallUdevRules.patch \
		  "
inherit autotools
SRC_URI[md5sum] = "e1de0c9e62e10236542e70c2f33aacc2"
SRC_URI[sha256sum] = "a329ddcd7e95c169e7e37f9d37bb1146da6617be2f7325e7b6ffd0314962036f"

autotools_do_install_prepend() {
mkdir -p ${D}/etc/udev/rules.d
mkdir -p ${D}/etc/hotplug.d/usb 

}

