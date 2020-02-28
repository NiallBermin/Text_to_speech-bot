import os

def systemCommand(input, place):
    #takes in the command and converts it to lowercase and splits into a list
    command = input.lower().capitalize().split()
    #change directory command as cd
    if ("Change" and "Directory") in command:
        command.remove("Directory")
        command.remove("Change")
        if "Root" in command:
            command = [c.replace("Root", "~") for c in command]
        place = "~/Documents/Test/"

    return True
