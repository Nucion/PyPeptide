import os
import pandas as pd

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
        

#Table = import_file(path,"/mnt/c/Users/nicol/Documents/Peptidos.xlsx","Peptidos.xlsx")
Table = path + "/netMHCpan-4.1/my_directory/Peptidos.csv"
print(Table)
# if(Table[-4:] == "xlsx"):
#     df = pd.read_excel(Table)
#     df
#     a=df.to_string(index=False)
#     print(a)



peps = pd.read_csv(Table)
peps = peps[["Gene ID","Sequence","WT","HLA","Longitud"]].dropna()
inputs = peps["Sequence"]
pepList = inputs.values.tolist()
inputs2 = peps["HLA"]
HLAlist = inputs2.values.tolist()
print(len(pepList)-1)
print(len(HLAlist)-1)

# f= open(path + "/netMHCpan-4.1/my_directory/CompleteList.txt","w+")
# f.close()

# for i in range(len(pepList)):
#     f= open(path + "/netMHCpan-4.1/my_directory/guru99.txt","w+")
#     my_str=pepList[i]
#     f.write(my_str)
#     f.close()
#     HLA=HLAlist[i].replace("*","")
#     os.system("cd "+ path + "/netMHCpan-4.1/my_directory/ && ../netMHCpan -p guru99.txt -BA -a "+ HLA+" > guru.pep.myout")
#     print("completed ",i)
#     with open(path + "/netMHCpan-4.1/my_directory/guru.pep.myout") as f2:
#         script = f2.read().splitlines()
#         if(len(script)>=49):
#             print (script[49])
#             new_line = script[49]+"\n"
#             f3=open(path + "/netMHCpan-4.1/my_directory/CompleteList.txt", "a+")
#             f3.write(new_line)
#             f3.close()
divided_list= []
with open(path + "/netMHCpan-4.1/my_directory/CompleteList.txt") as f:
    script = f.read().splitlines()
    for i in range(len(script)):
        words = script[i].split()
        divided_list.append(words)
df = pd.DataFrame(divided_list)
df.drop(16, axis=1, inplace=True)

with open(path + "/netMHCpan-4.1/my_directory/guru.pep.myout") as f:
    script = f.read().splitlines()
    columns = script[47].split()



peps = pd.concat([peps, inputs], axis=1)
peps.columns = ["Gene ID","Sequence","WT","HLA","Longitud","Peptide"]
df.columns=columns
print(peps)
completedTable = pd.merge(peps, df, on=["Peptide"])
print(completedTable)

df.to_csv(path + "/netMHCpan-4.1/my_directory/CompleteList.csv", index=False)