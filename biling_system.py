from tkinter import *
import random
import os
from tkinter import messagebox
from datetime import datetime

# ============Main Application============================


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x750+0+0")
        self.root.title("Modern Billing System")
        self.root.config(bg="#f5f6fa")

        # Modern color scheme
        self.primary_color = "#2c3e50"
        self.secondary_color = "#3498db"
        self.accent_color = "#e74c3c"
        self.bg_color = "#ecf0f1"
        self.light_color = "#ffffff"

        # Header Frame with branding
        header_frame = Frame(self.root, bg=self.primary_color, bd=0)
        header_frame.pack(fill=X)

        title = Label(header_frame, text="🛒 Modern Billing System",
                      font=('Segoe UI', 32, 'bold'),
                      bg=self.primary_color,
                      fg="white",
                      pady=15)
        title.pack(side=LEFT, padx=30)

        # Branding
        brand = Label(header_frame, text="Powered by ProjectsHub",
                      font=('Segoe UI', 10),
                      bg=self.primary_color,
                      fg="#bdc3c7",
                      pady=15)
        brand.pack(side=RIGHT, padx=30)
    # ================variables=======================
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()
    # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        # =============coldDtinks=============================
        self.sprite = IntVar()
        self.limka = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()
    # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============Customer Details Section======================
        F1 = LabelFrame(self.root, text="📋 Customer Details",
                        font=('Segoe UI', 14, 'bold'),
                        bd=8,
                        fg=self.primary_color,
                        bg=self.light_color,
                        relief=RIDGE)
        F1.place(x=10, y=100, relwidth=0.98)

        cname_lbl = Label(F1, text="Customer Name:", bg=self.light_color,
                          font=('Segoe UI', 12, 'bold'), fg=self.primary_color)
        cname_lbl.grid(row=0, column=0, padx=20, pady=12)
        cname_txt = Entry(F1, width=18, textvariable=self.c_name,
                          font=('Segoe UI', 12), bd=3, relief=SOLID)
        cname_txt.grid(row=0, column=1, pady=12, padx=10)

        cphn_lbl = Label(F1, text="Phone Number:", bg=self.light_color,
                         font=('Segoe UI', 12, 'bold'), fg=self.primary_color)
        cphn_lbl.grid(row=0, column=2, padx=20, pady=12)
        cphn_txt = Entry(F1, width=18, textvariable=self.c_phone,
                         font=('Segoe UI', 12), bd=3, relief=SOLID)
        cphn_txt.grid(row=0, column=3, pady=12, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg=self.light_color,
                           font=('Segoe UI', 12, 'bold'), fg=self.primary_color)
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=12)
        c_bill_txt = Entry(F1, width=18, textvariable=self.search_bill,
                           font=('Segoe UI', 12), bd=3, relief=SOLID)
        c_bill_txt.grid(row=0, column=5, pady=12, padx=10)

        bil_btn = Button(F1, text="🔍 Search", command=self.find_bill,
                         width=12, bd=0, font=('Segoe UI', 11, 'bold'),
                         bg=self.secondary_color, fg="white",
                         cursor="hand2", relief=FLAT, activebackground="#2980b9")
        bil_btn.grid(row=0, column=6, pady=12, padx=10)

    # ===================Medical Section====================================
        F2 = LabelFrame(self.root, text="💊 Medical Items",
                        font=('Segoe UI', 13, 'bold'),
                        bd=8, fg=self.primary_color,
                        bg=self.light_color, relief=RIDGE)
        F2.place(x=10, y=190, width=340, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('Segoe UI', 12),
                              bg=self.light_color, fg=self.primary_color)
        sanitizer_lbl.grid(row=0, column=0, padx=15, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=12, textvariable=self.sanitizer,
                              font=('Segoe UI', 12), bd=2, relief=SOLID)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('Segoe UI', 12),
                         bg=self.light_color, fg=self.primary_color)
        mask_lbl.grid(row=1, column=0, padx=15, pady=10, sticky='W')
        mask_txt = Entry(F2, width=12, textvariable=self.mask,
                         font=('Segoe UI', 12), bd=2, relief=SOLID)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('Segoe UI', 12),
                                bg=self.light_color, fg=self.primary_color)
        hand_gloves_lbl.grid(row=2, column=0, padx=15, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=12, textvariable=self.hand_gloves,
                                font=('Segoe UI', 12), bd=2, relief=SOLID)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        dettol_lbl = Label(F2, text="Dettol", font=('Segoe UI', 12),
                           bg=self.light_color, fg=self.primary_color)
        dettol_lbl.grid(row=3, column=0, padx=15, pady=10, sticky='W')
        dettol_txt = Entry(F2, width=12, textvariable=self.dettol,
                           font=('Segoe UI', 12), bd=2, relief=SOLID)
        dettol_txt.grid(row=3, column=1, padx=10, pady=10)

        newsprin_lbl = Label(F2, text="Newsprin", font=('Segoe UI', 12),
                             bg=self.light_color, fg=self.primary_color)
        newsprin_lbl.grid(row=4, column=0, padx=15, pady=10, sticky='W')
        newsprin_txt = Entry(F2, width=12, textvariable=self.newsprin,
                             font=('Segoe UI', 12), bd=2, relief=SOLID)
        newsprin_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('Segoe UI', 12),
                                bg=self.light_color, fg=self.primary_color)
        thermal_gun_lbl.grid(row=5, column=0, padx=15, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=12, textvariable=self.thermal_gun,
                                font=('Segoe UI', 12), bd=2, relief=SOLID)
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========Grocery Items Section=========================
        F3 = LabelFrame(self.root, text="🛒 Grocery Items",
                        font=('Segoe UI', 13, 'bold'),
                        bd=8, fg=self.primary_color,
                        bg=self.light_color, relief=RIDGE)
        F3.place(x=360, y=190, width=340, height=380)

        rice_lbl = Label(F3, text="Rice", font=('Segoe UI', 12),
                         bg=self.light_color, fg=self.primary_color)
        rice_lbl.grid(row=0, column=0, padx=15, pady=10, sticky='W')
        rice_txt = Entry(F3, width=12, textvariable=self.rice,
                         font=('Segoe UI', 12), bd=2, relief=SOLID)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('Segoe UI', 12),
                             bg=self.light_color, fg=self.primary_color)
        food_oil_lbl.grid(row=1, column=0, padx=15, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=12, textvariable=self.food_oil,
                             font=('Segoe UI', 12), bd=2, relief=SOLID)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('Segoe UI', 12),
                          bg=self.light_color, fg=self.primary_color)
        wheat_lbl.grid(row=2, column=0, padx=15, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=12, textvariable=self.wheat,
                          font=('Segoe UI', 12), bd=2, relief=SOLID)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=('Segoe UI', 12),
                         bg=self.light_color, fg=self.primary_color)
        daal_lbl.grid(row=3, column=0, padx=15, pady=10, sticky='W')
        daal_txt = Entry(F3, width=12, textvariable=self.daal,
                         font=('Segoe UI', 12), bd=2, relief=SOLID)
        daal_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('Segoe UI', 12),
                          bg=self.light_color, fg=self.primary_color)
        flour_lbl.grid(row=4, column=0, padx=15, pady=10, sticky='W')
        flour_txt = Entry(F3, width=12, textvariable=self.flour,
                          font=('Segoe UI', 12), bd=2, relief=SOLID)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('Segoe UI', 12),
                          bg=self.light_color, fg=self.primary_color)
        maggi_lbl.grid(row=5, column=0, padx=15, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=12, textvariable=self.maggi,
                          font=('Segoe UI', 12), bd=2, relief=SOLID)
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========Cold Drinks Section================================
        F4 = LabelFrame(self.root, text="🥤 Cold Drinks",
                        font=('Segoe UI', 13, 'bold'),
                        bd=8, fg=self.primary_color,
                        bg=self.light_color, relief=RIDGE)
        F4.place(x=710, y=190, width=340, height=380)

        sprite_lbl = Label(F4, text="Sprite", font=('Segoe UI', 12),
                           bg=self.light_color, fg=self.primary_color)
        sprite_lbl.grid(row=0, column=0, padx=15, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=12, textvariable=self.sprite,
                           font=('Segoe UI', 12), bd=2, relief=SOLID)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        limka_lbl = Label(F4, text="Limka", font=('Segoe UI', 12),
                          bg=self.light_color, fg=self.primary_color)
        limka_lbl.grid(row=1, column=0, padx=15, pady=10, sticky='W')
        limka_txt = Entry(F4, width=12, textvariable=self.limka,
                          font=('Segoe UI', 12), bd=2, relief=SOLID)
        limka_txt.grid(row=1, column=1, padx=10, pady=10)

        mazza_lbl = Label(F4, text="Mazza", font=('Segoe UI', 12),
                          bg=self.light_color, fg=self.primary_color)
        mazza_lbl.grid(row=2, column=0, padx=15, pady=10, sticky='W')
        mazza_txt = Entry(F4, width=12, textvariable=self.mazza,
                          font=('Segoe UI', 12), bd=2, relief=SOLID)
        mazza_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('Segoe UI', 12),
                         bg=self.light_color, fg=self.primary_color)
        coke_lbl.grid(row=3, column=0, padx=15, pady=10, sticky='W')
        coke_txt = Entry(F4, width=12, textvariable=self.coke,
                         font=('Segoe UI', 12), bd=2, relief=SOLID)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta", font=('Segoe UI', 12),
                          bg=self.light_color, fg=self.primary_color)
        fanta_lbl.grid(row=4, column=0, padx=15, pady=10, sticky='W')
        fanta_txt = Entry(F4, width=12, textvariable=self.fanta,
                          font=('Segoe UI', 12), bd=2, relief=SOLID)
        fanta_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_duo_lbl = Label(F4, text="Mountain Dew", font=('Segoe UI', 12),
                                 bg=self.light_color, fg=self.primary_color)
        mountain_duo_lbl.grid(row=5, column=0, padx=15, pady=10, sticky='W')
        mountain_duo_txt = Entry(F4, width=12, textvariable=self.mountain_duo,
                                 font=('Segoe UI', 12), bd=2, relief=SOLID)
        mountain_duo_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================Bill Area======================
        F5 = LabelFrame(self.root, text="📄 Bill Preview",
                        font=('Segoe UI', 13, 'bold'),
                        bd=8, fg=self.primary_color,
                        bg=self.light_color, relief=RIDGE)
        F5.place(x=1060, y=190, width=330, height=380)

        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set,
                            font=('Courier New', 10),
                            bg="#f9f9f9", fg=self.primary_color,
                            bd=2, relief=SOLID)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1, padx=5, pady=5)

    # =======================Billing Summary & Controls=============
        F6 = LabelFrame(self.root, text="💰 Billing Summary & Controls",
                        font=('Segoe UI', 13, 'bold'),
                        bd=8, fg=self.primary_color,
                        bg=self.light_color, relief=RIDGE)
        F6.place(x=10, y=580, relwidth=0.98, height=160)

        m1_lbl = Label(F6, text="Total Medical:", font=('Segoe UI', 11, 'bold'),
                       bg=self.light_color, fg=self.primary_color)
        m1_lbl.grid(row=0, column=0, padx=15, pady=8, sticky='W')
        m1_txt = Entry(F6, width=16, textvariable=self.medical_price,
                       font=('Segoe UI', 10, 'bold'), bd=2, relief=SOLID, state='readonly')
        m1_txt.grid(row=0, column=1, padx=10, pady=8)

        m2_lbl = Label(F6, text="Total Grocery:", font=('Segoe UI', 11, 'bold'),
                       bg=self.light_color, fg=self.primary_color)
        m2_lbl.grid(row=1, column=0, padx=15, pady=8, sticky='W')
        m2_txt = Entry(F6, width=16, textvariable=self.grocery_price,
                       font=('Segoe UI', 10, 'bold'), bd=2, relief=SOLID, state='readonly')
        m2_txt.grid(row=1, column=1, padx=10, pady=8)

        m3_lbl = Label(F6, text="Total Cold Drinks:", font=('Segoe UI', 11, 'bold'),
                       bg=self.light_color, fg=self.primary_color)
        m3_lbl.grid(row=2, column=0, padx=15, pady=8, sticky='W')
        m3_txt = Entry(F6, width=16, textvariable=self.cold_drinks_price,
                       font=('Segoe UI', 10, 'bold'), bd=2, relief=SOLID, state='readonly')
        m3_txt.grid(row=2, column=1, padx=10, pady=8)

        m4_lbl = Label(F6, text="Medical Tax:", font=('Segoe UI', 11, 'bold'),
                       bg=self.light_color, fg=self.primary_color)
        m4_lbl.grid(row=0, column=2, padx=15, pady=8, sticky='W')
        m4_txt = Entry(F6, width=16, textvariable=self.medical_tax,
                       font=('Segoe UI', 10, 'bold'), bd=2, relief=SOLID, state='readonly')
        m4_txt.grid(row=0, column=3, padx=10, pady=8)

        m5_lbl = Label(F6, text="Grocery Tax:", font=('Segoe UI', 11, 'bold'),
                       bg=self.light_color, fg=self.primary_color)
        m5_lbl.grid(row=1, column=2, padx=15, pady=8, sticky='W')
        m5_txt = Entry(F6, width=16, textvariable=self.grocery_tax,
                       font=('Segoe UI', 10, 'bold'), bd=2, relief=SOLID, state='readonly')
        m5_txt.grid(row=1, column=3, padx=10, pady=8)

        m6_lbl = Label(F6, text="Cold Drinks Tax:", font=('Segoe UI', 11, 'bold'),
                       bg=self.light_color, fg=self.primary_color)
        m6_lbl.grid(row=2, column=2, padx=15, pady=8, sticky='W')
        m6_txt = Entry(F6, width=16, textvariable=self.cold_drinks_tax,
                       font=('Segoe UI', 10, 'bold'), bd=2, relief=SOLID, state='readonly')
        m6_txt.grid(row=2, column=3, padx=10, pady=8)

    # =======Action Buttons======================================
        btn_f = Frame(F6, bg=self.light_color)
        btn_f.place(x=780, y=10, width=590, height=130)

        total_btn = Button(btn_f, command=self.total, text="💵 Calculate Total",
                           bg=self.secondary_color, bd=0, fg="white",
                           pady=12, width=14, font=('Segoe UI', 12, 'bold'),
                           cursor="hand2", relief=FLAT, activebackground="#2980b9")
        total_btn.grid(row=0, column=0, padx=8, pady=8)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="📋 Generate Bill",
                                  bd=0, bg="#27ae60", fg="white",
                                  pady=12, width=14, font=('Segoe UI', 12, 'bold'),
                                  cursor="hand2", relief=FLAT, activebackground="#229954")
        generateBill_btn.grid(row=0, column=1, padx=8, pady=8)

        clear_btn = Button(btn_f, command=self.clear_data, text="🔄 Clear All",
                           bg="#f39c12", bd=0, fg="white",
                           pady=12, width=14, font=('Segoe UI', 12, 'bold'),
                           cursor="hand2", relief=FLAT, activebackground="#e67e22")
        clear_btn.grid(row=1, column=0, padx=8, pady=8)

        exit_btn = Button(btn_f, command=self.exit_app, text="❌ Exit",
                          bd=0, bg=self.accent_color, fg="white",
                          pady=12, width=14, font=('Segoe UI', 12, 'bold'),
                          cursor="hand2", relief=FLAT, activebackground="#c0392b")
        exit_btn.grid(row=1, column=1, padx=8, pady=8)
        self.welcome_bill()

