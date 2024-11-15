import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import numpy as np

# Load the data
data = pd.read_csv("pakistan_tourism_data.csv")
df = pd.DataFrame(data)

# Add custom CSS for the navbar
st.markdown("""
    <style>
        body {
        text-align: justify;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
   /* Navbar container */
    .navbar {
        background-color: #ffffff36;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    
    /* Navbar links */
    .navbar a {
        margin: 0 20px;
        text-decoration: none;
        color: #ffff;
        font-weight: 500;
        font-size: 18px;
        transition: color 0.3s ease, background-color 0.3s ease;
        padding: 8px 16px;
        border-radius: 5px;
    }

    /* Hover effect */
    .navbar a:hover {
        color: #ffffff;
        background-color: #007bff4d;
    }

    /* Active link style */
    .navbar a.active {
        color: #ffffff;
        background-color: #007bff4d;
    }
    </style>
     <div class="navbar">
        <a href="#home" class="active">Home</a>
        <a href="#about">About</a>
        <a href="#certifications">Certifications</a>
        <a href="#contact">Contact</a>
    </div>
""", unsafe_allow_html=True)


def display_home():
    st.title("Welcome to the Pakistan Tourism Dashboard")
    st.markdown("Explore the tourism data of Pakistan with interactive visualizations!")
    st.markdown("""This dashboard provides insights into various aspects of tourism in Pakistan. 
        Use the navigation bar to explore different analyses and visualizations.""")

# Function to handle user login/logout
def handle_login_logout():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        if st.button("Logout"):
            logout()
    else:
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        if st.button("Login"):
            if username == "nadir" and password == "321": 
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
            else:
                st.error("Invalid credentials. Please try again.")

def logout():
    st.session_state.logged_in = False
    st.success("Logged out successfully!")

# Function to display Total Number of Tourists by City
def display_tourists_by_city():
    st.header("Total Number of Tourists by City")
    tourists_by_city = df.groupby('City')['Number of Tourists'].sum().sort_values()
    fig, ax = plt.subplots()
    tourists_by_city.plot(kind='barh', color='skyblue', ax=ax)
    ax.set_title('Total Number of Tourists by City', fontsize=16)
    ax.set_xlabel('Number of Tourists', fontsize=12)
    ax.set_ylabel('City', fontsize=12)
    ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)
    st.write("### Summary Statistics")
    st.write(tourists_by_city.describe())

# Function to display Tourist Satisfaction by Accommodation
def display_satisfaction_accommodation():
    st.header("Tourist Satisfaction by Accommodation")
    satisfaction_accommodation = df.groupby('Accommodation Type')['Tourist Satisfaction Rating'].mean()
    fig, ax = plt.subplots()
    satisfaction_accommodation.plot(kind='bar', color='coral', rot=45, ax=ax)
    ax.set_title('Average Tourist Satisfaction by Accommodation Type', fontsize=16)
    ax.set_xlabel('Accommodation Type', fontsize=12)
    ax.set_ylabel('Average Satisfaction Rating', fontsize=12)
    st.pyplot(fig)
    st.write("### Summary Statistics")
    st.write(satisfaction_accommodation.describe())

# Function to display Monthly Trend of Tourists
def display_monthly_trend():
    st.header("Monthly Trend of Tourists")
    monthly_tourists = df.groupby('Month')['Number of Tourists'].sum()
    fig, ax = plt.subplots()
    monthly_tourists.plot(kind='line', marker='o', color='green', ax=ax)
    ax.set_title('Monthly Trend of Tourists', fontsize=16)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Number of Tourists', fontsize=12)
    ax.grid(True)
    ax.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))
    st.pyplot(fig)
    st.write("### Summary Statistics")
    st.write(monthly_tourists.describe())

# Function to display Top 3 Cities by Tourism Revenue
def display_top_cities_revenue():
    st.header("Top 3 Cities by Tourism Revenue")
    revenue_by_city = (df.groupby('City')['Revenue Generated (PKR)'].sum() / 280).sort_values(ascending=False).head(3)
    fig, ax = plt.subplots()
    revenue_by_city.plot(kind='bar', color='purple', ax=ax)
    ax.set_title('Top 3 Cities by Tourism Revenue', fontsize=16)
    ax.set_xlabel('City', fontsize=12)
    ax.set_ylabel('Revenue Generated (USD)', fontsize=12)
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'${int(x):,}'))
    st.pyplot(fig)
    st.write("### Summary Statistics")
    st.write(revenue_by_city.describe())

