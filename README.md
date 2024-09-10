# Plated

Plated is a full-stack recipe application that provides a platform for users to discover, share, and manage recipes. The application features a Django RESTful API backend and a React frontend, offering a seamless and interactive user experience.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Recipe Management:** Users can add, edit, and delete recipes.
- **Search and Filter:** Discover recipes through search and filtering options.
- **User Authentication:** Secure user registration and login.
- **Responsive Design:** Optimized for both desktop and mobile devices.

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** React, Tailwind CSS
- **Database:** PostgreSQL (or as configured)
- **Deployment:** Docker (optional), Heroku/AWS/Other (as configured)

## Setup Instructions

### Backend Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sam-3l/Plated.git
   cd Plated
2. Navigate to the Backend Directory:
    ```bash
    cd Backend
3. Create and Activate a Virtual Environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4.  Install Dependencies:
     ```bash
     pip install -r requirements.txt
5.  Apply Migrations:
     ```bash
     python manage.py migrate 
6. Run the Development Server:
   ```bash
   python manage.py runserver

### Frontend Setup

1. **Navigate to the Frontend Directory:**
   ```bash
   cd ../Frontend
2. Install Dependencies::
    ```bash
    npm install
3. Run the Development Server:
    ```bash
    npm start
4.  Open Your Browser:
    Navigate to `http://localhost:3000` to view the application.

## Usage

- Backend: Access the API at `http://localhost:8000/api/`.
- Frontend: Access the application at `http://localhost:3000`.

## Contributing

We welcome contributions to improve Plated. If you have suggestions, bug reports, or would like to contribute code, please follow these steps:

1. **Fork the Repository**

   Click the "Fork" button at the top right of the repository page on GitHub to create a copy of the repository under your own account.

2. **Clone Your Fork**

   Clone the forked repository to your local machine:

   ```bash
   git clone https://github.com/Sam-3l/Plated.git

3. Create a New Branch:

   `git checkout -b feature/YourFeature`

5. Commit your changes: 

   `git commit -am 'Add new feature'`

6. Push to the branch:

`git push origin feature/YourFeature`

7. Create a new Pull Request.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
