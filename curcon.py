

def USD(n):
    if n==1:
        return (int(amount)*0.01205)
def EUR(n):
    if n==2:
        return (int(amount)*0.01137)  
def JPY(n):
    if n==3:
        return (int(amount)*1.80574)    
def SGD(n):
    if n==4:
        return (int(amount)*0.01648)   
def GBP(n):
    if n==5:
        return (int(amount)*0.0099)
        
     
print("welcome to jk currency converter \n")
print("enter amount only in Indian rupee\n")
print("this method is updated on 25-10-2023 ")
amount = int(input("please enter amount"))
print("please select different countries to exchange currency\n")
print("1.USD(united states) 2.EUR(euro) 3.JPY(japan) 4.sGD(singapore) 5.GBP(BRITISH)")
ch=int(input("enter choice "))

    
if ch==1:
   print( f"amount after conversion :{USD(1)}$")
   print("thank you visit again JK converter!")   
elif ch==2:
    print(f"amount AFTER conversion to euro {EUR(2)}eur ") 
    print("thank you visit again JK converter!")     
elif ch==3:
    print(f"amount after conversion to japan {JPY(3)} jpy ")
    print("thank you visit again JK converter!")   
elif ch==4:
    print(f"amount after conversion {SGD(4)} SGD")
    print("thank you visit again JK converter!")   
elif ch==5:
    print(f"amount after conversion to british pound {GBP(5)}")
    print("thank you visit again JK converter!")   
else:
    print("enter valid option")
    print("thank you visit again JK converter!")    
