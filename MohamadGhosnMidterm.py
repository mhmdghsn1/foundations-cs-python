import json
import tkinter as tk
from tkinter import messagebox

class Tab:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.is_active = False
        self.nested_tabs = []

    def open(self):
        self.is_active = True

    def close(self):
        self.is_active = False


tabs = []
current_tab = None


def open_tab(tab_title, tab_url):
    new_tab = Tab(tab_title, tab_url)
    new_tab.open()
    tabs.append(new_tab)


def close_tab(tab_index):
    if 0 <= tab_index < len(tabs):
        tabs[tab_index].close()
        del tabs[tab_index]


def switch_tab(index):
    global current_tab
    if index is None:
        current_tab = None
        messagebox.showinfo("Switch Tab", "No tabs are open.")
    elif 0 <= index < len(tabs):
        current_tab = tabs[index]
        messagebox.showinfo("Switch Tab", f"Switched to tab: {current_tab.title}")
    else:
        messagebox.showerror("Switch Tab", "Invalid tab index. Try again...")


def display_tab_content():
    if current_tab is not None:
        messagebox.showinfo("Tab Content", f"Title: {current_tab.title}\nURL: {current_tab.url}")
    else:
        messagebox.showinfo("Tab Content", "Nothing is open.")


def display_all_tabs(tabs_list, level=0):
    tabs_info = []
    for i, tab in enumerate(tabs_list):
        tabs_info.append("\t" * level + str(i) + "_" + tab.title)
        if len(tab.nested_tabs) > 0:
            nested_tabs_info = display_all_tabs(tab.nested_tabs, level + 1)
            tabs_info.extend(nested_tabs_info)
    return tabs_info


def open_nested_tab(parent_index, title, url):
    if 0 <= parent_index < len(tabs):
        tab = Tab(title, url)
        tabs[parent_index].nested_tabs.append(tab)
        messagebox.showinfo("Open Nested Tab", "Nested tab added successfully.")
    else:
        messagebox.showerror("Open Nested Tab", "Invalid parent tab index.")


def clear_all_tabs():
    global tabs, current_tab
    tabs = []
    current_tab = None
    messagebox.showinfo("Clear Tabs", "All tabs cleared.")


def save_tabs():
    file_path = messagebox.askstring("Save Tabs", "Enter file path to save the tabs:")
    if file_path:
        with open(file_path, "w") as file:
            json.dump(tabs, file)
        messagebox.showinfo("Save Tabs", "Tabs saved successfully.")


def import_tabs():
    file_path = messagebox.askstring("Import Tabs", "Enter file path to import tabs:")
    if file_path:
        with open(file_path, "r") as file:
            tabs_data = json.load(file)
            global tabs, current_tab
            tabs = tabs_data
            current_tab = None
        messagebox.showinfo("Import Tabs", "Tabs imported successfully.")


def open_tab_clicked():
    title = entry_title.get()
    url = entry_url.get()
    open_tab(title, url)


def close_tab_clicked():
    tab_index = int(entry_tab_index.get())
    close_tab(tab_index)


def switch_tab_clicked():
    index = entry_tab_index.get()
    if index == "":
        index = len(tabs) - 1
    else:
        index = int(index)
    switch_tab(index)


def display_tab_content_clicked():
    display_tab_content()


def display_all_tabs_clicked():
    tabs_info = display_all_tabs(tabs)
    messagebox.showinfo("All Tabs", "\n".join(tabs_info))


def open_nested_tab_clicked():
    parent_index = int(entry_parent_index.get())
    title = entry_nested_title.get()
    url = entry_nested_url.get()
    open_nested_tab(parent_index, title, url)


def clear_all_tabs_clicked():
    clear_all_tabs()


def save_tabs_clicked():
    save_tabs()


def import_tabs_clicked():
    import_tabs()


root = tk.Tk()
root.title("Tab Manager")

label_title = tk.Label(root, text="Title:")
label_title.grid(row=0, column=0, sticky=tk.W)
entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1)

label_url = tk.Label(root, text="URL:")
label_url.grid(row=1, column=0, sticky=tk.W)
entry_url = tk.Entry(root)
entry_url.grid(row=1, column=1)

button_open_tab = tk.Button(root, text="Open Tab", command=open_tab_clicked)
button_open_tab.grid(row=2, column=0, pady=10)

label_tab_index = tk.Label(root, text="Tab Index:")
label_tab_index.grid(row=3, column=0, sticky=tk.W)
entry_tab_index = tk.Entry(root)
entry_tab_index.grid(row=3, column=1)

button_close_tab = tk.Button(root, text="Close Tab", command=close_tab_clicked)
button_close_tab.grid(row=4, column=0)

button_switch_tab = tk.Button(root, text="Switch Tab", command=switch_tab_clicked)
button_switch_tab.grid(row=4, column=1)

button_display_tab_content = tk.Button(root, text="Display Tab Content", command=display_tab_content_clicked)
button_display_tab_content.grid(row=5, column=0, pady=10)

button_display_all_tabs = tk.Button(root, text="Display All Tabs", command=display_all_tabs_clicked)
button_display_all_tabs.grid(row=5, column=1)

label_parent_index = tk.Label(root, text="Parent Index:")
label_parent_index.grid(row=6, column=0, sticky=tk.W)
entry_parent_index = tk.Entry(root)
entry_parent_index.grid(row=6, column=1)

label_nested_title = tk.Label(root, text="Nested Title:")
label_nested_title.grid(row=7, column=0, sticky=tk.W)
entry_nested_title = tk.Entry(root)
entry_nested_title.grid(row=7, column=1)

label_nested_url = tk.Label(root, text="Nested URL:")
label_nested_url.grid(row=8, column=0, sticky=tk.W)
entry_nested_url = tk.Entry(root)
entry_nested_url.grid(row=8, column=1)

button_open_nested_tab = tk.Button(root, text="Open Nested Tab", command=open_nested_tab_clicked)
button_open_nested_tab.grid(row=9, column=0, pady=10)

button_clear_all_tabs = tk.Button(root, text="Clear All Tabs", command=clear_all_tabs_clicked)
button_clear_all_tabs.grid(row=9, column=1)

button_save_tabs = tk.Button(root, text="Save Tabs", command=save_tabs_clicked)
button_save_tabs.grid(row=10, column=0)

button_import_tabs = tk.Button(root, text="Import Tabs", command=import_tabs_clicked)
button_import_tabs.grid(row=10, column=1)

root.mainloop()