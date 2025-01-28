from django.shortcuts import render, redirect
from .helper.query import query_serpapi
from .models import InteractionLog, FAQ


# Home Page
def home(request):
    return render(request, "home.html")


# Ask Question View
def ask_question(request):
    user_query = request.GET.get("query", None)
    if not user_query:
        return render(request, "ask.html", {
            "error": "No query provided. Please go back and ask a question.",
        })

    # question exists in the FAQ model
    faq = FAQ.objects.filter(question=user_query).first()

    if faq:
        response = faq.answer
    else:
        response = query_serpapi('give the output in short ' + user_query)

    # Save to Interaction model
    InteractionLog.objects.create(user_query=user_query, response=response)

    return render(request, "ask.html", {
        "query": user_query,
        "response": response,
    })
