#   ..............     ...........      ...........       ...      .....        ...............      .................
#   ##############     ###########      ###########      .###      #####        .##############.     #################
#       .###.             .###.        .###.             .###   ###             .###                      .####.
#       .###.             .###.        .###.             .######                .##############.          .####.
#       .###.             .###.        .###.             .######.               .##############.          .####.
#       .###.             .###.        .###.             .###   ###.            .###                      .####.
#       .###.          ##########       ############     .###      #######.     .##############.          .####.
                                                                              



from ticketbook import ticket_booking
from view_tickets import list_of_tickets
from bookstatus import status
from update import update
from cancle import cancle

while True:
    print()
    print("(1) TICKET BOOKING")
    print("(2) VIEW BOOKED TICKETS")
    print("(3) TICKET BOOKING STATUS")
    print("(4) UPDATE PASSENGER DETAILS")
    print("(5) CANCLE TICKET")
    print("(6) LOGOUT")

    i=int(input("SELECT ONE REQUIRED OPTION FROM ABOVE :"))
    if i==1:
        ticket_booking()
    elif i==2:
        list_of_tickets()
    elif i==3:
        status()
    elif i==4:
        update()
    elif i==5:
        cancle()
    elif i==6:
        print("########################### LOGOUT SUCCESSFULLY ##############################")
        break
    else:
        print("######### WRONG INPUT ENTERED  #######")
        print()
