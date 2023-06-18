# neb_init.py
import os
import sys

sys.path.append('directory-pointing-to-vtstscripts/vtstscripts/vtstscripts-1033')
# https://theory.cm.utexas.edu/vtsttools/scripts.html

from aselite import read_vasp, write_vasp, NEB



n_im = 5  # Number of intermediate images

ini_fn = "prepare/ini/CONTCAR"
fin_fn = "prepare/fin/CONTCAR"

# Read in structures
ini = read_vasp(ini_fn)
fin = read_vasp(fin_fn)


def do_vasp(pos1, pos2, snimgs, is_linear):
    ini_atoms = read_vasp(pos1)
    fin_atoms = read_vasp(pos2)
    images = [ini_atoms]
    for i in range(snimgs):
        images.append(ini_atoms.copy())
    images.append(fin_atoms)
    neb = NEB(images)
    if is_linear:
        print('using Linear')
        neb.interpolate(mic=True)
    else:
        print('using IDPP')
        neb.interpolate('idpp',mic=True)
    dir_names = ['0'+str(i) if i < 10 else str(i) for i in range(len(images))]
    for i, image in zip(dir_names,neb.images):
        if not os.path.isdir(i):
            os.mkdir(i)
        write_vasp(i+'/POSCAR',image)
    print('Ok, all set up here.')
    print('For later analysis, put OUTCARs in folders 00 and ' + dir_names[-1])


do_vasp(pos1=ini_fn, pos2=fin_fn, snimgs=n_im, is_linear=False)
