import os
import pandas as pd


# Check if my_directory exists on netMHCpan directory, otherwise create it
# Move file into my_directory and return its path location

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
            if(file_path[-4:] != ".csv"):
                print("Please use a .csv file")
                path2=None
            else:
                path2 = netMHCpan_path + "/netMHCpan-4.1/my_directory/" + file_name
                os.rename(file_path, path2)
                print("File saved on my_directory!")
        else:
            path2 = file_path
    return path2

# make Database into pandas dataframe
# create a list with peptides and another with alleles
def inputsProcessing(Table):
    peps = pd.read_csv(Table)
    peps = peps[["Gene ID","Sequence","WT","HLA","Longitud"]].dropna()
    inputs = peps["Sequence"]
    pepList = inputs.values.tolist()
    inputs2 = peps["HLA"]
    HLAlist = inputs2.values.tolist()
    print(len(pepList)-1)
    print(len(HLAlist)-1)
    return pepList,HLAlist

# Creation of CompleteList, which contains all the binding results from the dataFrame provided:
# create a temporary file with piptide #i
# fix allele #i
# run "../netMHCpan -p peptide.txt -BA -a "+ HLA+" > tempResult.pep.myout" where peptide.txt is temporary peptide file and HLA is the allele
# Save result from tempResult into CompleteList (a file)

def make_txt(pepList,HLAlist,path):
    f= open(path + "/netMHCpan-4.1/my_directory/CompleteList.txt","w+")
    f.close()

    for i in range(len(pepList)):
        f= open(path + "/netMHCpan-4.1/my_directory/guru99.txt","w+")
        my_str=pepList[i]
        f.write(my_str)
        f.close()
        HLA=HLAlist[i].replace("*","")
        os.system("cd "+ path + "/netMHCpan-4.1/my_directory/ && ../netMHCpan -p guru99.txt -BA -a "+ HLA+" > guru.pep.myout")
        print("completed ",i)
        with open(path + "/netMHCpan-4.1/my_directory/guru.pep.myout") as f2:
            script = f2.read().splitlines()
            if(len(script)>=49):
                print (script[49])
                new_line = script[49]+"\n"
                f3=open(path + "/netMHCpan-4.1/my_directory/CompleteList.txt", "a+")
                f3.write(new_line)
                f3.close()


# Create a dataframe from completeList file
# Divide into collumns, ditch '<=' and place column titles

def make_dataframe(path):
    divided_list= []
    with open(path + "/netMHCpan-4.1/my_directory/CompleteList.txt") as f:
        script = f.read().splitlines()
        for i in range(len(script)):
            words = script[i].split()
            divided_list.append(words)
    df = pd.DataFrame(divided_list)
    df.drop(16, axis=1, inplace=True)
    return df

# Concat input with output
# Create a 'Peptide' column on input dataframe which has same data as "Sequence" column
# merge using 'Peptide' as index
# Export as .csv

def make_csv(path,df):

    with open(path + "/netMHCpan-4.1/my_directory/guru.pep.myout") as f:
        script = f.read().splitlines()
        columns = script[47].split()

    peps = pd.read_csv(Table)
    peps = peps[["Gene ID","Sequence","WT","HLA","Longitud"]].dropna()
    inputs = peps["Sequence"]

    peps = pd.concat([peps, inputs], axis=1)
    peps.columns = ["Gene ID","Sequence","WT","HLA","Longitud","Peptide"]
    df.columns=columns
    print(peps)
    completedTable = pd.merge(peps, df, on=["Peptide"])
    print(completedTable)

    completedTable.to_csv(path + "/netMHCpan-4.1/my_directory/CompleteList.csv", index=False)

# Imports the peptides csv and returns its processing
# needs input to be formatted in ["Gene ID","Sequence","WT","HLA","Longitud"]
# needs my_directory folder to exist and peptides csv to be inside, use import_file function if not

def complete_csv(Table,path):
    if(not os.path.isdir(path +'/netMHCpan-4.1/my_directory')):
        print("Please use 'import_file()' function to create 'my_directory folder'")
        return
    print("Creating pep and HLA lists...")
    pepList,HLAlist = inputsProcessing(Table)
    print("Completed!")
    print("Processing of peptides...")
    make_txt(pepList,HLAlist,path)
    print("Completed!")
    print("Exporting csv...")
    df = make_dataframe(path)
    make_csv(path,df)
    print("Completed!")

