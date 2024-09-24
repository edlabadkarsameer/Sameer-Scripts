from jira import JIRA

# Jira credentials and server URL
jira_server = 'http://192.168.31.11:8080/'
jira_username = 'sameer.edlabadkar'
jira_password = 'Test@123'

# Jira authentication
options = {'server': jira_server}
jira = JIRA(options, basic_auth=(jira_username, jira_password))

# Project key and board name
project_key = 'GVJ'
board_name = 'GVJ board'
sprint_name = 'GVJ Sprint 3'

# Get all boards and find the specific Scrum board by name
all_boards = jira.boards()
scrum_board = next((board for board in all_boards if board.type == 'scrum' and board.name == board_name), None)

if not scrum_board:
    print(f"No Scrum board named '{board_name}' found.")
    exit()

board_id = scrum_board.id

# Get the sprint ID for the target sprint
sprints = jira.sprints(board_id)
sprint_id = None
for sprint in sprints:
    if sprint.name == sprint_name:
        sprint_id = sprint.id
        break

if sprint_id is None:
    print(f"Sprint '{sprint_name}' not found.")
    exit()

# JQL query to get all issues in the backlog for the specific project
jql_query = f'project = {project_key} AND Sprint = EMPTY'

# Get all issues in the backlog
issues_in_backlog = jira.search_issues(jql_query, maxResults=False)

# Move each issue to the target sprint
for issue in issues_in_backlog:
    try:
        jira.add_issues_to_sprint(sprint_id, [issue.key])
        print(f"Issue {issue.key} moved to sprint {sprint_name}.")
    except Exception as e:
        print(f"Failed to move issue {issue.key}: {e}")
