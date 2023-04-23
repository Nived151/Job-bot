import pickle

# Read the cookies from the text file
with open('temp.txt', 'r') as f:
    cookies_str = f.read().replace('\n', '')

# Convert the cookies to a dictionary
cookies_dict = {}
for cookie in cookies_str.split(';'):
    name, value = cookie.strip().split('=', 1)
    cookies_dict[name] = value

# Dump the cookies dictionary to a pickle file
with open('kcookies.pkl', 'wb') as f:
    pickle.dump(cookies_dict, f)
