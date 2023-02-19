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

filters = {  # Animes watched are not updated
    "property": "Tags",
    "select": {
        "does_not_equal": "Watched"
    }
}

payload = {
    "filter": filters
}

# Get database from Notion
req = requests.post(
    f"https://api.notion.com/v1/databases/{databaseId}/query", json=payload, headers=headers)
dicc = json.loads(req.text)

isLongList = True
# Iterate over the database
print("Updating animes: ")
while isLongList:
    isLongList = dicc["has_more"]
    control = False
    for anime in dicc["results"]:
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

            # Format Status
            if data[0] == "FINISHED":
                data[0] = "Finished"
            elif data[0] == "RELEASING":
                data[0] = "Releasing"
            elif data[0] == "NOT_YET_RELEASED":
                data[0] = "Not yet released"
            elif data[0] == "CANCELLED":
                data[0] = "Cancelled"

            # Format number of episodes
            try:
                data[1] = int(data[1])
            except:
                data[1] = "None"
            # Format dates
            try:
                data[2] = json.loads(data[2].replace("'", '"')
                                     .replace("None", "null"))
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

    # If the list is 100+ items, get the next 100 items
    if isLongList:
        payload = {
            "filter": filters,
            "start_cursor": dicc["next_cursor"]
        }
        req = requests.post(
            f"https://api.notion.com/v1/databases/{databaseId}/query", json=payload, headers=headers)
        dicc = json.loads(req.text)

        # Relaxing pause for APIS
        input("What a long list! 100 items were updated this time.\n Press enter to continue updating...")

input("Press enter to exit")
