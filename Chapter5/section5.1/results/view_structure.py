from ase.io import read
from ase.visualize import view


file = read(filename='CONTCAR')


view(file)
