from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key='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',temperature=0.0)
prompt = PromptTemplate(
    input_variables=['content', 'customer_name', 'agent_name'],
    template="""
        You are an AI assistant that's optimized to write concise, friendly, & professional emails to customers.

        Write an email to a customer with the name {customer_name} that contains the following optimized contents: {content}

        The email should contain the name of the customer agent who wrote the email: {agent_name}
"""
)

content = input('Email content: ')
customer = input('Customer name: ')
agent = input(' Agent name: ')

response = llm(prompt.format(content=content, customer_name=customer, agent_name=agent))

print(response)
