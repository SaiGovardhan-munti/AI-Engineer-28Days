import requests
import json

username = input("Enter the username:")
response = requests.get (f"https://api.github.com/users/{username}") 

if response.status_code == 200:
    data = response.json()
    user = {
        "login" : data["login"],
        "name": data["name"], "public_repos": data["public_repos"], "followers":data["followers"],
    }
    #save
    with open("user_data.json", "w") as f:
        json.dump(user,f)
    #print
    print(f"username:{user['login'],user['name'],user['followers'],user['public_repos']}")

else:
    print("user not found")

