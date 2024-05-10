from langchain.prompts import PromptTemplate

REFINE_PROMPT_TMPL = (
    "Your job is to produce a final review of {words_count} words while following all rules\n"
    "=========\n"
    "Rules: {rules}\n"
    "=========\n"
    "We have provided an existing review up to a certain point: {existing_answer}\n"
    "We have the opportunity to refine the existing review"
    "(only if needed) with some more context below.\n"
    "------------\n"
    "{text}\n"
    "------------\n"
    "Given the new context, refine the original review\n"
    "If the context isn't useful, return the original review."
)
REFINE_PROMPT = PromptTemplate(
    input_variables=["existing_answer", "text", "words_count", "rules"],
    template=REFINE_PROMPT_TMPL,
)

prompt_template = """
=========
Rules:
{rules}
=========

Write a review of the following of {words_count} words following all rules:


"{text}"


Review:"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["text", "words_count", "rules"])