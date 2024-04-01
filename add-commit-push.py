import os





def printAndExecute(command):
    print("\nExecuting: " + command)
    os.system(command)

print("git status")
print("git add -A")
print('git commit -m ')
print("git push")
userResponse = input("[y/n]:")
print("userResponse:" + userResponse)

if userResponse != "y":
    print("Exiting")
    exit()

printAndExecute("git add -A")

if input("[y/n]:")!= "y":
    printAndExecute('git commit -m "'+input("message")+'"')
else:
    printAndExecute('git commit')
printAndExecute("gitCommand")
printAndExecute("git push origin master")