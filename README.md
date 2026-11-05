# 📚 Bookstore Inventory and Analytics System

## 🐍 Python Practical Exam / Final Project

**👩‍💻 Developed By: Tanvi Hirapara**

A Python-based command-line application to manage a bookstore's inventory and sales. This project stores book details in CSV files, tracks stock and sales, generates inventory reports, analyzes sales performance, and creates visual charts using Python libraries.

## 🎯 Project Objectives

- 📖 Maintain book details such as title, author, genre, price, and quantity.
- ➕ Add new books to the inventory.
- ❌ Remove books from the inventory.
- ✏️ Update stock quantities.
- 🛒 Record book sales and calculate revenue.
- 📋 View current inventory and generate summary reports.
- 📊 Analyze sales by book and by month.
- 📈 Create charts to understand sales and inventory data.

## ✨ Features

### 📚 1. Book Inventory Management

- ➕ Add a new book.
- ❌ Remove a book using its title.
- ✏️ Update the stock quantity.
- 📋 Display the current inventory.

### 🛒 2. Sales Management

- 💰 Record a sale by entering the book title and quantity sold.
- 📦 Reduce inventory stock after a successful sale.
- 🧮 Calculate and display revenue for the sale.
- 🚫 Prevent sales when sufficient stock is unavailable.

### 📊 3. Reports and Analytics

- 📋 Generate an inventory report containing:
  - 📚 Number of books in inventory
  - 📦 Total units in stock
  - 💰 Total inventory value
- 📖 Analyze sales by book.
- 📅 Analyze monthly sales revenue.
- 🏆 Identify the best-selling book.

### 📈 4. Data Visualization

The application creates charts and saves them in the `charts` folder:

| Symbol | Chart File | Description |
|---|---|---|
| 📊 | `sales_by_genre.png` | Sales grouped by genre |
| 📈 | `monthly_sales.png` | Monthly sales trend |
| 💰 | `revenue_share.png` | Revenue share visualization |
| 🔥 | `correlation_heatmap.png` | Correlation between numeric data |

## 🛠️ Technologies Used

The following technologies and libraries are used to develop this project:

### 🐍 1. Python
Used for developing the main application, managing inventory, processing sales, and handling user input.

### 🐼 2. Pandas
Used for reading, writing, managing, and analyzing CSV data.

### 🔢 3. NumPy
Used for numerical calculations and mathematical operations.

### 📊 4. Matplotlib
Used for creating graphs and charts to visualize sales and inventory data.

### 🎨 5. Seaborn
Used for creating attractive statistical visualizations and correlation heatmaps.

### 📁 6. CSV Files
Used for storing book inventory details and sales transaction records.

### 💻 7. Visual Studio Code (VS Code)
Used as the code editor for writing and executing the Python program.

### 🖥️ 8. Python Terminal
Used to run the application and interact with the menu-driven system.

## 📂 Project Files

```text
📁 Bookstore_Project/
│
├── 🐍 bookstore_system.py
├── 📁 inventory.csv
├── 📁 sales.csv
├── 📄 README.md
└── 📁 charts/
    ├── 📊 sales_by_genre.png
    ├── 📈 monthly_sales.png
    ├── 💰 revenue_share.png
    └── 🔥 correlation_heatmap.png
```

## 💻 Requirements

Install Python 3.10 or later.

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

## 🚀 How to Run the Project

1. 📂 Open the project folder in Visual Studio Code.
2. 💻 Open the terminal in the project folder.
3. 📦 Install the required libraries.
4. ▶️ Run the Python application.

```bash
python bookstore_system.py
```

5. 📋 Select an option from the displayed menu.
6. ✅ Follow the instructions shown on the screen.

## 📋 Main Menu

📚 **BOOKSTORE MANAGEMENT SYSTEM**

1. ➕ Add Book
2. ❌ Remove Book
3. ✏️ Update Stock Quantity
4. 🛒 Record a Sale
5. 📚 Show Inventory
6. 📋 Generate Report
7. 📊 Analyze Sales
8. 📈 Create Visualizations
9. 🚪 Exit

# 🖥️ Sample Output

The following is a sample demonstration of the project's output.


### ➕ Option 1 — Add Book

