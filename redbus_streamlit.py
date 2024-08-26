import streamlit as st
import pandas as pd
import mysql.connector

# MySQL connection setup (customize this with your credentials)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rifaya@23",
    database="redbus_selenium"
)
cursor = conn.cursor()

# Function to fetch data based on filters
def fetch_data(query):
    cursor.execute(query)
    return pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

st.title("Bus Routes Data")

# Filter for Bus Type
bus_type = st.selectbox("Select Bus Type", ["All", "SUPER LUXURY", "INDRA", "VOLVO", "Others"])


origin = st.selectbox("Enter your origin",['All','Kakinada', 'Visakhapatnam', 'Chittoor (Andhra Pradesh)', 'Kadapa',
       'Tirupati', 'Bangalore', 'Hyderabad', 'Guntur (Andhra Pradesh)',
       'Vijayawada', 'Kurnool', 'Rayachoti', 'Amalapuram', 'Madanapalli',
       'Narasaraopet', 'Kadiri', 'Chennai', 'Rajahmundry', 'Nellore',
       'Khammam', 'Karimnagar', 'Kothagudem', 'Godavarikhani', 'Kodad',
       'Jagityal', 'Kozhikode', 'Ernakulam', 'Mysore',
       'Kalpetta (kerala)', 'Thiruvananthapuram', 'Kannur', 'Kottayam',
       'Thrissur', 'Coimbatore', 'Burdwan', 'Kolkata', 'Haldia',
       'Midnapore', 'Siliguri', 'Digha', 'Durgapur (West Bengal)',
       'Jhargram', 'Berhampore (West Bengal)', 'Barasat (West Bengal)',
       'Purulia', 'Mandarmani', 'Patna (Bihar)', 'Gopalganj (Bihar)',
       'Delhi', 'Bettiah', 'Motihari', 'Balmiki Nagar (bihar)', 'Ranchi',
       'Hazaribagh', 'Muzaffarpur (Bihar)', 'Kathmandu', 'Lucknow',
       'Agra', 'Purnea', 'Darbhanga', 'Hajipur (Bihar)', 'Shimla',
       'Manali', 'Chandigarh', 'Hamirpur (Himachal Pradesh)',
       'Dharamshala (Himachal Pradesh)', 'Chamba (Himachal Pradesh)',
       'Dalhousie', 'Solan', 'Palampur', 'Kangra', 'Kullu', 'Ghumarwin',
       'Patiala', 'Ludhiana', 'Phagwara', 'Jalandhar', 'Delhi Airport',
       'Amritsar', 'Kapurthala', 'Jodhpur', 'Beawar (Rajasthan)',
       'Udaipur', 'Jaipur (Rajasthan)', 'Sikar', 'Kishangarh',
       'Aligarh (uttar pradesh)', 'Kota(Rajasthan)', 'Pali (Rajasthan)',
       'Bikaner', 'Tezpur', 'Guwahati', 'Nagaon (Assam)', 'Goalpara',
       'Jorhat', 'Dhubri', 'North Lakhimpur', 'Dhekiajuli', 'Sibsagar',
       'Haflong', 'Dibrugarh', 'Bihpuria', 'Biswanath Charali',
       'Tinsukia', 'Moran', 'Gohpur', 'Golaghat', 'Silchar', 'Bokakhat'])

