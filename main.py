
def readEmailFile():
    emailFile = input("Enter the EML file you want to parse: \n")
    with open(emailFile) as file:
        global EmailContents
        EmailContents = file.readlines()
        EmailStringSearch("", "")

    #print("Stuff: \n" + str(lines))

def EmailStringSearch(searchKeyword, msg):
    for i in EmailContents:
        if searchKeyword in i:
            print(msg)
            exit()

readEmailFile()