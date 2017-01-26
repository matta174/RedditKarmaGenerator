from OAuth2 import reddit
from twisted.internet import task, reactor
timeout = 60.0

def checkForTimes():
    print("function will go here")

runCheck = task.LoopingCall(checkForTimes())
runCheck.start(timeout)

reactor.run()



submission_id_list = [] # will collect the submission id's for comparision later.


for submission in reddit.subreddit('learnpython').hot(limit=10):
    submission_id_list.append(submission.id)
    print(submission.title)

print(submission_id_list)