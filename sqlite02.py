#!/usr/bin/env python
import sqlite3 as sql;
conn=sql.connect('database1.db');
curs=conn.cursor();
curs.execute('''
     create table IF NOT EXISTS tb1 (
        id int primary key,
        name text,
        kg float
        )
        ''');
while True:
	choice=raw_input("continue to add imf? press '#'to end it!");
	if choice=='#':	break;
	else:
		imf=raw_input("please enter id-name-kg:");
		query='insert into tb1 values(?,?,?)';

		fields=imf.split('-');
		curs.execute(query,fields);
        
conn.commit();
conn.close();
print "data saved!";    
