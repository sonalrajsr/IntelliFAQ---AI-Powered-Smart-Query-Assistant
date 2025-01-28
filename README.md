# FAQ Assistant - README

## Overview
The FAQ Assistant is a Django-based intelligent question-answering system designed to provide accurate and efficient answers to user queries. It leverages a hybrid approach by combining a database of predefined FAQs with the power of Large Language Models (LLMs) for dynamic query handling. This ensures that users get the best possible answers, whether their questions are pre-answered or require real-time generation.

---

## Features

### 1. **FAQ Database Querying**
   - The system maintains a structured database of frequently asked questions (FAQs) along with their corresponding answers.
   - When a user submits a query, the system first checks for a matching question in the database using semantic similarity techniques.
   - If a match is found with a similarity score of 70% or above, the associated answer is returned to the user.

### 2. **Integration with LLMs**
   - If no matching FAQ is found (similarity score below 70%), the system dynamically generates an answer using a connected Large Language Model (LLM).
   - This ensures users receive an accurate response even for queries not present in the FAQ database.
   - The LLM can handle complex, open-ended, or highly specific queries.

### 3. **Similarity Scoring Mechanism**
   - The system uses advanced natural language processing (NLP) techniques to calculate the similarity score between user queries and stored FAQs.
   - This ensures a high level of accuracy in retrieving relevant answers.

### 4. **Dynamic Knowledge Base**
   - Administrators can easily add, edit, or remove FAQs from the database.
   - The FAQ database is designed to evolve, allowing it to grow with the needs of its users.

### 5. **Fallback to LLMs for Unanswered Queries**
   - When a query is not present in the database, the system seamlessly transitions to an LLM to generate a relevant and contextually accurate answer.
   - This ensures that users are not left without a response, even for unique or unanticipated queries.

### 6. **Error Handling**
   - When the system cannot generate a response (e.g., if the LLM is unavailable), it provides a user-friendly error message.
   - Ensures that users are not left without guidance.

### 7. **Interactive Frontend**
   - A simple, user-friendly interface allows users to ask questions and view responses.
   - Responsive design ensures compatibility across various devices.

### 8. **Scalable Architecture**
   - The project is designed with scalability in mind, making it suitable for deployment in small-scale or enterprise-level environments.

### 9. **Real-Time Query Logging**
   - Logs user queries for future analysis.
   - Provides insights into user behavior and helps identify gaps in the FAQ database.

### 10. **Customizable Thresholds**
   - Administrators can adjust the similarity score threshold (default: 90%) to balance between precision and recall.

### 11. **Support for Static Files**
   - Static files (CSS, JavaScript, images) are seamlessly integrated for a polished user experience.

---

## System Workflow
1. **User Query Submission**:
   - Users submit their question through the frontend interface.
2. **Database Search**:
   - The system calculates similarity scores for the submitted query against all stored FAQs.
   - If a match with a score ≥90% is found, the corresponding answer is retrieved.
3. **Fallback to LLM**:
   - If no satisfactory match is found, the query is sent to an LLM for real-time answer generation.
4. **Response Display**:
   - The system returns the best answer to the user, whether from the database or the LLM.
5. **Query Logging**:
   - Each query is logged for future analysis and improvements.

---

## Demo
Visit this link for demo, Working of website and model.
```
https://youtu.be/S2up0BrRSFc
```
[![Watch the video](https://img.youtube.com/vi/S2up0BrRSFc/maxresdefault.jpg)](https://www.youtube.com/watch?v=S2up0BrRSFc)

---

## Benefits
- **Efficiency**: Quickly answers common questions with pre-stored FAQs.
- **Flexibility**: Handles unique or unforeseen queries using LLMs.
- **Scalability**: Adapts to growing databases and user bases.
- **User-Focused**: Provides a seamless and intuitive experience.
- **Customizable**: Allows administrators to fine-tune the system as needed.

---

## Usage Guidelines

### For Users
- Simply type your question into the input box and press "Ask Question."
- If your query is recognized, an answer will be displayed immediately.
- For unrecognized queries, please allow a moment for the LLM to generate a response.

### For Administrators
- Use Django's admin interface to manage the FAQ database.
- Regularly review query logs to identify popular or unanswered questions.
- Update the database to improve system accuracy and coverage.

---

## How to Run the Project Locally

### Prerequisites
- Python (version 3.8 or higher)
- Django (version 4.x or higher)
- SQLite (default database, pre-configured)
- Optional: API key for LLM integration (e.g., OpenAI or similar)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the project root.
   - Add the following variables:
     ```env
     SECRET_KEY=<your-django-secret-key>
     DEBUG=True
     LLM_API_KEY=<your-llm-api-key>
     ```

5. **Run Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Load Sample FAQs (Optional)**:
   - Use a script to populate the database with sample FAQs.
   - Example:
     ```bash
     python manage.py loaddata sample_faqs.json
     ```

7. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```
   - Access the application at `http://127.0.0.1:8000`.

8. **Access the Admin Interface**:
   - Create a superuser:
     ```bash
     python manage.py createsuperuser
     ```
   - Access the admin interface at `http://127.0.0.1:8000/admin`.

---

## Future Enhancements
- **Multilingual Support**: Enable query handling in multiple languages.
- **Enhanced Analytics**: Provide detailed reports on user behavior and system performance.
- **Improved NLP Techniques**: Incorporate state-of-the-art models for better similarity scoring.
- **Voice Query Integration**: Allow users to ask questions using voice input.

---

## Installation and Setup
1. **Clone the Repository:**
   - Download or clone the project repository to your local system.

2. **Install Dependencies:**
   - Use `pip` to install all required dependencies listed in the `requirements.txt` file.

3. **Set Up the Database:**
   - Run Django migrations to create the required database tables.

4. **Load Initial Data:**
   - Populate the database with initial FAQ entries using a Python script or Django admin.

5. **Start the Development Server:**
   - Use the `python manage.py runserver` command to start the server locally.

6. **Access the Application:**
   - Open the application in your web browser at `http://127.0.0.1:8000`.

---

## Folder Structure

```
smart_FAQ/
│-- db.sqlite3              # SQLite database file
│-- manage.py               # Django project management script
│-- .env                    # Environment variables file
│-- .gitignore              # Git ignore file
│-- README.md               # Project documentation
│
├── faq/                    # Main application directory
│   ├── __pycache__/        # Compiled Python files
│   ├── helper/             # Helper functions and utilities
│   ├── migrations/         # Database migrations
│   ├── __init__.py         # Package initialization
│   ├── admin.py            # Admin panel configuration
│   ├── apps.py             # Application configuration
│   ├── models.py           # Database models
│   ├── tests.py            # Unit tests
│   ├── views.py            # Application logic
│
├── smart_FAQ/              # Project settings directory
│   ├── __pycache__/        # Compiled Python files
│   ├── __init__.py         # Package initialization
│   ├── asgi.py             # ASGI configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI configuration
│
├── static/                 # Static assets
│   ├── styles.css          # CSS file for styling
│
├── templates/              # HTML templates
│   ├── ask.html            # User query page
│   ├── home.html           # Homepage
│
├── requirements.txt        # List of dependencies
├── Varified FAQ.py         # Script for verified FAQs

```

---

## Conclusion
The FAQ Assistant is a powerful tool designed to streamline information retrieval and enhance user engagement. Its combination of a structured FAQ database and dynamic LLM capabilities ensures that users receive timely and accurate answers, making it an invaluable asset for organizations looking to improve their support systems.
