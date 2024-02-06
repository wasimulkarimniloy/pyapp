from googlesearch import search

# Function to perform a Google search
def perform_google_search(query):
    results = []
    for j in search(query, num=10, stop=10, pause=2):
        results.append(j)
    return results

# Your chatbot code
while True:
    user_input = input('niloybot: ')
    
    # If user says "goodbye", the chatbot replies and exits the loop
    if user_input.lower() == 'goodbye':
        print('niloybot: Goodbye! Nice to meet you.')
        break

    # Display search results for the user's query
    search_results = perform_google_search(user_input)
    print("niloybot: Results:")
    for result in search_results:
        print(result)
