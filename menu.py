import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# Load the menu data from a CSV file
@st.cache_data
def load_menu_data():
    menu_df = pd.read_csv('waffels_menu.csv')
    return menu_df

menu_df = load_menu_data()

def main():

    # Navigation bar
    menu = ["Home", "Menu", "About Us", "Contact Us"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        st.title("Welcome to Desserty")
        # Display advertisements
        st.header("Advertisements")
        st.image("images/coco.jpg", use_column_width=True)
        st.image("images/heart.jpg", use_column_width=True)
        st.image("images/stick.jpg", use_column_width=True)

    elif choice == "Menu":
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
            continue_chat = st.button("Continue")

            if not continue_chat:
                break

    elif choice == "About Us":
        st.header("About Us")
        st.write(""" 
        Welcome to Two Young Boys' Dessert Waffles! We are a dessert waffle shop that has been delighting taste buds for the past 7 months. Our journey began with a shared passion for creating delicious and irresistible waffle creations that bring joy to people's lives.

Our story starts with two young boys, Alex and Mark, who dreamt of creating a place where people could indulge in the most decadent and mouthwatering dessert waffles. With their enthusiasm and love for culinary adventures, they embarked on a journey to turn their vision into a reality.

From the very beginning, our mission has been to craft waffles that not only satisfy your sweet cravings but also provide a memorable experience. We believe that every bite should be a moment of pure delight, filled with flavors that transport you to a world of sweet indulgence.

At Two Young Boys' Dessert Waffles, we take pride in our commitment to quality and taste. We source only the finest ingredients, ensuring that every waffle is made with care and precision. Our waffle batter is prepared fresh daily, resulting in a light and fluffy texture that melts in your mouth.

But it doesn't stop there. What truly sets us apart is our creativity and innovation when it comes to toppings and flavors. We are constantly experimenting with unique combinations, pushing the boundaries of traditional waffle recipes. From classic favorites like maple syrup and whipped cream to extravagant choices like chocolate ganache and fresh fruit compotes, our menu offers something for everyone.

Beyond the culinary delights, we also strive to create a warm and inviting atmosphere for our customers. Step into our cozy shop, and you'll be greeted with the sweet aroma of freshly baked waffles and a friendly smile. We believe that enjoying a delicious dessert should be an experience that brings people together, whether it's with friends, family, or loved ones.

As we reflect on the past 7 months, we are grateful for the incredible support we have received from our loyal customers. Your enthusiasm and feedback have motivated us to continuously improve and innovate. We are committed to delivering excellence in every waffle we serve, ensuring that each visit to Two Young Boys' Dessert Waffles is filled with sweet memories.

Thank you for being a part of our journey. We invite you to indulge in our delightful waffle creations and join us in celebrating the joy of dessert. Come and experience the magic of Two Young Boys' Dessert Waffles – where passion meets sweetness!

---

Please note that this is a fictional essay and can be further customized to fit the specific details and characteristics of your dessert waffle business.
        
        """)

    elif choice == "Contact Us":
        st.header("Contact Us")
        st.write("Phone: ☎️ +91887982324 / +917021953342")
        st.write("Address: 📍Dahisar East, Mumbai 400068")
        st.components.v1.html("""
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3766.6490565726644!2d72.86214687487862!3d19.254120681987416!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b1c3cecb80e9%3A0xd9179dd2ecdd442b!2sJari%20mari%20dahisar%20East%20garden!5e0!3m2!1sen!2sin!4v1687358917753!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>            width="600"
            height="450"
            style="border:0;"
            allowfullscreen=""
            loading="lazy">
        </iframe>
    """)

if __name__ == "__main__":
    main()
