from ase.io import read
from ase.visualize import view


file = read(filename='CONTCAR_cuh')


view(file)