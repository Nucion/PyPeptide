import tarfile
import requests 
from os import remove
import os
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    os.system("pip3 install tqdm")
    from tqdm import tqdm
    print("installing tqdm...")
import subprocess 

path = "/mnt/c/Users/nicol/Documents/Final_Test"


def install_T_Shell():
    print('installing tcsh...')
    subprocess = subprocess.Popen("tcsh --version", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    if(subprocess_return != b'tcsh 6.20.00 (Astron) 2016-11-24 (x86_64-unknown-linux) options wide,nls,dl,al,kan,sm,rh,nd,color,filec\n'):
        os.system("sudo apt-get install tcsh")



def netMHCpanExtract(path):

    file1 = tarfile.open(path + '/netMHCpan-4.1b.Linux.tar.gz') 
    print("Extracting netMHCpan-4.1b ...")
    file1.extractall(path + '/') 
    file1.close() 
    print("Removing tar...")
    remove(path + '/netMHCpan-4.1b.Linux.tar.gz')
    print ("Removed!")


# #---------------------------------------------------------------------------------
def DataDownload(path):
    print("Downloading Data...")

    URL = "https://services.healthtech.dtu.dk/services/NetMHCpan-4.1/data.tar.gz"
    file2 = requests.get(URL, stream = True)
  
    with open(path + "/data.tar.gz","wb") as pdf:
    #
        for chunk in tqdm(file2.iter_content(chunk_size=1024)):
  
             if chunk:
              pdf.write(chunk)

    print("Downloaded!")


def DataExtract(path):
    print("Removing trash Data file...")
    remove(path + "/netMHCpan-4.1/Linux_x86_64/data")
    print("Removed!")

    file3 = tarfile.open(path + '/data.tar.gz') 
    file3.extractall(path + "/netMHCpan-4.1/Linux_x86_64/")
    file3.close() 

    print("Removing Data Tar...")
    remove(path + "/data.tar.gz")
    print("Removed!")



def ChangeDir(path):
    with open(path + "/netMHCpan-4.1/netMHCpan") as f:
        script = f.read().splitlines()
        print (script[13])
    script[13] = 'setenv  NMHOME  "'+ path + '/netMHCpan-4.1"'
    with open(path + "/netMHCpan-4.1/netMHCpan", 'w') as f:
        f.write("\n".join(script))
    print("Script Changed (1/3)")

    directory = "tmp"
    
    # Parent Directory path
    parent_dir = path + "/netMHCpan-4.1"
    
    # Path
    path2 = os.path.join(parent_dir, directory)
    
    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    os.mkdir(path2)
    print("Directory '% s' created" % directory)


    with open(path + "/netMHCpan-4.1/netMHCpan") as f:
        script = f.read().splitlines()
        print (script[13])
    script[18] = '	setenv  TMPDIR  "'+ path + '/netMHCpan-4.1/tmp"'
    with open(path + "/netMHCpan-4.1/netMHCpan", 'w') as f:
        f.write("\n".join(script))

    print("Script changed (2/3)")

    with open(path + "/netMHCpan-4.1/netMHCpan") as f:
        script = f.read().splitlines()
        print (script[31])
    script[31] = 'setenv NETMHCpan "$NMHOME/$PLATFORM"'
    with open(path + "/netMHCpan-4.1/netMHCpan", 'w') as f:
        f.write("\n".join(script))
    print("Script Changed (3/3)")



#----------------------------------------------------------------------
def netMHCpanTest(path):

    print("tests:")
    os.system("cd "+ path + "/netMHCpan-4.1/test/ && ../netMHCpan -p test.pep > test.pep.myout")
    print("Completed (1/5)")
    os.system("cd "+ path + "/netMHCpan-4.1/test/ && ../netMHCpan test.fsa > test.fsa.myout")
    print("Completed (2/5)")
    os.system("cd "+ path + "/netMHCpan-4.1/test/ && ../netMHCpan -hlaseq B0702.fsa -p test.pep > test.pep_userMHC.myout")
    print("Completed (3/5)")
    os.system("cd "+ path + "/netMHCpan-4.1/test/ && ../netMHCpan -p test.pep -BA > test.pep_BA.out")
    print("Completed (4/5)")
    os.system("cd "+ path + "/netMHCpan-4.1/test/ && ../netMHCpan -p test.pep -BA -xls -a HLA-A01:01,HLA-A02:01 -xlsfile my_NetMHCpan_out.xls")
    print("Completed (5/5)")


def setPATH(plinstall_Tath):
    os.envirolinstall_Tn["PATH"] = (os.environ["PATH"] + ":" + path + "/netMHCpan-4.1")
    os.systemlinstall_T("echo $PATH")


def netMHCpanInstall(path):
    #install_T_Shell()
    try:
        netMHCpanExtract(path)
    except:
        print("Please install netMHCpan from https://services.healthtech.dtu.dk/service.php?NetMHCpan-4.1")
    DataDownload(path)
    DataExtract(path)
    ChangeDir(path)
    netMHCpanTest(path)
    setPATH(path)

    