#! /usr/bin/python

from __future__ import division

import pexpect

def function(db, length):
	for num in range(length):
		#turn length (e.g. 3) into a a range 00, 01, 02, 03
		#this will match the format of the ncbi database files
		if num < 10:
			num = "0{}".format(num)
		else: 
			num = num
		#initialize pexpect to bash
		kid = pexpect.spawn("ftp ftp.ncbi.nlm.nih.gov") #open the ftp server
		#log in
		kid.expect('Name .*:')
		kid.sendline('anonymous')
		kid.expect('Password:')
		kid.sendline('jnotar@ucla.edu')
		#run a couple of steps as specified in the ncbi tutorial
		kid.expect("ftp>")
		kid.sendline("cd blast/db")
		kid.expect("ftp>")
		kid.sendline("bin")
		kid.expect("ftp>")
		#ask to download the appropriate zipped database
		kid.sendline("get {}.{}.tar.gz".format(db, num))
		kid.expect("ftp> ", timeout=None) 
		#timeout = none asks .expect() to wait until the process is done running
		#close ftp
		kid.sendline("bye") 
		#kill process
		kid.kill(0)
		#unzip the file
		pexpect.run("tar zxvpf {}.{}.tar.gz".format(db, num))

#run the function for nucleotide database (nt), 00-25
function("nt", 26)

#Let me know that the script is done running
print "Done!"

