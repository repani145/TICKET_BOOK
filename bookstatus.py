import openpyxl

def status():
    print("#############    TICKET BOOKING STATUS ENQUIRY   #############")
    a=int(input('enter your ticket number :'))
    mo=openpyxl.load_workbook(r"C:\\Users\\dell\\PycharmProjects\\TICKETBOOKINGG\\TRICKET_BOOK.xlsx")
    list=mo.get_sheet_names()
    a1=mo[list[1]]
    c=0
    for i in a1:
        for j in i:
            pass
        c+=1
    if a<c:
        if a1.cell(a+1,8).value==1:
            print('#############     STATUS :YOUR TICKET BOOKED SUCCESSFULLY    ###############')
        else:
            print("############     STATUS : YOUR BOOKING IS GOT FAILED  ################")
    else:
        print("###########      STATUS :YOUR TICKET NOT FOUND    ##############")

    print("\n")

    #print("##########################################################################################################")