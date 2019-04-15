from bond_valence.calc_v import calc_v
from bond_valence.get_bond_dist import get_bond_dist
from bond_valence.get_parm import get_parm
from bond_valence.get_position import get_position

class BondValence(object):
	def __init__(self, file_parm, file_model, atom_1, atom_2):
		super(BondValence, self).__init__()
		self.file_1 = file_parm
		self.file_2 = file_model
		self.atom_1 = atom_1
		self.atom_2 = atom_2

	def calc(self):
		R_0, B = get_parm(self.file_1, self.atom_1, self.atom_2)
		# print('R_0: %f, B: %f' % (R_0, B))
		bond_dists = get_bond_dist(self.file_2, self.atom_1, self.atom_2)
		V_As = calc_v(bond_dists=bond_dists, R_0=R_0, B=B)
		return V_As

	def position(self):
		coordinates = get_position(self.file_2, self.atom_1, self.atom_2)
		return coordinates