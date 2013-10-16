SUMMARY = "X10 Deamon manager"
HOMEPAGE = "freefr.dl.sourceforge.net"
LICENSE = "GPLv3"
LIC_FILES_CHKSUM = "file://COPYING;md5=d32239bcb673463ab874e80d47fae504"
DEPENDS = " libusb1 "
RDEPENDS_${PN} = " libusb1 "
RDEPENDS_${PN}-cgi = " ${PN} apache2 perl perl-module-socket"

SRC_URI = "http://freefr.dl.sourceforge.net/mochad/mochad-${PV}.tar.gz \
		   file://FixInstallUdevRules.patch \
		   file://FixInitScript.patch \
		   file://FixUdevRules.patch \
		  "
inherit autotools update-rc.d
SRC_URI[md5sum] = "6073a6e0d865587defacc4ea00b6c298"
SRC_URI[sha256sum] = "6e7e5b953ae1350e246fd50b87a1b1a0ea628a4a66f641117a1d2521e0a309ec"


PACKAGES += "${PN}-cgi"
INITSCRIPT_NAME = "mochad"

autotools_do_install_prepend() {
mkdir -p ${D}/${sysconfdir}/init.d
mkdir -p ${D}/${sysconfdir}/udev/rules.d
mkdir -p ${D}/${sysconfdir}/hotplug.d/usb 
mkdir -p ${D}/${datadir}/apache2/cgi-bin

}


autotools_do_install_append() {
# Copy cgi script into cgi-bin directory of apache2. In Yocto it is {datadir}/apache2/cgi-bin/
cp cgi/* ${D}/${datadir}/apache2/cgi-bin/
chmod +x ${D}/${datadir}/apache2/cgi-bin/x10.pl
}

FILES_${PN} +=  "${sysconfdir}/init.d/mochad"
FILES_${PN} +=  "${sysconfdir}/udev/rules.d/91-usb-x10-controllers.rules"
FILES_${PN} +=  "${sysconfdir}/hotplug.d/usb/20-usb-x10"
FILES_${PN} +=  "${bindir}/mochad"

FILES_${PN}-cgi +=  "${datadir}/apache2/cgi-bin/*"
