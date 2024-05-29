   
import math
import random
import string
from decimal import Decimal
from multiprocessing.sharedctypes import Value
from re import A
from sys import flags
from tkinter import *
from turtle import color
MAX=100
MAX2=99999
luukq =[]
mystring=' '
def GTS1(tsp,n,v,cost):
  
    tour=[MAX]
    for i in range(0,n):
        tour.append(0)
    Flag=[MAX2]
    for i in range(0,n):
        Flag.append(0)
      
    # for i in range(0,n+1):
    #     Flag[i]=0            
    dem=0  
    tour[0]= v #
    Flag[v]= 1 #

    tmp=v
    
    while dem!=n-1:
        tempcost=MAX2
        co=0
        for i in range(1,n+1):
            if(tempcost>tsp[v][i] and Flag[i]==0 and tsp[v][i]!=0):
               tempcost=tsp[v][i]
               co=i
        dem=dem+1
        tour[dem]=co  #
        cost+= tempcost
        Flag[v]=1    #
        v=co
        
    
    cost+= tsp[v][tmp]
    
    luutam=[]
    for i in range(0,n):
        luutam.append(' ')
        
    # print("Chi phí là:",cost)
    # print("Hanh trinh là:")
    for i in range(0,n):
        if(tour[i]==1):
            luutam[i]='Dinh Độc Lập'
        if(tour[i]==2):
            luutam[i]='Chợ Bến Thành'
        if(tour[i]==3):
            luutam[i]='Nhà thờ Đức Bà'
        if(tour[i]==4):
            luutam[i]='Bến Bạch Đằng'
        if(tour[i]==5):
            luutam[i]='Bảo tàng lịch sử Việt Nam'
        if(tour[i]==6):
            luutam[i]='Nhà hát Thành Phố'
        if(tour[i]==7):
            luutam[i]='Bảo tàng chứng tích chiến tranh'
        
    s='-->'.join(map(str,luutam))
    mystring=s
    mystring+='-->'+luutam[0]
    # print(mystring)
    # for i in range(0,n):         
    #     print( luutam[i],end=' ')
    # print(luutam[0])
    return mystring,cost
    


     
def main():   
    
    
    window = Tk()
    txt = Entry(window,width=40) 
    # txt=Text(window, width=40, height=2)
    txt.grid(column=0, row=10)
    window.title("Nhóm 7")
    
    window.geometry('1000x800')
    
    lbl = Label(window, text="Danh lam thắng cảnh", font=("Times New Roman Bold" ,30,),bg="yellow")
    lbl.grid(column=0, row=0)
    #-----------------------------------------
    lbl = Label(window, text=" Mời bạn nhập địa điểm muốn đi",font=("Times New Roman", 20), compound='center')
    lbl.grid(column=0, row=7)

    lbl2 = Label(window)
    lbl2.config(height=4)
    lbl2.grid(column=0, row=30)
    # lbl2 = Label(window,font=("Times New Roman", 40), compound='center')
    
    
    imageA=PhotoImage(file='MayNay.png')
    
    lbl_image=Label(window,image=imageA,compound='center',width=850, height=500)
    lbl_image.grid(column=0, row=4)
    
    
    lbl = Label(window, text=" ",font=("Times New Roman", 20), compound='center')
    lbl.grid(column=0, row=1)

   
    
    def clicked():
     cost=0
     v0=txt.get()
     
     if(len(v0)==0):
        def docFile(dtls,filename1,n): 
            file = open(filename1,'r',encoding='UTF-8')
            n = file.readline()
            n = int(n)  
            for i in range(n):
                char =  i
                data = file.readline().rstrip().split(',')
                dtls[char] = data
            file.close()
            return n

        def doiTuChuoiSangSo(dtls, n):
            for i in range(n):
                for j in range(n):
                    dtls[i][j] = int(dtls[i][j])

        def timDTLSTiepTheo(dtls, W, start, n):
            min = math.inf
            next = None
            for i in range(n):
                if i not in W:
                    if dtls[start][i] < min and dtls[start][i] > 0:
                        min = dtls[start][i]
                        next = i
            return next
            
        def GTS2(dtls, n):
            ketqua = {}
            for i in range(n):
                start = i
                cost = 0
                W = []
                W.append(start)
                next = timDTLSTiepTheo(dtls,W,start, n)
                while(next != None):
                    cost+= dtls[start][next]
                    W.append(next)
                    start = next
                    next = timDTLSTiepTheo(dtls,W,start, n)
                W.append(W[0])
                cost+=dtls[W[6]][W[0]]
                ketqua[cost] = W
            xuatKQ(ketqua, n)
            return

        def chonDuongDiNganNhat(ketqua):
            max = math.inf
            for i in ketqua:
                if i < max:
                    max = i
            return max

        def xuatKQ(ketqua, n):
            max = chonDuongDiNganNhat(ketqua)
            string = ""
            count = 0
            for i in ketqua[max]:
                if i == 0:
                    string += "Dinh Độc Lập"
                if i == 1:
                    string += "Chợ Bến Thành"
                if i == 2:
                    string += "Nhà thờ Đức Bà"
                if i == 3:
                    string += "Bến Bạch Đằng"
                if i == 4:
                    string += "Bảo tàng lịch sử Việt Nam"
                if i == 5:
                    string += "Nhà hát Thành Phố"
                if i == 6:
                    string += "Bảo tàng chứng tích chiến tranh"
                if count < n:
                    string += " --> "
                count+=1
            string += "\nChi phí là: "
            string += str(max)
            lbl2.configure(text = string)

        def run():
            dtls={}
            n=None
            n=docFile(dtls,'DanhThangLichSu.txt', n)
            doiTuChuoiSangSo(dtls, n)
            GTS2(dtls, n)

        run()
        return
         
     if(v0=='Dinh Độc Lập'):
         v=1
     if(v0=='Chợ Bến Thành'):
         v=2
     if(v0=='Nhà thờ Đức Bà'):
         v=3
     if(v0=='Bến Bạch Đằng'):
         v=4
     if(v0=='Bảo tàng lịch sử Việt Nam'):
         v=5
     if(v0=='Nhà hát Thành Phố'):
         v=6
     if(v0=='Bảo tàng chứng tích chiến tranh'):
         v=7  
   
     n=7
     file = open('dsDanhLamThangCanh.txt') 
     t = file.readline().split()
     tsp=[]
     for i in file:
        x = list(map(int,i.split()))
        tsp.append(x) 
     luukq=GTS1(tsp,n,v,cost)
     str_s1=str(luukq[0])
     str_s2=str(luukq[1])
     
     
     
     
    #  +"\n"+"Tổng chi phí là: "+cost+"\n"
     res = "Đường đi là: " + str_s1 +"\n"+"Tổng chi phí là: "+ str_s2 +"\n"

     lbl2.configure(text = res)

    btn = Button(window, text="Thực thi",command = clicked)
    btn.grid(column=0, row=15)
    window.mainloop()        

if __name__ == "__main__":
    main()  
    
      
