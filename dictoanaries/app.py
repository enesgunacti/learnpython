# keyler unique olmak zorunda

monthConversations = {
    10: "January",
    1: "February",
    2: "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",  
    "Dec": "December", 
}

print(monthConversations["Apr"])
print(monthConversations.get("Dec"))

print(monthConversations.get("Luc"))
print(monthConversations.get("Luc","Not a valid key"))

print(monthConversations[10])