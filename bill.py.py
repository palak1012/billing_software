from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1350x800+0+0")
        self.root.title("Billing Software")
        bg_color="#07574C"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
       
        #**Variables***
        #**Cosmetics****
        self.Soap=IntVar()
        self.Face_cream=IntVar()
        self.Face_wash=IntVar()
        self.Hair_spray=IntVar()
        self.Shampoo=IntVar()
        self.Deo=IntVar()
        #****Grocery*****
        self.Cheese=IntVar()
        self.Maggie=IntVar()
        self.Oats=IntVar()
        self.Sauce=IntVar()
        self.Bread=IntVar()
        self.Butter=IntVar()
        #***Ice Cream****
        self.Chocolate=IntVar()
        self.Vanilla=IntVar()
        self.Butter_scotch=IntVar()
        self.Black_current=IntVar()
        self.Straberry=IntVar()
        self.choco_chips=IntVar()
        #***Cold drinks***
        self.Maza=IntVar()
        self.Frooti=IntVar()
        self.Limca=IntVar()  
        self.Sprite=IntVar()
        self.Coke=IntVar()
        self.Thumbs_up=IntVar()
        #***Total product price & Tax Variables***
        self.Cosmetic_price=StringVar()
        self.Grocery_price=StringVar()
        self.Ice_cream_price=StringVar()
        self.Cold_drink_price=StringVar()

        self.Cosmetic_tax=StringVar()
        self.Grocery_tax=StringVar()
        self.Ice_cream_tax=StringVar()
        self.Cold_dirnk_tax=StringVar()
        #****Customer***
        self.cname=StringVar()
        self.cphn=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.Search_bill=StringVar()

        #*****Customer Detail Frame
        F1=LabelFrame(self.root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=76,relwidth=1)

        cname_lb1=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=17,textvariable=self.cname,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
       
        cphn_lbl=Label(F1,text="Customer Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=17,textvariable=self.cphn,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
         
        cbill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=17,textvariable=self.Search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        csrch_lbl=Button(F1,text="Search",command=self.find_bill,width=15,bd=7,bg="white",fg="black",font=("times new roman",13,"bold")).grid(row=0,column=6,pady=10)

        #****Cosmetics detail frame****
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=1,y=165,width=290,height=380)

        p1_lbl=Label(F2,text="Bath Soap",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=0,column=0,padx=10,pady=10)
        p1_txt=Entry(F2,width=10,textvariable=self.Soap,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        p1_lbl=Label(F2,text="Face Cream",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=1,column=0,padx=10,pady=10)
        p1_txt=Entry(F2,width=10,textvariable=self.Face_cream,font="arial 15",bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        p1_lbl=Label(F2,text="Face Wash",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=2,column=0,padx=10,pady=10)
        p1_txt=Entry(F2,width=10,textvariable=self.Face_wash,font="arial 15",bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        p1_lbl=Label(F2,text="Hair Spray",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=3,column=0,padx=10,pady=10)
        p1_txt=Entry(F2,width=10,textvariable=self.Hair_spray,font="arial 15",bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        p1_lbl=Label(F2,text="Shampoo",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=4,column=0,padx=10,pady=10)
        p1_txt=Entry(F2,width=10,textvariable=self.Shampoo,font="arial 15",bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        p1_lbl=Label(F2,text="Deo",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=5,column=0,padx=10,pady=10)
        p1_txt=Entry(F2,width=10,textvariable=self.Deo,font="arial 15",bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
     

        #****Grocery Frame**
        F3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=290,y=165,width=290,height=380)

        g1_lbl=Label(F3,text="Cheese",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=0,column=0,padx=20,pady=10)
        g1_txt=Entry(F3,width=10,textvariable=self.Cheese,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=20)

        g1_lbl=Label(F3,text="Maggie",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=1,column=0,padx=20,pady=10)
        g1_txt=Entry(F3,width=10,textvariable=self.Maggie,font="arial 15",bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=20)

        g1_lbl=Label(F3,text="Oats",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=2,column=0,padx=20,pady=10)
        g1_txt=Entry(F3,width=10,textvariable=self.Oats,font="arial 15",bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=20)

        g1_lbl=Label(F3,text="Sauce",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=3,column=0,padx=20,pady=10)
        g1_txt=Entry(F3,width=10,textvariable=self.Sauce,font="arial 15",bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=20)

        g1_lbl=Label(F3,text="Bread",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=4,column=0,padx=20,pady=10)
        g1_txt=Entry(F3,width=10,textvariable=self.Bread,font="arial 15",bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=20)

        p1_lbl=Label(F3,text="Butter",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=5,column=0,padx=20,pady=10)
        p1_txt=Entry(F3,width=10,textvariable=self.Butter,font="arial 15",bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=20)

        #******Ice Cream Frame*****
        F4=LabelFrame(self.root,text="Ice Cream",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=580,y=165,width=290,height=380)

        i1_lbl=Label(F4,text="Chocolate",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=0,column=0,padx=10,pady=10)
        i1_txt=Entry(F4,width=10,textvariable=self.Chocolate,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        i1_lbl=Label(F4,text="Vanilla",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=1,column=0,padx=10,pady=10)
        i1_txt=Entry(F4,width=10,textvariable=self.Vanilla,font="arial 15",bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        i1_lbl=Label(F4,text="Butter Scotch",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=2,column=0,padx=10,pady=10)
        i1_txt=Entry(F4,width=10,textvariable=self.Butter_scotch,font="arial 15",bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        i1_lbl=Label(F4,text="Black Current",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=3,column=0,padx=10,pady=10)
        i1_txt=Entry(F4,width=10,textvariable=self.Black_current,font="arial 15",bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        i1_lbl=Label(F4,text="Straberry",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=4,column=0,padx=10,pady=10)
        i1_txt=Entry(F4,width=10,textvariable=self.Straberry,font="arial 15",bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        i1_lbl=Label(F4,text="Choco chips",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=5,column=0,padx=10,pady=10)
        i1_txt=Entry(F4,width=10,textvariable=self.choco_chips,font="arial 15",bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

        #***Cold Drink****
        F5=LabelFrame(self.root,text="Cold Drink",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F5.place(x=870,y=165,width=290,height=380)

        d1_lbl=Label(F5,text="Maza",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=0,column=0,padx=10,pady=10)
        d1_txt=Entry(F5,width=10,textvariable=self.Maza,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        d1_lbl=Label(F5,text="Frooti",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=1,column=0,padx=10,pady=10)
        d1_txt=Entry(F5,width=10,textvariable=self.Frooti,font="arial 15",bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        d1_lbl=Label(F5,text="Limca",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=2,column=0,padx=10,pady=10)
        d1_txt=Entry(F5,width=10,textvariable=self.Limca,font="arial 15",bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        d1_lbl=Label(F5,text="Sprite",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=3,column=0,padx=10,pady=10)
        d1_txt=Entry(F5,width=10,textvariable=self.Sprite,font="arial 15",bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        d1_lbl=Label(F5,text="Coke",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=4,column=0,padx=10,pady=10)
        d1_txt=Entry(F5,width=10,textvariable=self.Coke,font="arial 15",bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        d1_lbl=Label(F5,text="Thumbs Up",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=5,column=0,padx=10,pady=10)
        d1_txt=Entry(F5,width=10,textvariable=self.Thumbs_up,font="arial 15",bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

   
        #****Bill Area***
        F6=LabelFrame(self.root,text="Bill Area",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="Black",bg="White")
        F6.place(x=1160,y=165,width=380,height=380)

        bill_title=Label(F6,text="Bill Area",bd=5,relief=GROOVE,fg="black",font=("times new roman",15),pady=2).pack(fill=X)
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack()

        #***Bill Menu***
        F7=LabelFrame(self.root,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F7.place(x=0,y=540,relwidth=1,height=380)

        m1_lbl=Label(F7,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F7,width=10,textvariable=self.Cosmetic_price,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)

        m1_lbl=Label(F7,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F7,width=10,textvariable=self.Grocery_price,font="arial 15",bd=5,relief=SUNKEN).grid(row=1,column=1,pady=1,padx=10)

        m1_lbl=Label(F7,text="Total Ice Cream Price",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=2,column=0,padx=10,pady=1,sticky="w")
        m1_txt=Entry(F7,width=10,textvariable=self.Ice_cream_price,font="arial 15",bd=5,relief=SUNKEN).grid(row=2,column=1,pady=1,padx=10)

        m1_lbl=Label(F7,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=3,column=0,padx=10,pady=1,sticky="w")
        m1_txt=Entry(F7,width=10,textvariable=self.Cold_drink_price,font="arial 15",bd=5,relief=SUNKEN).grid(row=3,column=1,pady=1,padx=10)

       
        t1_lbl=Label(F7,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=0,column=2,padx=20,pady=10,sticky="w")
        t1_txt=Entry(F7,width=10,textvariable=self.Cosmetic_tax,font="arial 15",bd=5,relief=SUNKEN).grid(row=0,column=3,pady=10,padx=20)

        t1_lbl=Label(F7,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=1,column=2,padx=20,pady=10,sticky="w")
        t1_txt=Entry(F7,width=10,textvariable=self.Grocery_tax,font="arial 15",bd=5,relief=SUNKEN).grid(row=1,column=3,pady=10,padx=20)

        t1_lbl=Label(F7,text="Ice Cream Tax",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=2,column=2,padx=20,pady=10)
        t1_txt=Entry(F7,width=10,textvariable=self.Ice_cream_tax,font="arial 15",bd=5,relief=SUNKEN).grid(row=2,column=3,pady=10,padx=20)

        t1_lbl=Label(F7,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14)).grid(row=3,column=2,padx=20,pady=10)
        t1_txt=Entry(F7,width=10,textvariable=self.Cold_dirnk_tax,font="arial 15",bd=5,relief=SUNKEN).grid(row=3,column=3,pady=10,padx=20)

        #****box****
        F8=LabelFrame(self.root,bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="Black",bg="White")
        F8.place(x=670,y=560,width=850,height=190)

        Total_btn=Button(F8,command=self.total,text="Total",width=11,bd=9,bg=bg_color,fg="gold",font=("times new roman",20)).grid(row=0,column=6,padx=5,pady=40)
        Gbill_btn=Button(F8,text="Generate Bill",command=self.bill_area,width=11,bd=9,bg=bg_color,fg="gold",font=("times new roman",20)).grid(row=0,column=7,padx=5,pady=40)
        Clear_btn=Button(F8,text="Clear",command=self.clear_data,width=11,bd=9,bg=bg_color,fg="gold",font=("times new roman",20)).grid(row=0,column=8,padx=5,pady=40)
        Exit_btn=Button(F8,text="Exit",command=self.Exit_app,width=11,bd=9,bg=bg_color,fg="gold",font=("times new roman",20)).grid(row=0,column=9,padx=5,pady=40)
        self.welcome_bill()


    def total(self):

        self.c_s_p=self.Soap.get()*40
        self.c_fc_p=self.Face_cream.get()*200
        self.c_fw_p=self.Face_wash.get()*70
        self.c_hs_p=self.Hair_spray.get()*150
        self.c_sh_p=self.Shampoo.get()*350
        self.c_d_p=self.Deo.get()*190

        self.Total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_sh_p+
                                    self.c_d_p    
                                    )
        self.Cosmetic_price.set("Rs. "+str(self.Total_cosmetic_price))
        self.c_tax=round((self.Total_cosmetic_price*0.05),2)
        self.Cosmetic_tax.set("Rs. "+str(self.c_tax))  

        self.g_s_p=self.Cheese.get()*35
        self.g_pu_p=self.Maggie.get()*50
        self.g_r_p=self.Oats.get()*70
        self.g_f_p=self.Sauce.get()*70
        self.g_br_p=self.Bread.get()*40
        self.g_bu_p=self.Butter.get()*45

        self.Total_grocery_price=float(
                                    self.g_s_p+
                                    self.g_pu_p+
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_br_p+
                                    self.g_bu_p
                                    )
        self.Grocery_price.set("Rs. "+str(self.Total_grocery_price))
        self.g_tax=round((self.Total_grocery_price*0.1),2)
        self.Grocery_tax.set("Rs. "+str(self.g_tax))  

        self.i_c_p=self.Chocolate.get()*45
        self.i_v_p=self.Vanilla.get()*35
        self.i_bs_p=self.Butter_scotch.get()*50
        self.i_bc_p=self.Black_current.get()*80
        self.i_s_p=self.Straberry.get()*45
        self.i_cc_p=self.choco_chips.get()*75
 
        self.Total_ice_cream_price=float(
                                      self.i_c_p+
                                      self.i_v_p+
                                      self.i_bs_p+
                                      self.i_bc_p+
                                      self.i_s_p+
                                      self.i_cc_p
                                      )
        self.Ice_cream_price.set("Rs. "+str(self.Total_ice_cream_price))
        self.i_tax=round((self.Total_ice_cream_price*0.05),2)
        self.Ice_cream_tax.set("Rs. "+str(self.i_tax))

        self.d_m_p=self.Maza.get()*40
        self.d_f_p=self.Frooti.get()*50
        self.d_l_p=self.Limca.get()*35
        self.d_s_p=self.Sprite.get()*60
        self.d_c_p=self.Coke.get()*45
        self.d_t_p=self.Thumbs_up.get()*40

        self.Total_cold_drink_price=float(
                                       self.d_m_p+
                                       self.d_f_p+
                                       self.d_l_p+
                                       self.d_s_p+
                                       self.d_c_p+
                                       self.d_t_p
                                       )
        self.Cold_drink_price.set("Rs. "+str(self.Total_cold_drink_price))
        self.d_tax=round((self.Total_cold_drink_price*0.1),2)
        self.Cold_dirnk_tax.set("Rs. "+str(self.d_tax))        
       
        self.Total_bill=float(  self.Total_cosmetic_price+
                                self.Total_grocery_price+
                                self.Total_ice_cream_price+
                                self.Total_cold_drink_price+
                                self.c_tax+
                                self.g_tax+
                                self.i_tax+
                                self.d_tax
                            )  
                                           

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Maya Store Retail")
        self.txtarea.insert(END,f"\n Bill no.:{self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name:{self.cname.get()}")
        self.txtarea.insert(END,f"\n Phone numer:{self.cphn.get()}")
        self.txtarea.insert(END,f"\n==========================================")
        self.txtarea.insert(END,f"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n==========================================")

    def bill_area(self):
        if self.cname.get()=="" or self.cphn.get()=="":
            messagebox.showerror("Error","customer details are must")
        elif self.Cosmetic_price.get()=="Rs. 0.0" and self.Grocery_price.get()=="Rs. 0.0" and self.Ice_cream_price.get()=="Rs. 0.0" and self.Cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product purchased")    
        else:  
            self.welcome_bill()
            #==========cosmetics============
            if self.Soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t:{self.Soap.get()}\t\t{self.c_s_p}")          
            if self.Face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face cream\t\t:{self.Face_cream.get()}\t\t{self.c_fc_p}")
            if self.Face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face wash\t\t:{self.Face_wash.get()}\t\t{self.c_fw_p}")
            if self.Hair_spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair spray\t\t:{self.Hair_spray.get()}\t\t{self.c_hs_p}")
            if self.Shampoo.get()!=0:
                self.txtarea.insert(END,f"\n Shampoo\t\t:{self.Shampoo.get()}\t\t{self.c_sh_p}")
            if self.Deo.get()!=0:
                self.txtarea.insert(END,f"\n Deo\t\t:{self.Deo.get()}\t\t{self.c_d_p}")                  

            #==========Grocery============
            if self.Cheese.get()!=0:
                self.txtarea.insert(END,f"\n Cheese\t\t:{self.Cheese.get()}\t\t{self.g_s_p}")          
            if self.Maggie.get()!=0:
                self.txtarea.insert(END,f"\n Maggie\t\t:{self.Maggie.get()}\t\t{self.g_pu_p}")
            if self.Oats.get()!=0:
                self.txtarea.insert(END,f"\n Rise\t\t:{self.Oats.get()}\t\t{self.g_r_p}")
            if self.Sauce.get()!=0:
                self.txtarea.insert(END,f"\n Sauce\t\t:{self.Sauce.get()}\t\t{self.g_f_p}")
            if self.Bread.get()!=0:
                self.txtarea.insert(END,f"\n Bread\t\t:{self.Bread.get()}\t\t{self.g_br_p}")
            if self.Butter.get()!=0:
                self.txtarea.insert(END,f"\n Butter\t\t:{self.Butter.get()}\t\t{self.g_bu_p}")    

            #==========icecream=============
            if self.Chocolate.get()!=0:
                self.txtarea.insert(END,f"\n Chocolate\t\t:{self.Chocolate.get()}\t\t{self.i_c_p}")          
            if self.Vanilla.get()!=0:
                self.txtarea.insert(END,f"\n Vanilla\t\t:{self.Vanilla.get()}\t\t{self.i_v_p}")
            if self.Butter_scotch.get()!=0:
                self.txtarea.insert(END,f"\n Butter scotch\t\t:{self.Butter_scotch.get()}\t\t{self.i_bs_p}")
            if self.Black_current.get()!=0:
                self.txtarea.insert(END,f"\n Black current\t\t:{self.Black_current.get()}\t\t{self.i_bc_p}")
            if self.Straberry.get()!=0:
                self.txtarea.insert(END,f"\n Straberry\t\t:{self.Straberry.get()}\t\t{self.i_s_p}")
            if self.choco_chips.get()!=0:
                self.txtarea.insert(END,f"\n Choco chips\t\t:{self.choco_chips.get()}\t\t{self.i_cc_p}")  

            #=========cold drinks============
            if self.Maza.get()!=0:
                self.txtarea.insert(END,f"\n Maza\t\t:{self.Maza.get()}\t\t{self.d_m_p}")          
            if self.Frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t:{self.Frooti.get()}\t\t{self.d_f_p}")
            if self.Limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t:{self.Limca.get()}\t\t{self.d_l_p}")
            if self.Sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t:{self.Sprite.get()}\t\t{self.d_s_p}")
            if self.Coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t:{self.Coke.get()}\t\t{self.d_c_p}")
            if self.Thumbs_up.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs up\t\t:{self.Thumbs_up.get()}\t\t{self.d_t_p}")                  

            self.txtarea.insert(END,f"\n------------------------------------------")
            if self.Cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.Cosmetic_tax.get()}")
            if self.Grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.Grocery_tax.get()}")
            if self.Ice_cream_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Ice cream Tax\t\t\t{self.Ice_cream_tax.get()}")
            if self.Cold_dirnk_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold drink Tax\t\t\t{self.Cold_dirnk_tax.get()}")        

            self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {str(self.Total_bill)}")        
            self.txtarea.insert(END,f"\n------------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill no. : {self.bill_no.get()} saved succesfully")
        else:
            return  

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.Search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to clear?")
        if op>0:


            #**Cosmetics****
            self.Soap.set(0)
            self.Face_cream.set(0)
            self.Face_wash.set(0)
            self.Hair_spray.set(0)
            self.Shampoo.set(0)
            self.Deo.set(0)
            #****Grocery*****
            self.Cheese.set(0)
            self.Maggie.set(0)
            self.Oats.set(0)
            self.Sauce.set(0)
            self.Bread.set(0)
            self.Butter.set(0)
            #***Ice Cream****
            self.Chocolate.set(0)
            self.Vanilla.set(0)
            self.Butter_scotch.set(0)
            self.Black_current.set(0)
            self.Straberry.set(0)
            self.choco_chips.set(0)
            #***Cold drinks***
            self.Maza.set(0)
            self.Frooti.set(0)
            self.Limca.set(0)  
            self.Sprite.set(0)
            self.Coke.set(0)
            self.Thumbs_up.set(0)
            #***Total product price & Tax Variables***
            self.Cosmetic_price.set("")
            self.Grocery_price.set("")
            self.Ice_cream_price.set("")
            self.Cold_drink_price.set("")

            self.Cosmetic_tax.set("")
            self.Grocery_tax.set("")
            self.Ice_cream_tax.set("")
            self.Cold_dirnk_tax.set("")
            #****Customer***
            self.cname.set("")
            self.cphn.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.Search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()        
       



root=Tk()
obj = Bill_App(root)
root.mainloop()