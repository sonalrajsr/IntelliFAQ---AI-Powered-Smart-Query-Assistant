import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('smart_FAQ/db.sqlite3')

# Create a cursor object to interact with the database
cursor = conn.cursor()


# FAQ data (you can expand this list with more questions and answers)
faq_data = faq_data = [
    ("What is Django and what are its key features?", "Django is a high-level Python web framework that promotes rapid development and clean, pragmatic design. It comes with many built-in features like an admin panel, ORM (Object-Relational Mapping), security features, and built-in URL routing. Django’s goal is to make it easier to build robust, scalable web applications.", "2025-01-28 19:55:30"),
    ("How does the Django framework work and why is it preferred over other frameworks?", "Django follows the MVT (Model-View-Template) architectural pattern which separates the logic of the database, user interface, and presentation. It is preferred because of its 'batteries-included' approach, meaning it includes everything you need to build web applications without relying on third-party libraries.", "2025-01-28 19:55:30"),
    ("What is a model in Django and how does it relate to the database?", "In Django, a model is a Python class that represents a table in the database. Each model field corresponds to a column in the database, and Django automatically generates the necessary SQL queries to create the table. It is used to interact with the database and perform operations like CRUD (Create, Read, Update, Delete).", "2025-01-28 19:55:30"),
    ("How can I define a model in Django, and what are the key fields I should know?", "To define a model in Django, you need to create a class that inherits from `django.db.models.Model` and define fields as class variables. Common field types include `CharField`, `TextField`, `IntegerField`, and `DateTimeField`. Models allow you to interact with database records using an object-oriented approach.", "2025-01-28 19:55:30"),
    ("What is an API, and why is it crucial in web development?", "API stands for Application Programming Interface, which is a set of rules and protocols for interacting with a system. It allows one application to communicate with another, enabling integration between systems. In web development, APIs are crucial because they allow applications to access functionality and data from external sources like third-party services, databases, or other applications.", "2025-01-28 19:55:30"),
    ("What role does a view function play in Django's MVC architecture?", "In Django’s MVT (Model-View-Template) architecture, the view function acts as a controller. It takes a web request, interacts with models (if needed), and returns an appropriate response, often rendering an HTML template with the data passed from the model. Views are integral to generating the user-facing portion of an application.", "2025-01-28 19:55:30"),
    ("How do I define and manage URL patterns in Django for routing?", "In Django, URL patterns are defined in the `urls.py` file, where each URL is mapped to a view function. These URL patterns can be regular expressions or simple string patterns. Django will use the defined URL patterns to route the incoming requests to the appropriate view function.", "2025-01-28 19:55:30"),
    ("What is a queryset in Django and how is it used to interact with the database?", "A queryset in Django is a collection of database queries that can be filtered, ordered, and sliced to retrieve specific records from the database. Querysets are used to interact with the database and can be chained together for more complex operations. They are one of the key components of Django’s ORM.", "2025-01-28 19:55:30"),
    ("What is middleware in Django and how does it affect request handling?", "Middleware in Django is a lightweight, low-level plugin system for globally altering the request and response objects. It allows developers to process requests before they reach the view or manipulate responses after the view has processed them. Middleware can be used for tasks like authentication, session management, and security.", "2025-01-28 19:55:30"),
    ("How do I use static files in Django, and why are they important?", "Static files (CSS, JavaScript, and image files) are managed separately from the rest of your content in Django. You can link to these static files using the `{% static %}` template tag. Proper management of static files is important for enhancing the performance and user experience of web applications.", "2025-01-28 19:55:30")
]

# Insert FAQ data into the tablexx00
cursor.executemany('''
INSERT INTO faq_faq (question, answer, timestamp)
VALUES (?, ?, ?)
''', faq_data)

# Commit the changes and close the connection
conn.commit()

# Close the connection
conn.close()

print("FAQs have been successfully inserted into the database!")
