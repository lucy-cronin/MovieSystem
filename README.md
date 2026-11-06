# Django

# Movie System

A Django web application for managing a movie catalogue. Built for INFO8011 CA1.

**Student:** Lucy Cronin | **Student number:** R00244083

## Features

- Add, view, edit and delete movies (full CRUD)
- Search by name, genre or director from the navbar
- Sort by name, highest rating or newest release
- Pagination that keeps the current search and sort
- Optional cover image upload, shown beside the title on the detail page
- Form validation with clear error messages
- Responsive Bootstrap 5 layout with a pink theme
- Navbar and footer (name, student number, current year) on every page

## Tech stack

- Python 3.9 or newer
- Django 4.2
- SQLite (included with Python)
- Pillow (image uploads)
- Bootstrap 5 and Font Awesome (loaded from a CDN, so internet access is needed)

## How to run

1. Unzip the project and open a terminal in the folder that contains `manage.py`.

2. Create and activate a virtual environment:

   Mac or Linux:
   ```
   python3 -m venv env
   source env/bin/activate
   ```

   Windows:
   ```
   python -m venv env
   env\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create the database tables:
   ```
   python manage.py migrate
   ```

5. (Optional) Create an admin user for `/admin/`:
   ```
   python manage.py createsuperuser
   ```

6. Start the server:
   ```
   python manage.py runserver
   ```

7. Open <http://127.0.0.1:8000/> in your browser.

If the project was submitted with `db.sqlite3` and the `media/` folder, the sample movies and cover images are already included, and step 4 will report that there is nothing to apply.

## Pages

| URL | Page |
| --- | --- |
| `/` | Movie list with search, sort and pagination |
| `/movie/add/` | Add a movie |
| `/movie/<id>/` | Movie details and cover |
| `/movie/<id>/edit/` | Edit a movie |
| `/movie/<id>/delete/` | Delete confirmation |
| `/admin/` | Admin site |

## Validation rules

- Name, genre, director, release date and rating are required
- Rating must be between 0 and 5
- Genre must be one of the listed choices
- Name must be at least 2 characters
- Release date must be 1888 or later
- Cover image must be a real image under 2 MB (optional)

## Project structure

```
MovieSystem/                 project root
  manage.py
  requirements.txt
  db.sqlite3
  MovieSystem/               settings.py, urls.py
  MovieSystemApp/movies/     models, forms, views, urls, templates, static
  media/posters/             uploaded cover images
```

