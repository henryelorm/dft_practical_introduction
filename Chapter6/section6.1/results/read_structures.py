from ase.io.vasp import read_vasp
from ase.visualize import view

file = read_vasp(file='hollow/CONTCAR')


view(file)