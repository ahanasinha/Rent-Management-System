import authentication as auth
import dashboard as dash
import os

auth.firstRun()

while (True):
    os.system('cls')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("RENT MANAGEMENT SYSTEM (RMS)".center(60))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    print("LOGIN".center(60," "))
    usernamelogin=input("Enter your Username: ")
    passwordlogin=input("Enter your Password: ")
    return_value=auth.login(usernamelogin,passwordlogin)

    if(return_value==1):
        dash.adminDash(usernamelogin)
        break
    if(return_value==2):
        dash.ownerDash(usernamelogin)
        break
    if(return_value==3):
        dash.tenantDash(usernamelogin)
        break
    if(return_value==0):
        choice=input("\nIncorrect username / password... \nPress x to exit: ")
        if(choice=='x' or choice=="X"):
            break
    if(return_value==10):
        choice=input("Account is inactive... \nPress x to exit: ")
        if(choice=='x' or choice=="X"):
            break

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("\n\nTHANK YOU".center(60))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