# ================totalBill==========================
    def total(self):
        self.m_h_g_p = self.hand_gloves.get()*12
        self.m_s_p = self.sanitizer.get()*2
        self.m_m_p = self.mask.get()*5
        self.m_d_p = self.dettol.get()*30
        self.m_n_p = self.newsprin.get()*5
        self.m_t_g_p = self.thermal_gun.get()*15
        self.total_medical_price = float(
            self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.medical_price.set("Rs. "+str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price*0.05), 2)
        self.medical_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*10
        self.g_f_o_p = self.food_oil.get()*10
        self.g_w_p = self.wheat.get()*10
        self.g_d_p = self.daal.get()*6
        self.g_f_p = self.flour.get()*8
        self.g_m_p = self.maggi.get()*5
        self.total_grocery_price = float(
            self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_d_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*5), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*10
        self.c_d_l_p = self.limka.get()*10
        self.c_d_m_p = self.mazza.get()*10
        self.c_d_c_p = self.coke.get()*10
        self.c_d_f_p = self.fanta.get()*10
        self.c_m_d = self.mountain_duo.get()*10
        self.total_cold_drinks_price = float(
            self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_medical_price+self.total_grocery_price +
                                self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

# ==============Welcome Bill Screen==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t  *** RETAIL STORE ***")
        self.txtarea.insert(END, f"\n{'='*42}")
        self.txtarea.insert(END, f"\n Bill No: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone: {self.c_phone.get()}")
        self.txtarea.insert(
            END, f"\n Date: {datetime.now().strftime('%d-%m-%Y %I:%M %p')}")
        self.txtarea.insert(END, f"\n{'='*42}")
        self.txtarea.insert(
            END, f"\n {'Product':<20} {'Qty':<6} {'Price':>10}")
        self.txtarea.insert(END, f"\n{'-'*42}")

# =========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
    # ============Medical Items===========================
        if self.sanitizer.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Sanitizer':<20} {self.sanitizer.get():<6} Rs.{self.m_s_p:>7}")
        if self.mask.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Mask':<20} {self.mask.get():<6} Rs.{self.m_m_p:>7}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Hand Gloves':<20} {self.hand_gloves.get():<6} Rs.{self.m_h_g_p:>7}")
        if self.dettol.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Dettol':<20} {self.dettol.get():<6} Rs.{self.m_d_p:>7}")
        if self.newsprin.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Newsprin':<20} {self.newsprin.get():<6} Rs.{self.m_n_p:>7}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Thermal Gun':<20} {self.thermal_gun.get():<6} Rs.{self.m_t_g_p:>7}")
    # ==============Grocery Items============================
        if self.rice.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Rice':<20} {self.rice.get():<6} Rs.{self.g_r_p:>7}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Food Oil':<20} {self.food_oil.get():<6} Rs.{self.g_f_o_p:>7}")
        if self.wheat.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Wheat':<20} {self.wheat.get():<6} Rs.{self.g_w_p:>7}")
        if self.daal.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Daal':<20} {self.daal.get():<6} Rs.{self.g_d_p:>7}")
        if self.flour.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Flour':<20} {self.flour.get():<6} Rs.{self.g_f_p:>7}")
        if self.maggi.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Maggi':<20} {self.maggi.get():<6} Rs.{self.g_m_p:>7}")
        # ================Cold Drinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Sprite':<20} {self.sprite.get():<6} Rs.{self.c_d_s_p:>7}")
        if self.limka.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Limka':<20} {self.limka.get():<6} Rs.{self.c_d_l_p:>7}")
        if self.mazza.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Mazza':<20} {self.mazza.get():<6} Rs.{self.c_d_m_p:>7}")
        if self.coke.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Coke':<20} {self.coke.get():<6} Rs.{self.c_d_c_p:>7}")
        if self.fanta.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Fanta':<20} {self.fanta.get():<6} Rs.{self.c_d_f_p:>7}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(
                END, f"\n {'Mountain Dew':<20} {self.mountain_duo.get():<6} Rs.{self.c_m_d:>7}")
            self.txtarea.insert(END, f"\n{'-'*42}")
            self.txtarea.insert(
                END, f"\n Fanta\t\t{self.newsprin.get()}\t\t{self.c_d_f_p}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(
                END, f"\n Mountain Duo\t\t{self.sanitizer.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
        # ===============Taxes & Total==============================
        if self.medical_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(
                END, f"\n Medical Tax (5%):{' '*18}{self.medical_tax.get()}")
        if self.grocery_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(
                END, f"\n Grocery Tax (5%):{' '*18}{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != 'Rs. 0.0':
            self.txtarea.insert(
                END, f"\n Cold Drinks Tax (10%):{' '*15}{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n{'='*42}")
        self.txtarea.insert(
            END, f"\n {'TOTAL BILL:':<25} Rs.{self.total_bill:>10.2f}")
        self.txtarea.insert(END, f"\n{'='*42}")
        self.txtarea.insert(END, f"\n\n   Thank you for shopping with us!")
        self.txtarea.insert(END, f"\n      Visit Again! 😊")
        self.txtarea.insert(END, f"\n   GitHub: github.com/techabbayi")
        self.save_bill()

    # =========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo(
                "Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
            return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.dettol.set(0)
            self.newsprin.set(0)
            self.thermal_gun.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.maggi.set(0)
    # =============coldDrinks=============================
            self.sprite.set(0)
            self.limka.set(0)
            self.mazza.set(0)
            self.coke.set(0)
            self.fanta.set(0)
            self.mountain_duo.set(0)
    # ====================taxes================================
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
