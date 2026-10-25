def build_ledger(callsigns, statuses):
    ledger = {}

    for i in range(len(callsigns)):
        ledger[callsigns[i]] = statuses[i]
    
    return ledger


