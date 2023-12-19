import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import sqlite3




class Login:
    
    def __init__(self, master):
        
        self.master = master
        self.frame = tk.Frame(self.master)
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.email_lbl = tk.Label(self.frame, text="Email address: ").grid(column=0, row=0)
        self.email_entr = tk.Entry(self.frame, textvariable = self.email).grid(column=1, row=0)
        self.password_lbl = tk.Label(self.frame, text="Password:").grid(column=0, row=1)
        self.password_entr = tk.Entry(self.frame, show = "*", textvariable = self.password).grid(column=1, row=1)
        self.register = tk.Button(self.frame, text="Register", width=10, command=self.registreren).grid(column=0, row=2)
        self.cancel = tk.Button(self.frame, text="Cancel", width=10, command=self.close_window).grid(column=1, row=2)
        self.login = tk.Button(self.frame, text="Login", width=10, command=self.logging_in).grid(column=2, row=2)
        self.frame.pack()
        
        
    def registreren(self):
        
        self.newWindow = tk.Toplevel(self.master)
        self.app = Register(self.newWindow)
        
        
    def close_window(self):
        
        self.master.destroy()
        
        
    def logging_in(self):
              
        email = self.email.get()
        password = self.password.get()
        conn = sqlite3.connect("Sqlite_Persoonlijkegegevens.db")
        cursor = conn.cursor()
        sql_select_query = """select password from gegevens where email = ?""" # Selects specific information from the SQLite database using the last name as identifier
        cursor.execute(sql_select_query, (email,)) 
        record = cursor.fetchone() # Selects the specific SQLite Database row which was found in the previous .execute command
        check_pw = record[0]
        if password == check_pw: # If password matches that of the one from the database (record) -> Proceed to Logged In screen
            self.newWindow = tk.Toplevel(self.master)
            self.app = LoggedIn(self.newWindow)
        else:
            messagebox.showerror("Login failed!", "Login failed!")



class Register: # Register page
    
    def __init__(self, master): # Initializes the Register page with base variables and widgets
        
        self.master = master
        self.frame = tk.Frame(self.master)
        self.email = tk.StringVar()
        self.email2 = tk.StringVar()
        self.password = tk.StringVar()
        self.lastname = tk.StringVar()
        self.name = tk.StringVar()
        self.address = tk.StringVar()
        self.hometown = tk.StringVar()
        
        
        self.email_lbl = tk.Label(self.frame, text="Email address: ").grid(column=0, row=0) 
        self.email_entr = tk.Entry(self.frame, textvariable = self.email).grid(column=1, row=0)
        
        self.email2_lbl = tk.Label(self.frame, text="Repeat email address: ").grid(column=0, row=1)
        self.email2_entr = tk.Entry(self.frame, textvariable=self.email2).grid(column=1, row=1)
        
        self.password_lbl = tk.Label(self.frame, text="Password: ").grid(column=0, row=2)
        self.password_entr = tk.Entry(self.frame, show="*", textvariable=self.password).grid(column=1, row=2)
        
        self.name_lbl = tk.Label(self.frame, text="First name: ").grid(column=0, row=3)
        self.name_entr = tk.Entry(self.frame, textvariable=self.name).grid(column=1, row=3)
        
        self.lname_lbl = tk.Label(self.frame, text="Last name: ").grid(column=0, row=4)
        self.lname_entr = tk.Entry(self.frame, textvariable=self.lastname).grid(column=1, row=4)
        
        self.adress_lbl = tk.Label(self.frame, text="Address: ").grid(column=0, row=5)
        self.adress_entr = tk.Entry(self.frame, textvariable=self.address).grid(column=1, row=5)
        
        self.hometown_lbl = tk.Label(self.frame, text="Hometown: ").grid(column=0, row=6)
        self.hometown_entr = tk.Entry(self.frame, textvariable=self.hometown).grid(column=1, row=6)
        
        
        self.quitButton = tk.Button(self.frame, text="Quit", width=10, command=self.close_window).grid(column=0, row=7)
        self.registerButton = tk.Button(self.frame, text="Register", width=10, command=self.success).grid(column=1, row=7)
        self.frame.pack()
  
  
    def success(self): # Determines if the registration was successful
        
        email = self.email.get()
        email2 = self.email2.get()
        password = self.password.get()
        lastname = self.lastname.get()
        name = self.name.get()
        address = self.address.get()
        hometown = self.hometown.get()
        
        if email == email2: # If Emails match -> Input into Database and close window
            
            messagebox.showinfo("Registration successful!", "Registration successful!")
            database(email, password, lastname, name, address, hometown)
            self.close_window()
            
        else:
            messagebox.showerror("Error!", "Email addresses do not match!")

        
        
        
    def close_window(self): # Closes the window
        
        self.master.destroy()
        
        
        
