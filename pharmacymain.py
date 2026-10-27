from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

class Pharmacy_Management_System:
   def __init__(self,root):
       self.root=root
       self.root.geometry("1920x1080+0+0")
       self.root.title("Pharmacy Management System")
# =====================Main pharmacy data table variables==========
       self.ref_no_var=StringVar()
       self.company_name_var=StringVar()
       self.type_of_medicine_var=StringVar()
       self.medicine_name_var=StringVar()
       self.lot_no_var=StringVar()
       self.issue_date_var=StringVar()
       self.expire_date_var=StringVar()
       self.uses_var=StringVar()
       self.side_effect_var=StringVar()
       self.prec_and_warning_var=StringVar()
       self.dosage_var=StringVar()
       self.table_prices_var=StringVar()
       self.productQT_var=StringVar()


# ===================add medicine btn variable==================
       self.add_medi_btn_ref_var=StringVar()
       self.add_medi_btn_mediname_var=StringVar()
      # ======================Main Title==============================
       lbl_main=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg="white",fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
       lbl_main.pack(side=TOP,fill=X)

       img_logo=Image.open(r"E:\Pharmacy Management System\photos\pharmacy.png")
       img_logo=img_logo.resize((80,80),Image.ANTIALIAS)
       self.logo=ImageTk.PhotoImage(img_logo)
       lbl1=Label(self.root,image=self.logo,borderwidth=0,bg="white")
       lbl1.place(x=70,y=20)

        # ===================Data Frame===============================

       main_frame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
       main_frame.place(x=0,y=120,width=1530,height=400)

       medicien_info=LabelFrame(main_frame,text="Medicine Information",bd=10,relief=RIDGE,padx=20,fg="darkgreen",font=("times new roman",12,"bold"))
       medicien_info.place(x=0,y=5,width=900,height=350)

       medicien_department_info=LabelFrame(main_frame,text="Medicine & Department",bd=10,relief=RIDGE,fg="darkgreen",font=("times new roman",12,"bold"))
       medicien_department_info.place(x=910,y=5,width=540,height=350)
# ======================butyon frame======================

       btn_frame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
       btn_frame.place(x=0,y=520,width=1530,height=65)
