# HR Multi-Agent Onboarding System

An AI-powered multi-agent backend system that automates the employee onboarding process using LangGraph, Groq LLM, FastAPI, and SQLite.

The system uses multiple AI agents to analyze candidate resumes, generate HR documents, and simulate IT onboarding tasks through an automated backend workflow.

---

# Team Members

| Name | GitHub |
|------|--------|
| Munira Abuhaimed | @MuniraNasser3 |
| Saja Alshammari | @SajaAlshammari |
| Jood Alhumaimidi | @Joodalhu |

---

# Problem Statement

Employee onboarding is usually a manual process that requires coordination between different departments, such as HR and IT.

This project automates the onboarding process using a multi-agent AI system where specialized agents collaborate to extract candidate information, generate HR documents, and perform employee provisioning tasks through a backend API.

---

# How the Agent Solves the Problem

## Input

A candidate resume uploaded through the FastAPI API endpoint.

---

## Workflow

### 1. Resume Agent

The Resume Agent analyzes the uploaded resume and extracts candidate information:

- Candidate Name
- Email
- Position
- Experience
- Skills

---

### 2. HR Agent

The HR Agent uses extracted candidate information to automatically generate onboarding documents:

- Job Offer
- Employment Contract
- 4-Week Onboarding Plan
- Offer Letter (HTML)
- Employment Contract (HTML)

---

### 3. IT Agent

The IT Agent simulates employee account provisioning tasks:

- Generate Employee ID
- Create Username
- Generate Company Email
- Generate Temporary Password
- Assign Company Applications
- Store Employee Information in SQLite Database

---

### 4. Final Output

The complete onboarding package is returned through the backend API.

---

# Agentic Behavior

The project demonstrates several agentic behaviors:

- Multi-Agent Collaboration
- LangGraph State Management
- Sequential Agent Routing
- Shared State Between Agents
- Automated Workflow Execution
- Specialized Agents for Different Tasks

---

# Architecture
flowchart TD

A[Upload Resume API]

B[Resume Agent]

C[Extract Candidate Information]

D[HR Agent]

E[Generate Job Offer]

F[Generate Employment Contract]

G[Generate Onboarding Plan]

H[Generate Offer Letter HTML]

I[Generate Contract HTML]

J[IT Agent]

K[Generate Employee ID]

L[Create Username]

M[Create Company Email]

N[Generate Temporary Password]

O[Assign Applications]

P[(SQLite Database)]

A --> B
B --> C
C --> D

D --> E
D --> F
D --> G
D --> H
D --> I

I --> J

J --> K
J --> L
J --> M
J --> N
J --> O

O --> P

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | REST API Development |
| LangGraph | Multi-Agent Workflow Management |
| LangChain | LLM Integration |
| Groq API | Large Language Model |
| SQLite | Employee Database |
| Jinja2 | HTML Document Generation |
| PyPDF2 | Resume PDF Extraction |

---



---

# How to Run

Clone the repository:
git clone https://github.com/<username>/AAASE-CAPSTONE.git

Navigate to the backend folder:
cd Backend

Create a virtual environment:
python -m venv .venv

Activate the environment:

### Windows
.venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Create environment variables:
cp .env.example .env

Add your Groq API key inside .env.

Run the FastAPI server:
uvicorn app:app --reload

Open API documentation:
http://127.0.0.1:8000/docs

The system can be tested directly through the FastAPI Swagger interface by uploading a resume file and executing the onboarding workflow.

---

# Demonstration

The backend API successfully performs the complete employee onboarding workflow.

The system generates:

- Extracted Candidate Information from Resume
- Job Offer
- Employment Contract
- 4-Week Onboarding Plan
- Offer Letter (HTML)
- Employment Contract (HTML)
- Employee ID
- Company Username
- Company Email
- Temporary Password
- Assigned Applications
- Employee Information Stored in SQLite Database

Screenshots of API responses and generated documents are available in:
