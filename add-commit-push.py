import os
import sys
import subprocess as sub
def gitCommitMessage():
   #Check if there is a -m parameter
   #if -m exist, then use second parameter as message
    returnMessage="Update Files."
    # total arguments
    n = len(sys.argv)
    if n == 3:
        print(sys.argv[1])
        print(sys.argv[2])

    return returnMessage



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

commitMessage=gitCommitMessage()
printAndExecute('git commit -m "'+input("message")+'"')


printAndExecute("gitCommand")
printAndExecute("git push main master")