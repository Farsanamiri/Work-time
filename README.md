# Login System

This Python script is a basic implementation of a user authentication system. It verifies user credentials, allows new user registration for an admin account, updates login timestamps, and stores the data in a text file.

---

## Features
1. **Login Verification**:
   - Checks the username and password from a file (`demofile3.txt`).
   - Updates the login timestamp if the credentials are correct.

2. **Admin User Registration**:
   - An admin user (`username: admin`, `password: 12345`) can register new users by entering their credentials.

3. **File Storage**:
   - Usernames, passwords, and login timestamps are stored in `demofile3.txt`.

---

## Requirements
- Python 3.x
- A text file located at `/Users/telia/Documents/Work/demofile3.txt` with a list of stored usernames, passwords, and timestamps.

---

## File Structure

The `demofile3.txt` file must have the following structure:
```
name: user1
password: pass1
12:00:00
name: user2
password: pass2
13:30:45
...
```

Each user is stored as:
- Line 1: `name: <username>`
- Line 2: `password: <password>`
- Line 3: `<last login timestamp>`

---

## How to Use
1. Run the script.
2. Enter your username and password:
   - If valid credentials are provided, you will see "Login successful," and the login time will be updated in the file.
   - If invalid credentials are provided, you will see "Wrong username or password."
3. Admin can add a new user:
   - Log in as `username: admin` and `password: 12345`.
   - Enter the new user's username and password when prompted.

---

## Code Explanation

- **Reading File**:
  The script reads the `demofile3.txt` file to load the stored user data into the `filearr` list.
  
- **Admin Registration**:
  If the admin logs in, the script appends a new user to `filearr`.

- **User Authentication**:
  For each stored user, the script compares credentials. If a match is found, the timestamp is updated.

- **Writing to File**:
  After updates, the script writes all user data back to `demofile3.txt`.

---

## Notes
1. Ensure the path to `demofile3.txt` is correct and accessible.
2. The file should already contain initial data, or the admin should create users after running the script for the first time.
3. This implementation assumes the admin credentials are hardcoded as `admin` and `12345`.

---

## Limitations
- Passwords are stored in plain text (not secure).
- No user deletion or password update functionality.
- Only one admin user is supported.

---

## Future Improvements
- Encrypt passwords for better security.
- Implement error handling for invalid file paths or formats.
- Add support for additional admin features (e.g., user deletion, password reset).