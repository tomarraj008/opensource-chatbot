jobs = [{"name": "Mobile Entwickler iOS", "formOfEmployment": "vollzeit", "jobTask": ["entwickeln"], "domain": ["mobile", "security"], "technology": [
        "swift", "ios", "c#", "verschlüsselung", "unit test", "accessibilty", "usability", "c++", "rest", "graphql", "xml", "maven", "datensicherheit", "ui-test", "git"]}]

foundJobs = []

# Store the values of slots given by the user with the tracker object
taskSlot = ['entwickeln']
domainSlot = ['mobile', 'fullstack']
technologySlot = ['ios', 'swift']
formOfEmploymentSlot = 'vollzeit'

for job in jobs:
    # Store the values of each key for all job dictionaries in the jobs list
    tech = job["technology"]
    task = job["jobTask"]
    domain = job["domain"]
    employment = job["formOfEmployment"]

    # Search for matches between slots sent by the user and stored jobs in the jobs list.
    # If a job has at least one value for each key in the dictionary the job is appended to the foundJobs list.
    if [i.lower() for i in technologySlot if i.lower() in tech] and \
        [i.lower() for i in domainSlot if i.lower() in domain] and \
        [i.lower() for i in taskSlot if i.lower() in task] and \
            [i.lower() for i in formOfEmploymentSlot if i.lower() in employment]:
        foundJobs.append(job)
    # Create a message for the user with a list of names of all found jobs, separated by comma
    jobMessage = ", ".join([c["name"] for c in foundJobs])

# Send message with all found jobs to the user with the dispatcher object
print("Found: " + jobMessage)
