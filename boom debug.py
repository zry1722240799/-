#!/usr/bin/python
from random import randint
fi = 6
tro = ['1']
all = ['1']
for aaa in range(0,fi):
    tro = ['1']
    for aa in range(0,fi):
        tro.append('?')
    tro.append('1')
    all.append(tro)
all.append('1') 
#print all
#all[y][x],no need -1
boom = []
zero = []
done = []
coun = 0
while coun <= 6: 
    wq = [randint(1,fi),randint(1,fi)]
    if wq in boom:
        pass
    else:
        boom.append(wq)
        coun = coun + 1
#print 'boom' +  str(boom)
for ins in boom:
    all[ins[1]][ins[0]] = 'x'
def scan(x):
    num = 0
    for i in range(-1,2):
        for j in range(-1,2):
            jp = [x[0]+i,x[1]+j]
            if jp != x:
                if jp in boom:
                    num = num + 1
    return num
for c in range(1,fi+1):
    for t in range(1,fi+1):
        bm = scan([c,t])
        if [c,t] not in boom:
            all[t][c] = str(bm)
            if bm == 0:
                zero.append([c,t]) 
#print 'zero' + str(zero)   
for ins in zero:
    all[ins[1]][ins[0]] = 'z'
def white(x):
    key = 0
    while key == 0:
        key = 1
        argu = x
        args = [argu]
        for arg in args:
            #print done
            #print arg
            for i in range(-1,2):
                for j in range(-1,2):
                    jp = [arg[0]+i,arg[1]+j]
                    #print jp
                    if jp in done:
                        pass
                    else:
                        if jp in zero:
                            all[arg[1]][arg[0]] = '0'
                            args.append(jp) 
                            key = 0
                            done.append(jp)
    return
#white([2,2])
def show(x):         #x = done
    for arg in x:
        for po in range(-1,2):
            for pk in range(-1,2):
                n = [arg[1]+po,arg[0]+pk]
                if all[n[1]] != '1' and n not in boom:
                    all[n[1]][n[0]] = str(scan(n)) 
    return
#show(done)
#for i in all[1:-1]:
    #print i[1:-1]
#basic function
#console 
for ins in done:
    all[done[1]][done[0]] = 'd'
flag = 0
while flag == 0:
    mi = 0
    for ttt in range(1,fi):
        for ccc in range(1,fi):
            if [ccc,ttt] not in boom and all[ccc][ttt] != '?':
                pass
            else:
                mi = 1
    if mi == 0:
        print 'you win'
        break
    for i in all[1:-1]:
        print i[1:-1]
    mood = raw_input('please slect mood\no for open\nb for boom\nq for quit\n')
    if mood == 'o':
        xx = input('input x\n')
        yy = input('input y\n')
        xy = [xx,yy]
        if xy in boom:
            print 'you loose'
            break
        if xx < 1 or xx > fi or yy < 1 or yy > fi:
            print 'examine your x,y'
        else:
            all[yy][xx] = str(scan(xy))
            white(xy)
            show(done)
    elif mood == 'b':
        xx = input('input x\n')
        yy = input('input y\n')
        all[yy][xx] = '*' 
    elif mood == 'q':
        break
    else:
        print 'examine your input'
