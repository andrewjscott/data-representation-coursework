""" 
Write a program in python that will read a file from a repository, 
The program should then replace all the instances of the text "Andrew" with your name
The program should then commit those changes and push the file back to the repository.

Author: Andrew Scott 
"""

import requests
from github import Github
from config import config as cfg

# Since my name is also Andrew, I will instead get user input to specify the name they wish to 
# replace replace all the instances of the text "Andrew" with
name = input('Enter a name to replace "Andrew" with: ')

# using key from hidden config file and pygithub module to access github repo
api_key = cfg["git_key"]
g = Github(api_key)
repo = g.get_repo("andrewjscott/aprivateone")
clone_url = repo.clone_url
# print(repo)

# See the contents of the repo
file_info = repo.get_contents("")
# for files in file_info:
#     print(files)

# Access the file we want to change
file_info = repo.get_contents("names.txt")
url_of_file = file_info.download_url

# Get the text contents of the file
# https://stackoverflow.com/questions/61292766/read-content-of-file-which-is-in-github-using-pygithub
file_content = file_info.decoded_content.decode("utf-8")

# print(file_content)

# Write the contents from github to a new file that will be altered
with open ("names.txt", "w") as f:
    f.write(file_content)

# Function that takes in the name to be replaced and changes it with the name entered by the user
def replace_name(old_name):
# Find and replace instances of "Andrew" with name input by user
# adapted from: https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
    with open("names.txt") as r:
        text = r.read().replace(old_name, name)
    with open("names.txt", "w") as w:
        w.write(text)
    with open("names.txt") as r:
        new_text = r.read()    
  
    # Replace the content in the github file with the text from the locally edited version that has the names changed
    repo.update_file(file_info.path, "Replacing all Andrew's in names.txt", new_text, file_info.sha)

if __name__ == "__main__":
    replace_name("Andrew")

