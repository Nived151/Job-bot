import pickle
from datetime import datetime

# Load the cookies from the pickle file
with open('cookies.pkl', 'rb') as f:
    cookies = pickle.load(f)

# Check if the cookies are expired
for cookie in cookies:
    # Check if the "expiry" key is present in the cookie dictionary
    if 'expiry' in cookie:
        # Convert the cookie's "expiry" value to a datetime object
        expiry = datetime.fromtimestamp(cookie['expiry'])
        # Check if the expiry date is in the past
        if expiry < datetime.now():
            print(f"Cookie {cookie['name']} is expired!")
        else:
            print(f"Cookie {cookie['name']} is still valid!")
    else:
        print(f"Cookie {cookie['name']} doesn't have an expiry date.")