import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

def run_nexus_system(problem):

    yield "ST_PLANNER", "Strategic Planner is mapping the task..."
    plan = (ChatPromptTemplate.from_template("Break this task into 3 execution steps: {t}") | llm).invoke({"t": problem}).content
    yield "RES_PLANNER", plan


    yield "ST_SOLVER", "Reasoning Agent is generating solution..."
    solution = (ChatPromptTemplate.from_template("Solve this plan with logic: {p}") | llm).invoke({"p": plan}).content
    yield "RES_SOLVER", solution


    yield "ST_CRITIC", "Critic Agent is scanning for errors..."
    critique = (ChatPromptTemplate.from_template("Find 1 major flaw in this solution: {s}. If it's perfect, say 'CLEAR'.") | llm).invoke({"s": solution}).content
    yield "RES_CRITIC", critique

 
    if "CLEAR" not in critique.upper():
        yield "ST_REPLAN", "🔄 Weakness detected! Re-generating improved solution..."
        improved_prompt = ChatPromptTemplate.from_template(
            "Original Task: {t}\nInitial Solution: {s}\nCriticism: {c}\nProvide a final improved version that fixes the flaw."
        )
        final_solution = (improved_prompt | llm).invoke({"t": problem, "s": solution, "c": critique}).content
        yield "FINAL", final_solution
    else:
        yield "FINAL", solution


def get_system_explanation(problem, plan, critique):
    explanation_prompt = ChatPromptTemplate.from_template(
        "Explain the 'thinking process' for this problem: {t}. Why did the Planner suggest: {p}? And why did the Critic find this flaw: {c}? Explain in 3 bullet points."
    )
    return (explanation_prompt | llm).invoke({"t": problem, "p": plan, "c": critique}).content