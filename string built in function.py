def strlen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


def strrev(str):
    rstr = " "
    l = strlen(str)
    while l>0:
        rstr = rstr + str[l-1]
        l=l-1
    return rstr

def strcat(st1,st2):
    return(st1 + st2)

def strcmp(st1,st2):
    if(st1 == st2):
        print(st1+"and"+st2+"are same")  
    elif(st1>st2):
        print (st1 + " comes after" +  st2 + " in the Dictionary")
    else:
        print(st1 + " comes before" +  st2 + " in the Dictionary")

print("String Functions:\n 1.String Length \n 2.String Reverse \n 3.String Concatenation
              \n 4.Sring Comparison \n 5.Exit \n")

while(1):
    n=int(input("Enter your choice:"))
    if (n==1):
        str=input("Enter a string:")
        print("Length of the string is:",strlen(str))
    elif (n==2):
        str=input("Enter a string:")
        print("Reversed string is:",strrev(str))
    elif (n==3):
        st1=input("Enter the first string:")
        st2=input("Enter the second string:")  
        print("Concatenated string is:",strcat(st1,st2))
    elif (n==4):
        str1=input("Enter the first string:")
        str2=input("Enter the second string:")  
        strcmp(str1,str2)
    elif (n==5):
        print("Exited")
        break
    else:
        print("Invalid choice")
