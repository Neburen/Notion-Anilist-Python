import requests
import json
from Anilist import getAnime

# Your Notion data goes here
token = "secret_KEY"
databaseId = "databaseId"

# For Notion API calls
headers = {"Authorization": "Bearer " + token,
           "Content-Type": "application/json",
           "Notion-Version": "2022-06-28"}

# Get database from Notion
req = requests.post(
    f"https://api.notion.com/v1/databases/{databaseId}/query", headers=headers)
dicc = json.loads(req.text)

# Iterate over the database
print("Updating animes: ")
control = False
for anime in dicc["results"]:
    # Animes watched are not updated
    if anime["properties"]["Tags"]["select"]["name"] != "Watched":
        print(anime["properties"]["Name"]["title"]
              [0]["plain_text"]+"...", end=" ", flush=True)
        # Try to get the anime info, if it fails, try again removing last 2 characters
        # and then ask the user to select the anime
        try:
            animeInfo = getAnime(anime["properties"]
                                 ["Name"]["title"][0]["plain_text"])
            control = True
        except IndexError:
            try:
                animeInfo = getAnime(
                    anime["properties"]["Name"]["title"][0]["plain_text"][:-2], manualSelect=True)
                control = True
            except Exception:
                print("\n" + anime["properties"]["Name"]["title"]
                      [0]["plain_text"], "is not updating")

        # If the anime info is found, update the Notion database
        if control:
            page_id = anime["id"]

            # Format the anime info
            data = [animeInfo["status"], animeInfo["episodes"],
                    str(animeInfo["endDate"])]
            try:
                data[1] = int(data[1])
            except ValueError:
                data[1] = "None"
            try:
                date = f"{data[2]['year']}-{data[2]['month']:02}-{data[2]['day']:02}"
            except:
                date = "null"

            # Format the payload to update the Notion database
            payload = {
                "properties": {
                    "End date": {
                        "date": {
                            "start": date
                        }
                    },
                    "Episodes": {
                        "number": data[1]
                    },
                    "Status": {
                        "select": {
                            "name": data[0]
                        }
                    }
                }
            }
            if payload["properties"]["End date"]["date"]["start"] == "null":
                payload["properties"].pop("End date")
            if payload["properties"]["Episodes"]["number"] == "None":
                payload["properties"].pop("Episodes")

            # Update the Notion database
            response = requests.patch(
                f"https://api.notion.com/v1/pages/{page_id}", json=payload, headers=headers)
            if response.status_code == 200:
                print("Updated")
        control = False
input("Press enter to exit")
