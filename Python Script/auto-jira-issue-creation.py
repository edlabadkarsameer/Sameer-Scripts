from jira import JIRA
import random

# Jira credentials and server URL
jira_server = 'http://192.168.31.11:8080/'
jira_username = 'sameer.edlabadkar'
jira_password = 'Test@123'

# Jira project details
project_key = 'GVJ'

# Jira authentication
options = {'server': jira_server}
jira = JIRA(options, basic_auth=(jira_username, jira_password))

# Expanded lists of summaries, descriptions, issue types, and assignees
summaries = [
    'Fix bug in login module',
    'Add new feature to dashboard',
    'Update user profile page',
    'Improve performance of search functionality',
    'Refactor codebase for better readability',
    'Add unit tests for existing modules',
    'Design new UI for settings page',
    'Update API documentation',
    'Implement caching for data requests',
    'Fix UI responsiveness issues on mobile',
    'Migrate database to new server',
    'Optimize image loading times',
    'Integrate third-party authentication',
    'Set up CI/CD pipeline',
    'Add error tracking and logging',
    'Improve security measures',
    'Update dependencies to latest versions',
    'Fix memory leak in data processing',
    'Conduct user research for new features',
    'Prepare for product launch'
]

descriptions = [
    'The login module has a bug that needs to be fixed.',
    'A new feature should be added to the dashboard.',
    'The user profile page needs an update.',
    'The search functionality should be optimized for performance.',
    'Refactor the codebase to improve readability and maintainability.',
    'Add unit tests to ensure code quality and prevent regressions.',
    'Design a modern and user-friendly UI for the settings page.',
    'Update the API documentation to reflect recent changes.',
    'Implement caching to reduce load times for data requests.',
    'Fix issues with UI responsiveness on mobile devices.',
    'Migrate the database to a new, more powerful server.',
    'Optimize image loading times to improve page speed.',
    'Integrate third-party authentication providers for single sign-on.',
    'Set up a CI/CD pipeline to automate testing and deployment.',
    'Add error tracking and logging to monitor application health.',
    'Implement additional security measures to protect user data.',
    'Update project dependencies to the latest versions.',
    'Fix a memory leak that occurs during data processing.',
    'Conduct user research to identify desired features.',
    'Prepare the application for the upcoming product launch.'
]

issue_types = [
    'Bug',
    'Task',
    'Epic',
    'Story'
]

assignees = [
    'sameer.edlabadkar',
    'Bhushan',
    'Arun',
    'John',
    'Nick',
    'Rock'
]

# Number of issues to create
num_issues = 2

for i in range(1, num_issues + 1):
    summary = random.choice(summaries)
    description = random.choice(descriptions)
    issue_type = random.choice(issue_types)
    assignee = random.choice(assignees)
    
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},
        'labels': ['DevSecOps'],
        'assignee': {'name': assignee}
    }
    
    # Add Epic Name if issue type is Epic
    if issue_type == 'Epic':
        issue_dict['customfield_10105'] = summary  # Assuming customfield_10105 is the Epic Name field
    
    try:
        issue = jira.create_issue(fields=issue_dict)
        print(f"Issue {i} created: {issue.key}")
        print(f"Description: {description}\n")
    except Exception as e:
        print(f"Failed to create issue {i}: {e}")
