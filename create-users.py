#!/usr/bin/python3

# INET4031
# Sulekha
# 10/27/2025
# 10/30/2025


import os
import re
import sys


def main():
    for line in sys.stdin:

        #This expression is looking to see if there's any line that start with # as it lists down below.
        #It's looking for '#' because this is character is used when writing a comment in python, and it's checking to see if there's any '#' so it can skip through it.
        match = re.match("^#",line)

        #This code here is splitting the line shown below with the ':' and this is used to seperate everything apart, it prevents username and password from being all in one spot with no seperation or space. 
        fields = line.strip().split(':')

        #It's checking for whether or not the line is valid before it goes through it.
        #If it evaluates to true, it means that it wasn't able to pass that check so if it's looking for '#', then it wasn't able to match that and failed
        #It does rely on the previous lines of code because it uses those to see if the line starts with the '#' and those results to figure out whether or not if that line is correct or should be skipped. 
        #Because the in the input file it only has 5 parts to it, the usernmae, password, last, first and group. If there's an extra or empty field, then it would fail to pass.
        if match or len(fields) != 5:
            continue

        #Those three lines are asking the user for their username and password, as well as the 'gecos' to create the account, and for storing as well. The 'gecos' field is used for storing info regarding user like name. 
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This split is being done because in the input file, the user has groups seperated by comma and this makes it easier to process all that info one by one.
        groups = fields[4].split(',')

        #This is good for seeing if there is any problems in the code, it's mean to to print what account and group it's working on.
        print("==> Creating account for %s..." % (username))
        #This is creating a new user account and the 'cmd' contains the whole string that has the info about the user which is the full name and username filled in.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #The first test the code, it's important to keep them commented and uncomment the print so that you can dry run it first, once thats tested and works, removing the # from cmd command will run the program and makes actual system changes.
        print(cmd)
        os.system(cmd)

        #The point of this print statement is to output a message and shows what acoount it's on, outputting what user it's setting a pssword for. 
        print("==> Setting the password for %s..." % (username))
        #This line is allowing for the password to be asked to the user two times due to the 'echo -ne' portion,  and to set the password for the user automatically and it will run in the terminal.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #The point is to test the code without actually making systemchanges and create users, passwords and run into a bug, it will take longer to fix if you don't dryrun it first. When it gets uncommented it will run and add users, set the passwords.
        print(cmd)
        os.system(cmd)

        for group in groups:
            #The if statement is looking for the dash '-' from the input file, its checking to see if it has that and will skip it since it will be false due to the if statement but if its true, it will run the next line and add the user, it's trying to prevent missing group fields so  it helps skip it to prevent errors. 
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
