from google import genai
from dotenv import load_dotenv
import datetime
import json
import os

load_dotenv()
class Parser:
    def __init__(self, event_text):
        api_key=os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        self.client = genai.Client(api_key=api_key)
        self.event = event_text

    def parse(self):
         # Define the prompt for the model
        current_time = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
        prompt = "today's date is " + current_time + "parse the event that i type into a calendar event making sure that event names are capitalized, " \
             "and return the event in standard JSON format: " \
                "'{'Event Title': the event's title, Start time: 'YYYY-MM-THH:MM:SSZ', End Time: 'YYYY-MM-DDTHH:MM:DDZ', 'Event Location': Location, 'Event Description': description', 'Type': type}'. \
                     the field name 'type' and takes value of add, delete, or modify which provides context to whether this event should be added, deleted, or modified.  default value is add."" here is the event: " + self.event

        # Call the model with the prompt
        response = self.client.models.generate_content(
            model="gemini-2.5-flash", contents= prompt
     )
        # Print the response from the model
        output = str(response.text)
        print("Response from the model:", output)
        # Parse the output to extract the event details
        start = output.find('{')
        end = output.rfind('}') + 1
        json_output = output[start:end]
        print("JSON Output:", json_output)
        parsed = json.loads(json_output)
        return parsed
