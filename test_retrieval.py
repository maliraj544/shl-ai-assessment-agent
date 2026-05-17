from app.retrieval import retrieve_assessments

query = "Java developer assessment"

results = retrieve_assessments(query)

for item in results:

    print("=" * 50)

    print("NAME:", item["name"])

    print("URL:", item["link"])

    print("DESCRIPTION:", item["description"][:200])