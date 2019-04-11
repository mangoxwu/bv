# BV法实现

## 使用

在此程序包根目录打开命令行，输入

```powershell
$ python run.py
```

运行得到结果

```shell
The valence charge of atom Ca3 is: 0.918354777537.
The valence charge of atom Ca2 is: 0.918354777537.
The valence charge of atom Ca1 is: 0.918354777537.
The valence charge of atom Ca4 is: 0.918354777537.
Run time: 0.00187587738037.
```

## 更改数据

在*data*文件夹中存放数据文件后，将*run.py*中的

```python
bv = BondValence('./data/bvparm2016.cif', './data/CaO2.cif', 'Ca', 'O')
```

更改为新的文件名与要计算的元素名称（除非加上变量名，否则不能改变参数顺序）

```python
bv = BondValence('./data/new_parm.cif', './data/new_molecule.cif', 'atom_1', 'atom_2')
```

