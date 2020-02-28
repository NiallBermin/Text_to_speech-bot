import os

def editFile(filename):

    return True


# creates a newfile
def newfile(filename, directory):
    fileExtension = check_extension(filename)
    # opens/creates a file of that name

    with open(fileExtension ,"+w") as f:
        #puts in a string for testing
        f.write("This is a test")
        f.close()
        #returns an acknoledgement of the file being created
    os.system("mv " + fileExtension + " " + directory)
    return "The " + fileExtension + " has been created"



#checks for extension
def check_extension(filename):
    #checks if last thing in string is a extention type
    extensionPosition = filename.split()[-1].lower()
    extension = ""
    if "text" in extensionPosition or "txt" in extensionPosition:
        extension = ".txt"

    elif "python" in extensionPosition or "py" in extensionPosition:
        extension = ".py"

    elif "java" in extensionPosition:
        extension = ".java"

    if extension != "":
        #joins the filename and the believed extension into one string and changes the spaces into _
        fileExtension = "_".join(filename.split()[:-1]) + extension
    else:
        fileExtension = "_".join(filename.split()) + ".txt"
    return fileExtension
