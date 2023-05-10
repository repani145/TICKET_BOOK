import openpyxl
def list_of_tickets():
    print("########### PASSENGERS LIST ###############")
    mo=openpyxl.load_workbook(r"C:\\Users\\dell\\PycharmProjects\\TICKETBOOKINGG\\TRICKET_BOOK.xlsx")
    list=mo.get_sheet_names()
    a1=mo[list[1]]

    for i in a1:
        for j in i:
            print(j.value,end=" , ")
        print()
    print("#########################################################################################################")