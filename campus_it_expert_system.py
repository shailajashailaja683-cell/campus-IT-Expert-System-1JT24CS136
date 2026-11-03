# Project 13: Campus IT Troubleshooting Expert System
# USN: 1JT24CS136
# AI Lab - FOL, Unification, Forward Chaining

facts = [
    "HasSymptom(User1, NoInternet)",
    "Connected(User1, Wifi)",
    "HasSymptom(User1, CannotAccessWifi)",
    "HasSymptom(User2, PrinterUnavailable)",
    "Connected(User2, Wifi)",
    "HasSymptom(User3, LoginFailure)",
    "HasSymptom(User4, NoInternet)",
    "Connected(User4, Wired)",
    "CableStatus(User4, Unplugged)"
]

rules = [
    {"name": "R1_Wifi_NoInternet", "if": ["Connected(x, Wifi)", "HasSymptom(x, NoInternet)"], "then": "PossibleIssue(x, NetworkConfiguration)"},
    {"name": "R2_Wifi_CannotAccess", "if": ["HasSymptom(x, CannotAccessWifi)"], "then": "PossibleIssue(x, WifiRouterDown)"},
    {"name": "R3_Printer", "if": ["HasSymptom(x, PrinterUnavailable)", "Connected(x, Wifi)"], "then": "PossibleIssue(x, PrinterOfflineOrDriver)"},
    {"name": "R4_LoginFailure", "if": ["HasSymptom(x, LoginFailure)"], "then": "PossibleIssue(x, AuthenticationServer)"},
    {"name": "R5_CableIssue", "if": ["Connected(x, Wired)", "HasSymptom(x, NoInternet)", "CableStatus(x, Unplugged)"], "then": "PossibleIssue(x, NetworkCableIssue)"},
    {"name": "R6_D
