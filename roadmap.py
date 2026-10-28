
from groq import Groq


def generate_roadmap(field, level, weeks, hours, api_key, model):
    """Generate a personalized learning roadmap using Groq."""

    client = Groq(api_key=api_key)

    prompt = f"""
Create a practical learning roadmap using the details below.

Learning field: {field}
Current skill level: {level}
Duration: {weeks} weeks
Study time: {hours} hours per week

Include these sections:

1. Learning goals
2. Week-by-week plan
3. Topics in the correct learning order
4. Practical exercises for each week
5. One final project suitable for this level
6. Free learning resources with useful URLs
7. Progress checklist

Instructions:
- Use simple English and clear headings.
- Keep the plan realistic for the available time.
- Make the exercises relevant to the selected field.
- Adapt the difficulty to the selected skill level.
- Do not promise mastery in a short time.
- Do not return JSON. Use normal Markdown.
- Make the weekly plan detailed but concise.
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a learning planner. "
                    "Create realistic, well-organized learning roadmaps "
                    "for students at different skill levels."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        max_tokens=4000,
    )

    result = response.choices[0].message.content

    if not result or not result.strip():
        raise ValueError("The AI returned an empty response.")

    return result.strip()
