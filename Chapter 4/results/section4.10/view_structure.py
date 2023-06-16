from ase.io import read
from ase.visualize import view


file = read(filename='CuH/CONTCAR')


view(file)
