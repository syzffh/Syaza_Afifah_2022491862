import tkinter as tk
import mysql.connector

# Connect MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Meal_Box"
)

mycursor = mydb.cursor()

# Coding and Calculation
def collect_data():
    Box_Type =box_var.get()
    Total_Box = int(box_entry.get())
    User_First_Name = str(user_first_name_entry.get())
    User_Last_Name= str(user_last_name_entry.get())

    # The price
    Price = {
        "Box A": 15,
        "Box B": 25,
        "Box C": 28,
    }


    # Calculate the total price.
    Total_Price = (Price[Box_Type] * Total_Box)
    
    # To insert Data to database
    sql = "INSERT INTO `meal_box` (User_First_Name, User_Last_Name, Box_Type, Total_Box, Price) VALUES (%s, %s, %s, %s, %s)"
    val = (User_First_Name, User_Last_Name, Box_Type, Total_Box, Total_Price)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back the output.
    output_label.config(text=f"Name: { User_First_Name} {User_Last_Name} \nBox Type: {Box_Type} \nTotal Box: {Total_Box} \nTotal Price: RM{Total_Price}")


# Main window.
root = tk.Tk()
root.title("Meal Box")
root.geometry('600x700')


# Page Title
label = tk.Label(root, text='Order Meal Box Prices', font=("Imprint MT Shadow",14, "bold"))
label.pack(ipadx=20, ipady=20)


# Prices List 
prices_text = tk.Text(root, height=13, width=62)
prices_text.pack(pady=20)

# The defined list
prices_text.insert(tk.END, "Box Type & Prices:\n\n")
prices_text.insert(tk.END, "Box A: 2 Chicken Sandwich, Mix Fruits, Salad \nPrice: RM15\n\n")
prices_text.insert(tk.END, "Box B: Chicken Rice, Crispy Wanton, Mix Fruits \nPrice: RM25\n\n")
prices_text.insert(tk.END, "Box C: Spaghetti Aglio Olio, 3 pieces of Chicken Wings, Salad \nPrice: RM28\n\n")
prices_text.insert(tk.END, "Important!\nState the order amount in the box pack using numbers only")
prices_text.configure(state='disabled')

# Box Type Dropdown (Label)
box_label = tk.Label(root, text="Choose your box type:")
box_label.pack()

# Box Type Dropdown
box_var = tk.StringVar(root)
box_var.set("Select Meal Box")
box_dropdown = tk.OptionMenu(root, box_var, "Box A", "Box B", "Box C")
box_dropdown.pack(pady=10)


# Box Entry. Label and user can insert data thru entry
box_label = tk.Label(root, text="Total Box:")
box_label.pack()
box_entry = tk.Entry(root)
box_entry.pack()

#User First Name Type Dropdown
user_first_name_entry=tk.Label(root, text="Insert your first name:")
user_first_name_entry.pack()
user_first_name_entry=tk.Entry(root)
user_first_name_entry.pack()

#User Last Name Type Dropdown
user_last_name_entry=tk.Label(root, text="Insert your last name:")
user_last_name_entry.pack()
user_last_name_entry=tk.Entry(root)
user_last_name_entry.pack()

# Save Button
save_button = tk.Button (root, text="Calculate", command=collect_data)
save_button.pack(pady=10)

# Output Label & Result
label = tk.Label(root, text='Total Price Meal Box:', font=("Imprint MT Shadow",12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
