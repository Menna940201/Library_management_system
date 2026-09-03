# Library Management System

A Django-based web application for managing library books, borrowing operations, and user authentication.

## Features
- **User Authentication:** Signup and Login with validation.
- **Book Browsing & Search:** Filter books by title, author, or category.
- **Borrowing System:** Users can borrow and return books seamlessly.
- **My Loans Page:** Dynamic list tracking active loans.

## Admin Capabilities (Custom Dashboard):
- **Book Management (CRUD):** Fully functional admin dashboard to add, edit, and remove books directly from the front-end.
- **Role-Based Access Control:** Secure routes restricted to admin/staff users using `@staff_member_required`.
- **Media Uploads:** Support for uploading book covers and PDF files.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (Default)
