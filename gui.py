import customtkinter as ctk


def save_info_and_switch_screen(screen_name, info_to_save):
    saved_info[screen_name] = info_to_save

    show_screen(screen_name)


def show_screen(screen_name):
    for screen in screens.values():
        screen.pack_forget()

    screens[screen_name].pack()


def add_buttons_to_screen2():


    country_options = ["Great Britain", "The Netherlands", "the United States of America"]
    for button_text in country_options:
        button = ctk.CTkButton(master=screens["screen2"], text=button_text, command=lambda
        button_text=button_text: save_info_and_switch_screen("screen2", button_text))
        button.pack(pady=12, padx=10)


root = ctk.CTk()
root.geometry("800x600")

screens = {}
screens["screen1"] = ctk.CTkFrame(master=root)
screens["screen2"] = ctk.CTkFrame(master=root)

saved_info = {"screen1": None, "screen2": None}

category_options = ["Business", "Entertainment", "General", "Health", "Science", "Sport", "Technology"]


for category in category_options:
    button = ctk.CTkButton(master=root, text=category,
                           command=lambda category=category: save_info_and_switch_screen("screen1", category))
    button.pack(pady=12, padx=10)


show_screen("screen1")


def use_selected_options():
    selected_option_screen1 = saved_info["screen1"]
    selected_option_screen2 = saved_info["screen2"]


    print("Selected option from screen 1:", selected_option_screen1)
    print("Selected option from screen 2:", selected_option_screen2)



use_button = ctk.CTkButton(master=root, text="Use Selected Options", command=use_selected_options)
use_button.pack(pady=12, padx=10)

root.mainloop()
