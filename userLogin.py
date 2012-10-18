#!/usr/bin/env python

database=[ ['tequila','111111'],['leth','222222'],['amy','333333'] ]
username=raw_input('username:')
password=raw_input('password:')
if [username,password] in database:print 'hello'+' '+username+'!'
else :print "sorry you are not granted the right!"
