import gitSynchronization

def start():
    
    gitSynchronization.printLocalRemoteSha()
    result = gitSynchronization.checkLocalRemoteSync()
    
    print("\nRepo in Sync? : ", result)