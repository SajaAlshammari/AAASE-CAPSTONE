from typing import TypedDict


class HRState(TypedDict):
    candidate: dict
    offer: str
    contract: str
    onboarding: str
    offer_letter: str
    employment_contract: str
    it_account: dict