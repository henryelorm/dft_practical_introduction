from ase.build import fcc100,  add_adsorbate
from ase.visualize import view
from ase.constraints import FixAtoms
from ase.io.vasp import write_vasp

a = 3.64

slab_cu = fcc100(a=a, symbol='Cu', size=(2,2,4))

# add_adsorbate(slab=slab_cu, position=(0.36*a, 0.36*a), adsorbate='Ag', height=1.8, ) # initial state (hollow site)

add_adsorbate(slab=slab_cu, position=(0.36*a, 0.66*a), adsorbate='Ag', height=1.8, )   # final state (bridge site)

slab_cu.center(axis=2, vacuum=14)


masks  = []
for i in slab_cu:
    constrain = i.tag > 2
    masks.append(constrain)

slab_cu.set_constraint(FixAtoms(mask=masks))


# Move atoms to the base of the supercell
slab_cu.positions[:, 2] -= slab_cu.cell[2, 2] / 2.5


# write_vasp(file='POSCAR_h', atoms=slab_cu,  direct=True)
write_vasp(file='POSCAR_b', atoms=slab_cu,  direct=True)


view(slab_cu)

