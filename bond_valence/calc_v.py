import math

def calc_v(bond_dists, R_0, B):
	old_atom_1 = ''
	V_As = {}
	V_A = 0
	for bond_dist in bond_dists:
		if bond_dist[0] != old_atom_1: # new atom
			if V_A != 0: # save old atom data
				V_As[old_atom_1] = V_A
			S_A_X = calc_s(R_0=R_0, B=B, R=bond_dist[-1])
			V_A = S_A_X
		else : # old atom
			if bond_dist[1] != old_atom_2: # second atom not same
				S_A_X = calc_s(R_0=R_0, B=B, R=bond_dist[-1])
				V_A += S_A_X
		old_atom_1 = bond_dist[0]
		old_atom_2 = bond_dist[1]
	V_As[old_atom_1] = V_A
	return V_As

def calc_s(R_0, R, B):
	return math.exp((R_0-R)/B)