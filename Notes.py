a= input('What do u want to do first(read last minutes(lm) or take new(nm)):\n')
def lm():
    d= input('What was the date')
    do= open(f'C:/Users/Isaac/Documents/Programing/Python/{d}meeting.txt','r')
    r= do.read()
    r=[r]
    print(r)
    do.close()
def obj():
    i= input('What do you want to add:')
    a= open('C:/Users/Isaac/Documents/Programing/Python/10.13.22meeting.txt','a')
    w= a.write(i)
    a.close()
    lm()
def nm():
    d= input('What is the date:')
    c= open(f'C:/Users/Isaac/Documents/Programing/Python/{d}meeting.txt','w')
    i= input('What do you want to add:')
    c.write(i)
    c.close()
if a.lower() == 'lm':
    lm()
    o= input('Was there an objection?(y or n):')
    if o.lower() == 'y':
        obj()
    elif o.lower() == 'n':
        print("")
    else:
        print('CODE RED!!!!')
    nm()
else:
    print('Big mistake')