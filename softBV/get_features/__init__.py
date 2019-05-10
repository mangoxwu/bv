from get_features.get_energy_b import get_energy_b
from get_features.get_atoms import get_atoms

class GetFeatures(object):
	def __init__(self, file_txt, file_cif, distance=1, number=3):
		super(GetFeatures, self).__init__()
		self.file_txt = file_txt
		self.file_cif = file_cif
		self.distance = distance
		self.number = number

	def energy_b_atoms(self):
		energy, position = get_energy_b(self.file_txt)
		atoms = get_atoms(self.file_cif, position, self.distance, self.number)
		return energy, atoms