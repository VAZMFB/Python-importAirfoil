# Python Airfoil coordinates import function

Airfoil coordinates import function in Python.

<p align="center">
  <img src="https://vazmfb.com/web/img/github/importAirfoil_PY.png" width="800">
</p>


## Requirements
[Python](https://www.python.org/)<br>

Provided code is tested with **Python 3.10.1**.

## Usage

Use `importAirfoil` function with the full path to document with airfoil data as only input argument. 

Please check provided test in `test/_App` folder. In order to run the test first run CreateApp.cmd file (with adjusted input variables).

## Airfoil file parsing rules

- The file is read a line at a time starting from the top. 
- Blank lines are discarded.
- The first line that is not discarded is the line on which function `scanf()` finds two float numbers, with the first number in the range [-0.1, 1.1] and the second in the range [-1.1, 1.1].
- All subsequent lines on which function `scanf()` finds two float numbers are taken into the account.
- If any value is greater than 1.1 all values are divided by 100 (see NACA file format).
- If there is one change in x value gradient, flip data that is after the change of gradient (see Lednicer file format).

## Airfoil file formats

> - [Siegel](https://m-selig.ae.illinois.edu/ads.html)

Lists points from the trailing edge, goes over the upper surface, then over the lower surface, to go back to the trailing edge (or in other direction, first lower and then upper surface).

> - Lednicer 

Lists points on the upper surface (from leading edge to trailing edge), then points on the lower surface (from leading edge to trailing edge).

> - OpenVSP .af 

Same as the Siegel format but with the additional header.

> - NACA (as in Report No. 824)

Same as the Lednicer format but multiplied by 100.

## License
Copyright (C) 2022 Miloš Petrašinović <info@vazmfb.com>
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
  
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
  
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
