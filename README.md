# Harmony Bites

[![Build Status](https://travis-ci.org/jyoung90ie/django-ecommerce.svg?branch=master)](https://travis-ci.org/jyoung90ie/django-ecommerce)
[![codecov](https://codecov.io/gh/jyoung90ie/django-ecommerce/branch/master/graph/badge.svg)](https://codecov.io/gh/jyoung90ie/django-ecommerce)

Harmony Bites is a project designed to create a seamless restaurant booking experience. It aims to provide users with an easy and efficient way to book tables at their favorite restaurants. This project showcases my learning and understanding of web development technologies and best practices.

## Deployed Application

You can access the application [here](https://harmony-bites-753d102f24d0.herokuapp.com). If you wish to test account functionality, demo accounts have been provided below. Please note that email functionality has not been configured yet, and any messages related to emails can be ignored.

## UX

Harmony Bites focuses on providing a smooth and user-friendly experience for booking restaurant tables. The design is centered around simplicity and ease of use, ensuring that users can find, book, and manage their reservations effortlessly. The website is responsive and accessible on various devices, ensuring a consistent experience for all users.

### Wireframes

Wireframes were created to visualize the layout and functionality of the website on different devices. You can view these wireframes
<details>
  <summary>My wireframes</summary>

  ### Home Page

  **Header:**
  - Navigation Bar (Top)
    - Logo/Website Name: "Harmony Bites" (Top left)
    - Menu Items (aligned horizontally): Home, About Us, Menu, Contact Us, Opening Times, Login, Sign Up (Top center/right)

  **Main Content:**
  - Welcome Message (center)
    - Text: "Welcome to Harmony Bites"
    - Subtext: "Your favorite restaurant booking service."
    - Button: "Book Now" (center, below text)

  **Footer:**
  - Text: "© 2024 Book My Table. All rights reserved." (center)
  - Social Media Icons: Facebook, Instagram (center below text)

  ### About Us Page

  **Header:**
  - Same as Home Page

  **Main Content:**
  - About Us Message (center)
    - Text: "Welcome to Book My Table. We are your favorite restaurant booking service."

  **Footer:**
  - Same as Home Page

  ### Menu Page

  **Header:**
  - Same as Home Page

  **Main Content:**
  - Menu Section (center)
    - Title: "The Restaurant Menu"
    - Description: Informational text about menu availability
    - Menu Categories and Items (listed vertically and horizontally)

  **Footer:**
  - Same as Home Page

  ### Contact Us Page

  **Header:**
  - Same as Home Page

  **Main Content:**
  - Contact Information (center)
    - Email: contact@restaurant.com
    - Phone: +1 234 567 890
    - Address: 123 Food Street, Flavor Town
    - Map Placeholder: "Sorry! Something went wrong." (center below contact information)

  **Footer:**
  - Same as Home Page

  ### Opening Times Page

  **Header:**
  - Same as Home Page

  **Main Content:**
  - Opening Times Table (center)
    - Table listing days of the week with opening and closing times

  **Footer:**
  - Same as Home Page

  ### Login Page

  **Header:**
  - Same as Home Page

  **Main Content:**
  - Login Form (center)
    - Fields: Username, Password
    - Button: "Login"
    - Links: "Forgot password?", "Don't have an account? Sign Up"

  **Footer:**
  - Same as Home Page

  ### Sign Up Page

  **Header:**
  - Same as Home Page

  **Main Content:**
  - Sign Up Form (center)
    - Fields: Username, Email, Password, Password confirmation
    - Button: "Sign Up"

  **Footer:**
  - Same as Home Page

  ### Profile Page

  **Header:**
  - Navigation Bar (with additional "Admin Dashboard" link for admins)

  **Main Content:**
  - Profile Information (center)
    - Text: "Profile"
    - Fields: Username, Email
    - Buttons: "Edit Profile", "Edit My Bookings"

  **Footer:**
  - Same as Home Page

  ### Profile Settings Page

  **Header:**
  - Same as Profile Page

  **Main Content:**
  - Profile Settings Form (center)
    - Fields: First name, Last name, Email address, Username
    - Button: "Save Changes"

  **Footer:**
  - Same as Home Page

  ### My Bookings Page

  **Header:**
  - Same as Profile Page

  **Main Content:**
  - Booking Information (center)
    - Text: "My Bookings"
    - Details of bookings with "Cancel" button

  **Footer:**
  - Same as Home Page

</details>


### User Stories

#### Customer

As a customer, I want to be able to:

- Book a table at my favorite restaurant quickly and easily.
- View available booking times and select the one that suits me best.
- Manage my bookings, including canceling reservations.
- View detailed information about the restaurant, including menu and opening times.
- Sign up and log in to save my booking preferences.

#### Admin

As an admin, I want the ability to:

- Add new restaurants and update existing restaurant details.
- View and manage all bookings made by customers.
- Manage customer reviews and feedback to ensure high-quality service.

## Features

### Existing Features

- **User Authentication:** Sign up, log in, and manage user accounts.
- **Booking System:** Users can book tables at their preferred restaurant and manage their reservations.
- **Responsive Design:** The website is fully responsive and works seamlessly on all devices.

### Features to be Implemented

- **Email Notifications:** Send confirmation and reminder emails to users about their bookings.
- **Review System:** Allow users to leave reviews and ratings for restaurants.
- **Edit users table booking:** Allow users to edit their bookings.
- **Reviews and Feedback control:** Allow admins to edit and delete reviews and feedback.

## Technologies Used

- **HTML:** For structuring the content of the website.
- **CSS:** For styling the website and ensuring a responsive design.
- **JavaScript:** For interactive elements and dynamic content.
- **Python:** The main programming language used for backend development.
- **Django:** The web framework used for building the application.
- **PostgreSQL:** The database used to store application data.
- **Heroku:** The platform used for deploying the application.

## Fixed Bugs

- **Image Loading Issues:** Sometimes images do not load correctly due to caching issues.
- **Form Validation:** Some forms do not provide detailed error messages for invalid input.
- **Session Handling:** Occasionally, user sessions expire prematurely, causing users to be logged out unexpectedly.
- **Database Connections:** There have been intermittent issues with the database connection, leading to occasional downtime.
- **Booking Overlap:** In rare cases, bookings may overlap if two users attempt to book the same slot simultaneously.
- **CSS Styling:** Some CSS styles may not render correctly on older versions of certain browsers.
- **Pages Not Loading:** Some pages may not load correctly due to caching issues.
- **Admin Dashboard:** The admin dashboard does not load correctly due to caching issues.
- **Login Page:** The login page links to the Admin login page.
- **Admin Dashboard:** The admin dashboard does not load correctly due to caching issues.
- **Admin capabilities:** The admin dashboard does not have the ability to edit user accounts or user bookings(gave a page error)

## Deployment
### Remote (Heroku)

1. Create an account at [Heroku](https://www.heroku.com/).
2. Download CLI [here](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
3. Open CMD (Windows) or Terminal (MacOS) and log in using `heroku login`.
4. Create a new Heroku app using `heroku create app-name-here`.
5. Modify the `ALLOWED_HOSTS` in the `settings.py` file to include your Heroku app name.
6. Add environment variables in Heroku under the Settings tab:
   - `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST`, `DATABASE_PORT`, `SECRET_KEY`, `mybookingr35t`
7. Set the Heroku stack to container with `heroku stack:set container -a app-name-here`.
8. Create a PostgreSQL database with `heroku addons:create heroku-postgresql:hobby-dev -a app-name-here`.
9. Push the code to Heroku using `git push heroku master`.
10. Run migrations with `heroku run python manage.py migrate`.
11. Create a superuser with `heroku run python manage.py createsuperuser`.

## Credits

### Content

- [Main idea of web design](https://www.youtube.com/watch?v=M67Ax2S3xm4&t=178s)
- [Main and Menu design idea](https://www.mandarinbuffet.co.uk)
- [Login forms](https://freefrontend.com/css-login-forms/) for login form design.

### Media

- [Icons](https://www.flaticon.com)
- [Background](https://www.pexels.com)
- [Logo](https://www.vistaprint.co.uk/logo-design)

### Acknowledgements

- [UI Cookies](https://uicookies.com/bootstrap-footer/) for footer design.6
- [How to code](https://www.youtube.com/watch?v=TuXFAl8aMvc)
    - [How to code 2](https://www.youtube.com/watch?v=xcsbQHdtI2k)
    - [How to code 3](https://www.youtube.com/watch?v=QVDJ1BJ2qnE) and many other videos
- [W3Schools - How to make a restaurant web](https://www.w3schools.com/howto/howto_website_restaurant.asp)
- [Admin dashboards](https://github.com/topics/admin-dashboard?l=python)
