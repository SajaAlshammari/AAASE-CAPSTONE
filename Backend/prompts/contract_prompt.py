def contract_prompt(candidate):

    return f"""
You are an HR Manager at TechNova Company in Riyadh, Saudi Arabia.

Generate ONLY the following information.

Employee Name:
{candidate.name}

Position:
{candidate.position}

Company:
TechNova

Determine the salary based on the employee position.

Salary rules:
- Manager positions: 25000 SAR/month
- Engineer positions: 12000 SAR/month
- Analyst positions: 14000 SAR/month
- Other positions: 10000 SAR/month

Return exactly:

Employee Name
Position
Salary: [calculated salary]
Probation Period: 90 Days
Working Hours: Sunday - Thursday | 8 AM - 5 PM
Annual Leave: 21 Days
Location: Riyadh, Saudi Arabia

Do not add any extra text.
"""