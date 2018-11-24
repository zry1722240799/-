#!/usr/bin/python
# -*- coding: utf-8 -*-
#final!!!
'''
说明：
xy()用于改写坐标格式
distance()用于取得坐标之间距离
perdis()用于计算目标距离概率
centre()用于计算远离市中心带来的衰减
count()用于计算总人数
假设人都去距离最近的地方
先假设人都从家出发
假设人都从出发原路回家
假设市-家：250 人/day
工-地：300 人/day
地-家：300 人/day
假设以0.5格，5格为标准
percent1 = -0.025(x-0.5)(x-5) + 0.01(x是目标间距离)
percent2 = 1 - 0.075 * x(x是到市中心距离)
总人数 = (percent1 + percent2) * people
'''
class city:
    length = 10
    cross = []
    through = []
    market = [[4,4],[5,6],250]
    factory = [[0,9],[9,0],300]
    house = [[3,3],[6,6],1000]
    underground = [[4,2],[3,5],[0,7],[7,0],[7,5],300]
    #坐标顺序与输出顺序对应
    for cro in range(0,length):
        through = []
        for thr in range(0,length): 
            through.append('o')
        cross.append(through)
    for al in market[0:-1]:
        n = 0 
        for num in al:
            if n == 0:
                p = num
            else:
                j = num
            n = n + 1
        cross[j][p] = 'M'
    for al in factory[0:-1]:
        n = 0
        for num in al:
            if n == 0:
                p = num
            else:
                j = num
            n = n + 1
        cross[j][p] = 'F'
    for al in house[0:-1]:
        n = 0
        for num in al:
            if n == 0:
                p = num
            else:
                j = num
            n = n + 1
        cross[j][p] = 'H'
    for al in underground[0:-1]:
        n = 0
        for num in al:
            if n == 0:
                p = num
            else:
                j = num
            n = n + 1
        cross[j][p] = 'U'

    def xy(self,x):
        a = []
        b = []
        for al in x[0:-1]:
            e = 0
            for num in al:
                if e == 0:
                    p = num
                else:
                    j = num
                e = e + 1
            a.append(p)
            b.append(j)
        return a,b
    def distance(self,x,y):
        #由x到y
        first = self.xy(x)
        second = self.xy(y)
        lf = len(first[0])
        ls = len(second[0])
        self.xy(y)
        dis = []
        dis1 = []
        dismin = []
        for nf in range(0,lf):
            dis1 = []

            fisx = first[0][nf]
            fisy = first[1][nf]
            for ns in range(0,ls):
                secx = second[0][ns]
                secy = second[1][ns]
                disnow = (fisx - secx)**2 + (fisy - secy) ** 2
                for com in range(0,20):
                    if nf == com:
                        dis1.append(disnow ** 0.5)
            dis.append(dis1)
        for o in dis:
            dismin.append(min(o))
        return dismin
    def perdis(self,a,b):
        mini = self.distance(a,b)
        #x,y已处理;a,b未处理 若用xy()则已处理
        #x = house
        fin = [(0.03 * (m - 0.5) * (5 - m) + 0.01) for m in mini]
        return fin
    def centre(self,a,b=[[4.5,4.5],'waste']):
        discen = self.distance(a,b)
        percent_centre = [-0.01 * disc for disc in discen]
        return percent_centre
    def day(self,n):
        per2 = 1
        if n <= 6:
            per2 = per2 * (0.1 + 1) ** n
        elif n > 6 and n <= 9:
            per2 = (-0.03 + 1) ** (n - 6) * per2 * (1.1) ** 5
        else:
            per2 = (-0.03 + 1) ** 3  * per2 * (1.1) ** 5
        return per2 
    def count(self,a,b):
        peob = b[-1]
        final = []
        per1 = self.perdis(a,b)
        per2 = self.centre(a)
        for pn in range(0,len(per1)):
            final.append((per2[pn] + per1[pn])*peob)

        return final





c = city()
text = file('cycle.txt','w') 
text.write('fin\n')
text.close()
text = file('cycle.txt','a')
for t in c.cross:
    print t
for d in range(1,11):
    l1 = c.count(c.house,c.underground)
    text.write('day' + str(d))
    for e in [q*c.day(d) for q in l1]:
        text.write(' , ' + str(int(e)))
    text.write('\n')
for d in range(1,11):
    l1 = c.count(c.house,c.market)
    text.write('day' + str(d))
    for e in [q*c.day(d) for q in l1]:
        text.write(' , ' + str(int(e)))
    text.write('\n')
for d in range(1,11):
    l1 = c.count(c.factory,c.underground)
    text.write('day' + str(d))
    for e in [q*c.day(d) for q in l1]:
        text.write(' , ' + str(int(e)))
    text.write('\n')

    
print 'house-undergroud:',c.count(c.house,c.underground)

h = c.xy(c.house)
for s in range(0,len(c.house)-1):
    c.cross[h[1][s]][h[0][s]] = str(int(c.count(c.house,c.underground)[s]))
h = c.xy(c.market)
for s in range(0,len(c.market)-1):
    c.cross[h[1][s]][h[0][s]] = str(int(c.count(c.house,c.market)[s]))
h = c.xy(c.factory)
for s in range(0,len(c.factory)-1):
    c.cross[h[0][s]][h[1][s]] = int(c.count(c.factory,c.underground)[s])

#print '                  ',[[4,2],[3,5]]
print 'house-market:',c.count(c.house,c.market)
#print '             ',c.market[0:-1]
print 'factory-underground:',c.count(c.factory,c.underground)
#print '                    ',[[0,7],[7,0]]
text.close()
for t in c.cross:
   print t
