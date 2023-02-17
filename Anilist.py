import requests
import json

# Data we want from the anilist API
query = '''
query ($query: String, $page: Int, $perpage: Int) {
    Page (page: $page, perPage: $perpage) {
        pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
        }
        media (search: $query, type: ANIME) {
            title {
                romaji
            }
            endDate {
                year
                month
                day
            }
            status
            episodes
            nextAiringEpisode {
                airingAt
                timeUntilAiring
                episode
            }
        }
    }
}
'''


def getAnime(nombre, manualSelect=False):
    if manualSelect == False:
        data = getServer(nombre)
        # return first anime found
        try:
            animeInfo = data['data']['Page']['media'][0]
            return animeInfo
        except IndexError:
            raise IndexError('Anime not found')

    elif manualSelect == True:
        data = getServer(nombre)
        counter = 1  # 1 for exit option
        # print all anime found
        print()
        for i in range(len(data['data']['Page']['media'])):
            curr_anime = data['data']['Page']['media'][i]['title']['romaji']
            print(f"{counter}. {curr_anime}")
            counter += 1
        print(f"{counter}. Exit")
        if counter > 1:
            # ask user to select anime
            while True:
                try:
                    user_input = input(
                        "Please select the anime number you want: ")
                    user_input = int(user_input)
                except:
                    user_input = None
                    print("Your input is incorrect")

                if user_input == None:
                    pass
                elif user_input > counter or user_input <= 0:
                    print(
                        "Your input does not correspond to any of the anime displayed")
                else:
                    break

        elif counter == 1:
            print('No search result has been found for the anime')
            return -1
        elif counter == 2:
            user_input = 1

        if user_input == counter:
            raise Exception("Exit")

        return data['data']['Page']['media'][user_input - 1]

    else:
        pass


def getServer(nombre):
    # Send request to anilist API
    headers = {'Content-Type': 'application/json'}
    getData = {
        'query': query,
        'variables': {
            "query": nombre,
            "page": 1,
            "perpage": 3
        }
    }
    req = requests.post('https://graphql.anilist.co',
                        headers=headers, json=getData)

    # Check if request was successful
    if req.status_code != 200:
        message = req.text.find("message")
        message += 11
        endMessage = req.text[message:].find("\"") + message

        raise Exception(f"Data post unsuccessful. Status code: {req.status_code}, \
message: {req.text[message:endMessage]}. Retry after: {req.headers['Retry-After']} seconds")

    # Extract data from json
    try:
        extracted_data = json.loads(req.text)
    except ValueError:
        return None
    except TypeError:
        return None
    else:
        return extracted_data
