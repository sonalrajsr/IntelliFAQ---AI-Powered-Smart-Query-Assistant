from django.shortcuts import render
from .helper.query import query_serpapi
from .models import FAQ, InteractionLog
from .helper.embeddings import generate_embedding, compute_similarity, initialize_faq_embeddings
from .helper.google_search import google_search

# Home Page
def home(request):
    initialize_faq_embeddings()
    return render(request, "home.html")

# Ask Question View
def ask_question(request):
    user_query = request.GET.get("query", None)
    if not user_query:
        return render(request, "ask.html", {
            "error": "No query provided. Please go back and ask a question.",
        })

    # Generate embedding for the user query
    query_embedding = generate_embedding(user_query)

    # Fetch all FAQs
    faqs = FAQ.objects.all()

    # Ensure FAQ embeddings and answers are properly aligned
    faq_data = [(faq.embedding, faq.answer) for faq in faqs if faq.embedding]
    
    if faq_data:
        faq_embeddings, faq_answers = zip(*faq_data)  # Extract embeddings and answers
        similarity_scores = compute_similarity(query_embedding, faq_embeddings)

        # Find the most similar FAQ
        max_index, max_similarity = max(enumerate(similarity_scores), key=lambda x: x[1])

        if max_similarity >= 0.7:
            response = faq_answers[max_index]
        else:
            # No match found, query Google and LLM
            google_result = google_search(user_query)
            full_query = f"Give a concise answer for: {user_query} {google_result} for polynomial.ai"
            response = query_serpapi(full_query)

            # Log interaction
            InteractionLog.objects.create(user_query=user_query, response=response)
    else:
        # If no FAQs exist, query the LLM
        google_result = google_search(user_query)
        full_query = f"Give a concise answer for: {user_query} {google_result} for polynomial.ai"
        response = query_serpapi(full_query)

        # Log interaction
        InteractionLog.objects.create(user_query=user_query, response=response)

    # Render the response
    return render(request, "ask.html", {
        "query": user_query,
        "response": response,
    })
