# netMHCpan-py
Library for installation and usage of netMHCpan algorithm for predicton of peptides binding to MHC molecules. This library works for any linux enviroment where there is access to the terminal, including the ubuntu terminal for windows.

## Installation of the library:
- !git clone https://github.com/Nucion/netMHCpan-py.git.
- import PyPeptide as pyp.

##  Prerequisites for usage of library:
- install tqdm library (will authomatically do so regardless).
- install tcsh enviroment (this library contains a function to do so).
- install pandas library

## Installing netMHC pan:
- Check t-shell (tcsh) is correctly installed.
- Download tool from https://services.healthtech.dtu.dk/service.php?NetMHCpan-4.1 and place it in the folder where the tool will be installed.
- Check the folder path doesnt have spaces in the folders' name.
### Use installer.py functions:
You can either:
- Use the nerMHCpanInstall function, providing the path for the destination
- Use each of the sub functions separately for a more step-by step installation. Each needs the same path to be provided

## Usage of netMHCpan:
##### Once installed this library provides functions to fascilitate the usage of netMHCpan. (still a work in progress)
For this library to work, the input csv must be in the 'my_directory' folder. This is created in the inport_file() function, so be sure to use it the first time.
Once everything is set up, you can either:
- Use the complete_csv function, providing path to the csv and folder where netMHCpan is (the same as with the installe functions)
- Use each function separately, check how the complete_csv function uses them for more detail with their parameters

# Authors
- Nicolas Leszezyñski - Univ. Católica de Córdoba
- Martina Liz Ceballos - Univ. Católica de Córdoba
- Guadalupe Nibeyro
- Elmer A. Fernández - Centro de Investigación y Desarrollo en Inmunología y Enfermedades Infecciosas (CIDIE) - Univ. Católica de Córdoba - CONICET, Argentina
