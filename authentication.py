import os
import pickle
import dashboard

#first run
def firstRun():
    user={
        "username":"admin01",
        "password":"ahana",
        "name":"Ahana Sinha",
        "category":"Admin",
        "status":"Active",
        "securityQuestion":"",
        "securityAnswer":"",
        "remarks":""
    }
    fileExist=os.path.exists("userMaster.dat")
    if (fileExist==False):
        with open ("userMaster.dat","wb") as f:
            pickle.dump(user,f)

#authentication
def login(usernamelogin,passwordlogin):
    return_value=0
    user=[]
    with open ("userMaster.dat","rb") as f:
        while (True):
            try:
                user.append(pickle.load(f))
            except EOFError:
                break
    
    for user1 in user:
        if (user1["username"]==usernamelogin and user1["password"]==passwordlogin):
            if (user1["status"]=='Inactive'):
                return_value=10
            else: 
                if (user1["category"]=="Admin"):
                    return_value=1
                    break
                if (user1["category"]=="Owner"):
                    return_value=2
                    break
                if (user1["category"]=="Tenant"):
                    return_value=3
                    break
    return return_value

#user creation
def createUser():
    os.system('cls')
    print()
    print("CREATE USER")
    username=input("Enter username of user: ")
    password=input("Enter password of user: ")
    name=input("Enter the display name: ")
    category=input("Enter the category (Owner/ Admin): ")
    status=input("Enter the status (Active/ Inactive): ")
    securityQuestion=input("Enter a security question: ")
    securityAnswer=input("Enter a security answer: ")
    remarks=input("Enter remarks: ")

    #username duplicacy check
    userid=[]
    duplicate=False
    with open ("userMaster.dat","rb") as f:
        while (True):
            try:
                userid.append(pickle.load(f))
            except EOFError:
                break
    for search in userid:
        if (search["username"]==username):
            duplicate=True
            input("Username already taken. Press any key to continue...")
            
    #creating dictionary
    if (duplicate==False):
        user={
            "username":username,
            "password":password,
            "name":name,
            "category":category,
            "status":status,
            "securityQuestion":securityQuestion,
            "securityAnswer":securityAnswer,
            "remarks":remarks
        }
        with open("userMaster.dat","ab+") as g:
            pickle.dump(user,g)
        f.close()
    
#user viewing
def listUser():
    os.system('cls')
    print("LIST OF USERS ")

    user=[]
    with(open('userMaster.dat','rb')) as f:
        while (True):
            try:
                user.append(pickle.load(f))
            except EOFError:
                break

    print("{0:<15s}{1:<30s}{2:<30s}{3:<20s}".format("username","name","category","status"))
    print("----------------------------------------------------------------------------------------------------------")
    for user1 in user:
        print("{0:<15s}{1:<30s}{2:<30s}{3:<20s}".format(user1["username"],user1["name"],user1["category"],user1["status"]))
    print("----------------------------------------------------------------------------------------------------------")
    input("Enter any key to continue...")

#user modifying
def modifyUser():
    os.system('cls')
    print("MODIFY USER")
    recordFound=False
    user=[]
    finalUser=[]
    searchUsername=input("Enter the username whose information you want to modify: ")

    with open ("userMaster.dat","rb") as f:
        while (True):
            try:
                user.append(pickle.load(f))
            except EOFError:
                break

    for search in user:
        if(search["username"]==searchUsername):
            recordFound=True
            tempUsername=search["username"]
            tempPassword=search["password"]
            tempName=search["name"]
            tempCategory=search["category"]
            tempStatus=search["status"]
            tempSecurityQuestion=search["securityQuestion"]
            tempSecurityAnswer=search["securityAnswer"]
            tempRemarks=search["remarks"]
            print("Password: ",tempPassword)
            print("Name: ",tempName)
            print("Status: ",tempStatus)
            print("Security question: ",tempSecurityQuestion)
            print("Security answer: ",tempSecurityAnswer)
            print("Remarks: ",tempRemarks)
            choice=input("Press 1 to modify: ")
            if(choice=='1'):
                password=input("Enter password of user: ")
                name=input("Enter the display name: ")
                status=input("Enter the status (Active/ Inactive): ")
                securityQuestion=input("Enter a security question: ")
                securityAnswer=input("Enter a security answer: ")
                remarks=input("Enter remarks: ")
                if (password==''):
                    password=tempPassword
                if (name==''):
                    name=tempName
                if (status==''):
                    status=tempStatus
                if (securityQuestion==''):
                    securityQuestion=tempSecurityQuestion
                if (securityAnswer==''):
                    securityAnswer=tempSecurityAnswer
                if (remarks==''):
                    remarks=tempRemarks
                user1={
                    "username":tempUsername,
                    "password":password,
                    "name":name,
                    "category":tempCategory,
                    "status":status,
                    "securityQuestion":securityQuestion,
                    "securityAnswer":securityAnswer,
                    "remarks":remarks
                }
                finalUser.append(user1)
            else:
                finalUser.append(search)
        else:
            finalUser.append(search)

    f=open("userMaster.dat","wb")
    for x in finalUser:
        pickle.dump(x,f)
    f.close()

    if (recordFound==False):
        input("Record not found.")

#reset password
def resetPassword():
    os.system('cls')
    print("RESET PASSWORD")
    user=[]
    recordFound=False
    searchUsername=input("Enter the username whose password you want to reset: ")
    count=0

    with open ("userMaster.dat","rb") as f:
        while (True):
            try:
                user.append(pickle.load(f))
            except EOFError:
                break

    for i,search in enumerate(user):
        if (searchUsername==search["username"]):
            recordFound=True
            count=i
            tempUsername=search["username"]
            tempPassword="password"
            tempName=search["name"]
            tempCategory=search["category"]
            tempStatus=search["status"]
            tempSecurityQuestion=search["securityQuestion"]
            tempSecurityAnswer=search["securityAnswer"]
            tempRemarks=search["remarks"]
            user1={
            "username":tempUsername,
            "password":tempPassword,
            "name":tempName,
            "category":tempCategory,
            "status":tempStatus,
            "securityQuestion":tempSecurityQuestion,
            "securityAnswer":tempSecurityAnswer,
            "remarks":tempRemarks
            }
            user[count]=user1

    with open ("userMaster.dat","wb") as f:
        for i in user:
            pickle.dump(i,f)

    if (recordFound==False):
        input("Username doesn't exist...")
    
#password changing
def passwordChange(a):
    os.system('cls')
    print("CHANGE PASSWORD")
    user=[]

    with open ("userMaster.dat","rb") as f:
        while (True):
            try:
                user.append(pickle.load(f))
            except EOFError:
                break
    
    for i,search in enumerate(user):
        if (a==search["username"]):
            count=i
            tempUsername=search["username"]
            tempPassword=search["password"]
            tempName=search["name"]
            tempCategory=search["category"]
            tempStatus=search["status"]
            tempSecurityQuestion=search["securityQuestion"]
            tempSecurityAnswer=search["securityAnswer"]
            tempRemarks=search["remarks"]
            
            print("Old password: ",tempPassword)
            newPassword=input("Enter new password: ")

            user1={
            "username":tempUsername,
            "password":newPassword,
            "name":tempName,
            "category":tempCategory,
            "status":tempStatus,
            "securityQuestion":tempSecurityQuestion,
            "securityAnswer":tempSecurityAnswer,
            "remarks":tempRemarks
            }
            user[count]=user1

    with open ("userMaster.dat","wb") as f:
        for i in user:
            pickle.dump(i,f)
