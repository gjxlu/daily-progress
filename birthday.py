year= raw_input('yeah of birth:')
month= raw_input('month of birth:')
day= raw_input('day of birth:')
monthEnd=[ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', \
           'Oct', 'Nov', 'Dec' ]
dayEnd=[ 'st', 'nd', 'rd']+['th']*17+['st', 'nd', 'rd']+['th']*7+['st']
MNum=int(month)
DNum=int(day)
Month=monthEnd[MNum-1]
Day=dayEnd[DNum-1]
print Month+','+day+Day+','+year
