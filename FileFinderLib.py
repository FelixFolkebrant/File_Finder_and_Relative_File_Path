import sys,os
#Filefinder

#Finds a file in any subfolder in the specified directory and returns the full path so that you can use it in code. 
# Either use relative path (.../sms/sms.py) or full path (C:\Users\Barn\sms.py) and just end it with the filename that you want to search in. 
# That means that you can just as well search in (.../sms/sms.py) as (.../sms.py) but the more precise you are the faster the search becomes. If you just want to use relative file path use the rfp() function instead
#-------------------------------------------------------------
def find_file(directory):
    #Full path
    if directory[1] == ":":
        root = "".join(directory[0:2])
        target = directory.split("\\")[-1]
        directory = "".join(directory[2:len(directory)-len(target)])
        path = os.path.join(root, directory)
        for paths,subdirs,files in os.walk(directory):
            for name in files:
                if name == target:
                    subdirname = (os.path.join(paths, name))
                    result = (os.path.abspath(subdirname))
        try:
            return(result)
        except:
            print(f"{target} was not found in {path}")
    #Relative path
    else:
        #If directory goes to far back up the tree
        if os.path.dirname(os.path.realpath(__file__)).count('\\')+2 < directory.count("."):
            print("Too many dots")
        else:
            #If we have specified the path more (..../folder/file.py)
            if len(directory.split("/")) > 2:
                area = "\\".join(directory.split("/")[1:-1])
                target = directory.split("/")[-1]
                currentdir = os.path.dirname(os.path.realpath(__file__)).split('\\')
                currentdir = "\\".join(currentdir[0:os.path.dirname(os.path.realpath(__file__)).count('\\')-(directory.count(".")-3)])
                currentdir = currentdir +"\\" +area
                root = "".join(currentdir[0:2])
                path = os.path.join(root, currentdir)
                print(currentdir)
                for path,subdirs,files in os.walk(currentdir):
                    for name in files:
                        if name == target:
                            root = "".join(currentdir[0:2])
                            subdirname = (os.path.join(path, name))
                            subdirname = "".join(subdirname)[2:len(subdirname)]
                            result = (os.path.abspath(subdirname))
                try:
                    return(result)
                except:
                    return(f"{target} was not found in {currentdir}")
            #If we have a simple search (..../file.py)
            else:
                target = directory.split("/")[1]
                currentdir = os.path.dirname(os.path.realpath(__file__)).split('\\')
                currentdir = "\\".join(currentdir[0:os.path.dirname(os.path.realpath(__file__)).count('\\')-(directory.count(".")-3)])
                root = "".join(currentdir[0:2])
                directory = "".join(currentdir[2:len(currentdir)])
                path = os.path.join(root, directory)
                for path,subdirs,files in os.walk(currentdir):
                    for name in files:
                        # print(os.path.join(path, name))
                        if name == target:
                            root = "".join(currentdir[0:2])
                            subdirname = (os.path.join(path, name))
                            subdirname = "".join(subdirname)[2:len(subdirname)]
                            result = (os.path.abspath(subdirname))
                try:
                    return(result)
                except:
                    print(f"{target} was not found in {directory}")

#rfp ("Relative File Path")

#A command that lets you use relative filepaths in python 
#-------------------------------------------------------------
def rfp(input:str):
    if os.path.dirname(os.path.realpath(__file__)).count('\\')+2 < input.count("."):
        print("Too many dots")
    else:
        filename = input.split("/")[1]
        currentdir = os.path.dirname(os.path.realpath(__file__)).split('\\')
        currentdir = "\\".join(currentdir[0:os.path.dirname(os.path.realpath(__file__)).count('\\')-(input.count(".")-3)])
        return(f"{currentdir}\{filename}")

def file_info(file:str, info):
    if info == "ending":
        file = file.split(".") 
        return "."+file[-1]
    if info == "name":
        try:
            name = file.split("\\")[-1]
            return name
        except:
            return file

#Yoink

#Fil-yoinkaren som hittar och plockar en fil från ett directory och kopierar den till ett annat ställe
#Params = (the find_file() search for the file so scroll to that function, the name that you save it as (Default: Yoink), the outputfolder (Default: same as this script))
def yoink(file:str, output_name="", output_path=rfp('./')):
    file = find_file(file)
    ending = file_info(file, "ending")
    output = f"{output_path}{output_name}{ending}"
    print(file_info(file, "name"))
    if output_name == "":
        output = f'{output_path}{file_info(file, "name")}'
        os.popen(f'copy {file} {output}')
    else:
        output = f"{output_path}{output_name}{ending}"
        os.popen(f'copy {file} {output}')

yoink(".../MatrixMathLib.py")


