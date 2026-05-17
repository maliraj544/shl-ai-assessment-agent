from app.recommender import recommend_assessments

query = "I want to hire Java backend developers"

response = recommend_assessments(query)

print(response)