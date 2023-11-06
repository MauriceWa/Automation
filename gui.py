import customtkinter as ctk


def save_info_and_switch_screen(screen_name, info_to_save):
    # Save the information for the selected screen
    saved_info[screen_name] = info_to_save

    # Switch to the selected screen
    show_screen(screen_name)


def show_screen(screen_name):
    # Hide all screens
    for screen in screens.values():
        screen.pack_forget()

    # Show the selected screen
    screens[screen_name].pack()


def add_buttons_to_screen2():
    # Clear existing buttons on screen2


    # Add three buttons to screen2 based on the selected category
    country_options = ["Great Britain", "The Netherlands", "the United States of America"]
    for button_text in country_options:
        button = ctk.CTkButton(master=screens["screen2"], text=button_text, command=lambda
            button_text=button_text: save_info_and_switch_screen("screen2", button_text))
        button.pack(pady=12, padx=10)


# Create the main application window
root = ctk.CTk()
root.geometry("800x600")

# Create screens as frames
screens = {}
screens["screen1"] = ctk.CTkFrame(master=root)
screens["screen2"] = ctk.CTkFrame(master=root)

# Dictionary to store information for each screen
saved_info = {"screen1": None, "screen2": None}

# Define category options
category_options = ["Business", "Entertainment", "General", "Health", "Science", "Sport", "Technology"]

# Create buttons for 7 categories
for category in category_options:
    button = ctk.CTkButton(master=root, text=category,
                           command=lambda category=category: save_info_and_switch_screen("screen1", category))
    button.pack(pady=12, padx=10)

# Define country options


# Initially show the first screen
show_screen("screen1")


# Function to use the selected options
def use_selected_options():
    selected_option_screen1 = saved_info["screen1"]
    selected_option_screen2 = saved_info["screen2"]

    # Use the selected options in other functions or print them
    print("Selected option from screen 1:", selected_option_screen1)
    print("Selected option from screen 2:", selected_option_screen2)


# Create a button to use the selected options
use_button = ctk.CTkButton(master=root, text="Use Selected Options", command=use_selected_options)
use_button.pack(pady=12, padx=10)

root.mainloop()
