import os;
import pandas as pd;
import platform;
def clear():
    if(platform.system()=="Linux"):
        os.system("clear");
    elif(platform.system()=="Windows"):
        os.system("cls");
    else:
        print("Error: platform not recognized. useage of this program is not recomended");


running=True;

def new():
    filename=input("please enter the new file name ").lower();
    filename="passwd/"+filename+".csv";
    os.system("touch "+filename);
    with open(filename, 'a') as file:
        file.write("website/application,user name,password\n");
    os.system("gpg -c --no-symkey-cache "+filename);
    os.system("rm "+filename);

def listall():
    os.system("ls passwd/");

def append(filename):
    clear();
    arr=["app", "name", "passwd"];
    appending=True;
    while(appending):
        clear();
        arr[0]=input("enter application or site name\nappending>");
        arr[1]=input("enter user name\nappending>");
        arr[2]=input("enter password\nappending>");
        print("the entered credentials are:\n");
        for i in range(3):
            print(arr[i]);
        opt=input("would you like to append these to the password file? [Y/n]\nappending>").lower();
        if(opt=="y"):
            with open(filename, 'a') as file:
                file.write(arr[0]+","+arr[1]+","+arr[2]+"\n");
            clear();
            appending=False;
        elif(opt=="n"):
            opt=input("would you like to enter the credentials again? [Y/n]\nappending>").lower();
            if(opt=="y"):
                clear();
            elif(opt=="n"):
                appending=False;
                clear();
            else:
                print("invalid choice\nreturning");
        else:
            print("invalid choice\nreturning")
    return filename;

def remove(filename):
    clear();
    rmentry=input("enter  website/application name to remove entry\nremoving>");
    df=pd.read_csv(filename);
    df.drop(df[df["website/application"]==rmentry].index, inplace=True);
    print(df);
    df.to_csv(filename, index=False);
    input();

def search(filename):
    clear();
    locate=input("enter the website/application name\nsearching>");
    df=pd.read_csv(filename);
    df=df.loc[df["website/application"]==locate];
    print(df);
    input();

def displayall(filename):
    clear()
    df=pd.read_csv(filename);
    print(df);
    input();

def openfile():
    clear();
    filename=input("please enter the file name\nopening>");
    filename="passwd/"+filename+".csv";
    if(os.path.isfile(filename+".gpg")):
        os.system("gpg -d --output "+filename+" --no-symkey-cache "+filename+".gpg");
        fileopen=True;
        while(fileopen):
            clear()
            print(
                "add - appends new password to list\n",
                "list - display all passwords in the list\n",
                "search - shearches for a password based on the website name\n",
                "removes - removes a password based on the website name\n",
                "return - encrypts the file and returns to the main menu"
                );opt=input("file open>").lower();
            if(opt=="add"or opt=="append"or opt=="a"):
                append(filename);
            elif(opt=="list"or opt=="ls"):
                displayall(filename);
            elif(opt=="remove"or opt=="rm"):
                remove(filename);
            elif(opt=="search"):
                search(filename);
            elif(opt=="return"or opt=="q"):
                os.system("rm "+filename+".gpg && gpg -c --no-symkey-cache "+filename);
                os.system("rm "+filename);
                fileopen=False;
    else:
        print("file not found")

print(
        "welcome to my password manager\n",
        "\tWarning!\n",
        "\tDo not use this program for legitimate use!\n",
        "\tI do not know anything about storing passwords safely and there may be majour security holes in this program\n",
        "\tpress enter to continue"
        );
input(">")
while(running):
    clear();
    print(
            "new - creates new password file\n",
            "list - displays all password files\n",
            "open - opens the file so new password entries can be added\n",
            );
    opt=input("main menu>").lower();
    if(opt=="quit"or opt=="q"):
        running=False;
        clear();
    elif(opt=="new"):
        new();
    elif(opt=="list"):
        listall();
    elif(opt=="open"):
        openfile();
    else:
        print("invalid option\ntype \"man\" to print the manual");
