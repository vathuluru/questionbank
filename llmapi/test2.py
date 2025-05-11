from openai import OpenAI
import json

# Set your OpenAI API key
#OPENAI_API_KEY = "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"
#openai.api_key = os.getenv("OPENAI_API_KEY")


api_key = "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"

#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
def get_answer(question):
#    try:
        
    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        input=question,
        model="gpt-4.1-nano"
    )
    print(response)
    answer = response.to_dict()["output"]
    print(answer[0].get("content")[0].get("text"))
   
    #answer = response.choices[0].message['content']
    print(answer)
    return response 
        #return answer

#    except Exception as e:
#        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    question = "What is the capital of India?"
    answer = get_answer(question)
    print(answer)
    