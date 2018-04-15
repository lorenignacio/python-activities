#Exercise No. 4 -   FUNCTION
#Maria Loren I.Ignacio
#github.com/lorenignacio/
#lorenignacio00@gmail.com

print ("Please enter your order :")
def order():
    rice1 = input("1 -Yang Chow\n2 -Fried Rice\n3 -Plain Rice\n   Enter Rice: ")
    maindish2 =input("1 -Hotdog\n2 -Egg\n3 -Hotdog and Egg\n   Enter Main Dish: ")
    if rice1 == 1:
        if maindish2 == 2:
             print ("   Yang Chow with Egg\n")
        elif maindish2 ==3:
            print ("   Yang Chow with Hotdog and Egg\n")
        elif maindish2==1:
             print ("   Yang Chow with Hotdog\n")
        return order()
    elif rice1 ==3:
        if maindish2==1:
             print ("   Plain Rice with Hotdog\n")
        elif maindish2==2:
             print ("   Plain Rice with Egg\n")
        elif maindish2==3:
             print ("   Plain Rice with Hotdog and Egg\n")
        return order()
    elif rice1 ==2:
        if maindish2==2:
             print ("   Fried Rice with Egg\n")
        elif maindish2==3:
             print ("   Fried Rice with Hotdog and Egg\n")
        elif maindish2==1:
             print ("   Fried Rice with Hotdog\n")
        return order()
    
order()
