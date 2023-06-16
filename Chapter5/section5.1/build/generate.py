from ase import Atoms
from ase.visualize import view
from ase.io.vasp import write_vasp


CO = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.128)])


box_size = (10, 10, 10)
gas_phase_box = Atoms('C' + 'O', positions=[(0, 0, 0), (0, 0, 1.128)])
gas_phase_box.set_cell(box_size)


v = CO[1].position - CO[0].position
gas_phase_box.rotate(v=v, a=CO[1].position, center=(0, 0, 0))

write_vasp(file='POSCAR_CO', atoms=gas_phase_box,  direct=True)

view(gas_phase_box)



