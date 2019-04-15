import time

start = time.time()

from bond_valence import BondValence

bv = BondValence('./data/bvparm2016.cif', './data/ZnBi6P2O15_mvc-16210_computed.cif', 'Zn', 'O')

V_As = bv.calc()
Coordinate = bv.position()
# print(V_As)
print("{:<10s}{:<20s}{:<10s}{:<10s}{:<10s}".format("atom", "valence charge", "x", "y", "z"))
for atom in V_As:
	print("{atom:<10s}{v:<20f}{x:<10s}{y:<10s}{z:<10s}".format(atom=atom, v=V_As[atom],
												 	x=Coordinate[atom][0],
												 	y=Coordinate[atom][1],
												 	z=Coordinate[atom][2])
												 	)

end = time.time()
print('Run time: {runtime}s'.format(runtime=end-start))