```text
📚 Enter Book Title: Python Programming
✍️ Enter Author Name: James
🎭 Enter Genre: Education
💰 Enter Price: 550
📦 Enter Quantity: 12

✅ Book added successfully!
```

### ❌ Option 2 — Remove Book

```text
📚 Enter Book Title to Remove: Data Science

✅ Book removed successfully!
```

### ✏️ Option 3 — Update Stock Quantity

```text
📚 Enter Book Title: Python Basics
📦 Enter New Quantity: 20

✅ Stock quantity updated successfully!
```

### 🛒 Option 4 — Record a Sale

```text
📚 Enter Book Title: Python Basics
🛒 Enter Quantity Sold: 2

🧾 SALES RECEIPT

Book Name       : Python Basics
Quantity Sold   : 2
Price Per Book  : ₹450.00
Total Revenue   : ₹900.00

✅ Sale recorded successfully!
📦 Remaining Stock: 8
```

### 📚 Option 5 — Show Inventory

```text
📚 BOOK INVENTORY

Title              Author          Genre       Price    Quantity
Python Basics      John Smith      Education   450.00      10
Data Science       Alex Brown      Technology  650.00       8
The Alchemist      Paulo Coelho     Fiction     350.00      15
Rich Dad Poor Dad  Robert Kiyosaki  Finance     500.00       6

✅ Inventory displayed successfully!
```

### 📋 Option 6 — Generate Report

```text
📊 INVENTORY REPORT

📚 Total Books       : 4
📦 Total Units       : 39
💰 Inventory Value   : ₹17,150.00

✅ Report generated successfully!
```

### 📊 Option 7 — Analyze Sales

```text
📈 SALES ANALYSIS

📚 Best Selling Book : Python Basics
🛒 Total Units Sold  : 2
💰 Total Revenue     : ₹900.00

📅 Monthly Sales Revenue:

November 2026 : ₹900.00

🏆 Best-selling book identified successfully!
```

### 📈 Option 8 — Create Visualizations

```text
📊 DATA VISUALIZATION

📊 Sales by Genre
📈 Monthly Sales Trend
💰 Revenue Share
🔥 Correlation Heatmap

✅ All charts generated successfully!

📁 Charts saved in the 'charts' folder:

✔ sales_by_genre.png
✔ monthly_sales.png
✔ revenue_share.png
✔ correlation_heatmap.png
```

### 🚪 Option 9 — Exit

```text
📚 BOOKSTORE SYSTEM

🙏 Thank you for using our system!
👋 Exiting the application...
```

## 📁 CSV Data Format

### 📚 `inventory.csv`

The inventory file contains the following columns:

```csv
Title,Author,Genre,Price,Quantity
```

Each row represents one book.

### 🛒 `sales.csv`

The sales file stores recorded transactions. The application reads this file for sales analysis and reports.

## 📊 Using the Visualization Feature

1. ▶️ Run the program.
2. 📚 Add or confirm that inventory data is available.
3. 🛒 Make sure sales records are available.
4. Select **8 — Create Visualizations**.
5. 📂 Open the `charts` folder.
6. 🖼️ View the generated PNG chart files.

## ⚠️ Notes

- 📁 Keep `inventory.csv` and `sales.csv` in the same folder as the Python script.
- ✍️ Book titles should be entered consistently.
- 📦 A sale can only be recorded when sufficient stock is available.
- 📊 The `charts` folder and chart images are generated when the visualization option runs successfully.
- 💾 Inventory and sales data are stored using CSV files.

## 🎓 Conclusion

The **Bookstore Inventory and Analytics System** provides a simple and efficient way to manage bookstore stock and sales using Python.

This project combines:

- 📚 Book Inventory Management
- 🛒 Sales Management
- 📊 Data Analysis
- 📈 Data Visualization
- 📁 CSV File Handling

It helps users maintain inventory, record transactions, calculate revenue, generate reports, and visualize sales performance.

🚀 **This project demonstrates the practical application of Python programming, data handling, and data visualization.**

## 🙏 Thank You

**👩‍💻 Developed By: Tanvi Hirapara**

📚 **Bookstore Inventory and Analytics System**

*Developed with Python 🐍 and Data Analytics 📊*