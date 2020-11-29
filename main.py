print("Hi mr. Billu it's your billing software made by Tanishq for your content")
from tkinter import*
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software By Tanishq")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",34,"bold"),pady=2).pack(fill=X)
#=====================variabes======================================
# ======================paints======================================
        self.paint1=IntVar()
        self.paint2=IntVar()
        self.paint3=IntVar()
        self.paint4=IntVar()
        self.paint5=IntVar()
        self.paint6=IntVar()
        #=====================items====================================
        self.item1=IntVar()
        self.item2=IntVar()
        self.item3=IntVar()
        self.item4=IntVar()
        self.item5=IntVar()
        self.item6=IntVar()
        #===========================extras==================================
        self.extras1=IntVar()
        self.extras2=IntVar()
        self.extras3=IntVar()
        self.extras4=IntVar()
        self.extras5=IntVar()
        self.extras6=IntVar()
        #=================products total andx tax============================
        self.paint_price=StringVar()
        self.item_price=StringVar()
        self.extras_price=StringVar()
        
        self.paint_tax=StringVar()
        self.item_tax=StringVar()
        self.extras_tax=StringVar()
        #=======================coustumer details================
        self.c_name=StringVar
        self.c_phone=StringVar
        self.c_details=StringVar
        self.search_bill=StringVar
        #=====================phrase end=========================
        #==================================details==========================================================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Coustomer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(F1,text="Coustomer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=14,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        cphn_lbl=Label(F1,text="Phone no.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=14,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=14,textvariable=self.c_details,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        bill_btn=Button(F1,text="Search",textvariable=self.search_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=6)
        # ========================================paints=====================================================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Paint Items",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=315,height=380)
        bath_lbl=Label(F2,text="Brown paint",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.paint1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        paint2_lbl=Label(F2,text="Paint 2",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        paint2_txt=Entry(F2,width=10,textvariable=self.paint2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        paint3_lbl=Label(F2,text="Paint 3",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        paint3_txt=Entry(F2,width=10,textvariable=self.paint3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        paint_4_lbl=Label(F2,text="Paint 4",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        paint_4_txt=Entry(F2,width=10,textvariable=self.paint4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        painy_5_lbl=Label(F2,text="Paint 5",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        painy_5_txt=Entry(F2,width=10,textvariable=self.paint5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        paint_6_lbl=Label(F2,text="Paint 6",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        paint_6_txt=Entry(F2,width=10,textvariable=self.paint6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #==============================================items===============================================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Items",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=315,height=380)
        item_1_lbl=Label(F3,text="Item 1",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        item_1_txt=Entry(F3,width=10,textvariable=self.item1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        item_2_lbl=Label(F3,text="Item 2",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        item_2_txt=Entry(F3,width=10,textvariable=self.item2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        item_3_lbl=Label(F3,text="Item 3",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        item_3_txt=Entry(F3,width=10,textvariable=self.item3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        item_4_lbl=Label(F3,text="Item 4",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        item_4_txt=Entry(F3,width=10,textvariable=self.item4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        item_5_lbl=Label(F3,text="Item 5",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        item_5_txt=Entry(F3,width=10,textvariable=self.item5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        item_6_lbl=Label(F3,text="Item 6",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        item_6_txt=Entry(F3,width=10,textvariable=self.paint6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #================================================extras========================================================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Extra",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=315,height=380)
        extra_1_lbl=Label(F4,text="Extra 1",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        extra_1_txt=Entry(F4,width=10,textvariable=self.extras1,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        extra_2_lbl=Label(F4,text="Extra 2",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        extra_2_txt=Entry(F4,width=10,textvariable=self.extras2,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        extra_3_lbl=Label(F4,text="Extra 3",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        extra_3_txt=Entry(F4,width=10,textvariable=self.extras3,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        extra_4_lbl=Label(F4,text="Extra 4",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        extra_4_txt=Entry(F4,width=10,textvariable=self.extras4,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        extra_5_lbl=Label(F4,text="Extra 5",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        extra_5_txt=Entry(F4,width=10,textvariable=self.extras5,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        extra_6_lbl=Label(F4,text="Extra 6",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        extra_6_txt=Entry(F4,width=10,textvariable=self.extras6,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        #==============================================bill area=========================================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=270,height=380)
        bill_title=Label(F5,text="Billing Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #==============================buttonframe==================================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1=Label(F6,text="total paints price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.paint_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=1)
        
        m2=Label(F6,text="total items price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.item_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=1)
        
        m3=Label(F6,text="total extras price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.extras_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=1)
        
        c1=Label(F6,text="paints Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.paint_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=1)
        
        c2=Label(F6,text="items Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.item_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,pady=1)
        
        c3=Label(F6,text="extras Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.extras_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=630,width=630,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=0,pady=5)
        save_btn=Button(btn_F,text="Save",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=1,pady=5)
        clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=2,pady=5)
        exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=3,pady=5)

def total(self):
        self.total_paint_price=(
                                (self.paint1.get()*40)+
                                (self.paint2.get()*120)+
                                (self.paint3.get()*60)+
                                (self.paint4.get()*180)+
                                (self.paint5.get()*140)+
                                (self.paint6.get()*230)
                                )
        self.paint_price.set(str(self.total_paint_price))

root=Tk()
obj = Bill_App(root)
root.mainloop()
