import fitz
import json

from services.llm import llm


def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


def extract_candidate(pdf_path):

    resume = extract_text(pdf_path)

    prompt = f"""
You are an HR Resume Parser.

Extract the candidate information from this resume.

Return ONLY valid JSON.

Format:

{{
    "name": "",
    "email": "",
    "position": "",
    "experience": "",
    "skills": []
}}

Resume:

{resume}
"""

    response = llm.invoke(prompt)

    print(response.content)

    content = response.content

    # استخراج أول { وآخر }
    start = content.find("{")
    end = content.rfind("}")

    if start == -1 or end == -1:
        raise Exception("No JSON returned from LLM")

    json_text = content[start:end + 1]

    return json.loads(json_text)