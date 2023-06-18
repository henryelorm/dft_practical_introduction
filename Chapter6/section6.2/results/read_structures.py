from ase.io.vasp import read_vasp
from ase.visualize import view

file = read_vasp(file='bridge/CONTCAR')


view(file)