from fastapi import APIRouter, UploadFile, File
import shutil
import os

from agents.resume_agent import extract_candidate
from graph.graph import graph

router = APIRouter(
    prefix="/hr",
    tags=["HR"]
)


@router.post("/resume")
async def analyze_resume(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    candidate = extract_candidate(file_path)

    result = graph.invoke(
        {
            "candidate": candidate,
            "offer": "",
            "contract": "",
            "onboarding": "",
            "offer_letter": "",
            "employment_contract": "",
            "it_account": {}
        }
    )

    return result