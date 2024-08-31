from textwrap import dedent
from crewai import Agent

class ArticleWritingAgents():
    def planner(self, topic):
        return Agent(
            role="Content Planner",
            goal="Plan engaging and factually accurate content on {topic}",
            tool=[],
            backstory="You're working on planning a blog article "
                    "about the topic: {topic}."
                    "You collect information that helps the "
                    "audience learn something "
                    "and make informed decisions. "
                    "Your work is the basis for "
                    "the Content Writer to write an article on this topic.",
            allow_delegation=False,
            verbose=True
        )
    
    def checker(self, topic):
        return Agent(
            role="Plan Checker",
            goal="Check and verify if the content plan is in line or relevant to the {topic}",
            tool=[],
            backstory="You're working on planning a blog article "
                    "about the topic: {topic}."
                    "You check and verify the planned information to see if its about the {topic} "
                    "You are strict, if the plan is off topic you ask for a rewrite.",
            allow_delegation=False,
            verbose=True
        )


    def writer(self, topic):
        return Agent(
            role="Content Writer",
            goal="Write insightful and factually accurate "
                "opinion piece about the topic: {topic}",
            backstory="You're working on a writing "
                    "a new opinion piece about the topic: {topic}. "
                    "You base your writing on the work of "
                    "the Content Planner, who provides an outline "
                    "and relevant context about the topic. "
                    "You follow the main objectives and "
                    "direction of the outline, "
                    "as provide by the Content Planner. "
                    "You also provide objective and impartial insights "
                    "and back them up with information "
                    "provide by the Content Planner. "
                    "You acknowledge in your opinion piece "
                    "when your statements are opinions "
                    "as opposed to objective statements.",
            allow_delegation=False,
            verbose=True
        )
    
    def editor(self):
        return Agent(
            role="Editor",
            goal="Edit a given blog post to align with "
                "the writing style of the organization. ",
            backstory="You are an editor who receives a blog post "
                    "from the Content Writer. "
                    "Your goal is to review the blog post "
                    "to ensure that it follows journalistic best practices,"
                    "provides balanced viewpoints "
                    "when providing opinions or assertions, "
                    "and also avoids major controversial topics "
                    "or opinions when possible.",
            allow_delegation=False,
            verbose=True
        )