:: UploadPyPi.cmd
:: Author: Milos D. Petrasinovic <mpetrasinovic@mas.bg.ac.rs>
:: Structural Analysis of Flying Vehicles
:: Faculty of Mechanical Engineering, University of Belgrade
:: Department of Aerospace Engineering, Flying structures
:: https://vazmfb.com
:: Belgrade, 2022
:: --------------------
::
:: Copyright (C) 2022 Milos Petrasinovic <info@vazmfb.com>
::  
:: This program is free software: you can redistribute it and/or modify
:: it under the terms of the GNU General Public License as 
:: published by the Free Software Foundation, either version 3 of the 
:: License, or (at your option) any later version.
::   
:: This program is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
:: GNU General Public License for more details.
::   
:: You should have received a copy of the GNU General Public License
:: along with this program.  If not, see <https://www.gnu.org/licenses/>.
::
:: --------------------
@echo off

:: --------------------
:: Set directory
setlocal
set realPath=%~dp0
cd /d %realPath%

:: Get admin rights
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"  
if '%errorlevel%' NEQ '0' ( echo Requesting administrative privileges... ) else ( goto gotAdmin )
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"  
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"  
    "%temp%\getadmin.vbs"  
    exit /B
:gotAdmin

:: Execute commands
cmd /k "cd ../ & Scripts\activate & cd %realPath% & cd ../../ & pip install -U pip setuptools twine & python setup.py sdist & twine upload --repository pypi dist/*"
:: --------------------