#===================================main button=======================

       medicine_btn=Button(btn_frame,text="Medicine Add",command=self.pharmacy_database,font=("arial",12,"bold"),bg="darkgreen",fg="white",cursor="hand2",activebackground="darkgreen",activeforeground="white")
       medicine_btn.grid(row=0,column=0)

       update_btn=Button(btn_frame,command=self.pharmacy_database_update,text="Update",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white",cursor="hand2",activebackground="darkgreen",activeforeground="white")
       update_btn.grid(row=0,column=1,padx=5)

       delete_btn=Button(btn_frame,command=self.pharmacy_database_delete,text="Delete",font=("arial",12,"bold"),width=14,bg="red",fg="white",cursor="hand2",activebackground="red",activeforeground="white")
       delete_btn.grid(row=0,column=2)

       reset_btn=Button(btn_frame,text="Reset",command=self.pharmacy_database_reset,font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white",cursor="hand2",activebackground="darkgreen",activeforeground="white")
       reset_btn.grid(row=0,column=3,padx=5)

       exit_btn=Button(btn_frame,text="Exit",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white",cursor="hand2",activebackground="darkgreen",activeforeground="white")
       exit_btn.grid(row=0,column=4 )

# =====================================Search By======================================
# ============================search by variables====================================
       
       self.search_combo_entry=StringVar()

       search_by_lbl=Label(btn_frame,text="Search By",font=("arial",17,"bold"),bg="red",fg="white")
       search_by_lbl.grid(row=0,column=5,padx=5)
    # variable 
       self.search_combo_var=StringVar()
       search_combo=ttk.Combobox(btn_frame,textvariable=self.search_combo_var,width=12,font=("arial",13,"bold"),state="readonly")
       search_combo["values"]=("Reference_No","Medicine_Name","Lot_No")
       search_combo.grid(row=0,column=6)
       search_combo.current(0)
       
    #    variable
       self.search_combo_entry=StringVar()
       search_entry=Entry(btn_frame,textvariable=self.search_combo_entry,bd=3,relief=RIDGE,font=("arial",12,"bold"),width=12)
       search_entry.grid(row=0,column=7)

       search_btn=Button(btn_frame,command=self.search_data_main_table,text="SEARCH",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white",cursor="hand2",activebackground="darkgreen",activeforeground="white")
       search_btn.grid(row=0,column=8,padx=5 )

       show_all_btn=Button(btn_frame,command=self.main_data_fetch,text="SHOW ALL",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white",cursor="hand2",activebackground="darkgreen",activeforeground="white")
       show_all_btn.grid(row=0,column=9)
#=====================================main frame objects=================
       # refernce
       reference_lbl=Label(medicien_info,text="Reference No", font=("times new roman",12,"bold"))
       reference_lbl.grid(row=0,column=0,sticky=W,pady=5)

       conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
       mycursor1=conn.cursor()
       mycursor1.execute("select Reference_No from add_medicine_btn")
       rows=mycursor1.fetchall()

       reference_combobox=ttk.Combobox(medicien_info,textvariable=self.ref_no_var,font=("times new roman",12,"bold"),state="readonly",width=27)
       reference_combobox['values']=rows
       reference_combobox.current(0)
       reference_combobox.grid(row=0,column=1,pady=5)

        #  company name
       Company_lbl=Label(medicien_info,text="Company Name",font=("times new roman",12,"bold"))
       Company_lbl.grid(row=1,column=0,sticky=W,pady=5)
       company_entry= ttk.Entry(medicien_info,textvariable=self.company_name_var,font=("times new roman",12,"bold"),width=29)
       company_entry.grid(row=1,column=1,pady=5)

        # type of medicine 
       type_of_medicine_lbl=Label(medicien_info,text="Type Of Medicine",font=("times new roman",12,"bold"))
       type_of_medicine_lbl.grid(row=2,column=0,sticky=W)
       type_of_medicin_combobox=ttk.Combobox(medicien_info,textvariable=self.type_of_medicine_var,font=("times new roman",12,"bold"),state="readonly",width=27)
       type_of_medicin_combobox['values']=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
       type_of_medicin_combobox.current(0)
       type_of_medicin_combobox.grid(row=2,column=1)

        # medicine name
       medicine_name_lbl=Label(medicien_info,text="Medicine Name",font=("times new roman",12,"bold"))
       medicine_name_lbl.grid(row=3,column=0,sticky=W)

       conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
       mycursor2=conn.cursor()
       mycursor2.execute("select Medicine_Name from add_medicine_btn")
       rows=mycursor2.fetchall()

       medicine_name_combobox=ttk.Combobox(medicien_info,textvariable=self.medicine_name_var,font=("times new roman",12,"bold"),state="readonly",width=27)
       medicine_name_combobox['values']=rows
       medicine_name_combobox.current(0)
       medicine_name_combobox.grid(row=3,column=1,pady=5)

        # lot no
       lot_no_lbl=Label(medicien_info,text="Lot No",font=("times new roman",12,"bold"))
       lot_no_lbl.grid(row=4,column=0,sticky=W,pady=5)
       lot_no_entry= ttk.Entry(medicien_info,textvariable=self.lot_no_var,font=("times new roman",12,"bold"),width=29)
       lot_no_entry.grid(row=4,column=1,pady=5)
       
        # Issue Date
       issue_date_lbl=Label(medicien_info,text="Issue Date",font=("times new roman",12,"bold"))
       issue_date_lbl.grid(row=5,column=0,sticky=W,pady=5)
       issue_date_entry= ttk.Entry(medicien_info,textvariable=self.issue_date_var,font=("times new roman",12,"bold"),width=29)
       issue_date_entry.grid(row=5,column=1,pady=5)

        # expire date
       expire_date_lbl=Label(medicien_info,text="Expire Date",font=("times new roman",12,"bold"))
       expire_date_lbl.grid(row=6,column=0,sticky=W,pady=5)
       expire_date_entry=ttk.Entry(medicien_info,textvariable=self.expire_date_var,font=("times new roman",12,"bold"),width=29)
       expire_date_entry.grid(row=6,column=1,pady=5)

        # uses
       uses_lbl=Label(medicien_info,text="Uses",font=("times new roman",12,"bold"))
       uses_lbl.grid(row=7,column=0,sticky=W,pady=5)
       uses_entry= ttk.Entry(medicien_info,textvariable=self.uses_var,font=("times new roman",12,"bold"),width=29)
       uses_entry.grid(row=7,column=1,pady=5)

        # side effect
       side_effect_lbl=Label(medicien_info,text="Side Effect",font=("times new roman",12,"bold"))
       side_effect_lbl.grid(row=8,column=0,sticky=W,pady=5)
       side_effect_entry= ttk.Entry(medicien_info,textvariable=self.side_effect_var,font=("times new roman",12,"bold"),width=29)
       side_effect_entry.grid(row=8,column=1,pady=5)

        # pre&warning
       pre_and_warning_lbl=Label(medicien_info,text="Prec & Warning:",font=("times new roman",12,"bold"))
       pre_and_warning_lbl.grid(row=0,column=3,sticky=W,pady=5,padx=50)
       pre_and_warning_entry= ttk.Entry(medicien_info,textvariable=self.prec_and_warning_var,font=("times new roman",12,"bold"),width=29)
       pre_and_warning_entry.grid(row=0,column=4,pady=5)

        # Dosage
       dosage_lbl=Label(medicien_info,text="Dosage:",font=("times new roman",12,"bold"))
       dosage_lbl.grid(row=1,column=3,sticky=W,pady=5,padx=50)
       dosage_entry= ttk.Entry(medicien_info,textvariable=self.dosage_var,font=("times new roman",12,"bold"),width=29)
       dosage_entry.grid(row=1,column=4,pady=5)

        # tablet price
       tablet_price_lbl=Label(medicien_info,text="Tablet Price:",font=("times new roman",12,"bold"))
       tablet_price_lbl.grid(row=2,column=3,sticky=W,pady=5,padx=50)
       tablet_price_entry= ttk.Entry(medicien_info,textvariable=self.table_prices_var,font=("times new roman",12,"bold"),width=29)
       tablet_price_entry.grid(row=2,column=4,pady=5)

        # product QT
       product_QT_lbl=Label(medicien_info,text="ProductQT:",font=("times new roman",12,"bold"))
       product_QT_lbl.grid(row=3,column=3,sticky=W,pady=5,padx=50)
       product_QT_entry= ttk.Entry(medicien_info,textvariable=self.productQT_var,font=("times new roman",12,"bold"),width=29)
       product_QT_entry.grid(row=3,column=4,pady=5)

# =============main frame photos======================
       img1=Image.open(r"E:\Pharmacy Management System\photos\lab.jpg")
       img1=img1.resize((160,130),Image.ANTIALIAS)
       self.img_demo=ImageTk.PhotoImage(img1)
       lbl1=Label(self.root,image=self.img_demo,borderwidth=0,bg="white")
       lbl1.place(x=440,y=340)

       img2=Image.open(r"E:\Pharmacy Management System\photos\heartbeat.jpg")
       img2=img2.resize((160,130),Image.ANTIALIAS)
       self.img_demo2=ImageTk.PhotoImage(img2)
       lbl1=Label(self.root,image=self.img_demo2,borderwidth=0,bg="white")
       lbl1.place(x=600,y=340)

       img3=Image.open(r"E:\Pharmacy Management System\photos\medicine.jpg")
       img3=img3.resize((160,130),Image.ANTIALIAS)
       self.img_demo3=ImageTk.PhotoImage(img3)
       lbl1=Label(self.root,image=self.img_demo3,borderwidth=0,bg="white")
       lbl1.place(x=760,y=340)

       lbl_stay_home_stay_safe=Label(self.root,text="STAY HOME STAY SAFE",font=("times new roman",15,"bold"),fg="red")
       lbl_stay_home_stay_safe.place(x=550,y=311)

# ==================Right frame================================

       imgleft=Image.open(r"E:\Pharmacy Management System\photos\capsuls.png")
       imgleft=imgleft.resize((250,90),Image.ANTIALIAS)
       self.img_left=ImageTk.PhotoImage(imgleft)
       lbl1=Label(medicien_department_info,image=self.img_left,borderwidth=0)
       lbl1.place(x=0,y=0)

       imgright2=Image.open(r"E:\Pharmacy Management System\photos\firstaid.png")
       imgright2=imgright2.resize((220,150),Image.ANTIALIAS)
       self.img_right2=ImageTk.PhotoImage(imgright2)
       lbl1=Label(medicien_department_info,image=self.img_right2,borderwidth=0)
       lbl1.place(x=300,y=0)

       reference_no=Label(medicien_department_info,text="Reference No:",font=("times new roman",12,"bold"))
       reference_no.place (x=10,y=90)
       reference_entry=ttk.Entry(medicien_department_info,textvariable=self.add_medi_btn_ref_var,font=("times new roman",12,"bold"))
       reference_entry.place(x=127,y=90)

       medicine_name=Label(medicien_department_info,text="Medicine Name:",font=("times new roman",12,"bold"))
       medicine_name.place (x=10,y=120)
       medicine_name_entry=ttk.Entry(medicien_department_info,textvariable=self.add_medi_btn_mediname_var,font=("times new roman",12,"bold"))
       medicine_name_entry.place(x=127,y=120)
# ==============================right frame1=====================================
       frame_right1=Frame(medicien_department_info,bd=4,relief=RIDGE,bg="white")
       frame_right1.place(x=10,y=150,width=290,height=160)

       scroll_x=Scrollbar(frame_right1,orient=HORIZONTAL)
       scroll_x.pack(side=BOTTOM,fill=X)
         
       scroll_y=Scrollbar(frame_right1,orient=VERTICAL)
       scroll_y.pack(side=RIGHT,fill=Y)

       self.medicine_table=ttk.Treeview(frame_right1,columns=("Reference_No",
                                                              "Medicine_Name"),
                                                              xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

       scroll_x.config(command=self.medicine_table.xview)
       scroll_y.config(command=self.medicine_table.yview)

       self.medicine_table.heading("Reference_No",text="Reference_No")
       self.medicine_table.heading("Medicine_Name",text="Medicine_Name")
       self.medicine_table["show"]="headings"
       self.medicine_table.pack(fill=BOTH,expand=1)

       self.medicine_table.column("Reference_No",width=100)
       self.medicine_table.column("Medicine_Name",width=100)

       self.medicine_table.bind("<ButtonRelease-1>",self.getcursor)

# ========================right frame2================================

       frame_right2=Frame(medicien_department_info,bd=4,relief=RIDGE,bg="darkgreen")
       frame_right2.place(x=330,y=150,width=135,height=160)

       add_btn=Button(frame_right2,command=self.addmedicine,text="ADD",font=("times new roman",12,"bold"),width=13,bg="lime",fg="white",cursor="hand2",activebackground="lime",activeforeground="white",pady=4)
       add_btn.grid(row=1,column=0)

       update_btn=Button(frame_right2,command=self.update_btn,text="UPDATE",font=("times new roman",12,"bold"),width=13,bg="purple",fg="white",cursor="hand2",activebackground="purple",activeforeground="white",pady=4)
       update_btn.grid(row=2,column=0)

       delete_btn=Button(frame_right2,command=self.delete_btn,text="DELETE",font=("times new roman",12,"bold"),width=13,bg="red",fg="white",cursor="hand2",activebackground="red",activeforeground="white",pady=4)
       delete_btn.grid(row=3,column=0)

       clear_btn=Button(frame_right2,command=self.clear_btn,text="CLEAR",font=("times new roman",12,"bold"),width=13,bg="orange",fg="white",cursor="hand2",activebackground="orange",activeforeground="white",pady=4)
       clear_btn.grid(row=4,column=0)
# =========================pharmacy table main===============

       Pharmacy_main_frame=Frame(self.root,bd=15,relief=RIDGE)
       Pharmacy_main_frame.place(x=0,y=590,width=1530,height=210)

       scroll_x2=Scrollbar(Pharmacy_main_frame,orient=HORIZONTAL)
       scroll_x2.pack(side=BOTTOM,fill=X)

       scroll_y2=Scrollbar(Pharmacy_main_frame,orient=VERTICAL)
       scroll_y2.pack(side=RIGHT,fill=Y)

       self.pharmacy_main_table=ttk.Treeview(Pharmacy_main_frame,
                                              columns=("Reference_No",
                                              "Company_Name",
                                              "Type_Of_Medicine",
                                              "Medicine_Name",
                                              "Lot_No",
                                              "Issue_Date",
                                              "Expire_Date",
                                              "Uses",
                                              "Side_Effect",
                                              "Prec_and_Warning",
                                              "Dosage",
                                              "Tablet_Price",
                                              "Product_QT"),xscrollcommand=scroll_x2.set,yscrollcommand=scroll_y2.set)
        
       scroll_x2.pack(side=BOTTOM,fill=X)
       scroll_y2.pack(side=RIGHT,fill=Y)

       scroll_x2.config(command=self.pharmacy_main_table.xview)
       scroll_y2.config(command=self.pharmacy_main_table.yview)

       self.pharmacy_main_table["show"]="headings"

       self.pharmacy_main_table.heading("Reference_No",text="Reference_No")
       self.pharmacy_main_table.heading("Company_Name",text="Company_Name")
       self.pharmacy_main_table.heading("Type_Of_Medicine",text="Type_Of_Medicine")
       self.pharmacy_main_table.heading("Medicine_Name",text="Medicine_Name")
       self.pharmacy_main_table.heading("Lot_No",text="Lot_No")
       self.pharmacy_main_table.heading("Issue_Date",text="Issue_Date")
       self.pharmacy_main_table.heading("Expire_Date",text="Expire_Date")
       self.pharmacy_main_table.heading("Uses",text="Uses")
       self.pharmacy_main_table.heading("Side_Effect",text="Side_Effect")
       self.pharmacy_main_table.heading("Prec_and_Warning",text="Prec_and_Warning")
       self.pharmacy_main_table.heading("Dosage",text="Dosage")
       self.pharmacy_main_table.heading("Tablet_Price",text="Tablet_Price")
       self.pharmacy_main_table.heading("Product_QT",text="Product_QT")
       self.pharmacy_main_table.pack(fill=BOTH,expand=1)

       self.pharmacy_main_table.column("Reference_No",width=100)
       self.pharmacy_main_table.column("Company_Name",width=100)
       self.pharmacy_main_table.column("Type_Of_Medicine",width=100)
       self.pharmacy_main_table.column("Medicine_Name",width=100)
       self.pharmacy_main_table.column("Lot_No",width=100)
       self.pharmacy_main_table.column("Issue_Date",width=100)
       self.pharmacy_main_table.column("Expire_Date",width=100)
       self.pharmacy_main_table.column("Uses",width=100)
       self.pharmacy_main_table.column("Side_Effect",width=100)
       self.pharmacy_main_table.column("Prec_and_Warning",width=100)
       self.pharmacy_main_table.column("Dosage",width=100)
       self.pharmacy_main_table.column("Tablet_Price",width=100 )
       self.pharmacy_main_table.column("Product_QT",width=100)
       self.fetch_data_medicine_table()
       self.main_data_fetch()
       self.pharmacy_main_table.bind("<ButtonRelease-1>",self.pharmacy_database_getcursor)

# =======================add medicine function declaration======================
   def addmedicine(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
       mycursor=conn.cursor()
       mycursor.execute("insert into add_medicine_btn values(%s,%s)",(
                                                                             self.add_medi_btn_ref_var.get(),
                                                                             self.add_medi_btn_mediname_var.get()
                                                                                                   
                                                                              ))
        
       conn.commit()
       messagebox.showinfo("Success","Successfully Medicine Added")
       self.fetch_data_medicine_table()
       self.getcursor()
       conn.close()
        

   def fetch_data_medicine_table(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
       mycursor=conn.cursor()
       mycursor.execute("select * from  add_medicine_btn")
       rows=mycursor.fetchall()
       if len(rows)!=0:
           self.medicine_table.delete(*self.medicine_table.get_children())
           for i in rows:
               self.medicine_table.insert("",END,values=i)
           conn.commit()
       conn.close()
           
# ======================Get Cursor====================
   def getcursor(self,event=""):
       cursor_row=self.medicine_table.focus()
       content=self.medicine_table.item(cursor_row)
       rows=content["values"]
       self.add_medi_btn_ref_var.set(rows[0])
       self.add_medi_btn_mediname_var.set(rows[1])
# ======================Update Button=================
   def update_btn(self):
       if self.add_medi_btn_mediname_var.get()=="" or self.add_medi_btn_ref_var.get()=="":
           messagebox.showerror("Error","All Fields Are Required")
       else:
           conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
           mycursor=conn.cursor()
           mycursor.execute("update add_medicine_btn set Medicine_Name=%s where Reference_No=%s",(
                                                                                                  self.add_medi_btn_mediname_var.get(),
                                                                                                  self.add_medi_btn_ref_var.get()                 
                                                                                                    ))
           conn.commit()
           self.fetch_data_medicine_table()
           conn.close()

           messagebox.showinfo("Success","Medicine has been updated")


   def delete_btn(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
       mycursor=conn.cursor()
       sql="delete from add_medicine_btn where Reference_No=%s"
       val=(self.add_medi_btn_ref_var.get(),)
       mycursor.execute(sql,val)

       conn.commit()
       self.fetch_data_medicine_table()
       conn.close()
       messagebox.showinfo("Success","selected item is deleted")

   def clear_btn(self):
       self.add_medi_btn_ref_var.set("")
       self.add_medi_btn_mediname_var.set("")

# ===========================main pharmacy table=====================================================
   def pharmacy_database(self):
       if self.ref_no_var.get()=="" or self.lot_no_var.get()=="" :
           messagebox.showerror("Error","All fields are required")
       else:
           conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
           mycursor=conn.cursor()
           mycursor.execute("insert into pharmacy_main_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                     self.ref_no_var.get(),
                                                                                                     self.company_name_var.get(),
                                                                                                     self.type_of_medicine_var.get(),
                                                                                                     self.medicine_name_var.get(),
                                                                                                     self.lot_no_var.get(),
                                                                                                     self.issue_date_var.get(),
                                                                                                     self.expire_date_var.get(),
                                                                                                     self.uses_var.get(),
                                                                                                     self.side_effect_var.get(),
                                                                                                     self.prec_and_warning_var.get(),
                                                                                                     self.dosage_var.get(),
                                                                                                     self.table_prices_var.get(),
                                                                                                     self.productQT_var.get()
                                                                                                    ))
       conn.commit()
       messagebox.showinfo("Success","Data has been added successfully")
       self.main_data_fetch()
       self.pharmacy_database_getcursor()
       conn.close()
        

   
   def main_data_fetch(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
       mycursor=conn.cursor()
       mycursor.execute("select * from pharmacy_main_table")
       row_main=mycursor.fetchall()
       if len(row_main)!=0:
           self.pharmacy_main_table.delete(*self.pharmacy_main_table.get_children())
           for i in row_main:
               self.pharmacy_main_table.insert("",END,values=i)
           conn.commit()
       conn.close()

   def pharmacy_database_getcursor(self,ev=""):
       focus=self.pharmacy_main_table.focus()
       content=self.pharmacy_main_table.item(focus)
       rows=content["values"]

       self.ref_no_var.set(rows[0])
       self.company_name_var.set(rows[1])
       self.type_of_medicine_var.set(rows[2])
       self.medicine_name_var.set(rows[3])
       self.lot_no_var.set(rows[4])
       self.issue_date_var.set(rows[5])
       self.expire_date_var.set(rows[6])
       self.uses_var.set(rows[7])
       self.side_effect_var.set(rows[8])
       self.prec_and_warning_var.set(rows[9])
       self.dosage_var.set(rows[10])
       self.table_prices_var.set(rows[11])
       self.productQT_var.set(rows[12])



   def pharmacy_database_update(self):
       if self.ref_no_var.get()=="" or self.lot_no_var.get()=="" :
            messagebox.showerror("Error","All fields are required")
       else:
           conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
           mycursor1=conn.cursor()
           mycursor1.execute("update pharmacy_main_table set Company_Name=%s,Type_Of_Medicine=%s,Medicine_Name=%s,Lot_No=%s,Issue_Date=%s,Expire_Date=%s,Uses=%s,Side_Effect=%s,Prec_and_Warning=%s,Dosage=%s,Tablet_Price=%s,Product_QT=%s where Reference_No=%s", 
                                                                                                  (
                                                                                                     self.company_name_var.get(),
                                                                                                     self.type_of_medicine_var.get(),
                                                                                                     self.medicine_name_var.get(),
                                                                                                     self.lot_no_var.get(),
                                                                                                     self.issue_date_var.get(),
                                                                                                     self.expire_date_var.get(),
                                                                                                     self.uses_var.get(),
                                                                                                     self.side_effect_var.get(),
                                                                                                     self.prec_and_warning_var.get(),
                                                                                                     self.dosage_var.get(),
                                                                                                     self.table_prices_var.get(),
                                                                                                     self.productQT_var.get(),
                                                                                                     self.ref_no_var.get(),
                                                                                      ))
           conn.commit()
           self.main_data_fetch()
           conn.close()
           messagebox.showinfo("Success","Data has been updated")


   def pharmacy_database_delete(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
       mycursor1=conn.cursor()
       sql="delete from pharmacy_main_table where Reference_No=%s"
       value=(self.ref_no_var.get(),)
       mycursor1.execute(sql,value)

       conn.commit()
       self.main_data_fetch()
       conn.close()
       messagebox.showinfo("Success","selected item is deleted")
  
   def pharmacy_database_reset(self):
    #    self.ref_no_var.set("")
       self.company_name_var.set("")
    #    self.type_of_medicine_var.set("")
    #    +self.medicine_name_var.set("")
       self.lot_no_var.set("")
       self.issue_date_var.set("")
       self.expire_date_var.set("")
       self.uses_var.set("")
       self.side_effect_var.set("")
       self.prec_and_warning_var.set("")
       self.dosage_var.set("")
       self.table_prices_var.set("")
       self.productQT_var.set("")

   def search_data_main_table(self):
       if self.search_combo_var.get()=="" or self.search_combo_entry.get()=="":
            messagebox.showerror("Error","All Fields are required")
       else:
            conn=mysql.connector.connect(host="localhost",username="root",password="OnkarA@060105",database="pharmacy_management_system")
            mycursor1=conn.cursor()
            mycursor1.execute("SELECT * FROM pharmacy_main_table WHERE " + str(self.search_combo_var.get()) + " LIKE '%" + str(self.search_combo_entry.get()) + "%'")
            rows = mycursor1.fetchall()
    
            if len(rows)!=0:
                self.pharmacy_main_table.delete(*self.pharmacy_main_table.get_children())
                for i in rows:
                      self.pharmacy_main_table.insert("",END,values=i)
                conn.commit()
            conn.close() 
                 

       


if __name__=="__main__":
    root=Tk()
    app=Pharmacy_Management_System(root)
    root.mainloop()
