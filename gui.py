import customtkinter as ctk


def save_info_and_switch_screen(screen_name, info_to_save):
    # Save the information here
    saved_info[screen_name] = info_to_save

    # Switch to the selected screen
    show_screen(screen_name)

    # Add three buttons to screen2 based on the selected category
    add_buttons_to_screen2(info_to_save)




def show_screen(screen_name):
    # Hide all screens
    for screen in screens.values():
        screen.pack_forget()

    # Show the selected screen
    screens[screen_name].pack()


def add_buttons_to_screen2(category):
    # Clear existing buttons on screen2
    for widget in screens["screen2"].winfo_children():
        widget.destroy()

    # Add three buttons to screen2 based on the selected category
    buttons_for_category = ["Great Britain", "The Netherlands", "the United States of America"]
    for button_text in buttons_for_category:
        button = ctk.CTkButton(master=screens["screen2"], text=button_text, command=lambda
        button_text=button_text: save_info_and_switch_screen("screen1", button_text))
        button.pack(pady=12, padx=10)


# Create the main application window
root = ctk.CTk()
root.geometry("800x600")

# Create screens as frames
screens = {}
screens["screen1"] = ctk.CTkFrame(master=root)
screens["screen2"] = ctk.CTkFrame(master=root)

# Dictionary to store information for each category
saved_info = {}

# Create buttons for 7 categories
categories = ["Business", "Entertainment", "General", "Health", "Science", "Sport", "Technology"]
for category in categories:
    button = ctk.CTkButton(master=root, text=category,
                           command=lambda category=category: save_info_and_switch_screen("screen2", category))
    button.pack(pady=12, padx=10)

# Initially show the first screen
show_screen("screen1")


root.mainloop()

print(saved_info)
print(saved_info["1"])