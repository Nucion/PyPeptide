import os

santo_grial ="../netMHCpan -p test.txt -BA -a HLA-A01:01 > final_out.txt"
path = "/mnt/c/Users/nicol/Documents/Final_Test"

def import_file(netMHCpan_path,file_path=None,file_name=None):
    if(not os.path.isdir(netMHCpan_path +'/netMHCpan-4.1/my_directory')):
        directory = "my_directory"
        
        # Parent Directory path
        parent_dir = netMHCpan_path + "/netMHCpan-4.1"
        
        # Path
        path2 = os.path.join(parent_dir, directory)

        os.mkdir(path2)
        print("Directory '% s' created" % directory)
    if(file_path is not None):
        if(file_path != netMHCpan_path + "/netMHCpan-4.1/my_directory/" + file_name):
            path2 = netMHCpan_path + "/netMHCpan-4.1/my_directory/" + file_name
            os.rename(file_path, path2)
            print("File saved on my_directory!")
        else:
            path2 = file_path
    return path2
        

Table = import_file(path,"/mnt/c/Users/nicol/Documents/Peptidos.xlsx","Peptidos.xlsx")

print(Table)
