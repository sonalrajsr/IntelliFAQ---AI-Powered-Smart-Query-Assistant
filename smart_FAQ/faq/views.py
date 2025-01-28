from django.shortcuts import render, redirect
from .helper.query import query_serpapi
from .models import InteractionLog
from datetime import datetime


# Home Page View
def home(request):
    return render(request, "home.html")


# Ask Question View
def ask_question(request):
    user_query = request.GET.get("query", None)  # Retrieve the query from GET parameter
    if not user_query:
        return render(request, "ask.html", {
            "error": "No query provided. Please go back and ask a question.",
        })

    # Query SerpAPI for the response
    response = query_serpapi('give the output in sort ' + user_query)

    # Log the interaction to the database
    InteractionLog.objects.create(user_query=user_query, response=response)

    # Render the Ask page with the response
    return render(request, "ask.html", {
        "query": user_query,
        "response": response,
    })
