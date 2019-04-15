import re

def get_position(file, atom_1, atom_2):
	with open(file, 'r') as f:
		data = f.read()
	positions = {}
	atoms = iter([atom_1, atom_2])
	for atom in atoms:
		s = atom + r'\d+\s+' + atom + r'\s+\-?\d+\.\d+\s+\-?\d+\.\d+\s+\-?\d+\.\d+'
		m = re.finditer(s, data)
		for match in m:
			position = re.split(r'\s+', match.group())
			positions[position[0]] = position[-3:]
	return positions