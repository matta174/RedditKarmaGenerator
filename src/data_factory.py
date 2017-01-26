from OAuth2 import reddit

submission_id_list = [] # will collect the submission id's for comparision later.


for submission in reddit.subreddit('learnpython').hot(limit=10):
    submission_id_list.append(submission.id)

    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)  # Output: the submission's ID
    print(submission.url)
    print('\n')


print(submission_id_list)



for ID in submission_id_list: #loops through submission_id_list based on id
    submission = reddit.submission(id=ID)
    print(submission.title +'\t' + str(submission.score))

