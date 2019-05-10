from get_features import GetFeatures

import pandas as pd
import re

with open('name_list.txt','r') as f:
    data = f.read()

name_list = re.split('\\n', data)

df_features = pd.DataFrame()

for i in range(len(name_list)):
    if name_list[i]:
        file_txt = './cif_txt/' + name_list[i] +'.gh.txt'
        file_cif = './finish_bv/' + name_list[i]

        features = GetFeatures(file_txt, file_cif, number=6)

        feature_energy, feature_atoms = features.energy_b_atoms()
        if not feature_atoms:
            continue
        feature_atoms.append(feature_energy)
        feature_atoms = pd.DataFrame(feature_atoms).T
        df_features = df_features.append(feature_atoms, ignore_index=True)
    else:
        continue

df_features.to_csv('./train.csv', index=False)