Destination = st.selectbox("enter your destination",['All','Visakhapatnam', 'Kakinada', 'Bangalore', 'Vijayawada', 'Tirupati',
       'Kadapa', 'Ongole', 'Hyderabad', 'Kurnool',
       'Chittoor (Andhra Pradesh)', 'Rajahmundry',
       'Anantapur (andhra pradesh)', 'Amalapuram', 'Madanapalli',
       'Narasaraopet', 'Kadiri', 'Rayachoti', 'Chennai', 'Srisailam',
       'Nirmal', 'Mancherial', 'Adilabad', 'Karimnagar', 'Bhadrachalam',
       'Kothagudem', 'Sathupally', 'Armoor', 'Godavarikhani', 'Warangal',
       'Guntur (Andhra Pradesh)', 'Kozhikode', 'Ernakulam', 'Mysore',
       'Thiruvananthapuram', 'Kalpetta (kerala)', 'Thrissur', 'Kannur',
       'Kottayam', 'Ooty', 'Kolkata', 'Burdwan', 'Haldia',
       'Arambagh (West Bengal)', 'Bankura', 'Siliguri', 'Nimtouri',
       'Durgapur (West Bengal)', 'Midnapore', 'Nandakumar (west bengal)',
       'Mecheda (West Bengal)', 'Digha', 'Kolaghat',
       'Barasat (West Bengal)', 'Heria', 'Chandipur (West Bengal)',
       'Suri', 'Futishanko', 'Berhampore (West Bengal)', 'Malda',
       'Asansol (West Bengal)', 'Ramnagar (West Bengal)',
       'Bajkul (West Bengal)', 'Kirnahar (West Bengal)', 'Mandarmani',
       'Bakkhali', 'Bettiah', 'Delhi', 'Motihari', 'Patna (Bihar)',
       'Balmiki Nagar (bihar)', 'Kathmandu', 'Katihar', 'Purnea',
       'Hazaribagh', 'Raxaul', 'Ranchi', 'Muzaffarpur (Bihar)', 'Lucknow',
       'Janakpur (Nepal)', 'Araria (Bihar)', 'Saharsa', 'Agra',
       'Forbesganj', 'Hajipur (Bihar)', 'Gopalganj (Bihar)', 'Shimla',
       'Chandigarh', 'Manali', 'Hamirpur (Himachal Pradesh)',
       'Dharamshala (Himachal Pradesh)', 'Dalhousie',
       'Chamba (Himachal Pradesh)', 'Palampur', 'Solan',
       'Reckong Peo (Himachal Pradesh)', 'Kullu', 'Kangra', 'Nalagarh',
       'Sarkaghat', 'Patiala', 'Ludhiana', 'Jalandhar', 'Delhi Airport',
       'Phagwara', 'Amritsar', 'Bathinda', 'Faridkot', 'Ajmer',
       'Jaipur (Rajasthan)', 'Jodhpur', 'Beawar (Rajasthan)',
       'Aligarh (uttar pradesh)', 'Kota(Rajasthan)', 'Udaipur',
       'Pali (Rajasthan)', 'Bikaner', 'Bharatpur', 'Bhilwara', 'Pilani',
       'Mathura', 'Sikar', 'Guwahati', 'Tezpur', 'Nagaon (Assam)',
       'North Lakhimpur', 'Sibsagar', 'Jorhat', 'Dibrugarh', 'Dhemaji',
       'Tinsukia', 'Biswanath Charali', 'Haflong', 'Moran', 'Silchar',
       'Gogamukh', 'Bihpuria', 'Bokakhat'])

# Filter for Price Range
min_price, max_price = st.slider("Select Price Range", 0, 1000, (100, 500))

# Filter for Star Rating
min_rating = st.slider("Select Minimum Rating", 0.0, 5.0, 3.0)

# Filter for Availability
seats_available = st.selectbox("Seats Availability", ["All", "Available"])

# Build the SQL query based on filters
query = "SELECT * FROM bus_routess WHERE 1=1"

if bus_type != "All":
    query += f" AND Bus_type LIKE '%{bus_type}%'"
if origin !="All":
    query += f" AND Origin LIKE '%{origin}%'"
query += f" AND Price BETWEEN {min_price} AND {max_price}"
if Destination !="All":
    query += f" AND Destination LIKE '%{Destination}%'"
query += f" AND Price BETWEEN {min_price} AND {max_price}"

# Corrected the column name from 'Rating' to 'Ratings'
query += f" AND Ratings >= {min_rating}"

if seats_available == "Available":
    query += " AND Seats_Available > 0"

# Fetch and display the data
df = fetch_data(query)
st.write(f"Displaying {len(df)} results:")
st.dataframe(df)
