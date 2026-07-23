def offer_prompt(candidate):

    return f"""
You are an HR Manager at TechNova Company in Riyadh, Saudi Arabia.

Generate ONLY the following information as plain text.

Candidate Name:
{candidate.name}

Position:
{candidate.position}

Experience:
{candidate.experience}

Skills:
{", ".join(candidate.skills)}

Company:
TechNova


Determine the employment details based on the position:

Salary rules:
- Manager positions: 25000 SAR
- Engineer positions: 12000 SAR
- Analyst positions: 14000 SAR
- Other positions: 10000 SAR


Department rules:
- Manager positions: Management
- Engineer positions: Engineering
- Analyst positions: Data & Analytics
- Other positions: General


Manager rules:
- Manager positions: CEO
- Engineer positions: Mohammed Alqahtani
- Analyst positions: Data Manager
- Other positions: HR Manager


Return exactly:

Employee Name
Position
Department
Salary (SAR)
Start Date: 1 September 2026
Manager
Working Hours: Sunday - Thursday | 8 AM - 5 PM

Do not write a letter.

Do not add any extra text.
"""