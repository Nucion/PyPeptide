import tarfile
import requests 
#from tqdm import tqdm
from os import remove
import os

# path = "/mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-4.1b.Linux.tar.gz"
# file1 = tarfile.open('/mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-4.1b.Linux.tar.gz') 
  
# file1.extractall('./') 
  
# file1.close() 

# #---------------------------------------------------------------------------------

# print("Downloading Data...")

# URL = "https://services.healthtech.dtu.dk/services/NetMHCpan-4.1/data.tar.gz"
  
# file2 = requests.get(URL, stream = True)
  
# with open("data.tar.gz","wb") as pdf:
#     #tqdm(file2.iter_content(chunk_size=1024))
#     for chunk in file2.iter_content(chunk_size=1024):
  
#          if chunk:
#              pdf.write(chunk)

# print("Downloaded!")
# #---------------------------------------------------------------
# file3 = tarfile.open('./data.tar.gz') 
  
# file3.extractall('./') 
  
# file3.close() 

# #---------------------------------------------------------
# print("Removing...")
# remove("./data.tar.gz")
# print("Removed!")
# #--------------------------------------------------

# with open("/mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-py/netMHCpan-4.1/netMHCpan") as f:
#     script = f.read().splitlines()
#     print (script[13])
# script[13] = "setenv  NMHOME  /mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-py/netMHCpan-4.1"
# with open("/mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-py/netMHCpan-4.1/netMHCpan", 'w') as f:
#     f.write("\n".join(script))
# print("Script Changed (1/2)")

# directory = "tmp"
  
# # Parent Directory path
# parent_dir = "/mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-py"
  
# # Path
# path = os.path.join(parent_dir, directory)
  
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# os.mkdir(path)
# print("Directory '% s' created" % directory)


# with open("/mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-py/netMHCpan-4.1/netMHCpan") as f:
#     script = f.read().splitlines()
#     print (script[13])
# script[18] = "	setenv  TMPDIR  /mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-py/tmp"
# with open("/mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos y Ejercicios/Ing Comp 7mo Semestre/Sistemas_Inteligentes/netMHCpan-py/netMHCpan-4.1/netMHCpan", 'w') as f:
#     f.write("\n".join(script))

# print("Script changed (2/2)")

#----------------------------------------------------------------------

os.system("cd /mnt/c/Users/nicol/OneDrive/Escritorio/Proyectos\ y\ Ejercicios/Ing\ Comp\ 7mo\ Semestre/Sistemas_Inteligentes/netMHCpan-py/netMHCpan-4.1/test/")
print("tests:")
os.system("-p test/test.pep")