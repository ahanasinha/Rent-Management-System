import os
import pickle

#property
def property(a):
    os.system('cls')
    print("PROPERTY")
    fileExist=os.path.exists("propertyMaster.dat")
    if (fileExist==False):
        print("No properties exist.")
        addProperty(a)
    else:
        viewProperty(a)
    
#property dashboard
def propertyDash(a):
    while (True):
        print('''        1. Add property
        2. View Property
        3. Modify property
        4. Exit''')
        choice=input("Enter the function you want to perform: ")
        if (choice=='1'):
            addProperty(a)
        if (choice=='2'):
            viewProperty(a)
        if (choice=='3'):
            modifyProperty(a)
        if (choice=='4'):
            break
        if (choice not in ['1','2','3','4']):
            input("Invalid input...")

#add property
def addProperty(a):
    os.system('cls')
    print("ADD PROPERTY")
    p_id=input("Enter property id: ")
    p_name=input("Enter property name: ")
    p_add=input("Enter property address: ")
    p_room=int(input("Enter numbers of rooms: "))
    p_kitchen=int(input("Enter numbers of kitchens: "))
    p_wash=int(input("Enter numbers of washrooms: "))
    p_balcony=int(input("Enter numbers of balconies: "))
    p_floor=int(input("Enter floor number: "))
    p_others=input("Enter any other information: ")
    p_deposit=int(input("Enter deposit amount: "))
    p_rent=int(input("Enter rent amount: "))
    p_remarks=input("Enter remarks: ")
    p_ownerid=a

    property={
        "id":p_id,
        "name":p_name,
        "address":p_add,
        "room":p_room,
        "kitchen":p_kitchen,
        "washroom":p_wash,
        "balcony":p_balcony,
        "floor":p_floor,
        "others":p_others,
        "deposit":p_deposit,
        "rent":p_rent,
        "remarks":p_remarks,
        "ownerid":p_ownerid
    }

    with open ("propertyMaster.dat","ab") as f:
        pickle.dump(property,f)

#view property
def viewProperty(a):
    os.system('cls')
    print("LIST OF PROPERTIES")
    property=[]
    displayProperty=[]

    with open ("propertyMaster.dat","rb") as f:
        while(True):
            try:
                property.append(pickle.load(f))
            except EOFError:
                break
    
    for i in property:
        if(i["ownerid"]==a):
            displayProperty.append(i)

    print("{0:<15s}{1:<30s}{2:<30s}{3:>20s}{4:>20s}".format("property id","name","address","no of rooms","owner id"))
    print("---------------------------------------------------------------------------------------------------------------------------")
    for owner in displayProperty:
        print("{0:<15s}{1:<30s}{2:<30s}{3:>20d}{4:>20s}".format(owner["id"],owner["name"],owner["address"],owner["room"],owner["ownerid"]))
    print("---------------------------------------------------------------------------------------------------------------------------")
    propertyDash(a)
    return displayProperty

#modify property
def modifyProperty(a):
    os.system('cls')
    print("MODIFY PROPERTY")
    recordFound=False
    property=[]
    finalProperty=[]
    searchProperty=input("Enter the id of the property you want to modify: ")

    with open ("propertyMaster.dat","rb") as f:
        while (True):
            try:
                property.append(pickle.load(f))
            except EOFError:
                break

    for search in property:
        if(search["id"]==searchProperty and search["ownerid"]==a):
            recordFound=True
            tempPropertyid=search["id"]
            tempName=search["name"]
            tempAddress=search["address"]
            tempRoom=search["room"]
            tempKitchen=search["kitchen"]
            tempWashroom=search["washroom"]
            tempBalcony=search["balcony"]
            tempFloor=search["floor"]
            tempOthers=search["others"]
            tempDeposit=search["deposit"]
            tempRent=search["rent"]
            tempRemarks=search["remarks"]
            tempOwnerid=search["ownerid"]
            print("Property id: ",tempPropertyid)
            print("Name: ",tempName)
            print("Address: ",tempAddress)
            print("Room: ",tempRoom)
            print("Kitchen: ",tempKitchen)
            print("Washroom: ",tempWashroom)
            print("Balcony: ",tempBalcony)
            print("Floor: ",tempFloor)
            print("Others: ",tempOthers)
            print("Deposit: ",tempDeposit)
            print("Rent: ",tempRent)
            print("Remarks: ",tempRemarks)
            print("Owner id: ",tempOwnerid)
            choice=input("Press 1 to modify: ")
            if(choice=='1'):
                name=input("Enter property name: ")
                address=input("Enter property address: ")
                room=input("Enter numbers of rooms: ")
                kitchen=input("Enter numbers of kitchens: ")
                washroom=input("Enter numbers of washrooms: ")
                balcony=input("Enter numbers of balconies: ")
                floor=input("Enter floor number: ")
                others=input("Enter any other information: ")
                deposit=input("Enter deposit amount: ")
                rent=input("Enter rent amount: ")
                remarks=input("Enter remarks: ")
                if (name==''):
                    name=tempName
                if (address==''):
                    address=tempAddress
                if (room==''):
                    room=tempRoom
                if (kitchen==''):
                    kitchen=tempKitchen
                if (washroom==''):
                    washroom=tempWashroom
                if (balcony==''):
                    balcony=tempBalcony
                if (floor==''):
                    floor=tempFloor
                if (others==''):
                    others=tempOthers
                if (deposit==''):
                    deposit=tempDeposit
                if (rent==''):
                    rent=tempRent
                if (remarks==''):
                    remarks=tempRemarks
                property1={
                    "id":tempPropertyid,
                    "name":name,
                    "address":address,
                    "room":room,
                    "kitchen":kitchen,
                    "washroom":washroom,
                    "balcony":balcony,
                    "floor":floor,
                    "others":others,
                    "deposit":deposit,
                    "rent":rent,
                    "remarks":remarks,
                    "ownerid":tempOwnerid
                }
                finalProperty.append(property1)
            else:
                finalProperty.append(search)
        else:
            finalProperty.append(search)

    f=open("propertyMaster.dat","wb")
    for x in finalProperty:
        pickle.dump(x,f)
    f.close()

    if (recordFound==False):
        input("Record not found.")

