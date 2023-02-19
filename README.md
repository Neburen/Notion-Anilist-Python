# Notion-Anilist-Python
This program will automatically update the properties Anime Status, Episodes and End date from your Notion Anime Database collecting the data from AniList.

# Requirements
* Tested in Python 3.6 and 3.9

# Steps: 
- [1. Create a new integration in Notion](#1-create-a-new-integration-in-notion)
- [2. Create the database](#2-create-the-database)
- [3. Grant access to the database](#3-Grant-access-to-the-database)
- [4. Try the website (alternative)](#4-try-the-website-alternative)
- [5. Update the code](#4-Update-the-code)
- [6. Run Notion.py !!!](#5-run-notionpy-)

# 1. Create a new integration in Notion 
First go to: [Notion integrations](https://www.notion.so/my-integrations), create a new integration with the name you want, make sure to check all "Content Capabilities" and "Comment Capabilities", also check only "Read user information without email addresses" in User Capabilities and Submit.

Finally copy your "Internal Integration Token"

# 2. Create the database
2 options:

(Later you can modify other properties in the database with both options)

1.- (Easy) [Duplicating the template](t.ly/loy7) 

2.- (Hard) Create your own database. You will need to add these properties with these names: 

    (type Select) Tags with options: Watch, Watching and Watched
    (type Select) Status with options: Not yet released, Releasing and Finished
    (type Number) Episodes
    (type Date) End date

# 3. Grant access to the database
Now you need to grant it access to a database going to the database page (Important, it should be the database page, not the page that contains the database) in your Notion workspace.

Click the ••• on the top right corner of the page, at the bottom of the pop-up, click "Add connections", 
search and select your integration in the search bar.

Now look at the URL and save the Database ID ![App Screenshot](https://files.readme.io/62e5027-notion_database_id.png)

# 4. Try the website (alternative)

I've made a website where you can try the code. It has some restrictions but mostly works fine.

You only need to follow the steps up to number 3 (included) [Website](https://t.ly/qOgV)

# 5. Update the code
Open Notion.py and paste your "Internal Integration Token" in token variable and the Database ID in databaseId variable

# 6. Run Notion.py !!!
Enjoy! (Watched animes won't be updated)

## Contributing
Contributions are always welcome!

AniList allows to see a lot of data relationated with an anime, the properties you want to see in Notion can be expanded
