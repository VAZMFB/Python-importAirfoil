# Test importAirfoil
# Author: Milos D. Petrasinovic <mpetrasinovic@mas.bg.ac.rs>
# Structural Analysis of Flying Vehicles
# Faculty of Mechanical Engineering, University of Belgrade
# Department of Aerospace Engineering, Flying structures
# https://vazmfb.com
# Belgrade, 2022
# ---------------
#
# Copyright (C) 2022 Milos Petrasinovic <info@vazmfb.com>
#  
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as 
# published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# --------------------
import time
t = time.time()
import sys
import os
pwd = os.getcwd();
sys.path.append(pwd + '\\..\\..\\src\\')
from importAirfoil import *
import matplotlib.pyplot as plt

print(' --- ' + os.path.basename(__file__) + ' --- ')
afns = os.listdir('.\\airfoils') # airfoil names
N_afns = len(afns)

# - Import airfoil then show and save figure
fig, ax = plt.subplots()
ax.set_xlabel('x [-]')
ax.set_ylabel('y [-]')
ax.set_box_aspect('1')
ax.set_aspect('equal')
for i, afn in enumerate(afns):
    ax.clear()
    ax.grid()
    print(' Importing ' + afn + ' [' + str(i+1) + '/' + str(N_afns) + ']')
    af = importAirfoil('.\\airfoils\\' + afn)
    ax.plot([0, 1], [0, 0], linewidth=2)
    if len(af) == 2 and len(af[0]) > 0 and len(af[1]) > 0:
        ax.plot(af[0], af[1], linewidth=2)
    ax.set_title(afn)
    ax.set_xlim(0, 1)
    path = pwd + '\\figures\\' + afn.replace('.', '-').replace('/', ' ');
    plt.savefig(path + '.png')
    plt.savefig(path + '.svg')
    
# - End of program
print(' The program was successfully executed... ');
print(' Execution time: ' + "{:.2f}".format(time.time() - t) + ' seconds');
print(' -------------------- ');