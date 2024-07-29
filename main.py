import re
import tkinter as tk
from tkinter import messagebox


#complete the functions below

def login():
    username_input = username_entry.get()
    password_input = password_entry.get()
    with open("logincredentials.txt", "r+") as registering:      
      file_info = registering.read()
      file_info = re.split("\n|,", file_info)
      for tokens in file_info:
        k = file_info.index(tokens)
        file_info[k] = file_info[k].strip()
      if username_input in file_info and password_input in file_info:
        messagebox.showinfo("LOGIN SUCCESFUL", "You have successfully logged in! Welcome back!")
      else:
        messagebox.showerror("INVALID USER/PASS", "Invalid username or password.")
      


def register():  
    username_input = username_entry.get()
    password_input = password_entry.get()
  # 
    checking_for_spaces = any(stuff.isspace() for stuff in password_input)
    again_checking_for_spaces = any(stuff.isspace() for stuff in username_input)
  # 
    if username_input == "" or password_input == "" or checking_for_spaces or again_checking_for_spaces:
      messagebox.showerror("SPACE ERROR", "Username or password cannot contain spaces.")
    else:
      with open("logincredentials.txt", "r+") as registering:
        file_info = registering.read()
        file_info = re.split("\n|,", file_info)
        for tokens in file_info:
          k = file_info.index(tokens)
          file_info[k] = file_info[k].strip()
          print(k)
        # 
        uppercase = any(stuff.isupper() for stuff in password_input)
        lowercase = any(stuff.islower() for stuff in password_input)
        numbers = any(stuff.isdigit() for stuff in password_input)
        # 
        if uppercase and lowercase and numbers:
          if username_input not in file_info:
            print(username_input + ", " + password_input, file=registering)
            messagebox.showinfo("REGISTER SUCCESSFUL", "You have successfully registered")
          else:
            messagebox.showerror("USERNAME ERROR", "This username already exists.")
        else: 
          messagebox.showerror("PASSWORD ERROR", "Password is invalid. The password must contain at least one capital letter, lowercase letter and number")

      
    # You can replace these with your own registration logic

with open("logincredentials.txt", "r") as login_info:
  list_of_login_info = login_info.readlines()
  index_counter = 0
  for items in list_of_login_info:
    list_of_login_info[index_counter] = list_of_login_info[index_counter].strip("\n")
    index_counter += 1




def alpha_sorter(list):
  holder = list.copy() #we create another list called holder that is the exact same as "list"
  another_list = [] #we create an empty list called "another list"
  for i in range(0,len(holder)): #indented code repeats for as many times as the length of the list "holder" (hence range(0,len(holder)))
    y = holder[0] #y is the item at index 0 of holdler
    t = 0 #t is our index counter 
    while t < len(holder): #while t is less than the length of holder (t is less than the amount of items in holder) the indented code is performed
      if y > holder[t]: #the program checks if y, which starts off as the first item in the list, comes sooner in the alphabet than holder[t]
        y = holder[t] #if y comes before alphabetically, then the value of y becomes the value of the item at index t. This means that if my program finds any item in the list that comes before alphabetically than the item currently in y, which starts off as the first item in the list, the value of y becomes that item. Esentially, we start off with the first item and compare it with every other item, and everytime we find one that comes before we use that one to compare with the list items instead. 
      t += 1 #increase the value of the index counter by 1 to access the next list item
    index_of_highest_integer = holder.index(y) #now that we have gone through for every item in the list and have stored the biggest in y we assign the index of that value to a variable called index_of_highest_integer
    holder.pop(index_of_highest_integer) #we remove the item that comes before all the other ones from the original list so that when the code continues all over again it can find the next largest item
    another_list.append(y) #we add the item into another list, and when we keep finding the item that comes first alphabetically, and add it to this list eventuallly we create a new list with all the values of the ooriginal list in alphabetical order!
    if len(holder) == 0: #if there are no items in our list we break out of the while loop
      break
  return another_list #in the end once there are no items left in our original list we return our new list with the items in max to min order

print(alpha_sorter(list_of_login_info))



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
######DO NOT EDIT ANY OF THE CODE BELOW. It is not necessary to understand############
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Create the main window
root = tk.Tk()
root.geometry("300x200") 
root.title("Login Screen")

# Create and place entry boxes and buttons on the window
username_label = tk.Label(root, text="Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

login_button = tk.Button(root, text="Register", command=register)
login_button.pack()

# Start the main loop
username_entry.delete(0, tk.END)
password_entry.delete(0, tk.END)
username_entry.insert(0, "d")
password_entry.insert(0, "a1C")
login()

username_entry.delete(0, tk.END)
password_entry.delete(0, tk.END)
username_entry.insert(0, "a")
password_entry.insert(0, "a1a")
register()

username_entry.delete(0, tk.END)
password_entry.delete(0, tk.END)
username_entry.insert(0, "b")
password_entry.insert(0, "aAB")
register()

username_entry.delete(0, tk.END)
password_entry.delete(0, tk.END)
username_entry.insert(0, "c")
password_entry.insert(0, "B1A")
register()

username_entry.delete(0, tk.END)
password_entry.delete(0, tk.END)
username_entry.insert(0, "d")
password_entry.insert(0, "a1C")
register()


login()

username_entry.delete(0, tk.END)
password_entry.delete(0, tk.END)
username_entry.insert(0, "d")
password_entry.insert(0, "a1C")
register()

with open("logincredentials.txt", 'r') as f:
  s = f.read().split("\n")
  for i in range(0,len(s)):
    s[i]=s[i].replace(" ", "")

print("\n\ntests")
print("a,a1a" not in s)
print("b,aAB" not in s)
print("c,B1A" not in s)
print("d,a1C" in s)
print(s.count("d,a1C")==1)



# Start the main loop
root.mainloop()


#perfect! 5/5
