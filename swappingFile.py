
def swapfun(f1,f2):


    f=open(fileName1,"r")
    d=open(fileName2,"r")

    data1=f.read()
    data2=d.read()

    f.close()
    d.close()

    f=open(fileName1,"w")
    d=open(fileName2,"w")

    f.write(data2)
    d.write(data1)



fileName1=input("Enter Your File Name--")
fileName2=input("Enter Your Second File Name--")

swapfun(fileName1,fileName2)



    
    
 

