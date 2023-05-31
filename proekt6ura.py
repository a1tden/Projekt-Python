from tkinter import *
root=Tk()
root.title("M")
b=0
k=0
xk=[]
yk=[]
circlesline=[]
soidenu=[]
soidenu1=[]
def circle_create(click):
    global k
    k=0
    x=click.x
    y=click.y
    for i in range(len(xk)):
        k=0
        if (x>=xk[i]-40 and x<=xk[i]+40 and y>=yk[i]-40 and y<=yk[i]+40):
            k=1
            break
    if k==0:
        circle=cn.create_oval(x-20,y-20,x+20,y+20,fill="blue",outline="black")
        xk.append(x)
        yk.append(y)
def circle_check(click):
    global b
    b=0
    x=click.x
    y=click.y
    for i in range(len(xk)):
        if (x>=xk[i]-20 and x<=xk[i]+20 and y>=yk[i]-20 and y<=yk[i]+20):
            if len(circlesline)<4:
                circlesline.append(xk[i])
                circlesline.append(yk[i])
                circl=cn.create_oval(xk[i]-20,yk[i]-20,xk[i]+20,yk[i]+20,fill="light blue",outline="black")
                soidenu.append(i)
                b=2
                if len(circlesline)==4:
                    soidenu1.append(soidenu[0])
                    soidenu1.append(soidenu[1])
                    soidenu.pop(0)
                    soidenu.pop(0)
                    circl=cn.create_oval(circlesline[0]-20,circlesline[1]-20,circlesline[0]+20,circlesline[1]+20,fill="blue",outline="black")
                    circl=cn.create_oval(circlesline[2]-20,circlesline[3]-20,circlesline[2]+20,circlesline[3]+20,fill="blue",outline="black")
                    cn.create_line(circlesline[0],circlesline[1],circlesline[2],circlesline[3],fill="blue")
                    circlesline.pop(0)
                    circlesline.pop(0)
                    circlesline.pop(0)
                    circlesline.pop(0)
            break
        b=1
    if len(circlesline)== 2 and b==1:
        circl=cn.create_oval(circlesline[0]-20,circlesline[1]-20,circlesline[0]+20,circlesline[1]+20,fill="blue",outline="black")
        circlesline.pop(0)
        circlesline.pop(0)
        soidenu.pop(0)
    mat = [[0 for _ in range(len(xk))] for _ in range(len(xk))]
    for k in range(len(soidenu1)):
        if k+1>len(soidenu1)-1:
            break
        else:
            mat[soidenu1[k]][soidenu1[k+1]]=1
            mat[soidenu1[k+1]][soidenu1[k]]=1
    print("matrica:")
    for row in mat:
        print(row)
       
               
cn=Canvas(root,width=500,height=500,bg="white")
cn.pack()
root.bind("<Button 1>",circle_create)
root.bind("<Button 3>",circle_check)
root.mainloop()
