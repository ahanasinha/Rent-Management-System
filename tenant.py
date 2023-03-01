import os
import pickle

def tenant(a):
    os.system('cls')
    print("TENANT")
    fileExist=os.path.exists("tenantMaster.dat")
    if (fileExist==False):
        print("No properties exist.")
        createTenant(a)
    else:
        viewTenant(a)

#tenant creation
def createTenant(a):
    os.system('cls')
    print("CREATE TENANT")
    username=input("Enter username of user: ")
    password=input("Enter password of user: ")
    name=input("Enter the display name: ")
    status=input("Enter the status (Active/ Inactive): ")
    securityQuestion=input("Enter a security question: ")
    securityAnswer=input("Enter a security answer: ")
    remarks=input("Enter remarks: ")

    propertyid=input("Enter property id: ")
    mobile=input("Enter mobile number: ")
    address=input("Enter address: ")
    gender=input("Enter gender: ")
    aadhar=input("Enter aadhar card number: ")
    members=input("Enter number of members: ")
    email=input("Enter email id: ")
    occupation=input("Enter occupation: ")

    #propertyid check
    propertylist=[]
    displayProperty=[]

    with open ("propertyMaster.dat","rb") as f:
        while(True):
            try:
                propertylist.append(pickle.load(f))
            except EOFError:
                break
    
    for i in propertylist:
        if(i["ownerid"]==a):
            displayProperty.append(i["id"])


    if (propertyid in displayProperty):
        propertyCheck=True
    else:
        propertyCheck=False


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
    
    if (duplicate==False and propertyCheck==True):
        #creating user dictionary
        user={
            "username":username,
            "password":password,
            "name":name,
            "category":"Tenant",
            "status":status,
            "securityQuestion":securityQuestion,
            "securityAnswer":securityAnswer,
            "remarks":remarks
        }

        #creating tenant dictionary
        tenant_user={
            "tenantid":username,
            "propertyid":propertyid,
            "name":name,
            "mobile":mobile,
            "address":address,
            "gender":gender,
            "aadhar":aadhar,
            "members":members,
            "email":email,
            "occupation":occupation,
            "remarks":remarks,
            "ownerid":a
        }

        with open ("userMaster.dat","ab+") as f:
            pickle.dump(user,f)

        with open ("tenantMaster.dat","ab+") as g:
            pickle.dump(tenant_user,g)
    
    if (duplicate==True):
        input("Tenant with same username exists. Press any key to continue...")

    if (propertyCheck==False):
        input("The given propertyid does not exist. Press any key to continue...")

#list of tenants
def viewTenant(a):
    os.system('cls')
    print("LIST OF TENANTS")
    tenant=[]
    displayTenant=[]

    with open ("tenantMaster.dat","rb") as f:
        while(True):
            try:
                tenant.append(pickle.load(f))
            except EOFError:
                break
    
    for i in tenant:
        if(i["ownerid"]==a):
            displayTenant.append(i)

    # print("property id","\t","name","\t\t","address","\t","no of rooms","\t","owner id")
    print("{0:<15s}{1:<30s}{2:<30s}{3:>20s}{4:>20s}".format("tenant id","name","address","gender","owner id"))
    print("---------------------------------------------------------------------------------------------------------------------------")
    for i in displayTenant:
        print("{0:<15s}{1:<30s}{2:<30s}{3:>20s}{4:>20s}".format(i["tenantid"],i["name"],i["address"],i["gender"],i["ownerid"]))
        # print(owner["id"],'\t\t',owner["name"],'\t',owner["address"],'\t\t',owner["room"],'\t\t',owner["ownerid"])
    print("---------------------------------------------------------------------------------------------------------------------------")
    tenantDash(a)
    return displayTenant
    
#property dashboard
def tenantDash(a):
    while (True):
        print('''        1. Add tenant
        2. View tenant
        3. Modify tenant
        4. Exit''')
        choice=input("Enter the function you want to perform: ")
        if (choice=='1'):
            createTenant(a)
        if (choice=='2'):
            viewTenant(a)
        if (choice=='3'):
            modifyTenant(a)
        if (choice=='4'):
            break
        elif (choice not in ['1','2','3','4']):
            input("Invalid input...")

