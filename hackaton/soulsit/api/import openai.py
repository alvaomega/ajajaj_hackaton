import openai

openai.api_key = "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"

def suggest_specialists(project_description):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="In your project, based on the description '" + project_description + "', what specialist roles should you have?",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"].strip()
    return message

project_description = "I am building a website for a e-commerce store that sells handmade jewelry."
specialist_advice = suggest_specialists(project_description)
print("Advice:", specialist_advice)
