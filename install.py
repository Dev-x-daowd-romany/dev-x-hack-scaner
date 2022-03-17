#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

#---------------------------------------------------------------------------#
# This file is part of dev-x-hack-scaner.                                     #
# dev-x-hack-scaner is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# dev-x-hack-scaner is distributed in the hope that it will be useful         #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with dev-x-hack-scaner.  If not, see                                  #
#                                                                           #
#---------------------------------------------------------------------------#
#                                                                           #
#        Copyright © 2022 DAOWD ROAMNY (www.devx.shop)                         #
#                                                                           #
#---------------------------------------------------------------------------#

if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] dev-x-hack-scaner installer must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")

print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                     dev-x-hack-scaner Installer              █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")

def main():

	print("\033[1;34m\n[++] Please choose your operating system.\033[1;m")

	print("""
1) Ubuntu / Kali linux / Others
2) Parrot OS
""")
	system0 = raw_input(">>> ")
	if system0 == "1":
		print("\033[1;34m\n[++] Installing dev-x-hack-scaner ... \033[1;m")
		install = os.system("apt-get update && apt-get install -y nmap hping3 build-essential python-pip ruby-dev git libpcap-dev libgmp3-dev && pip install tabulate terminaltables")

		install1 = os.system("""cd tools/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/dev-x-hack-scaner && cp -R tools/ /opt/dev-x-hack-scaner/ && cp dev-x-hack-scaner.py /opt/dev-x-hack-scaner/dev-x-hack-scaner.py && cp banner.py /opt/dev-x-hack-scaner/banner.py && cp run.sh /usr/bin/dev-x-hack-scaner && chmod +x /usr/bin/dev-x-hack-scaner && tput setaf 34; echo "dev-x-hack-scaner has been sucessfuly instaled. Execute 'sudo python3 dev-x-hack-scaner.py' in your terminal." """)	
	elif system0 == "2":
		print("\033[1;34m\n[++] Installing dev-x-hack-scaner ... \033[1;m")

		bet_un = os.system("apt-get remove bettercap") # Remove bettercap to avoid some problems . Installed by default with apt-get .
		bet_re_ins = os.system("gem install bettercap") # Reinstall bettercap with gem.

		install = os.system("apt-get update && apt-get install -y nmap hping3 ruby-dev git libpcap-dev libgmp3-dev python-tabulate python-terminaltables")

		install1 = os.system("""cd tools/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/dev-x-hack-scaner && cp -R tools/ /opt/dev-x-hack-scaner/ && cp dev-x-hack-scaner.py /opt/dev-x-hack-scaner/dev-x-hack-scaner.py && cp banner.py /opt/dev-x-hack-scaner/banner.py && cp run.sh /usr/bin/dev-x-hack-scaner && chmod +x /usr/bin/dev-x-hack-scaner && tput setaf 34; echo "dev-x-hack-scaner has been sucessfuly instaled. Execute 'sudo python3 dev-x-hack-scaner.py' in your terminal." """)
		

	else:
		print("Please select the option 1 or 2")
		main()
main()
