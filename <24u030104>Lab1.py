while (1):
    marks = input("Enter marks between 0-100 (type exit/EXIT to exit):-")
    if marks=="EXIT" or marks=="exit":
        print("exited")
        break
    if marks.isdigit()!=1:
        print("Invalid input")
        continue
    marks = int(marks)
    if(marks>100 or marks<0):
        print("invalid input")
    else:
        if marks>=90:
            print("A")
        elif marks>=75:
            print("B")
        elif marks>=60:
            print("C")
        elif marks>=40:
            print("D")
        else:
            print("F")
