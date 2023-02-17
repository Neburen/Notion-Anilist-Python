# Notion-Anilist-Python
This program will automatically update properties like Anime Status, Episodes or End date from your Notion Database collecting the data from AniList

Steps: 
- [1. Create a new integration in Notion](#1-create-a-new-integration-in-notion)
- [2. Create the database](#2-create-the-database)
- [3. Grant access to the database](#3-Grant-access-to-the-database)
- [4. Update the code](#4-Update-the-code)
- [5. Run Notion.py !!!](#5-run-notionpy-)

# 1. Create a new integration in Notion 
First go to: [Notion integrations](https://www.notion.so/my-integrations), create a new integration with the name you want, make sure to check all "Content Capabilities" and "Comment Capabilities", also check only "Read user information without email addresses" in User Capabilities and Submit.

Finally copy your "Internal Integration Token"

# 2. Create the database
2 options:

1.- (Easy) [Copying the template](https://nebur.notion.site/Notion-Anilist-Python-15d384e86fd84feda877971a0d7ea15a)

2.- (Hard) Create your own database. You will need to add these properties with these names: 

    (type Select) Tags
    (type Select) Status with options: Not Released, Releasing and Finished
    (type Number) Episodes
    (type Date) End date

# 3. Grant access to the database
Now you need to grant it access to a database going to the database page (Important, it should be the database page, not the page that contains the database) in your Notion workspace.

Click the ••• on the top right corner of the page, at the bottom of the pop-up, click "Add connections", 
search and select your integration in the search bar.

Now look at the URL and save the Database ID ![App Screenshot](https://files.readme.io/62e5027-notion_database_id.png)

# 4. Update the code
Open Notion.py and paste your "Internal Integration Token" in token variable and the Database ID in databaseId variable

# 5. Run Notion.py !!!
