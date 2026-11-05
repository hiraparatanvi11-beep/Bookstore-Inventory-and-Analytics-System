"""
Bookstore Inventory and Analytics System
Practical Exam Project

"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
INVENTORY_FILE = BASE_DIR / "inventory.csv"
SALES_FILE = BASE_DIR / "sales.csv"
CHARTS_DIR = BASE_DIR / "charts"


class Bookstore:
    """Manage bookstore inventory, sales, reports, and visualizations."""

    def __init__(self):
        self.inventory = self._load_inventory()
        self.sales = self._load_sales()

    def _load_inventory(self):
        if INVENTORY_FILE.exists():
            df = pd.read_csv(INVENTORY_FILE)
        else:
            df = pd.DataFrame(columns=["Title", "Author", "Genre", "Price", "Quantity"])
        required = ["Title", "Author", "Genre", "Price", "Quantity"]
        for col in required:
            if col not in df.columns:
                df[col] = "" if col in ["Title", "Author", "Genre"] else 0
        df["Price"] = pd.to_numeric(df["Price"], errors="coerce").fillna(0.0)
        df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0).astype(int)
        return df[required]

    def _load_sales(self):
        if SALES_FILE.exists():
            df = pd.read_csv(SALES_FILE)
        else:
            df = pd.DataFrame(columns=["Date", "Title", "Quantity Sold", "Total Revenue"])
        required = ["Date", "Title", "Quantity Sold", "Total Revenue"]
        for col in required:
            if col not in df.columns:
                df[col] = "" if col in ["Date", "Title"] else 0
        df["Quantity Sold"] = pd.to_numeric(df["Quantity Sold"], errors="coerce").fillna(0).astype(int)
        df["Total Revenue"] = pd.to_numeric(df["Total Revenue"], errors="coerce").fillna(0.0)
        return df[required]

    def _save_data(self):
        self.inventory.to_csv(INVENTORY_FILE, index=False)
        self.sales.to_csv(SALES_FILE, index=False)

    def add_book(self, title, author, genre, price, quantity):
        if not title.strip() or not author.strip() or not genre.strip():
            raise ValueError("Title, author, and genre cannot be empty.")
        if price <= 0 or quantity < 0:
            raise ValueError("Price must be positive and quantity cannot be negative.")

        matches = self.inventory["Title"].str.casefold() == title.strip().casefold()
        if matches.any():
            raise ValueError("This book already exists. Use Update Stock instead.")

        new_row = pd.DataFrame([{
            "Title": title.strip(), "Author": author.strip(), "Genre": genre.strip(),
            "Price": float(price), "Quantity": int(quantity)
        }])
        self.inventory = pd.concat([self.inventory, new_row], ignore_index=True)
        self._save_data()
        print("Book added successfully.")

    def remove_book(self, title):
        matches = self.inventory["Title"].str.casefold() == title.strip().casefold()
        if not matches.any():
            print("Book not found.")
            return
        self.inventory = self.inventory.loc[~matches].reset_index(drop=True)
        self._save_data()
        print("Book removed successfully.")

    def update_inventory(self, title, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        matches = self.inventory["Title"].str.casefold() == title.strip().casefold()
        if not matches.any():
            print("Book not found.")
            return
        self.inventory.loc[matches, "Quantity"] = int(quantity)
        self._save_data()
        print("Stock updated successfully.")

    def record_sale(self, title, quantity):
        if quantity <= 0:
            raise ValueError("Sale quantity must be greater than zero.")
        matches = self.inventory["Title"].str.casefold() == title.strip().casefold()
        if not matches.any():
            print("Book not found.")
            return
        index = self.inventory.index[matches][0]
        available = int(self.inventory.loc[index, "Quantity"])
        if quantity > available:
            print(f"Not enough stock. Available quantity: {available}")
            return

        price = float(self.inventory.loc[index, "Price"])
        revenue = price * quantity
        self.inventory.loc[index, "Quantity"] = available - quantity
        new_sale = pd.DataFrame([{
            "Date": pd.Timestamp.today().strftime("%Y-%m-%d"),
            "Title": self.inventory.loc[index, "Title"],
            "Quantity Sold": int(quantity),
            "Total Revenue": float(revenue)
        }])
        self.sales = pd.concat([self.sales, new_sale], ignore_index=True)
        self._save_data()
        print(f"Sale recorded. Revenue: ₹{revenue:.2f}")

    def generate_report(self):
        print("\n========== BOOKSTORE REPORT ==========")
        print(f"Books in inventory: {len(self.inventory)}")
        print(f"Total units in stock: {self.inventory['Quantity'].sum()}")
        stock_value = (self.inventory["Price"] * self.inventory["Quantity"]).sum()
        print(f"Inventory value: ₹{stock_value:.2f}")
        total_revenue = self.sales["Total Revenue"].sum()
        print(f"Total sales revenue: ₹{total_revenue:.2f}")

        if not self.inventory.empty:
            average_price = np.mean(self.inventory["Price"].to_numpy())
            print(f"Average book price: ₹{average_price:.2f}")
        else:
            print("Average book price: N/A")

        if not self.sales.empty:
            top_book = self.sales.groupby("Title")["Quantity Sold"].sum().idxmax()
            top_quantity = self.sales.groupby("Title")["Quantity Sold"].sum().max()
            print(f"Best-selling book: {top_book} ({top_quantity} copies)")
        else:
            print("Best-selling book: No sales recorded")
        print("=====================================\n")

    def analyze_sales(self):
        if self.sales.empty:
            print("No sales data available for analysis.")
            return
        sales = self.sales.copy()
        sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")
        sales = sales.dropna(subset=["Date"])
        if sales.empty:
            print("Sales dates are invalid; please check sales.csv.")
            return

        sales["Month"] = sales["Date"].dt.to_period("M").astype(str)
        print("\nSales by book:")
        print(sales.groupby("Title")[["Quantity Sold", "Total Revenue"]].sum()
              .sort_values("Quantity Sold", ascending=False))
        print("\nSales by month:")
        print(sales.groupby("Month")["Total Revenue"].sum())

    def create_visualizations(self):
        if self.inventory.empty:
            print("Add books to inventory before creating charts.")
            return
        if self.sales.empty:
            print("Record at least one sale before creating charts.")
            return

        CHARTS_DIR.mkdir(exist_ok=True)
        sns.set_theme()

        # Bar chart: total sales by genre
        sales_by_title = self.sales.groupby("Title")["Quantity Sold"].sum().reset_index()
        chart_data = sales_by_title.merge(self.inventory[["Title", "Genre"]], on="Title", how="left")
        genre_sales = chart_data.groupby("Genre")["Quantity Sold"].sum().sort_values(ascending=False)
        plt.figure(figsize=(8, 5))
        genre_sales.plot(kind="bar")
        plt.title("Total Books Sold by Genre")
        plt.xlabel("Genre")
        plt.ylabel("Copies Sold")
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / "sales_by_genre.png")
        plt.close()

        # Line graph: monthly revenue
        monthly = self.sales.copy()
        monthly["Date"] = pd.to_datetime(monthly["Date"], errors="coerce")
        monthly = monthly.dropna(subset=["Date"])
        monthly["Month"] = monthly["Date"].dt.to_period("M").astype(str)
        monthly_revenue = monthly.groupby("Month")["Total Revenue"].sum().sort_index()
        plt.figure(figsize=(8, 5))
        monthly_revenue.plot(kind="line", marker="o")
        plt.title("Monthly Sales Revenue")
        plt.xlabel("Month")
        plt.ylabel("Revenue (₹)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / "monthly_sales.png")
        plt.close()

        # Pie chart: revenue share by genre
        revenue_title = self.sales.groupby("Title")["Total Revenue"].sum().reset_index()
        revenue_genre = revenue_title.merge(self.inventory[["Title", "Genre"]], on="Title", how="left")
        genre_revenue = revenue_genre.groupby("Genre")["Total Revenue"].sum()
        if genre_revenue.sum() > 0:
            plt.figure(figsize=(7, 7))
            genre_revenue.plot(kind="pie", autopct="%1.1f%%", ylabel="")
            plt.title("Revenue Share by Genre")
            plt.tight_layout()
            plt.savefig(CHARTS_DIR / "revenue_share.png")
            plt.close()

        # Heatmap: correlation between price, quantity, and sold quantity
        heat_data = self.inventory[["Price", "Quantity"]].copy()
        sold = self.sales.groupby("Title")["Quantity Sold"].sum()
        heat_data["Quantity Sold"] = self.inventory["Title"].map(sold).fillna(0)
        corr = heat_data.corr(numeric_only=True)
        plt.figure(figsize=(6, 5))
        sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
        plt.title("Inventory and Sales Correlation")
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / "correlation_heatmap.png")
        plt.close()

        print(f"Charts saved in: {CHARTS_DIR}")

    def show_inventory(self):
        if self.inventory.empty:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            print(self.inventory.to_string(index=False))


def get_number(prompt, integer=False):
    while True:
        try:
            value = float(input(prompt))
            if integer:
                if not value.is_integer():
                    raise ValueError
                return int(value)
            return value
        except ValueError:
            print("Please enter a valid number.")


def main():
    store = Bookstore()
    while True:
        print("""
========== BOOKSTORE INVENTORY SYSTEM ==========
1. Add book
2. Remove book
3. Update stock quantity
4. Record a sale
5. Show inventory
6. Generate report
7. Analyze sales
8. Create visualizations
9. Exit
================================================
""")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                title = input("Book title: ")
                author = input("Author: ")
                genre = input("Genre: ")
                price = get_number("Price (₹): ")
                quantity = get_number("Quantity: ", integer=True)
                store.add_book(title, author, genre, price, quantity)
            elif choice == "2":
                store.remove_book(input("Book title to remove: "))
            elif choice == "3":
                title = input("Book title: ")
                quantity = get_number("New stock quantity: ", integer=True)
                store.update_inventory(title, quantity)
            elif choice == "4":
                title = input("Book title sold: ")
                quantity = get_number("Quantity sold: ", integer=True)
                store.record_sale(title, quantity)
            elif choice == "5":
                store.show_inventory()
            elif choice == "6":
                store.generate_report()
            elif choice == "7":
                store.analyze_sales()
            elif choice == "8":
                store.create_visualizations()
            elif choice == "9":
                store._save_data()
                print("Data saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please select from the menu.")
        except ValueError as error:
            print(f"Input error: {error}")


if __name__ == "__main__":
    main()
