import openai 
import json

openai.api_key = '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'

def get_chatGPT_inputs(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=3000
    )
    print(response)

    # Parse the output from the model to get the color palettes and font vector
    output_lines = response.choices[0].text.strip().split('\n')
    chatGPT_output = []

    for line in output_lines:
        if line.startswith("chatGPT_output =") or line.startswith("chatGPT_inputs ="):
            # Extract the JSON string from the line
            json_str = line.split(" = ")[1].strip()
            # Parse the JSON string as a list of dictionaries
            input_data = json.loads(json_str)
            chatGPT_output.extend(input_data)

    return chatGPT_output

