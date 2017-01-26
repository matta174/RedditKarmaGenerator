from OAuth2 import reddit
from twisted.internet import task, reactor
#timeout = 60.0

#def checkForTimes():
 #   print("function will go here")

#runCheck = task.LoopingCall(checkForTimes())
#runCheck.start(timeout)

#reactor.run()



submission_id_list = [] # will collect the submission id's for comparision later.

submission = {
    ''
}


for submission in reddit.subreddit('all').hot(limit=10):
    submission_id_list.append(submission.id)


print(submission_id_list)

for ID in submission_id_list:
    submission = reddit.submission(id=ID)
    print(submission.title + '\tScore: ' + str(submission.score) + '\n' +submission.url +'\n') #Outputs some of the data grabbed earlier in a formatted way


