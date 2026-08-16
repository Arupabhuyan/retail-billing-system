from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib



#functionality part
def clear():
    bathsoapEntry.delete(0,END)

    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    HairoilEntry.delete(0, END)
    PerfumeEntry.delete(0, END)
    FacepowderEntry.delete(0, END)
    HairShampooEntry.delete(0, END, )

    RiceEntry.delete(0, END)
    OilEntry.delete(0, END)
    DalEntry.delete(0, END)
    SugarEntry.delete(0, END)
    wheatEntry.delete(0, END)
    SemolinaEntry.delete(0, END)
    PohaEntry.delete(0, END)

    MaazaEntry.delete(0, END)
    spriteEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    FizzEntry.delete(0, END)
    ThumsupEntry.delete(0, END)
    FantaEntry.delete(0, END)
    RedBullEntry.delete(0, END)


    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    HairoilEntry.insert(0,0)
    PerfumeEntry.insert(0,0)
    FacepowderEntry.insert(0,0)
    HairShampooEntry.insert(0,0,)

    RiceEntry.insert(0,0)
    OilEntry.insert(0,0)
    DalEntry.insert(0,0)
    SugarEntry.insert(0,0)
    wheatEntry.insert(0,0)
    SemolinaEntry.insert(0,0)
    PohaEntry.insert(0,0)

    MaazaEntry.insert(0,0)
    spriteEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    FizzEntry.insert(0,0)
    ThumsupEntry.insert(0,0)
    FantaEntry.insert(0,0)
    RedBullEntry.insert(0,0)

    cosmetictaxEntry.delete(0,END)
    GrocerytaxEntry.delete(0,END)
    coldDrinkstaxEntry.delete(0,END)

    cosmeticpriceEntry.delete(0,END)
    GrocerypriceEntry.delete(0,END)
    DrinkspriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    BillEntry.delete(0,END)

    textarea.delete(1.0,END)









def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()  # Correct method
            ob.login('your_email@gmail.com', 'your_password')
            ob.sendmail('your_email@gmail.com', 'receiver_email@gmail.com', 'Your message here')
            ob.quit()
        except Exception as e:
            messagebox.showerror('Error', f'Something went wrong: {e}', parent=root1)

    if textarea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Bill  is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send_gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='sender',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry (senderFrame,font=('arial',14,'bold'),bd=6,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame, text="password", font=('arial', 14, 'bold'), bd=6, bg='gray20',
                            fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=6, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recipientLabel = Label(senderFrame, text="EmailAddress", font=('arial', 14, 'bold'), bd=6, bg='gray20',
                              fg='white')
        recipientLabel.grid(row=0, column=0, padx=10, pady=8)

        recipientEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=6, width=23, relief=RIDGE)
        recipientEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(senderFrame, text="Message", font=('arial', 14, 'bold'), bd=6, bg='gray20',
                               fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)
        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,
                            width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END,)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=2)




        root1.mainloop()


def print_bill():
    if textarea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Bill  is empty')
    else:
        file=tempfile.mktemp(',.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')




def search_bill():
    bill_no = 'billnumberEntry.get()'

    for i in os.listdir('bills/'):
        if i.split('.')[0] == bill_no:
            with open(f'bills/{i}', 'r') as f:
                textarea.delete('1.0', 'end')
                for data in f:
                    textarea.insert(END, data)
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')






