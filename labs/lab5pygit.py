# using the package PyGitHub to interact with GitHub

import requests
from github import Github
from config import config as cfg

filename = "test.txt"

api_key = cfg["git_key"]

g = Github(api_key)

repo = g.get_repo("andrewjscott/aprivateone")
clone_url = repo.clone_url

# print(repo.clone_url)

# with open(filename, "w") as f:
#     f.write(clone_url)
    
file_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url
#print(url_of_file)

response = requests.get(url_of_file)
contents_of_file = response.text
#print(contents_of_file)

new_contents = contents_of_file + " more stuff \n"
print(new_contents)

repo.update_file(file_info.path, "Updating test.txt using pygithub", new_contents, file_info.sha)



# for repo in g.get_user().get_repos():
#    print(repo.name)