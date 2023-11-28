"""
Author:     Caleb R.
Date:       11/26/2023
Purpose:    Create a program that offers the user choices: to find the total length of a path OR assist in setting up an integral to find the length of a path.
"""
#Call the right libraries
import scipy as sp #import scipy as sp
import sympy as smp #import sympy as smp

#Initialize some variables
user_choice = "Initial Value"

#Welcome message and planned process / results we're striving for.
print("\nThis program is meant to find the length of a given path based on a starting and end point.\n"
       "You can also have assistance in setting up your own integral to find the length of a path or \n"
       "seeing where information was taken to create this program.\n")
#I could include an option that asks the user iof they would like to change the areas for which we are finding the path length.

#Set a while loop so that the user can choose to stop using the system
while user_choice != "4":
    user_choice = input("Which would you like to do?\n\t1.) Find the length of a path\n\t2.) Receive step-by-step help on how to set up an integral to find the length of a path\
                        \n\t3.) Research Materials and Sources\n\t4.) Quit the program\n\t")
    #The first optino: find the total length of a path
    if user_choice == "1":
        #Solves an integral that is ... "simple"
        print("\nPlease note that this program is only able to help integrate functions that include powers, square roots, and trig functions.")
        redo = "Initial Value"
        num_variables = 0
        while redo != "No" or redo !="N":
            print()
            a,b,f,g,t = smp.symbols("a,b,f,g,t", real=True)
            a = input("What is the lower bound for the path? ")
            b = input("What is the upper bound for the path? ")
            x,y,f,g,c,d = smp.symbols("x,y,f,g,c,d", real=True)
            #Find out what c and d are
            oper_c = smp.symbols("blank", real=True)
            oper_d = smp.symbols("blank", real=True)
            difficult = input("\nDoes the 'dx/dt' have a trig function or power (Y/N)? ").title()
            if difficult == "Y":
                num_trig = int(input("How many trig functions does the 'dx/dt' have (up to 1)? "))
                num_pow = int(input("How many power functions does the 'dx/dt' have (up to 1)? "))
                #Possible 0,1; 1,0; 1,1;
                if num_trig == 0 and num_pow == 1:
                    fraction = input("\nIs the power a fraction with something besides 1 in the denominator (Y/N)? ").capitalize()
                    if fraction == "Y":
                        t,b = smp.symbols("t,b", real=True)
                        t = input("\nWhat is the numerator of the fraction? ")
                        b = input("What is the denomator of the fraction? ")
                        frac_power = smp.Rational(t,b)
                        x = smp.symbols("x", real=True)
                        oper_c = x**frac_power
                    elif fraction == "N":
                        a,x = smp.symbols("a,x", real=True)
                        a = int(input("What is the power? "))
                        oper_c = x**a
                    else:
                        print("\nIncorrect input, please try again.\n")
                        user_choice == "4"
                elif num_trig == 1 and num_pow == 0:
                    which_trig = input("\nWhich trig function is present (Sin, Cos, Tan, Sec, Csc, Cot)? ").title()
                    print()
                    if which_trig == "Sin":
                        print()
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the sin()? ")
                        oper_c = smp.sin(y)
                    elif which_trig == "Cos":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the cos()? ")
                        oper_c = smp.cos(y)
                    elif which_trig == "Tan":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the tan()? ")
                        oper_c = smp.tan(y)
                    elif which_trig == "Csc":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the csc()? ")
                        oper_c = smp.csc(y)
                    elif which_trig == "Sec":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the sec()? ")
                        oper_c = smp.sec(y)
                    elif which_trig == "Cot":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the cot()? ")
                        oper_c = smp.cot(y)
                    else:
                        print("\nIncorrect input, please try again.\n")
                        user_choice == "4"

                elif num_trig == 1 and num_pow == 1:
                    print("This process is still being developed. I am sorry for the inconvenience. Please try another function.")
                    user_choice == "4"
                else:
                    print("\nIncorrect input, please try again.\n")
                    user_choice == "4"
                print()

                #This will ahve to be included for every potential option in the trig and power functions.
            elif difficult == "N":
                operation = input("\nWould you like to:\n1.) add\n2.) subtract\n3.) multiple\n4.) divide?\n")
                print()
                if operation == "1":
                    oper_a = smp.symbols(input("What is the first thing that you would like to add? "), real=True)
                    oper_b = smp.symbols(input("What is the second thing that you would like to add? "), real=True)
                    oper_c = oper_a + oper_b
                elif operation == "2":
                    oper_a = smp.symbols(input("What is the first thing that you would like to subtract? "), real=True)
                    oper_b = smp.symbols(input("What is the second thing that you would like to subtract? "), real=True)
                    oper_c = oper_a - oper_b
                elif operation == "3":
                    oper_a = smp.symbols(input("What is the first thing that you would like to multiple? "), real=True)
                    oper_b = smp.symbols(input("What is the second thing that you would like to multiple? "), real=True)
                    oper_c = oper_a * oper_b
                elif operation == "4":
                    oper_a = smp.symbols(input("What is the first thing that you would like to divide? "), real=True)
                    oper_b = smp.symbols(input("What is the second thing that you would like to divide? "), real=True)
                    oper_c = oper_a / oper_b
                else:
                    print("\nIncorrect input, please try again.\n")
                    user_choice == "4"
            else:
                print("\nIncorrect input, please try again.\n")
                user_choice == "4"
            c = oper_c #Additional help and time is needed to complete this portion

            difficult = input("\nDoes the 'dy/dt' have a trig function or power (Y/N)? ").title()
            if difficult == "Y":
                num_trig = int(input("How many trig functions does the 'dy/dt' have (up to 1)? "))
                num_pow = int(input("How many power functions does the 'dy/dt' have (up to 1)? "))
                #Possible 0,1; 1,0; 1,1;
                if num_trig == 0 and num_pow == 1:
                    fraction = input("\nIs the power a fraction with something besides 1 in the denominator (Y/N)? ").capitalize()
                    if fraction == "Y":
                        t,b = smp.symbols("t,b", real=True)
                        t = input("\nWhat is the numerator of the fraction? ")
                        b = input("What is the denomator of the fraction? ")
                        frac_power = smp.Rational(t,b)
                        x = smp.symbols("y", real=True)
                        oper_d = x**frac_power
                    elif fraction == "N":
                        a,y = smp.symbols("a,y", real=True)
                        a = int(input("What is the power? "))
                        oper_d = y**a
                    else:
                        print("\nIncorrect input, please try again.\n")
                        user_choice == "4"

                elif num_trig == 1 and num_pow == 0:
                    which_trig = input("\nWhich trig function is present (Sin, Cos, Tan, Sec, Csc, Cot)? ").title()
                    print()
                    if which_trig == "Sin":
                        print()
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the sin()? ")
                        oper_d = smp.sin(y)
                    elif which_trig == "Cos":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the cos()? ")
                        oper_d = smp.cos(y)
                    elif which_trig == "Tan":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the tan()? ")
                        oper_d = smp.tan(y)
                    elif which_trig == "Csc":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the csc()? ")
                        oper_d = smp.csc(y)
                    elif which_trig == "Sec":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the sec()? ")
                        oper_d = smp.sec(y)
                    elif which_trig == "Cot":
                        y = smp.symbols("y", real=True)
                        y = input("What is the function within the cot()? ")
                        oper_d = smp.cot(y)
                    else:
                        print("\nIncorrect input, please try again.\n")
                        user_choice == "4"

                elif num_trig == 1 and num_pow == 1:
                    print("This process is still being developed. I am sorry for the inconvenience. Please try another function.")
                    user_choice == "4"
                else:
                    print("\nIncorrect input, please try again.\n")
                    user_choice == "4"
                print()

                #This will ahve to be included for every potential option in the trig and power functions.
            elif difficult == "N":
                operation = input("\nWould you like to:\n1.) add\n2.) subtract\n3.) multiple\n4.) divide?\n")
                print()
                if operation == "1":
                    oper_a = smp.symbols(input("What is the first thing that you would like to add? "), real=True)
                    oper_b = smp.symbols(input("What is the second thing that you would like to add? "), real=True)
                    oper_d = oper_a + oper_b
                elif operation == "2":
                    oper_a = smp.symbols(input("What is the first thing that you would like to subtract? "), real=True)
                    oper_b = smp.symbols(input("What is the second thing that you would like to subtract? "), real=True)
                    oper_d = oper_a - oper_b
                elif operation == "3":
                    oper_a = smp.symbols(input("What is the first thing that you would like to multiple? "), real=True)
                    oper_b = smp.symbols(input("What is the second thing that you would like to multiple? "), real=True)
                    oper_d = oper_a * oper_b
                elif operation == "4":
                    oper_a = smp.symbols(input("What is the first thing that you would like to divide? "), real=True)
                    oper_b = smp.symbols(input("What is the second thing that you would like to divide? "), real=True)
                    oper_d = oper_a / oper_b
                else:
                    print("\nIncorrect input, please try again.\n")
                    user_choice == "4"
            else:
                print("\nIncorrect input, please try again.\n")
                user_choice == "4"
            d = oper_d #Additional help and time is needed to complete this portion
            f = (c)**2
            g = (d)**2
            print("\nThis is what the integral would look like:")
            smp.pprint(smp.Integral(smp.sqrt(f+g),(t,a,b)), use_unicode=True)
            #Integrate
            print("This is the solution to the integral:")
            smp.pprint(smp.integrate(smp.sqrt(f+g),(t,a,b)).simplify())
            redo = input("\nWould you like to find the length of another integral? (Y/N)").title()
            print()

    #The second optino: receive step-by-step help on setting up an integral to find the path of a given length
    elif user_choice == "2":
        print("\nFirst, the length of a path relying on 3 variables is as follows:\n")
        a,b,f,g,t = smp.symbols("a,b,f,g,t", real=True)
        c = smp.symbols("dx")
        d = smp.symbols("dy")
        e = smp.symbols("dt")
        f = (c/e)**2
        g = (d/e)**2
        smp.pprint(smp.Integral(smp.sqrt(f+g),(t,a,b)), use_unicode=True)
        print("\n\tThis path has the variables x, y, and t. We'll be using these variables and their")
        print("differentials to set up the integral. It's perfectly fine to be somewhat freaked out")
        print("with the lingo. Take a deep breath, we'll get through this together.")
        print("\n\tTo start, let's focus on the bounds of the integral. 'a' is where the path begins")
        print("and 'b' is where it will end. If we're given that 't' must be greater than or equal to 1")
        print("and less than or equal to 5 (1 <= t <= 5). 1 would be the lower bound of the integral and")
        print("5 would be our upper bound. So go ahead and find the bouds for your specific problem and")
        print("put them on the integral.")
        print("\n\tAlright, now that that's out of the way, we'll start looking at the differentials")
        print("in the integral. Those are the 'dx/dt' and 'dy/dt' parts of the problem. 'dx/dt' is the")
        print("change in 'x' in respect to the change in 't'. In other words, what happens to 'x' as 't' gets")
        print("bigger or smaller. To find 'dx/dt', take the derivative of 'x' based on the path, this gets")
        print("us 'dx'.")
        print("\n\tTo get 'dx/dt', 'dx' sould be found in respect to 'dt'. This means, that we substitute")
        print("'t' for 'x'. But be careful, this doesn't mean that 't' = 'x'. Rather that we use what the")
        print("the path told us 'x' was in terms of 't'. If 'r(t) = (t^2, 2t)' 'x' would be equal to 't^2'.")
        print("It's similar to making a 'u' substituion for 't' but we used 'x' instead of 'u'. Now, find what")
        print("'dx/dt' would be for your specific path and place this under a square root in the integral")
        print("and square it. ")
        print("\n\t'dy/dt' is the same concept, but while focusing on 'y' instead of 'x'. So take the")
        print("derivative of 'y' and place it under the square root making sure to square it and add that to")
        print("the 'dx/dt'.")
        print("\n\tThe square root comes from the pythagorean theorem. We have 2 sides and are using")
        print("those to find the final side which isn the length of the path. 'dt' is the then there to")
        print("show over what change in 't' that we find the length for. Therefore, if 't' could be any")
        print("variable. 'dt' goes outside of the square root to show that we'll be integrating in respect")
        print("to t.")
        print("\n\tNow take a second look at your work and make sure you've placed everything where it.")
        print("goes. By now, there shouldn't be any 'x' or 'y' terms in the 'dx/dt' and 'dy/dt' parts of")
        print("theintegral. If there aren't any, then you should have set up the integral correctly and ")
        print("are now ready to integrate.\n")
        print("\n\n\n\n")

    #The third option: to review the credits / materials I used to create the program
    #Credits
    elif user_choice == "3":
        print("\nHere are the sources presented in a unprofessional manner. Please visit the links to learn more. :)")
        print("Most were used to figure out how to code this program.")
        print("\nVideos:")
        print("\tIntegration in PYTHON (Symbolic and Numeric): https://www.youtube.com/watch?v=2I44Y9hfQ4Q")
        print("\tHow To Install SciPy in Visual Studio Code (Mac): https://www.youtube.com/watch?v=Nm3LRQu4qOU")
        print("\tHow to install Python Libraries in Visual Studio Code: https://www.youtube.com/watch?v=ThU13tikHQw")
        print("\tHow To Install Pyhton Libraries In Visual Studio Code (Mac): https://www.youtube.com/watch?v=U0MdznoiCGY")
        print("\tInstall SymPy with Pip: https://www.youtube.com/watch?v=0qeoaaRSKcg")
        print("\nProblems:")
        print("\tThe test problems used were taken from Professor Ben Woodruff's 215 Problem Set")
        print("\nAdditional Research:")
        print("\thttps://www.geeksforgeeks.org/pprint-function-in-sympy/#\n")

    #The fourth option: to quit the program
    elif user_choice == "4":
        print("\nThank you for using this program! If you have any questions or suggestions please contact the programer"
              "\nat etherealprogramming13@gmail.com\n")

    #The escape option: incase the user inputs some string or value that isn't accepted
    else:
        print("\nYou didn't enter a given option. Please try again and type the number (ie 4) for the option you wish to choose.\n")