# Function to display Distribution of Tourist Expenditures
def display_expenditure_distribution():
    st.header("Distribution of Tourist Expenditures")
    fig, ax = plt.subplots()
    plt.hist(df['Tourist Expenditure (PKR)'], bins=20, color='orange', edgecolor='black')
    ax.set_title('Distribution of Tourist Expenditures', fontsize=16)
    ax.set_xlabel('Tourist Expenditure (PKR)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.grid(True)
    st.pyplot(fig)

# Function to display Tourist Count by Weather Condition
def display_weather_condition():
    st.header("Tourist Count by Weather Condition")
    tourists_by_weather = df.groupby('Weather Condition')['Number of Tourists'].sum()
    fig, ax = plt.subplots()
    tourists_by_weather.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.tab10.colors, ax=ax)
    ax.set_ylabel('')
    ax.set_title('Tourist Count by Weather Condition', fontsize=16)
    st.pyplot(fig)

# Function to display Peak Tourist Season
def display_peak_tourist_season():
    st.header("Tourists per Month (Peak Season Analysis)")
    monthly_tourists = df.groupby('Month')['Number of Tourists'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    monthly_tourists.plot(kind='bar', color='teal', ax=ax)
    ax.set_title('Tourists per Month (Peak Season Analysis)', fontsize=16)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Number of Tourists', fontsize=12)
    st.pyplot(fig)
    peak_month = monthly_tourists.idxmax()
    st.write(f"The peak tourist month is: {peak_month}")

# Function to display Revenue Contribution by Tourist Type
def display_revenue_by_tourist_type():
    st.header("Revenue Contribution by Tourist Type")
    revenue_by_tourist_type = df.groupby('Tourist Type')['Revenue Generated (PKR)'].sum()
    fig, ax = plt.subplots()
    revenue_by_tourist_type.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.tab20.colors, startangle=140, ax=ax)
    ax.set_ylabel('')
    ax.set_title('Revenue Contribution by Tourist Type', fontsize=16)
    st.pyplot(fig)

# Function to display Top 5 Cities by Tourist Expenditure
def display_top_cities_expenditure():
    st.header("Top 5 Cities by Tourist Expenditure")
    expenditure_by_city = (df.groupby('City')['Tourist Expenditure (PKR)'].sum() / 280).sort_values(ascending=False).head(5)
    fig, ax = plt.subplots()
    expenditure_by_city.plot(kind='bar', color='darkorange', ax=ax)
    ax.set_title('Top 5 Cities by Tourist Expenditure', fontsize=16)
    ax.set_xlabel('City', fontsize=12)
    ax.set_ylabel('Total Expenditure (USD)', fontsize=12)
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    st.pyplot(fig)

# Function to display Tourist Transport Mode Preference
def display_transport_mode():
    st.header("Tourist Transport Mode Preference")
    transport_mode = df.groupby('Transport Mode Preference')['Number of Tourists'].sum()
    
    fig, ax = plt.subplots()
    transport_mode.plot(kind='bar', rot=0, ax=ax)
    ax.set_title('Transport Mode Preference', fontsize=16)
    ax.set_xlabel('Transport Mode', fontsize=12)
    ax.set_ylabel('Number of Tourists', fontsize=12)
    
    for i, count in enumerate(transport_mode):
        ax.text(i, count + 0.1, str(count), ha='center', va='bottom')
    st.pyplot(fig)

# Function to display Total Tourists by Year
def display_total_tourists_by_year():
    st.header("Total Tourists by Year")
    total_tourists = df.groupby('Year')['Number of Tourists'].sum()
    
    fig, ax = plt.subplots()
    plt.scatter(["2021", "2022", "2023"], total_tourists.values, color='blue', s=100, edgecolor='black', alpha=0.7)
    ax.set_title("Total Tourists by Year", fontsize=16)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Number of Tourists", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    for x, y in zip(["2021", "2022", "2023"], total_tourists.values):
        ax.text(x, y + 50, str(y), ha='center', va='bottom')
    st.pyplot(fig)
def display_total_revenue():
    st.header("Total Revenue Generated by Tourism")
    total_revenue = df['Revenue Generated (PKR)'].sum()    
    st.subheader(f"Total Revenue: PKR {total_revenue:,.0f} (USD {total_revenue / 280:,.0f})")

st.header("Home")
st.write("""
    Welcome to my Streamlit project! This app is a demonstration of my skills and knowledge gained from the 
    PITP Certified Python Course at IBA Sukkur. Here, you can explore different sections and learn more about my journey
    in Python programming. I'm excited to share this project with you!
""")




