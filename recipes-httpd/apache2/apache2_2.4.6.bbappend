do_install_append() {
# make it depend of  'mochad-cgi' installation
sed -i 's@^#LoadModule cgid_module lib/apache2/modules/mod_cgid.so@LoadModule cgid_module lib/apache2/modules/mod_cgid.so@' ${D}/${sysconfdir}/${BPN}/httpd.conf
sed -i 's@Options Indexes FollowSymLinks@Options Indexes FollowSymLinks ExecCGI@' ${D}/${sysconfdir}/${BPN}/httpd.conf

}
