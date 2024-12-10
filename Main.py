import time

current_time = time.strftime('%H:%M:%S')

username = input("Username: ")
password = input("Password: ")
newusername = f"name: {username}"
newpassword = f"password: {password}"
checuser = 0
filearr = []

# Open the file for reading
with open("/Users/telia/Documents/Work/demofile3.txt", "r") as rf:
    for line in rf:
        filearr.append(line.strip())  # Strip newline characters from each line

if newusername == "name: admin" and newpassword == "password: 12345":
    username = input("Username: ")
    password = input("Password: ")
    filearr.append(f"name: {username}")
    filearr.append(f"password: {password}")
    filearr.append(current_time)
    checuser = 1
else:
# Check credentials
    for i in range(0, len(filearr)):
        if filearr[i] == newusername and filearr[i + 1] == newpassword:
            filearr[i + 2] = current_time  # Update the time
            checuser = 1
            break

# Print login status
if checuser != 1:
    print("Wrong username or password")
else:
    print("Login successful")

# Write updated data back to the file
with open("/Users/telia/Documents/Work/demofile3.txt", "w") as f:
    for item in filearr:
        f.write(f"{item}\n")
f.close()
