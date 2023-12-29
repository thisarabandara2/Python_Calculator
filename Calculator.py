def powerv(x , y):
    return pow(x , y)

def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    try:
        return x / y
    except Exception as e:
        print(e)

def remainder(x , y):
    return x % y



def select_op(choice):
    if choice == "#":  # Terminate
        return -1
    elif choice == "$":  # reset
        return 0
    elif choice == "^":
        # base number
        while True:
            base = input("Enter base number: ")
            print(base)
            if base.endswith("#"):  # Terminate
                return -1
            elif base.endswith("$"):  # reset
                return 0

        
            try:
                bse = float(base)
                break
            except:
                print("Not a valid base,please enter again")
                continue
            
            while True:
                power = input("Enter power number: ")
                print(power)
            if power == "#":  # Terminate
                return -1
            elif power == "$":  # reset
                return 0

            try:
                pwr = float(power)
                break
            except:
                print("Not a valid power,please enter again")
                continue

        print(bse, "^", pwr, "=", powerv(bse, pwr))

    elif choice in ('+', '-', '/', '*', '%'):
        # number1
        while True:
            n01 = input("Enter first number: ")
            print(n01)
            if n01.endswith("#"):  # Terminate
                return -1
            elif n01.endswith("$"):  # reset
                return 0

            try:
                n01 = float(n01)
                break
            except:
                print("Not a valid number,please enter again")
                continue

        # number 2
        while True:
            n02 = input("Enter second number: ")
            print(n02)
            if n02.endswith("#"):  # Terminate
                return -1
            elif n02.endswith("$"):  # reset
                return 0

            try:
                n02 = float(n02)
                break
            except:
                print("Not a valid number,please enter again")
                continue
        if choice == '+':
            print(n01, "+", n02, "=", add(n01, n02))

        elif choice == '-':
            print(n01, "-", n02, "=", subtract(n01, n02))

        elif choice == '*':
            print(n01, "*", n02, "=", multiply(n01, n02))

        elif choice == '/':
            print(n01, "/", n02, "=", divide(n01, n02))

        elif choice == '%':
            print(n01, "%", n02, "=", remainder(n01, n02))

        else:
            print("Unrecognized operation")

 


#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()
