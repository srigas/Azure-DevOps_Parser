from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# ----- Config details ---------------------------------------------------------------
personal_access_token = 'YOUR_PAT'
organization_url = 'YOUR_ORG_NAME'
project_name = 'YOUR_PROJECT_NAME'
repository_name = 'YOUR_REPO_NAME'
folder = '/' # set the path to the folder you want to list, leave / for root
# -------------------------------------------------------------------------------------

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url='https://dev.azure.com/'+organization_url, creds=credentials)

# Get the client for git operations
git_client = connection.clients.get_git_client()

# Get a list of all items (files and directories) starting at the folder level, to use their paths
items = git_client.get_items(repository_id=repository_name, scope_path=folder,
                             project=project_name, recursion_level='Full')

with open('contents.txt', 'w', encoding='utf-8') as contents_file:
    for item in items:
        # ensure that the selected item is not a folder
        if not item.is_folder:
            # get the path
            file_path = item.path
            # use the path to read the content of the file
            file_content_generator = git_client.get_item_content(repository_id=repository_name, path=file_path,
                                                                project=project_name, download=False)

            file_content = ''.join([chunk.decode('utf-8') for chunk in file_content_generator])

            # write contents to file
            contents_file.write(f"{item.path}:\n```\n")
            contents_file.write(f"{file_content}\n```\n\n")