if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result=messagebox.askyesno('confirm','Do You want to save the bill')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('sucess',f'bill number{billnumber} is saved successfully')
        billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
       messagebox.showerror('Error','customer Details Are Required')
    elif cosmeticpriceEntry.get() == '' or GrocerypriceEntry.get()==''or DrinkspriceEntry.get()=='':
        messagebox.showerror('Error','products Are Selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and GrocerypriceEntry.get()=='0 Rs' and DrinkspriceEntry.get()=='0 Rs':
         messagebox.showerror('Error','products Are Selected')

    else:
         textarea.delete('1.0','end')

         textarea.insert(END,'\t\t**Welcome customer**\n')
         textarea.insert(END,f'\nBill Number:{billnumber}\n')
         textarea.insert(END,f'\nCustomerName:{nameEntry.get()}\n')
         textarea.insert(END,f'\nCustomerPhone:{phoneEntry.get()}\n')
         textarea.insert(END,'\n============================================================')
         textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
         textarea.insert(END,'\n============================================================')
         if bathsoapEntry.get()!='0':
             textarea.insert(END,f'\nBathsoap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice}')
         if facecreamEntry.get()!='0':
             textarea.insert(END,f'\nfacecream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice}')
         if facewashEntry.get()!='0':
             textarea.insert(END,f'\nfacewash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice}')
         if HairoilEntry.get() != '0':
             textarea.insert(END, f'\nHairoil\t\t\t{HairoilEntry.get()}\t\t\t{hairoilprice}')
         if PerfumeEntry.get()!='0':
             textarea.insert(END,f'\nperfume\t\t\t{PerfumeEntry.get()}\t\t\t{perfumeprice}')
         if FacepowderEntry.get()!='0':
             textarea.insert(END,f'\nfacepowder\t\t\t{FacepowderEntry.get()}\t\t\t{facepowderprice}')
         if HairShampooEntry.get() != '0':
             textarea.insert(END, f'\nHairshampoo\t\t\t{HairShampooEntry.get()}\t\t\t{hairshampooprice}')
         #Grocery
         if RiceEntry.get()!='0':
             textarea.insert(END,f'\nRice\t\t\t{RiceEntry.get()}\t\t\t{Riceprice}')
         if OilEntry.get()!='0':
             textarea.insert(END,f'\noil\t\t\t{OilEntry.get()}\t\t\t{oilprice}')
         if DalEntry.get()!='0':
             textarea.insert(END,f'\ndal\t\t\t{DalEntry.get()}\t\t\t{dalprice}')
         if SugarEntry.get()!='0':
             textarea.insert(END,f'\nSugar\t\t\t{SugarEntry.get()}\t\t\t{Sugarprice}')
         if wheatEntry.get()!='0':
             textarea.insert(END,f'\nwheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice}')
         if SemolinaEntry.get()!='0':
             textarea.insert(END,f'\nsemolina\t\t\t{SemolinaEntry.get()}\t\t\t{Semolinaprice}')
         if PohaEntry.get()!='0':
             textarea.insert(END,f'\npoha\t\t\t{PohaEntry.get()}\t\t\t{Pohaprice}')
    #Cold drinks

         if MaazaEntry.get()!='0':
             textarea.insert(END,f'\nMaaza\t\t\t{MaazaEntry.get()}\t\t\t{Maazaprice}')
         if spriteEntry.get()!='0':
             textarea.insert(END,f'\nsprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice}')
         if pepsiEntry.get()!='0':
             textarea.insert(END,f'\npepsi\t\t\t{MaazaEntry.get()}\t\t\t{pepsiprice}')
         if FizzEntry.get()!='0':
             textarea.insert(END,f'\nFizz\t\t\t{FizzEntry.get()}\t\t\t{Fizzprice}')
         if ThumsupEntry.get()!='0':
             textarea.insert(END,f'\nThumsup\t\t\t{ThumsupEntry.get()}\t\t\t{Thumsupprice}')
         if FantaEntry.get()!='0':
             textarea.insert(END,f'\nFanta\t\t\t{FantaEntry.get()}\t\t\t{Fantaprice}')
         if RedBullEntry.get()!='0':
             textarea.insert(END,f'\nRedBull\t\t\t{RedBullEntry.get()}\t\t\t{RedBullprice}')
    textarea.insert(END,'\n------------------------------------------------------------')

    if cosmetictaxEntry.get()!='0.0 Rs':
             textarea.insert(END,f'\ncosmetic tax\t\t\t\t{cosmetictaxEntry.get()}')
    if GrocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery tax\t\t\t\t{GrocerytaxEntry.get()}'),
    if coldDrinkstaxEntry.get()!='0.0Rs':
       textarea.insert(END,f'\nDrinks tax\t\t\t\t{coldDrinkstaxEntry.get()}')
    textarea.insert(END,f'\n\nTotalBill \t\t\t\t{TotalBill}')
    textarea.insert(END,'\n-----------------------------------------------------------')
    save_bill()
























def total():
    global soapprice,facecreamprice,facewashprice,hairoilprice,perfumeprice,facepowderprice,hairshampooprice
    global Riceprice,oilprice,dalprice,Sugarprice,wheatprice,Semolinaprice,Pohaprice
    global Maazaprice,spriteprice,pepsiprice,Fizzprice,Thumsupprice,Fantaprice,RedBullprice
    global TotalBill

    soapprice=int(bathsoapEntry.get())*40
    facecreamprice=int(facecreamEntry.get())*68
    facewashprice=int(facewashEntry.get())*134
    hairoilprice=int(HairoilEntry.get())*300
    perfumeprice=int(PerfumeEntry.get())*299
    facepowderprice=int(FacepowderEntry.get())*65
    hairshampooprice=int(HairShampooEntry.get())*675

    totalcosmeticprice=(soapprice+facecreamprice+facewashprice+hairoilprice+perfumeprice+
                        facepowderprice+hairshampooprice)
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0, str(totalcosmeticprice)+'Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0, str(cosmetictax)+'%')

#grocery price calculation
    Riceprice=int(RiceEntry.get())*60
    oilprice=int(OilEntry.get())*180
    dalprice=int(DalEntry.get())*100
    Sugarprice=int(SugarEntry.get())*46
    wheatprice=int(wheatEntry.get())*30
    Semolinaprice=int(SemolinaEntry.get())*45
    Pohaprice=int(PohaEntry.get())*50
    totalGroceryprice=(Riceprice+oilprice+dalprice+Sugarprice+wheatprice+
                       Semolinaprice+Pohaprice)
    GrocerypriceEntry.delete(0,END)
    GrocerypriceEntry.insert(0, str(totalGroceryprice)+'Rs')
    Grocerytax = totalGroceryprice * 0.8
    GrocerytaxEntry.delete(0, END)
    GrocerytaxEntry.insert(0, str(Grocerytax) + '%')

    #colddrink price calculation
    Maazaprice=int(MaazaEntry.get())*35
    Spriteprice=int(spriteEntry.get())*40
    pepsiprice=int(pepsiEntry.get())*50
    Fizzprice=int(FizzEntry.get())*30
    Thumsupprice=int(ThumsupEntry.get())*45
    Fantaprice=int(FantaEntry.get())*20
    RedBullprice=int(RedBullEntry.get())*100
    totalcoldDrinksprice=(Maazaprice+Spriteprice+pepsiprice+Fizzprice+Thumsupprice
                          +Fantaprice+RedBullprice)
    DrinkspriceEntry.delete(0,END)
    DrinkspriceEntry.insert(0,str(totalcoldDrinksprice)+'Rs')
    Drinkstax = totalcoldDrinksprice * 0.15
    coldDrinkstaxEntry.delete(0, END)
    coldDrinkstaxEntry.insert(0, str(Drinkstax) + '%')

    TotalBill=totalcosmeticprice+totalGroceryprice+totalcoldDrinksprice+cosmetictax+Grocerytax+totalcoldDrinksprice


# GUI part
root=Tk()
root.title('Retail Billing System')
root.geometry('1280x800')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                   ,bg='gray20',fg='light blue',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)
customer_details_frame=LabelFrame(root,text='customer Details',font=('times new roman',15,'bold')
                                  ,fg='light blue',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)
