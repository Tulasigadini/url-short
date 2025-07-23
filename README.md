## Setup Instructions

1. **Clone the Repository**

   git clone https://github.com/Tulasigadini/url-short.git
   cd url_shortener


Create a Virtual Environment
----------------------------------
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies
----------------------
pip install -r requirements.txt

Apply Migrations
--------------------
python manage.py makemigrations
python manage.py migrate

Create a Superuser (for Admin Access)
--------------------------------------
python manage.py createsuperuser

Run the Development Server
---------------------------
python manage.py runserver

Access the Application
-----------------------------
Frontend: http://localhost:8000
Admin Panel: http://localhost:8000/admin
