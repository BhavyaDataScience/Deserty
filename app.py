import streamlit as st
import pandas as pd

# Load the menu data from a CSV file
@st.cache_data  
def load_menu_data():
    menu_df = pd.read_csv('waffels_menu.csv')
    return menu_df

menu_df = load_menu_data()

def main():
    st.title("Waffles Menu Chatbot")

    st.write("Welcome to our waffles menu chatbot. How can I assist you today?")

    category_key = "category"  # Unique key for category selection widget
    menu_item_key = "menu_item"  # Unique key for menu item selection widget

    while True:
        # User input for category selection
        category = st.selectbox("Please select a category:", menu_df['Category'].unique(), key=category_key)

        filtered_menu = menu_df[menu_df['Category'] == category]

        # User input for menu item selection
        menu_item = st.selectbox("Please select a menu item:", filtered_menu['Menu'], key=menu_item_key)

        menu_item_details = filtered_menu[filtered_menu['Menu'] == menu_item]

        if not menu_item_details.empty:
            st.write("Menu Item Details:")
            st.write("Price:", menu_item_details['Price'].values[0])
            st.write("Offer:", menu_item_details['Offer'].values[0] if not pd.isnull(menu_item_details['Offer'].values[0]) else "-")
            st.write("Description:", menu_item_details['Description'].values[0] if not pd.isnull(menu_item_details['Description'].values[0]) else "-")
        else:
            st.write("Sorry, that menu item is not available.")

        # Ask if the user wants to continue or exit
        continue_chat = st.button("Continue", disabled=st.session_state.get("disabled", True))

        if not continue_chat:
            break

    st.write("Thank you for using our chatbot. Have a great day!")

if __name__ == "__main__":
    main()
