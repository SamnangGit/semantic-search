import requests
import os
import cohere
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

cohere_api_key = os.getenv('COHERE_API_KEY')
groq_aoi_key = os.getenv('GROQ_API_KEY')

responses = []
ranked_response = []


prompt_template = """
    You are tasked with generating three insightful questions based on a topic provided by a user. These questions should be designed to elicit thoughtful and meaningful responses.

    The topic provided by the user is:
    <topic>
    {topic}
    </topic>

    To generate the questions, follow these guidelines:
    1. Analyze the given topic and consider its various aspects, implications, and potential areas of discussion.
    2. Formulate questions that encourage critical thinking, reflection, or exploration of the topic.
    3. Ensure that the questions are open-ended and cannot be answered with a simple "yes" or "no".
    4. Aim for a mix of questions that cover different angles or subtopics within the main topic.
    5. Avoid overly broad or vague questions; instead, focus on specific aspects that can lead to insightful discussions.

    Present your output in the following format:
    <questions>
    1. [First question]
    2. [Second question]
    3. [Third question]
    </questions>

    Here are two examples of how your output should look:

    Example 1:
    Topic: Climate change
    <questions>
    1. How might the effects of climate change impact global food security in the next 50 years?
    2. What role can emerging technologies play in mitigating the impacts of climate change?
    3. How can governments balance economic growth with environmental protection in their climate policies?
    </questions>

    Example 2:
    Topic: Social media influence
    <questions>
    1. In what ways has social media altered the landscape of political discourse and voter engagement?
    2. How has the rise of influencer culture on social media platforms affected traditional marketing strategies?
    3. What are the potential long-term psychological effects of constant social media use on younger generations?
    </questions>

    Remember, the goal is to create questions that will prompt insightful, thought-provoking answers and stimulate meaningful discussions on the given topic.
"""

prompt = prompt_template.format(topic='Mobile legend')

models = ['llama-3.1-8b-instant', 'gemma-7b-it', 'mixtral-8x7b-32768']


def make_request(prompt, model):
    groq = Groq(api_key=groq_aoi_key)
    response = groq.chat.completions.create(
        messages=[
            {
                'role' : 'user',
                'content' : prompt
            }
        ],
        model=model
    )
    return response.choices[0].message.content


def rerank_response(user_prompt, doc):
    cohere_obj = cohere.ClientV2(cohere_api_key)
    print(doc[0])
    print("=====================================")
    print(doc[1])
    print("=====================================")
    print(doc[2])
    print("=====================================")
    cohere_result = cohere_obj.rerank(
        model='rerank-english-v3.0',
        query=user_prompt,
        documents=doc,
        top_n=3

    )
    return cohere_result


def main():
    for model in models:
        result = make_request(prompt ,model)
        responses.append(result)
    ranked_response = rerank_response(prompt, responses)
    print(ranked_response)



if __name__ == "__main__":
    main()