Django User Authentication System
Overview
This project is a Django application that implements a user authentication system with the following features:

Login: Users can log in using either their username or email and password.
Signup: Users can create a new account with a username, email, and password.
Forgot Password: Users can reset their password by entering their email address.
Change Password: Users can change their password after logging in.
Dashboard: Displays a greeting message for authenticated users and includes links to other pages.
Profile: Displays user information such as username, email, date joined, and last updated.
Features
Login Page

Fields for Username/Email and Password.
Links for "Sign Up" and "Forgot Password".
Sign Up Page

Fields for Username, Email, Password, and Confirm Password.
A link to go back to the Login page.
Forgot Password Page

A field for Email.
A button to send a password reset link to the user's email.
Change Password Page

Requires authentication.
Fields for Old Password, New Password, and Confirm Password.
A link to go back to the Dashboard.
Dashboard

Accessible only to authenticated users.
Displays a greeting message like "Hi, username!".
Links to Profile and Change Password pages.
Option to logout.
Profile Page

Displays Username, Email, Date Joined, and Last Updated.
A link to go back to the Dashboard.
Option to logout.
