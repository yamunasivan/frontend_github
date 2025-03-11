import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

def fetch_data(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None

st.sidebar.header("📌 Select Feature")
feature = st.sidebar.selectbox(
    "Select Feature",
    [
        "Most Popular Repositories",
        "Most Forked Repositories",
        "Most Common Languages",
        "Most Active Commits",
        "License Distribution",
        "Most Pull Requests",
        "Activity By Language",
        "Most Watched Repositories",
        "Repository Creation Trends",
    ],
)

if feature == "Most Popular Repositories":
    data = fetch_data("/github/most-popular/")

elif feature == "Most Forked Repositories":
    data = fetch_data("/github/most-forked/")

elif feature == "Most Common Languages":
    data = fetch_data("/github/common-languages/")

elif feature == "Most Active Commits":
    data = fetch_data("/repositories/most-active-commits/")

elif feature == "License Distribution":
    data = fetch_data("/repositories/license-distribution/")

elif feature == "Most Pull Requests":
    data = fetch_data("/repositories/most-pull-requests/")

elif feature == "Activity By Language":
    data = fetch_data("/repositories/activity-by-language/")

elif feature == "Most Watched Repositories":
    data = fetch_data("/repositories/most-watched/")

elif feature == "Repository Creation Trends":
    data = fetch_data("/repositories/creation-trends/")

if data:
    st.write(data)  # Display fetched data
