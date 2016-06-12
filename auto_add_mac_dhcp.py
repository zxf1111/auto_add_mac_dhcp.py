#!/usr/bin/env python

import os,sys,fileinput

if not os.path.exists('/dhcp'):
        os.system("svn co --depth=empty  svn+ssh://root@xxx.xxxx.com/sw/systems/subversion/puppet/files/CentOS_7_x86_64/etc/dhcp/city /dhcp")

os.chdir("/dhcp")
os.system("svn up xxx.conf")
os.system("tail xxx.conf")

dp = raw_input('type in department: ')
mac = raw_input('type in mac_address: ')
ip = raw_input('type in ip_address last number: ')


for line in fileinput.input('xxx.conf', inplace=1):
        print line,
        if line.startswith('#auto_add'):
                print'          host %s { hardware ethernet %s;fixed-address 10.17.6.%s ;}' %(dp,mac,ip)

os.system('svn commit -m "add %s" ' %dp )