# Main logic to run the app
def main():
    # Create a top navigation bar
    st.title("Pakistan Tourism Data Dashboard")
    menu = ["Home",
            "Total Number of Tourists by City",
            "Tourist Satisfaction by Accommodation",
            "Monthly Trend of Tourists",
            "Top 3 Cities by Tourism Revenue",
            "Distribution of Tourist Expenditures",
            "Tourist Count by Weather Condition",
            "Peak Tourist Season",
            "Revenue Contribution by Tourist Type",
            "Top 5 Cities by Tourist Expenditure",
            "Tourist Transport Mode Preference",
            "Total Tourists by Year",
            "Total Revenue"]
    
    selected_option = st.selectbox("Select Analysis", menu)

    handle_login_logout()

    if st.session_state.logged_in:
        if selected_option == "Home":
            display_home()
        elif selected_option == "Total Number of Tourists by City":
            display_tourists_by_city()
        # Add additional conditions for other analysis functions...
        elif selected_option == "Total Number of Tourists by City":
            display_tourists_by_city()
        elif selected_option == "Tourist Satisfaction by Accommodation":
            display_satisfaction_accommodation()
        elif selected_option == "Monthly Trend of Tourists":
            display_monthly_trend()
        elif selected_option == "Top 3 Cities by Tourism Revenue":
            display_top_cities_revenue()
        elif selected_option == "Distribution of Tourist Expenditures":
            display_expenditure_distribution()
        elif selected_option == "Tourist Count by Weather Condition":
            display_weather_condition()
        elif selected_option == "Peak Tourist Season":
            display_peak_tourist_season()
        elif selected_option == "Revenue Contribution by Tourist Type":
            display_revenue_by_tourist_type()
        elif selected_option == "Top 5 Cities by Tourist Expenditure":
            display_top_cities_expenditure()
        elif selected_option == "Tourist Transport Mode Preference":
            display_transport_mode()
        elif selected_option == "Total Tourists by Year":
            display_total_tourists_by_year()
        elif selected_option == "Total Revenue":
            display_total_revenue()
        else:
            st.warning("Please log in to view the analysis.")

if __name__ == "__main__":
    main()

# Define sections for each navbar item


st.header("About")
st.write("""I am Nadir Ali Khan, a student of the PITP Certified Python Course at IBA Sukkur. 
    Through this course, I am honing my Python skills and building projects to demonstrate my learning. 
    This project is a reflection of my progress and the knowledge I've gained during the course. 
    Thank you for exploring my work!""")


st.header("Skills")
st.write("""
    - **Python**: Experienced with scripting, data analysis, and web development.
    - **Machine Learning**: Basic understanding of ML algorithms.
    - **Web Development**: Familiar with HTML, CSS, and JavaScript.
    - **Data Analysis**: Proficient in using Pandas and Matplotlib for data manipulation and visualization.
""")


st.header("Certifications")
st.write("""

    - **MERN Stack Certification**: Expertise in MongoDB, Express, React, and Node.js.
    - **Cloud Computing Certification**: Knowledge of cloud platforms like AWS, Azure, Google Cloud.
    - **Python Certified**: Completed an advanced course in Python, specializing in scripting, automation, data analysis, data  visualization, and streamlined GUI development.
    - **DIT (Diploma in Information Technology)**: Fundamental understanding of IT concepts and practices.

    These certifications have equipped me with the skills necessary to work on a variety of technologies and platforms.
""")

st.header("Contact")
st.write("""
    Feel free to reach out to me for any inquiries or collaboration opportunities:
    
    - 📞 Phone: +92 304 2019543
    - 📧 Email: nadiralikhanofficial@gmail.com
""")

st.write("---")
st.markdown("""
    <p style="text-align: center; font-size: 18px;">
        <a href="https://linkedin.com/in/teamnadiralikhan" target="_blank" style="text-decoration: none; color: #0A66C2; font-weight: bold; padding: 5px; border: 2px solid #0A66C2; border-radius: 5px; transition: background-color 0.3s, color 0.3s;">
            LinkedIn
        </a>
        &nbsp;&nbsp;|&nbsp;&nbsp;
        <a href="https://github.com/NadirAliOfficial" target="_blank" style="text-decoration: none; color: #333; font-weight: bold; padding: 5px; border: 2px solid #333; border-radius: 5px; transition: background-color 0.3s, color 0.3s;">
            GitHub
        </a>
    </p>
""", unsafe_allow_html=True)






# Footer
st.markdown("""
    <div style="text-align: center; font-size: 14px; color: gray;">
        &copy; 2024 All rights reserved to Nadir Ali Khan
    </div>
""", unsafe_allow_html=True)
