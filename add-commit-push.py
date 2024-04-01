import os


def printAndExecute(command):
    print("\nExecuting: " + command)
    os.system(command)

print("git status \n git add -A \n git commit -m \n git push")
userResponse = input("[y/n]:")
print("userResponse:" + userResponse)

if userResponse != "y":
    print("Exiting")
    exit()
print("git status\n") 
printAndExecute("git status")
print("git add -A\n")
printAndExecute("git add -A")

if input("message[y/n]:") == "y":
    print("git commit -m")
    printAndExecute('git commit -m "'+input("message")+'"')
else:
    print("git commit")
    printAndExecute('git commit')
if input("[y/n]:")!="y": 

    printAndExecute("git push origin master")
else:
    printAndExecute("git push origin master -f")