# Instructions  
```

create a file called "login credentials.txt"
then choose option 1 or option 2 (your grade will not depend on which option you chose)

Option 1 (with graphics)

**Note: the main.py file is already set up so that...
If you run the main.py file you will see that it looks like a login screen
When the register button is clicked, the register() function is called
When the login button is clicked, the login() function is called

Finish the register and login functions so that the program does the following...

When the registe button is clicked, the program should add a new line to the login credentials file to store that user's login info unless the username or password is invalid
the new line should have the format: username, password
username is whatever text was in the username box at the time register was clicked
password is whatever text was in the password box at the time register was clicked

The function "username_entry.get()" returns the text in the username box
The function "password_entry.get()" returns the text in the password box


the username is invalid if the file already contains that username
the password is invalid if it does not contain at least one capital letter, one lowercase letter, and one number

When the login button is clicked, the program should check if the username and password combo is valid (ie. is contained somewhere in the login credentials file). If the combo is valid it should open an info box containing a welcome message. If the combo is not valid, it should open an error box saying "invalid username or password"

for a successful login, use the following function to display the success message: 
messagebox.showinfo("title", "message") 
replace title and message with the text you wish to display

for an unsuccessful login, use the following function to display the success message: 
messagebox.showerror("title", "message")
replace title and message with the text you wish to display









Option 2 (no graphics)
Delete all of the code in the main.py file

prompt the user for a username
prompt the user for a password
prompt the user to enter 'L' for login if they have already signed up, or 'R' to register if they have not yet created an account

When "R" is entered, the program should add a new line to the login credentials file to store that user's login info unless the username or password is invalid
the new line should have the format: username, password

the username is invalid if the file already contains that username
the password is invalid if it does not contain at least one capital letter, one lowercase letter, and one number

When "L" is entered, the program should check if the username and password combo is valid (ie. an exact match is contained somewhere in the login credentials file). If the combo is valid your program should print a welcome message to the console. If the combo is not valid, the program should print a failure message to the console

```

  