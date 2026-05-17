from app.retrieval import retrieve_assessments
from app.llm import generate_response


def recommend_assessments(user_query):

    # Retrieve relevant assessments
    results = retrieve_assessments(user_query)

    context = ""

    recommendations = []

    for item in results:

        recommendations.append({
            "name": item["name"],
            "url": item["link"],
            "duration": item.get("duration", ""),
            "remote": item.get("remote", "")
        })

        context += f"""
        Assessment Name: {item['name']}
        URL: {item['link']}
        Description: {item['description']}
        Job Levels: {item.get('job_levels', [])}
        Duration: {item.get('duration', '')}
        Remote Testing: {item.get('remote', '')}
        Adaptive/IRT: {item.get('adaptive', '')}
        """

    prompt = f"""
    You are an SHL assessment recommendation assistant.

    User Query:
    {user_query}

    Available Assessments:
    {context}

    Instructions:
    - Recommend the best matching assessments.
    - Explain WHY they match.
    - Mention duration if available.
    - Mention remote testing support.
    - Keep response concise and professional.
    - Only use provided assessment data.
    """

    explanation = generate_response(prompt)

    return {
        "recommendations": recommendations,
        "explanation": explanation
    }