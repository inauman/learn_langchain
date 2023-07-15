from langchain.agents import  load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key='API Key',temperature=0.0)

tools = load_tools(['wikipedia','llm-math'], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

prompt = input('The wikipedia research task: ')

agent.run(prompt)

