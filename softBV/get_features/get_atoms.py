import heapq
import re

periodic_table = ('H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                  'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 
                  'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Te', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 
                  'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 
                  'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 
                  'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm','Md', 'No', 'Lr',
                  'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Uue')


def get_atoms(file, position, distance, number):
    with open(file,'r') as f:
        data = f.read()
    s_a = r'\_cell\_length\_a\s+(\d+\.\d+)'
    s_b = r'\_cell\_length\_b\s+(\d+\.\d+)'
    s_c = r'\_cell\_length\_c\s+(\d+\.\d+)'
    length_a = float(re.findall(s_a, data)[0])
    length_b = float(re.findall(s_b, data)[0])
    length_c = float(re.findall(s_c, data)[0])
    
    s_atoms = r'(\w+)\s+\w+\s+\d+\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+\.\d+)'
    m = re.findall(s_atoms, data)
    atoms = [list(t) for t in m]
    atoms_position = [atom[-3:] for atom in atoms]
    for i in range(len(atoms_position)):
        atoms_position[i] = [float(label) for label in atoms_position[i]]
        atoms_position[i][0]=atoms_position[i][0]*length_a
        atoms_position[i][1]=atoms_position[i][1]*length_b
        atoms_position[i][2]=atoms_position[i][2]*length_c
    distances = [calc_disc(position, atoms_position[i]) for i in range(len(atoms_position))]
    min_num_index_list = list(map(distances.index, heapq.nsmallest(number, distances)))

    list_atoms = []
    try:
        for i in range(number):
            list_atoms.append(get_atom_index(atoms[min_num_index_list[i]][0]))
            list_atoms.append(distances[min_num_index_list[i]])
    except:
        return []
    return list_atoms

def calc_disc(position_1, position_2):
    sq_sum = 0
    for i in range(len(position_1)):
        sq_sum += (position_1[i] - position_2[i])**2
    return sq_sum**0.5

def get_atom_index(atom):
    return periodic_table.index(atom)+1