nameLabel=Label(customer_details_frame,text='Name' ,font=('times new roman',15,'bold'),bg='gray20'

                ,fg='white',bd=8,relief=GROOVE,)
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number' ,font=('times new roman',15,'bold'),bg='gray20'

                ,fg='white',bd=8,relief=GROOVE,)
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)


BillnumberLabel=Label(customer_details_frame,text='Billnumber' ,font=('times new roman',15,'bold'),bg='gray20'

                ,fg='white',bd=8,relief=GROOVE,)
BillnumberLabel.grid(row=0,column=4,padx=20,pady=2)

BillEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
BillEntry.grid(row=0,column=5,padx=8)
searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=4,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=7)

productsFrame=Frame(root)
productsFrame.pack(pady=10)

cosmeticsFrame=LabelFrame(productsFrame,text='cosmetics',font=('times new roman',15,'bold'),
                          fg='lightblue',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)
bathsoaplabel=Label(cosmeticsFrame,text='Bath soap',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
bathsoaplabel.grid(row=0,column=0,pady=10,padx=10,sticky=W)
bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=8,padx=10)
bathsoapEntry.insert(0,0)


facecreamlabel=Label(cosmeticsFrame,text='Face cream',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
facecreamlabel.grid(row=1,column=0,pady=10,padx=10,sticky=W)
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=8,padx=10)
facecreamEntry.insert(0,0)

