from langgraph.graph import StateGraph, END

from graph.state import HRState

from agents.hr_agent import (
    generate_offer,
    generate_contract,
    generate_onboarding,
    generate_offer_document,
    generate_contract_document,
    create_candidate,
)
from agents.it_agent import ITAgent


def offer_node(state: HRState):
    candidate = create_candidate(state)
    state["offer"] = generate_offer(candidate)
    return state


def contract_node(state: HRState):
    candidate = create_candidate(state)
    state["contract"] = generate_contract(candidate)
    return state


def onboarding_node(state: HRState):
    candidate = create_candidate(state)
    state["onboarding"] = generate_onboarding(candidate)
    return state


def offer_letter_node(state: HRState):
    candidate = create_candidate(state)
    state["offer_letter"] = generate_offer_document(candidate)
    return state


def employment_contract_node(state: HRState):
    candidate = create_candidate(state)
    state["employment_contract"] = generate_contract_document(candidate)
    return state

def it_node(state: HRState):
    candidate = create_candidate(state)
    agent = ITAgent()
    state["it_account"] = agent.save_employee(candidate)
    return state


builder = StateGraph(HRState)

builder.add_node("offer", offer_node)
builder.add_node("contract", contract_node)
builder.add_node("onboarding", onboarding_node)
builder.add_node("offer_letter", offer_letter_node)
builder.add_node("employment_contract", employment_contract_node)
builder.add_node("it", it_node)

builder.set_entry_point("offer")

builder.add_edge("offer", "contract")
builder.add_edge("contract", "onboarding")
builder.add_edge("onboarding", "offer_letter")
builder.add_edge("offer_letter", "employment_contract")
builder.add_edge("employment_contract", "it")
builder.add_edge("it", END)

graph = builder.compile()