class LoggedIn: # Screen after logging in
    
    def __init__(self, master):
        
        self.master = master
        self.frame = tk.Frame(self.master)
        
        self.name = tk.StringVar()
        self.lastname = tk.StringVar()
        self.address = tk.StringVar()
        self.hometown = tk.StringVar()
        
        self.ziektes = ("Griep", "Verkouden", "Leukemie") # Values of different diseases to fit into the first listbox
        self.str_ziektes = tk.StringVar(value=self.ziektes)
        self.ziekte_listbox = tk.Listbox(self.frame, exportselection=0, listvariable=self.str_ziektes, height=10, selectmode='single') # Creates the listbox and its values
        self.ziekte_listbox.grid(column=0, row=6, pady=2, padx=2) # Places the 'ziekte' listbox
        
        self.artsen = ("Dr. Simone Groen", "Dr. Hans Bert", "Dr. Anton Grietje") # Values of different doctors for the second listbox
        self.str_artsen = tk.StringVar(value=self.artsen)
        self.arts_listbox = tk.Listbox(self.frame, exportselection=0, listvariable=self.str_artsen, height=10, selectmode='single') # Creates the listbox and its values
        self.arts_listbox.grid(column=1, row=6, pady=2, padx=2) # Places the 'arts' listbox 
        
        self.v2 = tk.StringVar()
        self.radio_db_1 = tk.Radiobutton(self.frame, text="Database", variable=self.v2, value=1, command=self.selectFile).grid(column=0, row=4, pady=5)
        self.radio_db_2 = tk.Radiobutton(self.frame, text="Bestand", variable=self.v2, value=2, command=self.selectFile).grid(column=1, row=4, pady=5)
        self.radio_db_3 = tk.Radiobutton(self.frame, text="Tekstveld", variable=self.v2, value=3).grid(column=2, row=4, pady=5)
        
        self.entr_txt = tk.StringVar()
        self.entr_tst = tk.Entry(self.frame, textvariable=self.entr_txt).grid(column=0, row=5, pady=2)
        
        self.submit_btn = tk.Button(self.frame, text="Submit", command=self.insert).grid(column=1, row=5)
        
        self.v1 = tk.StringVar()
        self.radio_db_4 = tk.Radiobutton(self.frame, text="Specialist",variable=self.v1, value=1, ).grid(column=2, row=5) #command=self.insert_arts
        self.radio_db_5 = tk.Radiobutton(self.frame, text="Ziektebeeld", variable=self.v1, value=2, ).grid(column=3, row=5) #command=self.insert_ziekte
        
        self.appointButton = tk.Button(self.frame, text="Make appointment", width=15, command=self.appointment).grid(column=0, row=7, padx=2) # Creates the appointment button that calls for the appointment function 
        
        self.lname_lbl = tk.Label(self.frame, text="Last name: ").grid(column=0, row=0)
        self.lname_entr = ttk.Combobox(self.frame, textvariable=self.lastname).grid(column=1, row=0)
        
        self.name_lbl = tk.Label(self.frame, text="First name: ").grid(column=0, row=1)
        self.name_entr = tk.Entry(self.frame, textvariable=self.name).grid(column=1, row=1)
        
        self.adress_lbl = tk.Label(self.frame, text="Address: ").grid(column=0, row=2)
        self.adress_entr = tk.Entry(self.frame, textvariable=self.address).grid(column=1, row=2)
        
        self.hometown_lbl = tk.Label(self.frame, text="Hometown: ").grid(column=0, row=3)
        self.hometown_entr = tk.Entry(self.frame, textvariable=self.hometown).grid(column=1, row=3)
        
        self.fetchButton = tk.Button(self.frame, text="Fetch", width=10, command=self.find_var).grid(column=2, row=0) # Fetches the information from the database depending on the last name filled in
        self.frame.pack()
        
        
    def find_var(self): # Finds the information in the SQLite database to autofill
    
        last_name = self.lastname.get()
        conn = sqlite3.connect("Sqlite_Persoonlijkegegevens.db")
        cursor = conn.cursor()
        sql_select_query = """select firstname, address, hometown from gegevens where lastname = ?""" # Selects specific information from the SQLite database using the last name as identifier
        cursor.execute(sql_select_query, (last_name,)) 
        record = cursor.fetchone() # Selects the specific SQLite Database row which was found in the previous .execute command
        self.name.set(record[0]) # Auto fills the first name entry field
        self.address.set(record[1]) # Auto fills the address entry field
        self.hometown.set(record[2]) # Auto fills the hometown entry field
        
    def appointment(self):
        
        arts = self.arts_listbox.get(self.arts_listbox.curselection()) # Gathers the information of the current selected value in the 'arts' listbox
        ziekte = self.ziekte_listbox.get(self.ziekte_listbox.curselection()) # Gathers the information of the current selected value in the 'ziekte' listbox
        
        bericht = "U heeft gekozen voor " + arts + " voor een behandeling voor " + ziekte # Compiles a message to send to the messagebox information popup
        messagebox.showinfo("Success!", bericht) # Sends the messagebox popup with the appointment
        
        
    def insert(self): #Inserts the values in either the 'Artsen' listbox, or the 'Ziektes' listbox
        
        insert_listbox = self.entr_txt.get() # Gathers the text put into the entry text StringVar()
        destination = self.v1.get() # Gathers the currently selected radio button to know which listbox to send to
        
        if destination == "1": # If listbox is 'Arts', send it to Arts listbox
            
            self.arts_listbox.insert(tk.END, insert_listbox)
            
        elif destination == "2": # If listbox is "Ziekte", send it to Ziekte listbox
            
            self.ziekte_listbox.insert(tk.END, insert_listbox)
            
        else: # If an error occurs, show a popup saying something went wrong
            messagebox.showerror("Error!", "Something went wrong!")
            
    
    def selectFile(self): # Selects the file using tkinter's askopenfilename command
        
        selected_file = askopenfilename() # Selects file using file explorer
        file_type = self.v2.get() # Gathers the type of file according to the radio button selected
        address = self.v1.get() # Gathers the recipient listbox according to the radio button selected
        
        if file_type == "1":
            
            if address == "2":
                
                self.checkDuplicateDiseases() # Checks for duplicate diseases
                with open(selected_file) as f:
                    
                    seen = [] # Creates the 'seen' list, used for identifying duplicate diseases
                    seen.append(self.griep) # Adds the "Griep" value already present in the 'Ziektes' listbox
                    seen.append(self.verkouden) # Adds the "Verkouden" value already present in the 'Ziektes' listbox
                    seen.append(self.leukemie) # Adds the "Leukemie" value already present in the 'Ziektes' listbox
                    
                    for line in f:
                        
                        if line not in seen: # If Disease has not been found yet
                            
                            self.ziekte_listbox.insert(tk.END, line) # Add it to the listbox
                            seen.append(line) # And add it to the seen list to avoid duplicate diseases
                            
                        else:
                            
                            pass
                        
                        
            elif address == "1":
                
                self.checkDuplicateDoctors() # Checks for duplicate doctors
                with open(selected_file) as f: # Open .txt file
                    
                    seen = [] # Create a set list
                    seen.append(self.arts1) # Adds the "Griep" value already present in the 'Ziektes' listbox
                    seen.append(self.arts2) # Adds the "Verkouden" value already present in the 'Ziektes' listbox
                    seen.append(self.arts3) # Adds the "Leukemie" value already present in the 'Ziektes' listbox
                    
                    for line in f: # Iterate each line
                        
                        if line not in seen: # If Doctor has not been seen yet
                            
                            self.arts_listbox.insert(tk.END, line) # Add it to the 'Arts' listbox
                            seen.append(line) # And add it to the seen list to avoid duplicates
                            
                        else:
                            
                            pass

                            

        elif file_type == "2": # Or if filetype is 'Bestand'
            
            if address == "2": # And Recipient is Ziekte listbox
                
                self.checkDuplicateDiseases() # Check for duplicate diseases
                with open(selected_file) as f: # Open the file
                    
                    seen = [] # Create a list
                    seen.append(self.griep) # Adds the "Griep" value already present in the 'Ziektes' listbox
                    seen.append(self.verkouden) # Adds the "Verkouden" value already present in the 'Ziektes' listbox
                    seen.append(self.leukemie) # Adds the "Leukemie" value already present in the 'Ziektes' listbox
                    
                    for line in f: # Iterate through every line of the file
                        
                        if line not in seen: # If no duplicate has been found
                            
                            self.ziekte_listbox.insert(tk.END, line) # Add it to the ziekte listbox
                            seen.append(line) # And add it to the seen list to avoid duplicates
                            
                        else:
                            
                            pass
                        
                        
            elif address == "1": # Or if the recipient is Arts listbox
                
                self.checkDuplicateDoctors() # Check for duplicate Doctors
                with open(selected_file) as f: # Open .txt file
                    
                    seen = [] # Create a set List
                    seen.append(self.arts1) # Adds the "Griep" value already present in the 'Arts' listbox
                    seen.append(self.arts2) # Adds the "Verkouden" value already present in the 'Arts' listbox
                    seen.append(self.arts3) # Adds the "Leukemie" value already present in the 'Arts' listbox
                    
                    for line in f: # Iterate each line
                        
                        if line not in seen: # If Arts not present in the set list
                            
                            self.arts_listbox.insert(tk.END, line) # Add it to Arts listbox
                            seen.append(line) # And add it to the seen list
                            
                        else:
                            
                            pass
           
        else:
            
            messagebox.showerror("Error!", "Something went wrong!") 
            
        
    def checkDuplicateDiseases(self): # Checks all of the values present in Ziekte listbox
        
        base_diseases = self.ziekte_listbox.get(0, tk.END) # Gathers all the diseases
        griep, verkouden, leukemie = base_diseases # Splits the 3 current existing values
        self.griep = griep + "\n" # Adds a breakline to avoid duplicate errors
        self.verkouden = verkouden + "\n" # Adds a breakline to avoid duplicate errors
        self.leukemie = leukemie + "\n" # Adds a breakline to avoid duplicate errors
        
        
    def checkDuplicateDoctors(self): # Checks for the doctors present in the Arts listbox
        
        base_doctors = self.arts_listbox.get(0, tk.END) # Gathers all the doctors 
        arts1, arts2, arts3 = base_doctors # Splits the 3 current existing values
        self.arts1 = arts1 + "\n" # Adds a breakline to avoid duplicate errors
        self.arts2 = arts2 + "\n" # Adds a breakline to avoid duplicate errors 
        self.arts3 = arts3 + "\n" # Adds a breakline to avoid duplicate errors
       
        
