# myapp/openai_service.py
from openai import OpenAI
from ..models.poops import Poops
import json


def evaluate_poop_log(user_id):
    # Retrieve the user's poop logs
    poop_logs = Poops.objects.filter(user_id=user_id)

    # Format the poop logs
    formatted_logs = "\n".join([f"{poop.date}: {poop.difficulty}" for poop in poop_logs])

    # Create the message payload
    messages = [
        {"role": "system", "content": "You are a poop professional and dietician, skilled in evaluating pooping "
                                      "patterns and diet."},
        {"role": "user", "content": f"Evaluate the given poop log and diet log and return a poop score 1-10 and make "
                                    f"better diet recommendations if any to improve poop.\n\nPoop Log:\n{formatted_logs}\n\n"
                                    f"Please return the result in the following JSON format:\n"
                                    f"{{\n"
                                    f"  \"score\": int(1-10),\n"
                                    f"  \"food_recommendations\": string,\n"
                                    f"  \"specific_nutrients\": string\n"
                                    f"}}"}
    ]

    # Call the OpenAI API
    try:
        key = ''
        client = OpenAI(api_key=key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        response_content = response.choices[0].message.content
        return response_content
    except Exception as e:
        return str(e)
