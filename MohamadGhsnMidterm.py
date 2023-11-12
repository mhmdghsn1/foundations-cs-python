import json


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
        print("No tabs are open.")
    elif 0 <= index < len(tabs):
        current_tab = tabs[index]
        print("Switched to tab:", current_tab.title)
    else:
        print("Invalid tab index. Try again...")


def display_tab_content():
    if current_tab is not None:
        print("Title:", current_tab.title)
        print("URL:", current_tab.url)
    else:
        print("Nothing is open.")


def display_all_tabs(tabs_list, level=0):
    for i, tab in enumerate(tabs_list):
        print("\t" * level, i, "_", tab.title)
        if len(tab.nested_tabs) > 0:
            display_all_tabs(tab.nested_tabs, level + 1)


def open_nested_tab():
    parent_index = int(input("Please enter the index of the parent tab: "))
    if 0 <= parent_index < len(tabs):
        title = input("Please enter the title of the nested tab: ")
        url = input("Please enter the URL of the nested tab: ")
        tab = Tab(title, url)
        tabs[parent_index].nested_tabs.append(tab)
    else:
        print("Invalid input...")


def clear_all_tabs():
    global tabs, current_tab
    tabs = []
    current_tab = None
    print("Done!")


def save_tabs():
    file_path = input("Enter file path to save the tabs: ")
    with open(file_path, "w") as file:
        json.dump(tabs, file)
    print("Done!")


def import_tabs():
    file_path = input("Enter file path to import tabs: ")
    with open(file_path, "r") as file:
        tabs_data = json.load(file)
        global tabs, current_tab
        tabs = tabs_data
        current_tab = None
    print("Done!")


def main():
    while True:
        print("Welcome!")
        print("1. Open tab")
        print("2. Close tab")
        print("3. Switch tab")
        print("4. Display all tabs")
        print("5. Open nested tab")
        print("6. Clear all tabs")
        print("7. Save tabs")
        print("8. Import Tabs")
        print("9. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter the title of the new tab: ")
            url = input("Enter the URL of the new tab: ")
            open_tab(title, url)
        elif choice == 2:
            tab_index = int(input("Enter the index to close: "))
            close_tab(tab_index)
        elif choice == 3:
            index = input("Enter the index: ")
            if index == "":
                index = len(tabs) - 1
            else:
                index = int(index)
            switch_tab(index)
        elif choice == 4:
            display_all_tabs(tabs)
        elif choice == 5:
            open_nested_tab()
        elif choice == 6:
            clear_all_tabs()
        elif choice == 7:
            save_tabs()
        elif choice == 8:
            import_tabs()
        elif choice == 9:
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")


main()
