import os
import cohere
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class RankLLM:

    def __init__(self) -> None:
        self.cohere_api_key = os.getenv('COHERE_API_KEY')
        self.groq_aoi_key = os.getenv('GROQ_API_KEY')

        self.responses = []
        self.ranked_response = []


        self.prompt_template = """
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

        self.prompt = self.prompt_template.format(topic='Mobile legend')

        self.models = ['llama-3.1-8b-instant', 'gemma-7b-it', 'mixtral-8x7b-32768']


    def make_request(self, prompt, model):
        groq = Groq(api_key=self.groq_aoi_key)
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


    def rerank_response(self, user_prompt, doc):
        cohere_obj = cohere.ClientV2(self.cohere_api_key)
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
            top_n=3,
            return_documents=True

        )
        return cohere_result


    def main(self):
        for model in self.models:
            result = self.make_request(self.prompt ,model)
            self.responses.append(result)
        ranked_response = self.rerank_response(self.prompt, self.responses)
        return ranked_response