def database(email, password, lastname, name, address, hometown): # Initializes the Database and enters information
    
    create_Database()
    
    conn = sqlite3.connect("SQLite_Persoonlijkegegevens.db") # Opens SQLite Database
    with conn:
        cursor = conn.cursor()
    cursor.execute("INSERT INTO gegevens (email, password, lastname, firstname, address, hometown) VALUES(?, ?, ?, ?, ?, ?)", (email, password, lastname, name, address, hometown)) # Inserts specific variables using the given parameters
    conn.commit()


def create_Database(): # Creates Database if no such Database exists
        
    try:
        
        sqliteConnection = sqlite3.connect("SQLite_Persoonlijkegegevens.db")
        sqlite_create_adres_query = '''
            CREATE TABLE IF NOT EXISTS `gegevens` (
                `idadres` INTEGER PRIMARY KEY AUTOINCREMENT,
                `email` VARCHAR(45) NOT NULL,
                `password` VARCHAR(45) NOT NULL,
                `lastname` VARCHAR(45) NOT NULL,
                `firstname` VARCHAR(45) NOT NULL,
                `address` VARCHAR(45) NOT NULL,
                `hometown` VARCHAR(45) NOT NULL);'''
        
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite_create_adres_query)
        sqliteConnection.commit()
        cursor.close()

        
    except sqlite3.Error as error:
        
            return f"Error while creating SQLite table: {error}"
            
    finally:
        
        if sqliteConnection:
            sqliteConnection.close()


def main(): # Initializes main tkinter functionality
    
    root = tk.Tk()
    root.geometry("400x200")
    app = Login(root)
    root.mainloop()
    
if __name__ == '__main__':
    
    main()
