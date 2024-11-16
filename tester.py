import GEO as utils # type: ignore

a,b = 3,4
c = utils.pythagoras(a,b)
print('c=',c)

r=10
area=utils.circle(r)
print('area=', area)