import re

def get_energy_b(file):
    with open(file, 'r') as f:
        data = f.read()
    s = r'\d+\.\d+\,\s+(\-?\d+\.\d+)\,\s+([a-zA-Z0-9\_]+)\,\s+[0-9]D\,\s+(\-?\d+\.\d+)\,\s+(\-?\d+\.\d+)\,\s+(\-?\d+\.\d+)'
    m = re.findall(s, data)
    states = [list(t) for t in m]
    atoms_states = [state for state in states if state[1]!='none' and state[1]!='saddle']
    saddle_states = [state for state in states if state[1]=='saddle']
    if len(atoms_states)==len(saddle_states):
        energy_bs = [float(saddle_states[i][0])-float(atoms_states[i][0]) for i in range(len(atoms_states))]
    else:
        print("原子和鞍点的数目不同")
    max_energy_b = max(energy_bs)
    index = energy_bs.index(max_energy_b)
    saddle_position = saddle_states[index][-3:]
    saddle_position = [float(label) for label in saddle_position]
    
    return max_energy_b, saddle_position