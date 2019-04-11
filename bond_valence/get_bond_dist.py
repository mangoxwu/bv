import re

def get_bond_dist(file, atom_1, atom_2):
	with open(file, 'r') as f:
		data = f.read()
	s = atom_1 + r'\d+\s+' + atom_2 + r'(\d+\s+\d+\.*[0-9]*)'
	m = re.finditer(s, data)
	bond_dist = []
	for match in m:
		now_dist = re.split(r'\s+', match.group())
		now_dist[-1] = float(now_dist[-1])
		yield now_dist