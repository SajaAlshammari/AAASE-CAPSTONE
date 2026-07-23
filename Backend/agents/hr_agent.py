from datetime import date

from services.llm import llm
from prompts.offer_prompt import offer_prompt
from prompts.contract_prompt import contract_prompt
from prompts.onboarding_prompt import onboarding_prompt
from utils.template_loader import render_template
from models.schemas import Candidate


def generate_offer(candidate: Candidate):
    response = llm.invoke(offer_prompt(candidate))
    return response.content


def generate_contract(candidate: Candidate):
    response = llm.invoke(contract_prompt(candidate))
    return response.content


def generate_onboarding(candidate: Candidate):
    response = llm.invoke(onboarding_prompt(candidate))
    return response.content


def get_offer_details(position):

    position = position.lower()

    if "manager" in position:
        return {
            "department": "Management",
            "salary": "25,000 SAR / Month",
            "manager": "CEO"
        }

    elif "engineer" in position:
        return {
            "department": "Engineering",
            "salary": "12,000 SAR / Month",
            "manager": "Mohammed Alqahtani"
        }

    elif "analyst" in position:
        return {
            "department": "Data & Analytics",
            "salary": "14,000 SAR / Month",
            "manager": "Data Manager"
        }

    else:
        return {
            "department": "General",
            "salary": "10,000 SAR / Month",
            "manager": "HR Manager"
        }


def generate_offer_document(candidate: Candidate):

    details = get_offer_details(candidate.position)

    return render_template(
        "offer_letter.html",
        date=date.today().strftime("%d %B %Y"),
        name=candidate.name,
        position=candidate.position,
        department=details["department"],
        salary=details["salary"],
        start_date="1 September 2026",
        manager=details["manager"],
        working_hours="Sunday - Thursday | 8 AM - 5 PM",
    )


def generate_contract_document(candidate: Candidate):

    details = get_offer_details(candidate.position)

    return render_template(
        "contract.html",
        name=candidate.name,
        position=candidate.position,
        salary=details["salary"],
        probation="90 Days",
        working_hours="Sunday - Thursday | 8 AM - 5 PM",
        annual_leave="21 Days",
        location="Riyadh, Saudi Arabia",
    )


def create_candidate(state) -> Candidate:
    data = state["candidate"]

    return Candidate(
        name=data["name"],
        email=data["email"],
        position=data["position"],
        experience=data["experience"],
        skills=data["skills"],
    )