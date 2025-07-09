from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from os import getenv
from dotenv import load_dotenv

load_dotenv()

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

headers = {
    "HTTP-Referer": getenv("YOUR_SITE_URL"),
    "X-Title": getenv("YOUR_SITE_NAME"),
}

llm = ChatOpenAI(
    api_key=getenv("OPENROUTER_API_KEY"),
    base_url=getenv("OPENROUTER_BASE_URL"),
    model="deepseek/deepseek-r1:free",
    default_headers={k: v for k, v in headers.items() if v is not None},
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

question = "yoo bro how are you doing , now tell me what was my last question to you"

print(chain.invoke({"question": question}))
print(llm.predict("what is the capital of France?"))