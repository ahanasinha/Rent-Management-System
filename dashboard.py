import authentication
import os
import property
import tenant
import pickle

def adminDash(a):
    while (True):
        os.system('cls')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("RENT MANAGEMENT SYSTEM (RMS)".center(60))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        print("ADMIN DASHBOARD !!".center(60," "))
        print('''        1. Create User
        2. List User
        3. Modify User
        4. Reset password
        5. Exit Program''')
        choice=input("Enter the choice number you want to perform: ")
        if (choice=='1'):
            authentication.createUser()
        if (choice=='2'):
            authentication.listUser()
        if (choice=='3'):
            authentication.modifyUser()
        if (choice=='4'):
            authentication.resetPassword()
        if (choice=='5'):
            return
        if (choice not in ['1','2','3','4','5']):
            input("Invalid input...")

def ownerDash(a):
    while (True):
        os.system('cls')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("RENT MANAGEMENT SYSTEM (RMS)".center(60))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        print("WELCOME OWNER !!".center(60," "))
        print('''        1. Property
        2. Tenant
        3. Service
        4. Change password
        5. Exit Program''')
        choice=int(input("Enter the choice number you want to perform: "))
        if (choice==1):
            property.property(a)
        if (choice==2):
            tenant.tenant(a)
        if (choice==3):
            property.service(a)
        if (choice==4):
            authentication.passwordChange(a)
        if (choice==5):
            return
        if (choice not in [1,2,3,4,5]):
            input("Invalid input...")

def tenantDash(a):
    while (True):
        os.system('cls')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("RENT MANAGEMENT SYSTEM (RMS)".center(60))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        print("WELCOME TENANT !!".center(60," "))
        print('''        1. Owner details
        2. Property details
        3. Service details
        4. Change password
        5. Exit Program''')
        choice=int(input("Enter the choice number you want to perform: "))
        if (choice==1):
            tenant.ownerDetail(a)
        if (choice==2):
            tenant.propertyDetail(a)
        if (choice==3):
            tenant.serviceDetail(a)
        if (choice==4):
            authentication.passwordChange(a)
        if (choice==5):
            return
        if (choice not in [1,2,3,4,5]):
            input("Invalid input...")