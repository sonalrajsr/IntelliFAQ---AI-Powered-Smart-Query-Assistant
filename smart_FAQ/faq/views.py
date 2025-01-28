from django.shortcuts import render
from .helper.query import query_serpapi
from .models import  FAQ, InteractionLog
from .helper.embeddings import generate_embedding, compute_similarity, initialize_faq_embeddings



# Home Page
def home(request):
    initialize_faq_embeddings()
    return render(request, "home.html")


# Ask Question View
def ask_question(request):
    user_query = request.GET.get("query", None)  # Get the query from the user
    if not user_query:
        return render(request, "ask.html", {
            "error": "No query provided. Please go back and ask a question.",
        })

    # Generate embedding for the user query
    query_embedding = generate_embedding(user_query)

    # Fetch all FAQs
    faqs = FAQ.objects.all()
    # Extract embeddings and answers from FAQs for matching the similarity scores
    faq_embeddings = [faq.embedding for faq in faqs if faq.embedding]
    faq_answers = [faq.answer for faq in faqs]
    
    
    if faq_embeddings:
        # similarity scores
        similarity_scores = compute_similarity(query_embedding, faq_embeddings)
        max_similarity = max(similarity_scores)
        max_index = similarity_scores.argmax()

        if max_similarity >= 0.7:
            response = faq_answers[max_index]
        else:
            # If no FAQ exists, query the LLM
            response = query_serpapi('give the output in sort ' + user_query)
            # save this as a new InteractionLog(Table)
            InteractionLog.objects.create(
                user_query=user_query,
                response=response
            )
    else:
        # If no FAQ exists, query the LLM
        response = query_serpapi('give the output in sort ' + user_query)

        # save this as a new InteractionLog(Table)
        InteractionLog.objects.create(
            user_query=user_query,
            response=response
        )

    # Render the response
    return render(request, "ask.html", {
        "query": user_query,
        "response": response,
    })
