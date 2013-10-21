#!/usr/bin/perl -w

# 
# Copyright 2010 Brian Uechi <buasst@gmail.com>
# 
# This file is part of mochad.
# 
# mochad is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
# 
# mochad is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with mochad.  If not, see <http://www.gnu.org/licenses/>.
# 

#use strict; 
use Socket; 

my $hostname = `/bin/uname -n`;
chomp($hostname);
my $server = '127.0.0.1';       # www server also is running mochad
my $port   = 1099;
my $hosttype = `/bin/uname -m`;

my $rootdir = '/usr/share/apache2/cgi-bin';              # Chumby or x86 Linux
my $chumbywww = 'x10.cgi';

require "$rootdir/netcat.pl";
require "$rootdir/getsensors.pl";
require "$rootdir/cgi-lib.pl";

sub paintform 
{
    print <<EndOfForm;
        <form action="$chumbywww" method="post">
            <P>
            <input type="submit"   name="UnitA1" value="On">
            <input type="submit"   name="UnitA1" value="Off">
            <label>A1 Module</label><br>

            <input type="submit"   name="UnitA2" value="On">
            <input type="submit"   name="UnitA2" value="Off">
            <label>A2 Module</label><br>

            </P>
        </form>
EndOfForm
    getsensors($server, 1099, $hostname);
}

my ($x10func, $housecode, $unitcode);
my ($varname, $varvalue);

print PrintHeader();
print '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">';
print HtmlTop("Lights");

if (!ReadParse()) {
    paintform();
}
else {
    $x10func = "";
    $housecode = "";
    $unitcode = "";
    foreach $varname (keys (%in)) {
        $varvalue = $in{$varname};
        if ($varname eq "Function") {
            $x10func = $varvalue;
        }
        elsif ($varname eq "House") {
            $housecode = $varvalue;
        }
        elsif ($varname =~ /^Unit/) {
            $x10func = $varvalue;
            $unitcode = $varname;
            $unitcode =~ s/^Unit//;
        }
        else {
            print "Unknown varname $varname<br>";
        }
    }
    if ($x10func ne "") {
        # Change blanks to underlines in function names
        $x10func =~ tr/ /_/;
        if ($x10func eq "Arm") {
            netcat($server, $port, "rfsec 0x11 arm\n");
        }
        elsif ($x10func eq "Disarm") {
            netcat($server, $port, "rfsec 0x11 disarm\n");
        }
        elsif ($x10func ne "Refresh") {
            if (length($unitcode) == 2) {
                netcat($server, $port, "pl $unitcode $x10func\n");
            }
            else {
                netcat($server, $port, "pl $housecode$unitcode $x10func\n");
            }
        }
    }
    paintform();
}

print HtmlBot();
exit;
