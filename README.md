# Harmony Bites

Harmony Bites is a project designed to create a seamless restaurant booking experience. It aims to provide users with an easy and efficient way to book tables at their favorite restaurants. This project showcases my learning and understanding of web development technologies and best practices.

## Deployed Application

You can access the application [--->here<---](https://harmony-bites-753d102f24d0.herokuapp.com)
![Homepage](/docs/readme-photos/main.png)

## Table of Contents
- [Harmony Bites](#harmony-bites)
  - [Deployed Application](#deployed-application)
  - [Table of Contents](#table-of-contents)
  - [UX](#ux)
    - [Site Map](#site-map)
    - [Planned Sections:](#planned-sections)
    - [Note:](#note)
    - [Wireframes](#wireframes)
    - [Home Page](#home-page)
    - [About Us Page](#about-us-page)
    - [Menu Page](#menu-page)
    - [Contact Us Page](#contact-us-page)
    - [Opening Times Page](#opening-times-page)
    - [Login Page](#login-page)
    - [Sign Up Page](#sign-up-page)
    - [Profile Page](#profile-page)
    - [Profile Settings Page](#profile-settings-page)
    - [My Bookings Page](#my-bookings-page)
      - [Customer](#customer)
      - [Admin](#admin)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be Implemented](#features-to-be-implemented)
  - [Agile Methodology](#agile-methodology)
  - [Technologies Used](#technologies-used)
  - [Fixed Bugs](#fixed-bugs)
  - [Deployment](#deployment)
    - [Remote (Heroku)](#remote-heroku)
  - [Testing](#testing)
    - [Test Coverage Report](#test-coverage-report)
  - [Validator Testing](#validator-testing)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)


## UX

Harmony Bites focuses on providing a smooth and user-friendly experience for booking restaurant tables. The design is centered around simplicity and ease of use, ensuring that users can find, book, and manage their reservations effortlessly. The website is responsive and accessible on various devices, ensuring a consistent experience for all users.

### Site Map
![Site Map](/docs/readme-photos/sitemap.png)

The image above represents the original layout plan for the "Harmony Bites" website. This sitemap was designed to outline the main sections of the website and their interconnections, providing a clear navigation path for users.
### Planned Sections:

- **Main Page (Home)**: The primary landing page, serving as the introduction to the website, with quick access to key sections.
- **About**: A page providing information about the restaurant, including history, mission, and other relevant details.
- **Menu**: The section dedicated to displaying the restaurant's menu, organized by categories.
- **Contact Us**: A page for users to reach out to the restaurant, including contact information and a form for inquiries.
- **Opening Times (Optimes)**: This page provides information about the restaurant's hours of operation.
- **Accounts**: A user account section where users can view their profiles and manage their details.
- **Login**: The login page for users to access their accounts.
- **Signup**: The registration page for new users to create an account.
- **Password Reset**: A page dedicated to allowing users to reset their passwords if they forget them.

### Note:
This structure was the initial plan to provide a comprehensive and user-friendly experience. However, some adjustments and changes have been made during development based on testing, feedback, and additional requirements to enhance the user experience.

### Wireframes

Wireframes were created to visualize the layout and functionality of the website on different devices. You can view these wireframes below. Or you can view them in full screen by clicking on this link: [--->Wireframes<---](/docs/wiraframes/)
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

- **Responsive Design**: The application is fully responsive and adapts to different screen sizes, providing a consistent user experience across devices.
- **Booking System**: Users can easily book a table by choosing a date, time, and the number of guests.
- **Admin Dashboard**: Allows administrators to manage bookings, users, and other data directly from the admin interface.
- **Security**: Sensitive data such as secret keys and database credentials are managed through environment variables.
- **Error Handling**: Custom error pages for common HTTP status codes (404, 500) are implemented to enhance user experience.

### Features to be Implemented

- **Email Notifications**: Send confirmation and reminder emails to users about their bookings.
- **Review System**: Allow users to leave reviews and ratings for restaurants.
- **Edit users table booking**: Allow users to edit their bookings.
- **Reviews and Feedback control**: Allow admins to edit and delete reviews and feedback.
- **Password Reset**: Allow users to reset their passwords. But now they have to contact the admin to reset their password.

## Agile Methodology

The development of Harmony Bites followed Agile principles. The project was broken down into sprints, with tasks prioritized and tracked using GitHub Issues. Here are some key aspects of the Agile approach used:

- **User Stories**: Each user story was created based on real user needs, such as "As a user, I want to book a table so that I can reserve a spot at my favorite restaurant." Each story included acceptance criteria to ensure it met user expectations.
- **Sprints**: The development was divided into three main sprints:
  - **Sprint 1**: Setting up the project structure, user authentication, and initial booking functionality.
  - **Sprint 2**: Implementing the admin dashboard, customizing models, and adding database integration.
  - **Sprint 3**: Testing, bug fixing, and deployment.
- **Prioritization**: User stories were labeled with priorities (High, Medium, Low) to ensure that the most important features were developed first.
- **Sprint Reviews and Retrospectives**: At the end of each sprint, a review was conducted to assess progress, identify any blockers, and plan for the next sprint.

## Technologies Used

- **HTML**: For structuring the content of the website.
- **CSS**: For styling the website and ensuring a responsive design.
- **JavaScript**: For interactive elements and dynamic content.
- **Python**: The main programming language used for backend development.
- **Django**: The web framework used for building the application.
- **PostgreSQL**: The database used to store application data.
- **Heroku**: The platform used for deploying the application.

## Fixed Bugs

- **Image Loading Issues**: Sometimes images do not load correctly due to caching issues.
- **Form Validation**: Some forms do not provide detailed error messages for invalid input.
- **Session Handling**: Occasionally, user sessions expire prematurely, causing users to be logged out unexpectedly.
- **Database Connections**: There have been intermittent issues with the database connection, leading to occasional downtime.
- **Booking Overlap**: In rare cases, bookings may overlap if two users attempt to book the same slot simultaneously.
- **CSS Styling**: Some CSS styles may not render correctly on older versions of certain browsers.
- **Pages Not Loading**: Some pages may not load correctly due to caching issues.
- **Admin Dashboard Issues**: The admin dashboard sometimes does not load correctly due to caching problems.
- **Login Redirection Issue**: The login page linked to the Admin login page instead of the user login.
- **Admin Capabilities**: There were issues with editing user accounts and bookings on the admin dashboard, resulting in page errors.

## Deployment

### Remote (Heroku)

1. Create an account at [Heroku](https://www.heroku.com/).
2. Download CLI [here](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
3. Open CMD (Windows) or Terminal (MacOS) and log in using `heroku login`.
4. Create a new Heroku app using `heroku create app-name-here`.
5. Modify the `ALLOWED_HOSTS` in the `settings.py` file to include your Heroku app name.
6. Add environment variables in Heroku under the Settings tab:
   - `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST`, `DATABASE_PORT`, `SECRET_KEY`, `DJANGO_DEBUG`
7. Set the Heroku stack to container with `heroku stack:set container -a app-name-here`.
8. Create a PostgreSQL database with `heroku addons:create heroku-postgresql:hobby-dev -a app-name-here`.
9. Push the code to Heroku using `git push heroku main`.
10. Run migrations with `heroku run python manage.py migrate`.
11. Create a superuser with `heroku run python manage.py createsuperuser`.

## Testing

The application was thoroughly tested to ensure that it met functional and non-functional requirements. The testing process included:

- **Manual Testing**: Each feature was manually tested to ensure correct behavior. This included:
  - User registration, login, and logout.
  - Booking creation, update, and deletion.
  - Admin functionalities, such as editing and managing bookings.
- **Automated Testing**: Python's `unittest` was used to create automated tests for core functionalities, including:
  - Testing models to verify correct data saving and retrieval.
  - Testing views to ensure the correct response status and templates used.
- **Custom Test Cases**: Specific scenarios, such as booking overlap prevention and session expiration, were tested manually to verify proper handling.
![Lighthouse-test](/docs/readme-photos/light-testing.png)

### Test Coverage Report

The following screenshot shows the test coverage report for the Harmony Bites project. The tests cover various parts of the application, including models, views, forms, and other key components.

![Test Coverage Report](/docs/readme-photos/coverage-test.png)

To generate the test coverage report, the following steps were taken:

1. **Install the `coverage` library**:
   ```bash
   pip install coverage
   coverage run manage.py test
   coverage report
   coverage html

   ## Validator Testing
- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/#validate_by_uri).
    ![HTML Validator](/docs/readme-photos/html-test.png)
- CSS
    - No errors were returned when passing through the official [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/).
    ![CSS Validator](/docs/readme-photos/css-test.png)
- JavaScript
    - No errors were returned when passing through the official [JSHint JavaScript Validator](https://jshint.com).
    ![JavaScript Validator](/docs/readme-photos/js-test.png)

## Credits

### Content

- [Main idea of web design](https://www.youtube.com/watch?v=M67Ax2S3xm4&t=178s)
- [Main and Menu design idea](https://www.mandarinbuffet.co.uk)
- [Login forms](https://freefrontend.com/css-login-forms/) for login form design.

### Media

- [Icons](https://www.flaticon.com) for the website's icons(user).
- [Background](https://www.pexels.com) for the website's background.
- [Logo](https://www.vistaprint.co.uk/logo-design) for the Harmony Bites logo.
- [Png images](https://www.pngegg.com) - Used for the README photos.
- [Octopus Sitemap](https://octopus.do/sitemap) - Used for the sitemap.

### Acknowledgements

- [UI Cookies](https://uicookies.com/bootstrap-footer/) for footer design.
- [How to code](https://www.youtube.com/watch?v=TuXFAl8aMvc)
- [W3Schools - How to make a restaurant web](https://www.w3schools.com/howto/howto_website_restaurant.asp)
- [Admin dashboards](https://github.com/topics/admin-dashboard?l=python)