facewashlabel=Label(cosmeticsFrame,text=' Face wash',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
facewashlabel.grid(row=2,column=0,pady=10,sticky=W)
facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=8)
facewashEntry.insert(0,0)

Hairoillabel=Label(cosmeticsFrame,text=' Hairoil',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Hairoillabel.grid(row=3,column=0,pady=10,sticky=W)
HairoilEntry=Entry(cosmeticsFrame,font=('times new roman',15),width=10,bd=5)
HairoilEntry.grid(row=3,column=1,pady=8)
HairoilEntry.insert(0,0)

Perfumelabel=Label(cosmeticsFrame,text='Perfume',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Perfumelabel.grid(row=4,column=0,pady=10,sticky=W)
PerfumeEntry=Entry(cosmeticsFrame,font=('times new roman',15),width=10,bd=5)
PerfumeEntry.grid(row=4,column=1,pady=8)
PerfumeEntry.insert(0,0)
Facepowderlabel=Label(cosmeticsFrame,text='Face powder',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Facepowderlabel.grid(row=5,column=0,pady=10,sticky=W)
FacepowderEntry=Entry(cosmeticsFrame,font=('times new roman',15),width=10,bd=5)
FacepowderEntry.grid(row=5,column=1,pady=8)
FacepowderEntry.insert(0,0)

HairShampoolabel=Label(cosmeticsFrame,text='Hairshampoo',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
HairShampoolabel.grid(row=6,column=0,pady=10,sticky=W)
HairShampooEntry=Entry(cosmeticsFrame,font=('times new roman',15),width=10,bd=5)
HairShampooEntry.grid(row=6,column=1,pady=8)
HairShampooEntry.insert(0,0)

GroceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),
                          fg='lightblue',bd=8,relief=GROOVE,bg='gray20')
GroceryFrame.grid(row=0,column=1)

Ricelabel=Label(GroceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Ricelabel.grid(row=0,column=0,pady=10,sticky=W)
RiceEntry=Entry(GroceryFrame,font=('times new roman',15),width=10,bd=5)
RiceEntry.grid(row=0,column=1,pady=8,padx=10)
RiceEntry.insert(0,0)

Oillabel=Label(GroceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Oillabel.grid(row=1,column=0,pady=10,sticky=W)
OilEntry=Entry(GroceryFrame,font=('times new roman',15),width=10,bd=5)
OilEntry.grid(row=1,column=1,pady=8,padx=10)
OilEntry.insert(0,0)

Dallabel=Label(GroceryFrame,text='Dal',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Dallabel.grid(row=2,column=0,pady=10,sticky=W)
DalEntry=Entry(GroceryFrame,font=('times new roman',15),width=10,bd=5)
DalEntry.grid(row=2,column=1,pady=8,padx=10)
DalEntry.insert(0,0)

Sugarlabel=Label(GroceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Sugarlabel.grid(row=3,column=0,pady=10,sticky=W)
SugarEntry=Entry(GroceryFrame,font=('times new roman',15),width=10,bd=5)
SugarEntry.grid(row=3,column=1,pady=8,padx=10)
SugarEntry.insert(0,0)

wheatlabel=Label(GroceryFrame,text='wheat',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
wheatlabel.grid(row=4,column=0,pady=10,sticky=W)
wheatEntry=Entry(GroceryFrame,font=('times new roman',15),width=10,bd=5)
wheatEntry.grid(row=4,column=1,pady=8,padx=10)
wheatEntry.insert(0,0)

Semolinalabel=Label(GroceryFrame,text='Semolina',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Semolinalabel.grid(row=5,column=0,pady=10,sticky=W)
SemolinaEntry=Entry(GroceryFrame,font=('times new roman',15),width=10,bd=5)
SemolinaEntry.grid(row=5,column=1,pady=8,padx=10)
SemolinaEntry.insert(0,0)


Pohalabel=Label(GroceryFrame,text='Poha',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Pohalabel.grid(row=6,column=0,pady=10,sticky=W)
PohaEntry=Entry(GroceryFrame,font=('times new roman',15),width=10,bd=5)
PohaEntry.grid(row=6,column=1,pady=8,padx=10)
PohaEntry.insert(0,0)

DrinksFrame=LabelFrame(productsFrame,text=' Cold Drinks',font=('times new roman',15,'bold'),
                          fg='lightblue',bd=8,relief=GROOVE,bg='gray20')
DrinksFrame.grid(row=0,column=2)

Maazalabel=Label(DrinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Maazalabel.grid(row=0,column=0,pady=10,sticky=W)
MaazaEntry=Entry(DrinksFrame,font=('times new roman',15),width=10,bd=5)
MaazaEntry.grid(row=0,column=1,pady=8,padx=10)
MaazaEntry.insert(0,0)

spritelabel=Label(DrinksFrame,text='sprite',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
spritelabel.grid(row=1,column=0,pady=10,sticky=W)
spriteEntry=Entry(DrinksFrame,font=('times new roman',15),width=10,bd=5)
spriteEntry.grid(row=1,column=1,pady=8,padx=10)
spriteEntry.insert(0,0)

pepsilabel=Label(DrinksFrame,text='pepsi',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
pepsilabel.grid(row=2,column=0,pady=10,sticky=W)
pepsiEntry=Entry(DrinksFrame,font=('times new roman',15),width=10,bd=5)
pepsiEntry.grid(row=2,column=1,pady=8,padx=10)
pepsiEntry.insert(0,0)

Fizzlabel=Label(DrinksFrame,text='Fizz',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Fizzlabel.grid(row=3,column=0,pady=10,sticky=W)
FizzEntry=Entry(DrinksFrame,font=('times new roman',15),width=10,bd=5)
FizzEntry.grid(row=3,column=1,pady=8,padx=10)
FizzEntry.insert(0,0)

Thumsuplabel=Label(DrinksFrame,text='Thumsup',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Thumsuplabel.grid(row=4,column=0,pady=10,sticky=W)
ThumsupEntry=Entry(DrinksFrame,font=('times new roman',15),width=10,bd=5)
ThumsupEntry.grid(row=4,column=1,pady=8,padx=10)
ThumsupEntry.insert(0,0)

Fantalabel=Label(DrinksFrame,text='Fanta',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
Fantalabel.grid(row=5,column=0,pady=10,sticky=W)
FantaEntry=Entry(DrinksFrame,font=('times new roman',15),width=10,bd=5)
FantaEntry.grid(row=5,column=1,pady=8,padx=10)
FantaEntry.insert(0,0)

RedBulllabel=Label(DrinksFrame,text='RedBull',font=('times new roman',15,'bold'),bg='gray20',
                         fg='white')
RedBulllabel.grid(row=6,column=0,pady=10,sticky=W)
RedBullEntry=Entry(DrinksFrame,font=('times new roman',15),width=10,bd=5)
RedBullEntry.grid(row=6,column=1,pady=8,padx=10)
RedBullEntry.insert(0,0)


BillFrame=Frame(productsFrame,bd=8,relief=GROOVE)
BillFrame.grid(row=0,column=3,padx=10)

BillareaLabel=Label(BillFrame,text='BillArea',font=('times new roman',20,'bold'),bd=7,relief=GROOVE)

BillareaLabel.pack(fill=X)

Scrollbar=Scrollbar(BillFrame,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(BillFrame,height=20,width=60,yscrollcommand=Scrollbar.set)
textarea.pack()
Scrollbar.config(command=textarea.yview)
BillMenuFrame=LabelFrame(root,text='BillMenu',font=('times new roman',15,'bold'),
                         fg='lightblue',bd=8,relief=GROOVE,bg='gray20')

BillMenuFrame.pack()


cosmeticpriceLabel=Label(BillMenuFrame,text='cosmeticprice',font=('times new roman',15,'bold'),
                        fg='white',bg='gray20')
cosmeticpriceLabel.grid(row=0,column=0,pady=10,sticky=W)

cosmeticpriceEntry=Entry(BillMenuFrame,font=('times new roman',15),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=8,padx=10)




GrocerypriceLabel=Label(BillMenuFrame,text='Groceryprice',font=('times new roman',14,'bold'),
                        fg='white',bg='gray20')
GrocerypriceLabel.grid(row=1,column=0,pady=10,sticky=W)

GrocerypriceEntry=Entry(BillMenuFrame,font=('times new roman',15),width=10,bd=5)
GrocerypriceEntry.grid(row=1,column=1,pady=8,padx=1)


DrinkspriceLabel=Label(BillMenuFrame,text=' Cold Drinksprice',font=('times new roman',14,'bold'),
                        fg='white',bg='gray20')
DrinkspriceLabel.grid(row=2,column=0,pady=10,sticky=W)

DrinkspriceEntry=Entry(BillMenuFrame,font=('times new roman',14),width=10,bd=5)
DrinkspriceEntry.grid(row=2,column=1,pady=8,padx=10)


cosmetictaxLabel=Label(BillMenuFrame,text='Cosmetic tax',font=('times new roman',15,'bold'),
                        fg='white',bg='gray20')
cosmetictaxLabel.grid(row=0,column=2,pady=10,sticky=W)

cosmetictaxEntry=Entry(BillMenuFrame,font=('times new roman',15),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=8,padx=10)

GrocerytaxLabel=Label(BillMenuFrame,text='Grocery tax',font=('times new roman',15,'bold'),
                        fg='white',bg='gray20')
GrocerytaxLabel.grid(row=1,column=2,pady=10,sticky=W)

GrocerytaxEntry=Entry(BillMenuFrame,font=('times new roman',15),width=10,bd=5)
GrocerytaxEntry.grid(row=1,column=3,pady=8,padx=10)


coldDrinkstaxLabel=Label(BillMenuFrame,text='Cold Drinks tax',font=('times new roman',15,'bold'),
                        fg='white',bg='gray20')
coldDrinkstaxLabel.grid(row=2,column=2,pady=10,sticky=W)

coldDrinkstaxEntry=Entry(BillMenuFrame,font=('times new roman',15),width=10,bd=5)
coldDrinkstaxEntry.grid(row=2,column=3,pady=8,padx=10)


buttonFrame=Frame(BillMenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)
totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=10,padx=10)


BillButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=bill_area)
BillButton.grid(row=0,column=1,pady=10,padx=10)

EmailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=send_email)
EmailButton.grid(row=0,column=2,pady=10,padx=10)

PrintButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=print_bill)
PrintButton.grid(row=0,column=3,pady=10,padx=10)
clearButton=Button(buttonFrame,text='clear',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=10,padx=10)


root.mainloop()









































