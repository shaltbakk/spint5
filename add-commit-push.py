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
printAndExecute("git status")
printAndExecute("git add -A")

if input("message[y/n]:") == "y":
    printAndExecute('git commit -m "'+input("message")+'"')
else:
    printAndExecute('git commit')
printAndExecute("git push origin master")