#service
def service(a):
    os.system('cls')
    print("SERVICE")
    fileExist=os.path.exists("serviceMaster.dat")
    if (fileExist==False):
        print("No properties exist.")
        addService(a)
    else:
        viewService(a)

#service dashboard
def serviceDash(a):
    while (True):
        print('''        1. Add Service
        2. View Service
        3. Modify Service
        4. Exit''')
        choice=input("Enter the function you want to perform: ")
        if (choice=='1'):
            addService(a)
        if (choice=='2'):
            viewService(a)
        if (choice=='3'):
            modifyService(a)
        if (choice=='4'):
            break
        if (choice not in ['1','2','3','4']):
            input("Invalid input...")

#create service
def addService(a):
    os.system('cls')
    print("ADD SERVICE")
    s_id=input("Enter service id: ")
    s_type=input("Enter type of service: ")
    s_name=input("Enter name of service person: ")
    s_phone=input("Enter phone number of service person: ")
    s_desc=input("Enter service description: ")
    s_prop=input("Enter property id: ")
    s_location=input("Enter service location: ")
    s_remarks=input("Enter remarks: ")
    s_ownerid=a

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


    if (s_prop in displayProperty):
        propertyCheck=True
    else:
        propertyCheck=False

    #service id duplicacy check
    userid=[]
    duplicate=False
    with open ("serviceMaster.dat","rb") as f:
        while (True):
            try:
                userid.append(pickle.load(f))
            except EOFError:
                break
    for search in userid:
        if (search["username"]==s_id):
            duplicate=True

    if(propertyCheck==True):
        service={
            "id":s_id,
            "type":s_type,
            "name":s_name,
            "phone":s_phone,
            "desc":s_desc,
            "prop":s_prop,
            "location":s_location,
            "remarks":s_remarks,
            "ownerid":s_ownerid
        }

        with open ("serviceMaster.dat","ab+") as f:
            pickle.dump(service,f)

    if (duplicate==True):
        input("Service with same username exists. Press any key to continue...")

    if (propertyCheck==False):
        input("The given propertyid does not exist. Press any key to continue...")

#view services
def viewService(a):
    os.system('cls')
    print("LIST OF SERVICES")
    service=[]
    displayService=[]

    with open ("serviceMaster.dat","rb") as f:
        while(True):
            try:
                service.append(pickle.load(f))
            except EOFError:
                break
    
    for i in service:
        if(i["ownerid"]==a):
            displayService.append(i)

    print("{0:<15s}{1:<30s}{2:<30s}{3:>20s}{4:>20s}".format("service id","name","address","type","owner id"))
    print("---------------------------------------------------------------------------------------------------------------------------")
    for owner in displayService:
        print("{0:<15s}{1:<30s}{2:<30s}{3:>20s}{4:>20s}".format(owner["id"],owner["name"],owner["location"],owner["type"],owner["ownerid"]))
    print("---------------------------------------------------------------------------------------------------------------------------")
    serviceDash(a)
    return displayService

#modify services
def modifyService(a):
    os.system('cls')
    print("MODIFY SERVICES")
    recordFound=False
    service=[]
    finalService=[]
    searchService=input("Enter the id of the property you want to modify: ")

    with open ("serviceMaster.dat","rb") as f:
        while (True):
            try:
                service.append(pickle.load(f))
            except EOFError:
                break

    for search in service:
        if(search["id"]==searchService and search["ownerid"]==a):
            recordFound=True
            tempServiceid=search["id"]
            tempType=search["type"]
            tempName=search["name"]
            tempPhone=search["phone"]
            tempDesc=search["desc"]
            tempProp=search["prop"]
            tempLocation=search["location"]
            tempRemarks=search["remarks"]
            tempOwnerid=search["ownerid"]
            print("Service id: ",tempServiceid)
            print("Type: ",tempType)
            print("Name: ",tempName)
            print("Phone: ",tempPhone)
            print("Description: ",tempDesc)
            print("Property id: ",tempProp)
            print("Location: ",tempLocation)
            print("Remarks: ",tempRemarks)
            print("Owner id: ",tempOwnerid)
            choice=input("Press 1 to modify: ")
            if(choice=='1'):
                type=input("Enter type of service: ")
                name=input("Enter name of service person: ")
                phone=input("Enter phone number of service person: ")
                desc=input("Enter service description: ")
                prop=input("Enter property id: ")
                location=input("Enter service location: ")
                remarks=input("Enter remarks: ")
                if (type==''):
                    type=tempType
                if (name==''):
                    name=tempName
                if (phone==''):
                    phone=tempPhone
                if (desc==''):
                    desc=tempDesc
                if (prop==''):
                    prop=tempProp
                if (location==''):
                    location=tempLocation
                if (remarks==''):
                    remarks=tempRemarks
                service1={
                    "id":tempServiceid,
                    "type":type,
                    "name":name,
                    "phone":phone,
                    "desc":desc,
                    "prop":prop,
                    "location":location,
                    "remarks":remarks,
                    "ownerid":tempOwnerid
                }
                finalService.append(service1)
            else:
                finalService.append(search)
        else:
            finalService.append(search)

    f=open("serviceMaster.dat","wb")
    for x in finalService:
        pickle.dump(x,f)
    f.close()

    if (recordFound==False):
        input("Record not found.")
