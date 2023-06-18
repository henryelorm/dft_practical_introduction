from ase.visualize import view
from ase.io.vasp import read_vasp
from ase.io.trajectory import Trajectory
from ase.visualize import view
from ase.io import read

atoms_list = []

is_original = False

image_size = 7
for i in range(image_size):
    print(i)
    atoms = read_vasp('./0' + str(i) +  ('/POSCAR' if is_original else  ('/POSCAR'  if  i == 0 or i == (image_size-1) else '/CONTCAR') ) 
                      if i < 10 else './' + str(i) + ('/POSCAR' if is_original else  ('/POSCAR'  if  i == 0 or i == (image_size-1) else '/CONTCAR') ))
    atoms_list.append(atoms)

# traj = Trajectory('movie.traj', mode='w')
# for atoms in atoms_list:
#     traj.write(atoms=atoms)

view(atoms_list)
