#!/bin/python3

pn = .7
pc = 1

npn = 1 - pn
npc = 1 - pc


pl =( .8 * npn * npc 
	+ .6 * npn * pc 
	+ .5 * pn  * npc 
	+ .2 * pn  * pc)	
npl = 1-pl

print("    pl:")
print(pl)



pb = (.9 * pl
	+ .2 * npl)
npb = 1-pb

print("    pb:")
print(pb)



pm = (.6 * pl
	+ .3 * npl)
npm = 1-pm

print("    pm:")
print(pm)



ps = (.8 * pm
	+ .1 * npm)
nps = 1-ps

print("    ps:")
print(ps)


