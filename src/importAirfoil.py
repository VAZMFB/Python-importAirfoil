# Airfoil coordinates import function
# Author: Milos D. Petrasinovic <mpetrasinovic@mas.bg.ac.rs>
# Structural Analysis of Flying Vehicles
# Faculty of Mechanical Engineering, University of Belgrade
# Department of Aerospace Engineering, Flying structures
# https://vazmfb.com
# Belgrade, 2022
# ----- INPUTS -----
# file - full path to document with airfoil data
# ----- OUTPUTS -----
# af - airfoil coordinates
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
# --------------------
import subprocess
import sys
import os
import re
    
# Import numpy 
try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])
finally:
    import numpy as np
   
def scanf(l):
    # scanf('%f %f', l)
    found = re.compile('([-+]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)(?:[eE][-+]?\\d+)?)\\s+([-+]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)(?:[eE][-+]?\\d+)?)').search(l)
    casts = [float, float]
    if found:
        groups = found.groups()
        return tuple([casts[i](groups[i]) for i in range(len(groups))])
    
def importAirfoil(file):
    """
    Airfoil coordinates import function
    
    :param file: full path to document with airfoil data
    """
    af = [];
    if(os.path.isfile(file)):
        with open(file) as f:
            ls = [line.strip() for line in f]
            
        x = []
        y = []
        h = 1
        for l in ls:
            if l:
                data = scanf(l);
                if(h and data and len(data) == 2 and data[0] > -0.1
                        and data[0] < 1.1 and data[1] > -1.1 
                        and data[1] < 1.1):
                    # First coordinate if there is both x and y data
                    # Range for x is [-0.1, 1.1] and for y is [-1.1, 1.1]
                    h = 0;
                    x.append(data[0])
                    y.append(data[1])
                elif(not h and data and len(data) == 2):
                    x.append(data[0])
                    y.append(data[1])
        
        if(len(x) > 0):
            if(any(xi >= 1.1 for xi in x)):
                # Data is probably multiplied by 100
                x = np.divide(x, 100)
                y = np.divide(y, 100)
                      
        d = np.diff(x)
        if(sum([di < 0 for di in d]) == 1):
            # Lednicer format
            i = np.where(d < 0)[0][0]
            x = [*np.flip(x[:i+1]).tolist(), *x[i+1:]]
            y = [*np.flip(y[:i+1]).tolist(), *y[i+1:]]

        af = np.array([x[1:-1], y[1:-1]])
        _, idx = np.unique(af, axis=1, return_index=True)
        af = [[x[0], *af[0][np.sort(idx)].tolist(), x[-1]],
            [y[0], *af[1][np.sort(idx)].tolist(), y[-1]]]
    return af