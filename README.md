# 🛒 Modern Billing System

A sleek, user-friendly billing system built with Python and Tkinter for retail stores, medical shops, and grocery stores. This application streamlines the billing process with an intuitive interface and automated calculations.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)



---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
- [Product Categories](#-product-categories)
- [Bill Storage](#-bill-storage)
- [Tax Calculations](#-tax-calculations)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## ✨ Features

### Core Features
- ✅ **Modern UI Design** - Clean, professional interface with contemporary color scheme
- ✅ **Multiple Product Categories** - Medical, Grocery, and Cold Drinks sections
- ✅ **Automatic Calculations** - Instant price and tax calculations
- ✅ **Bill Generation** - Professional bill format with all details
- ✅ **Bill Search** - Quick search and retrieval of saved bills
- ✅ **Data Persistence** - Automatic bill saving to text files
- ✅ **User-Friendly** - Intuitive design with emoji icons and clear labels

### Advanced Features
- 📅 **Date & Time Stamps** - Automatic timestamp on every bill
- 💰 **Tax Management** - Different tax rates for different categories
- 🔍 **Bill Lookup** - Search bills by bill number
- 🔄 **Clear Function** - Reset all fields with one click
- 📄 **Bill Preview** - Real-time bill preview before saving
- 🎨 **Responsive Design** - Optimized layout for better user experience

---

## 📸 Screenshots

### Main Interface
The application features a modern, clean interface divided into sections:
- Customer details input
- Three product categories (Medical, Grocery, Cold Drinks)
- Real-time bill preview
- Billing summary with tax calculations
- Action buttons for operations

---

## 📖 How to Use

### Step 1: Enter Customer Details
1. **Customer Name** - Enter the customer's full name
2. **Phone Number** - Enter the customer's contact number
3. **Bill Number** - Auto-generated unique bill number (you can also search existing bills here)

### Step 2: Add Products
Navigate through three categories and enter quantities:

#### 💊 Medical Items
- Sanitizer (Rs. 2 per unit)
- Mask (Rs. 5 per unit)
- Hand Gloves (Rs. 12 per unit)
- Dettol (Rs. 30 per unit)
- Newsprin (Rs. 5 per unit)
- Thermal Gun (Rs. 15 per unit)

#### 🛒 Grocery Items
- Rice (Rs. 10 per kg)
- Food Oil (Rs. 10 per liter)
- Wheat (Rs. 10 per kg)
- Daal (Rs. 6 per kg)
- Flour (Rs. 8 per kg)
- Maggi (Rs. 5 per packet)

#### 🥤 Cold Drinks
- Sprite (Rs. 10 per bottle)
- Limka (Rs. 10 per bottle)
- Mazza (Rs. 10 per bottle)
- Coke (Rs. 10 per bottle)
- Fanta (Rs. 10 per bottle)
- Mountain Dew (Rs. 10 per bottle)

### Step 3: Calculate Total
Click the **"💵 Calculate Total"** button to:
- Calculate subtotal for each category
- Apply respective tax rates
- Display totals in the summary section

### Step 4: Generate Bill
Click the **"📋 Generate Bill"** button to:
- Display formatted bill in the preview area
- Show all purchased items with quantities and prices
- Include tax breakdowns
- Show final total amount

### Step 5: Save Bill
- A dialog box will ask if you want to save the bill
- Click **"Yes"** to save the bill as a text file
- Bills are saved in the `bills` folder with the bill number as filename

### Step 6: Search Bills
1. Enter the bill number in the **"Bill Number"** field
2. Click **"🔍 Search"** button
3. The bill will be displayed in the preview area if found

### Step 7: Clear Data
- Click **"🔄 Clear All"** to reset all fields
- Confirm the action when prompted
- A new bill number will be generated automatically

### Step 8: Exit Application
- Click **"❌ Exit"** to close the application
- Confirm exit when prompted

---

## 📦 Product Categories

### Medical Products (Tax: 5%)
| Product | Price | Description |
|---------|-------|-------------|
| Sanitizer | Rs. 2 | Hand sanitizer bottle |
| Mask | Rs. 5 | Disposable face mask |
| Hand Gloves | Rs. 12 | Disposable gloves pair |
| Dettol | Rs. 30 | Antiseptic liquid |
| Newsprin | Rs. 5 | Pain relief medicine |
| Thermal Gun | Rs. 15 | Temperature checker |

### Grocery Items (Tax: 5%)
| Product | Price | Description |
|---------|-------|-------------|
| Rice | Rs. 10/kg | Premium rice |
| Food Oil | Rs. 10/L | Cooking oil |
| Wheat | Rs. 10/kg | Whole wheat |
| Daal | Rs. 6/kg | Lentils |
| Flour | Rs. 8/kg | All-purpose flour |
| Maggi | Rs. 5 | Instant noodles |

### Cold Drinks (Tax: 10%)
| Product | Price | Description |
|---------|-------|-------------|
| Sprite | Rs. 10 | Lemon-lime soda |
| Limka | Rs. 10 | Lemon drink |
| Mazza | Rs. 10 | Mango drink |
| Coke | Rs. 10 | Cola drink |
| Fanta | Rs. 10 | Orange drink |
| Mountain Dew | Rs. 10 | Citrus drink |

---

## 💾 Bill Storage

### File Format
- Bills are saved as `.txt` files
- Filename format: `{bill_number}.txt`
- Location: `bills/` folder in the project directory

### Bill Structure
```
          *** RETAIL STORE ***
       Powered by ProjectsHub
==========================================
 Bill No: 1234
 Customer: John Doe
 Phone: 1234567890
 Date: 20-10-2025 02:30 PM
==========================================
 Product              Qty    Price
------------------------------------------
 Sanitizer            2      Rs.     4
 Rice                 5      Rs.    50
 Sprite               3      Rs.    30
------------------------------------------
 Medical Tax (5%):              Rs. 0.2
 Grocery Tax (5%):              Rs. 2.5
 Cold Drinks Tax (10%):         Rs. 3.0
==========================================
 TOTAL BILL:                Rs.    89.70
==========================================

   Thank you for shopping with us!
      Visit Again! 😊
```

---

## 💰 Tax Calculations

### Tax Rates
- **Medical Products**: 5% GST
- **Grocery Items**: 5% GST
- **Cold Drinks**: 10% GST

### Calculation Formula
```python
Medical Tax = Total Medical Price × 0.05
Grocery Tax = Total Grocery Price × 0.05
Cold Drinks Tax = Total Cold Drinks Price × 0.10

Final Bill = (Medical + Grocery + Cold Drinks) + (All Taxes)
```

### Example
```
Medical Items:    Rs. 100  → Tax: Rs. 5
Grocery Items:    Rs. 200  → Tax: Rs. 10
Cold Drinks:      Rs. 150  → Tax: Rs. 15
-------------------------------------------
Subtotal:         Rs. 450
Total Tax:        Rs. 30
-------------------------------------------
FINAL TOTAL:      Rs. 480
```

---

## 🎨 UI Features

### Color Scheme
- **Primary Color**: `#2c3e50` (Dark Blue-Gray)
- **Secondary Color**: `#3498db` (Blue)
- **Accent Color**: `#e74c3c` (Red)
- **Background**: `#ecf0f1` (Light Gray)
- **Surface**: `#ffffff` (White)

### Typography
- **Primary Font**: Segoe UI
- **Bill Font**: Courier New (monospace)
- **Font Sizes**: 10pt - 32pt (responsive)

### Interactive Elements
- Hover effects on buttons
- Modern flat design
- Emoji icons for better UX
- Readonly fields for calculated values
- Responsive button states

---

## 🛠️ Technical Details

### Technologies Used
- **Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Date/Time**: datetime module
- **File I/O**: Built-in Python file handling
- **Random**: For bill number generation

### File Structure
```
billing-system/
│
├── biling_system.py      # Main application file
├── README.md             # This file
├── bills/                # Saved bills directory
│   ├── 1001.txt
│   ├── 1002.txt
│   └── ...
└── requirements.txt      # Dependencies (if any)
```

### Code Architecture
- **Class-based Design**: Single `Bill_App` class
- **Event-driven**: Button callbacks and event handlers
- **Modular Functions**: Separate methods for each operation
- **State Management**: Tkinter variables for data binding

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Ideas
- Add more product categories
- Implement database support (SQLite)
- Add PDF export functionality
- Create user authentication
- Add inventory management
- Multi-language support
- Dark mode theme
- Print functionality

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Bhanu Sree**


### Acknowledgments
- Built with ❤️ using Python and Tkinter
- Inspired by modern retail management systems
- Part of the 270 Python Projects collection

---


