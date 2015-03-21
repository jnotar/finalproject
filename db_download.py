#! /usr/bin/python

from __future__ import division

import pexpect

def function(db, length):
	for num in range(int(length)):
		#initialize pexpect to bash
		kid = pexpect.spawn("ftp ftp.ncbi.nlm.nih.gov")
		kid.expect('Name .*:')
		kid.sendline('anonymous')
		kid.expect('Password:')
		kid.sendline('jnotar@ucla.edu')
		kid.expect("ftp> ")
		kid.sendline("cd blast/db")
		kid.expect("ftp> ")
		kid.sendline("bin")
		kid.expect("ftp> ")
		kid.sendline("get {}.{}.tar.gz".format(str(db), str(num))
		kid.expect("ftp> ")
		kid.sendline("bye")
		#kid.sendline("quit")
		#tar xf db.num.tar.gz
		#rm db.num.tar.gz

function("nt", 3)

print "Done!"