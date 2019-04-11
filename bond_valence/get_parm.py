import re

def get_parm(file, atom_1, atom_2):
	with open(file, 'r') as f:
		data = f.read()
	s = atom_1 + r'\s+\d\s+' + atom_2 + r'\s+\-\d\s+(\d+\.\d+)\s+(\d+\.\d+)'
	m = re.search(s, data)
	R_0 = float(m.group(1))
	B = float(m.group(2))
	return R_0, B