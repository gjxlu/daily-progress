def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

def lookup(data, label, name):
    return data[label].get(name)

def store(data, full_name):
    names=full_name.split()
    labels=['first', 'middle', 'last']
    if len(names)==2:
        names.insert(1, '')
    for label, name in zip(labels, names):
        people= lookup(data, label, name)
        if people: people.append(full_name)
        else: data[label][name]=[full_name]

mynames={}
init(mynames)
while True:
    opt=raw_input('to save(s) or to loopup(c)? (press # to stop!):')
    if opt=='s':
        Name=raw_input('input the name:')
        cname=Name.split()
        if len(cname)<2:
            print "wrong! please enter again!"
            continue
        store(mynames, Name)
        print "ok!"
    elif opt=='c':
        Order=raw_input('Order (first/middle/last):')
        Name=raw_input('name:')
        if Order!='first' or Order!='midlle' or Order!='last':
            print "wrong order!"
            continue
        print lookup(mynames, Order, Name)
    elif opt=='#':
        break
    else:
        print "wrong!"
        continue


