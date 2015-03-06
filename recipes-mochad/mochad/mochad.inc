SUMMARY = "X10 Deamon manager"
HOMEPAGE = "freefr.dl.sourceforge.net"
DEPENDS = " libusb1 "
RDEPENDS_${PN} = " libusb1 "
RDEPENDS_${PN}-cgi = " ${PN} apache2 perl perl-module-socket"

SRC_URI = "http://freefr.dl.sourceforge.net/mochad/mochad-${PV}.tar.gz \
		   file://FixInstallUdevRules.patch \
		   file://FixInitScript.patch \
		   file://FixUdevRules.patch \
		  "
SRC_URI += "file://x10.cgi"
inherit autotools update-rc.d


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
cp ${S}/cgi/* ${D}/${datadir}/apache2/cgi-bin/
# Delete native x10.pl script 
rm ${D}/${datadir}/apache2/cgi-bin/x10.pl
cp ${WORKDIR}/x10.cgi ${D}/${datadir}/apache2/cgi-bin/
chmod +x ${D}/${datadir}/apache2/cgi-bin/x10.cgi
}

FILES_${PN} +=  "${sysconfdir}/init.d/mochad"
FILES_${PN} +=  "${sysconfdir}/udev/rules.d/91-usb-x10-controllers.rules"
FILES_${PN} +=  "${sysconfdir}/hotplug.d/usb/20-usb-x10"
FILES_${PN} +=  "${bindir}/mochad"

FILES_${PN}-cgi +=  "${datadir}/apache2/cgi-bin/*"
