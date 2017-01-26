from twisted.internet import task, reactor
timeout = 60.0

def checkForTimes():
    print("function will go here")

runCheck = task.LoopingCall(checkForTimes())
runCheck.start(timeout)

reactor.run()
