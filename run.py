import time

start = time.time()

from bond_valence import BondValence

bv = BondValence('./data/bvparm2016.cif', './data/CaO2.cif', 'Ca', 'O')

V_As = bv.calc()
# print(V_As)
for atom in V_As:
	print("The valence charge of atom {atom} is: {v}.".format(atom=atom, v=V_As[atom]))

end = time.time()
print('Run time: {runtime}.'.format(runtime=end-start))

