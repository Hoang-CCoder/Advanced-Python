import tkinter as tk
from tkinter import messagebox
import mysql.connector


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database App")

        # Database connection fields
        self.db_name = tk.StringVar(value='test')
        self.user = tk.StringVar(value='root')
        self.password = tk.StringVar(value='HuyHoang2911')
        self.host = tk.StringVar(value='127.0.0.1')
        self.port = tk.StringVar(value='3306')
        self.table_name = tk.StringVar(value='sinhvien')

        # Create the GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Connection section
        connection_frame = tk.Frame(self.root)
        connection_frame.pack(pady=10)

        tk.Label(connection_frame, text="Database Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.db_name).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(connection_frame, text="User:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.user).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Host:").grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.host).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(connection_frame, text="Port:").grid(row=1, column=2, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.port).grid(row=1, column=3, padx=5, pady=5)

        tk.Button(connection_frame, text="Create Table", command=self.create_table).grid(row=5, column = 1, columnspan=4, pady=10)

        tk.Button(connection_frame, text="Connect", command=self.connect_db).grid(row=5, column = 0, columnspan=3, pady=10)
        # Query section
        query_frame = tk.Frame(self.root)
        query_frame.pack(pady=10)

        tk.Label(query_frame, text="Table Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(query_frame, textvariable=self.table_name).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(query_frame, text="Load Data", command=self.load_data).grid(row=1, columnspan=2, pady=10)

        self.data_display = tk.Text(self.root, height=10, width=70)
        self.data_display.pack(pady=10)

        # Insert section
        insert_frame = tk.Frame(self.root)
        insert_frame.pack(pady=10)

        self.column1 = tk.StringVar()
        self.column2 = tk.StringVar()

        tk.Label(insert_frame, text="Ho ten:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.column1).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(insert_frame, text="MSSV:").grid(row=0, column=2, padx=5, pady=5)
        tk.Entry(insert_frame, textvariable=self.column2).grid(row=0, column=3, padx=5, pady=5)

        tk.Button(insert_frame, text="Insert Data", command=self.insert_data).grid(row=2, columnspan=4, pady=10)


    def connect_db(self):
        try:
            # Connect to MySQL
            self.conn = mysql.connector.connect(
                database=self.db_name.get(),
                user=self.user.get(),
                password=self.password.get(),
                host=self.host.get(),
                port=self.port.get()
            )
            self.cur = self.conn.cursor()
            messagebox.showinfo("Success", "Connected to the database successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def load_data(self):
        try:
            query = f"SELECT * FROM {self.table_name.get()}"
            self.cur.execute(query)
            rows = self.cur.fetchall()
            self.data_display.delete(1.0, tk.END)
            for row in rows:
                self.data_display.insert(tk.END, f"{row}\n")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

    def insert_data(self):
        try:
            insert_query = f"INSERT INTO {self.table_name.get()} (hoten, MSSV) VALUES (%s, %s)"
            data_to_insert = (self.column1.get(), self.column2.get())
            self.cur.execute(insert_query, data_to_insert)
            self.conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

    def create_table(self):
        try:
            # Create a table in the connected database
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {self.table_name.get()} (
                    sinhvien_ID INT NOT NULL AUTO_INCREMENT,
                    hoten VARCHAR(50) NOT NULL,
                    MSSV VARCHAR(20) NOT NULL,
                    PRIMARY KEY (sinhvien_ID)
                ) ENGINE=InnoDB;
            """
            self.cur.execute(create_table_query)
            self.conn.commit()
            messagebox.showinfo("Success", f"Table '{self.table_name.get()}' created successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error creating table: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
