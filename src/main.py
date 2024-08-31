from dotenv import load_dotenv
from crewai import Crew
from tasks import ArticleWritingTasks
from agents import ArticleWritingAgents
from textwrap import dedent

import os
from langchain_openai import ChatOpenAI
os.environ["OPENAI_API_KEY"] = ""
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

def main():
    load_dotenv()

    print("## Welcome to the Article Writing Agent Demo! ##")
    print('-----------------------------------')
    topic = input("What topic do you want to write about?\n")

    tasks = ArticleWritingTasks()
    agents = ArticleWritingAgents()

    #create agents
    planner = agents.planner(topic)
    checker = agents.checker(topic)
    writer = agents.writer(topic)
    editor = agents.editor()

    # create tasks
    plan = tasks.plan(topic, planner)
    check = tasks.check(topic, checker)
    write = tasks.write(topic, writer)
    edit = tasks.edit(editor)

    edit.context = [write]

    crew = Crew(
        agents=[planner, checker, writer, editor],
        tasks=[plan, check, write, edit],
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": topic})

    print(result)

if __name__ == "__main__":
    main()