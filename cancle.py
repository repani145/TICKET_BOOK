import openpyxl

def cancle():
    print('############## TICKET CANCELLATION ##############')
    a=int(input('enter TICKET NUMBER to cancle :'))
    mo=openpyxl.load_workbook(r"C:\\Users\\dell\\PycharmProjects\\TICKETBOOKINGG\\TRICKET_BOOK.xlsx")
    list=mo.get_sheet_names()
    a1=mo[list[1]]
    c=0
    for i in a1:
        for j in i:
            pass
        c+=1

    if a<c:
        a1.cell(a+1,8).value=0
        mo.save(r"C:\\Users\\dell\\PycharmProjects\\TICKETBOOKINGG\\TRICKET_BOOK.xlsx")
        print('#################  YOUR TICKET IS CANCELLED SUCCESSFULLY   ################')
        print()

    else:
        print('##################### ENTERED TICKET NUMBER NOT FOUND  #####################')
        print()