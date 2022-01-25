print("licznik    suma")
print("** O **  ** O **")
print("-----------------")
for i in range(11):
    if -4*i<0 and -4*i>-10:
        print("**",i,"**| *",i*-4,"**")
    elif -4*i<=-10 and i<10: 
        print("**",i,"**| *",i*-4,"*")
    elif i >= 10: 
        print("*",i,"**| *",i*-4,"*")
    else:
        print("**",i,"**| **",i*-4,"**")