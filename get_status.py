def get_status(ledger, callsign):  # Defines a function that takes a dictionary and a callsign.
    return ledger.get(callsign, "unknown")  # Returns the callsign's status or "unknown" if missing.


# Test 1: Callsign exists
print(get_status({"Ada": "active", "Tunde": "standby"}, "Ada"))  # Prints "active" because Ada exists.

# Test 2: Callsign does not exist
print(get_status({"Ada": "active"}, "Idris"))  # Prints "unknown" because Idris is missing.


