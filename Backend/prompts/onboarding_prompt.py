def onboarding_prompt(candidate):

    return f"""
You are an HR Manager.

Candidate:

{candidate.name}

Position:

{candidate.position}

Skills:

{", ".join(candidate.skills)}

Create a concise onboarding plan.

Format:

Week 1:
...

Week 2:
...

Week 3:
...

Week 4:
...

No introduction.
No conclusion.
"""