#modifying tenant
def modifyTenant(a):
    os.system('cls')
    print("MODIFY TENANT")
    tenantFound=False
    userFound=False
    tenant=[]
    user=[]
    finalTenant=[]
    searchTenant=input("Enter the id of the tenant you want to modify: ")

    with open ("tenantMaster.dat","rb") as f:
        while (True):
            try:
                tenant.append(pickle.load(f))
            except EOFError:
                break

    with open ("userMaster.dat","rb") as f:
        while (True):
            try:
                user.append(pickle.load(f))
            except EOFError:
                break

    for search in tenant:
        if(search["tenantid"]==searchTenant and search["ownerid"]==a):
            tenantFound=True
            tempPropertyid=search["propertyid"]
            tempMobile=search["mobile"]
            tempAddress=search["address"]
            tempGender=search["gender"]
            tempAadhar=search["aadhar"]
            tempMembers=search["members"]
            tempEmail=search["email"]
            tempOccupation=search["occupation"]
            tempOwnerid=search["ownerid"]         

    for search1 in user:
        if(search1["username"]==searchTenant):
            userFound=True
            tempUsername=search1["username"]
            tempPassword=search1["password"]
            tempName=search1["name"]
            tempCategory=search1["category"]
            tempStatus=search1["status"]
            tempSecurityQuestion=search1["securityQuestion"]
            tempSecurityAnswer=search1["securityAnswer"]
            tempRemarks=search1["remarks"]       

    if (userFound==True and tenantFound==True):
        print("Tenant id: ",tempUsername)
        print("Password: ", tempPassword)
        print("Name: ", tempName)
        print("Status: ",tempStatus)
        print("Security Question: ",tempSecurityQuestion)
        print("Security Answer: ", tempSecurityAnswer)
        print("Remarks: ", tempRemarks)
        print("Property id: ", tempPropertyid)
        print("Mobile: ", tempMobile)
        print("Address: ",tempAddress)
        print("Gender: ", tempGender)
        print("Aadhar: ", tempAadhar)
        print("Members: ", tempMembers)
        print("Email: ",tempEmail)
        print("Occupation: ",tempOccupation)
        print("Owner id: ", tempOwnerid)
        choice=input("Press 1 to modify: ")
        if(choice=='1'):
            username=input("Enter username of user: ")
            password=input("Enter password of user: ")
            name=input("Enter the display name: ")
            status=input("Enter the status (Active/ Inactive): ")
            securityQuestion=input("Enter a security question: ")
            securityAnswer=input("Enter a security answer: ")
            remarks=input("Enter remarks: ")
            propertyid=input("Enter property id: ")
            mobile=input("Enter mobile number: ")
            address=input("Enter address: ")
            gender=input("Enter gender: ")
            aadhar=input("Enter aadhar card number: ")
            members=input("Enter number of members: ")
            email=input("Enter email id: ")
            occupation=input("Enter occupation: ")
            if (username==''):
                username=tempUsername
            if (password==''):
                password=tempPassword
            if (name==''):
                name=tempName
            if (status==''):
                status=tempName
            if (securityQuestion==''):
                securityQuestion=tempSecurityQuestion
            if (securityAnswer==''):
                securityAnswer=tempSecurityAnswer
            if (remarks==''):
                remarks=tempRemarks
            if (propertyid==''):
                propertyid=tempPropertyid
            if (mobile==''):
                mobile=tempMobile
            if (address==''):
                address=tempAddress
            if (gender==''):
                gender=tempGender
            if (aadhar==''):
                aadhar=tempAadhar 
            if (members==''):
                members=tempMembers
            if (email==''):
                email=tempEmail                              
            if (occupation==''):
                occupation=tempOccupation

            tenant_user={
                "tenantid":username,
                "propertyid":propertyid,
                "name":name,
                "mobile":mobile,
                "address":address,
                "gender":gender,
                "aadhar":aadhar,
                "members":members,
                "email":email,
                "occupation":occupation,
                "remarks":remarks,
                "ownerid":a
            } 
 
            finalTenant.append(tenant_user)
        else:
            finalTenant.append(tenant_user)

    f=open("tenantMaster.dat","wb")
    for x in finalTenant:
        pickle.dump(x,f)
    f.close()




#show owner details
def ownerDetail(a):
    os.system('cls')
    print("OWNER DETAIL \n\n")
    tenant=[]

    with open ("tenantMaster.dat","rb") as f:
        while(True):
            try:
                tenant.append(pickle.load(f))
            except EOFError:
                break

    for search in tenant:
        if (search["tenantid"]==a):
            ownerid=search["ownerid"]

    owner=[]
    with open ("userMaster.dat","rb") as f:
        while(True):
            try:
                owner.append(pickle.load(f))
            except EOFError:
                break

    for search in owner:
        if (search["username"]==ownerid):
            print("Name: ",search["name"])
            print("Status: ",search["status"])
            input("Press any key to continue...")

#show property details
def propertyDetail(a):
    os.system('cls')
    print("PROPERTY DETAILS \n\n")
    tenant=[]

    with open ("tenantMaster.dat","rb") as f:
        while(True):
            try:
                tenant.append(pickle.load(f))
            except EOFError:
                break

    for search in tenant:
        if (search["tenantid"]==a):
            propertyid=search["propertyid"]
            ownerid=search["ownerid"]

    property=[]
    with open ("propertyMaster.dat","rb") as f:
        while(True):
            try:
                property.append(pickle.load(f))
            except EOFError:
                break

    for search in property:
        if (search["id"]==propertyid and search["ownerid"]==ownerid):
            print("Name: ",search["name"])
            print("Address: ",search["address"])
            print("Room: ",search["room"])
            print("Kitchen: ",search["kitchen"])
            print("Washroom: ",search["washroom"])
            print("Balcony: ",search["balcony"])
            print("Floor: ",search["floor"])
            print("Others: ",search["others"])
            print("Deposit: ",search["deposit"])
            print("Rent: ",search["rent"])
            print("Remarks: ",search["remarks"])
    input("Press any key to continue...")

#show service details
def serviceDetail(a):
    os.system('cls')
    print("SERVICE DETAILS \n\n")
    tenant=[]

    with open ("tenantMaster.dat","rb") as f:
        while(True):
            try:
                tenant.append(pickle.load(f))
            except EOFError:
                break

    for search in tenant:
        if (search["tenantid"]==a):
            propertyid=search["propertyid"]

    service=[]
    with open ("serviceMaster.dat","rb") as f:
        while(True):
            try:
                service.append(pickle.load(f))
            except EOFError:
                break

    for search in service:
        if(search["prop"]==propertyid):
            print("Type: ",search["type"])
            print("Name: ",search["name"])
            print("Phone: ",search["phone"])
            print("Description: ",search["desc"])
            print("Location: ",search["location"])
            print("Remarks: ",search["remarks"])
    input("Enter any key to continue...")