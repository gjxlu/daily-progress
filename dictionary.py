import string
people ={
    'alice':{
        'phone': '111111',
        'adr':'yy10#103'
        },
    'bob':{
        'phone':'222222',
        'adr':'yy11#218'
        },
    'teki':{
        'phone':'333333',
        'adr':'yy10423'
        }
    }

label ={
    'p':'phone number',
    'a':'address'
    }

name=raw_input('who do you want to check?')
if name.lower()in people: 
    request= raw_input('phone number(p)or address(a)?')
    if request=='p': key='phone'
    if request=='a': key='adr'
    else: print" wrong!"
    print "hello,%s's %s is %s"%\
                     (name, label[request],people[name.lower()][key])
                    
else: print"sorry,there is no %s"% name
