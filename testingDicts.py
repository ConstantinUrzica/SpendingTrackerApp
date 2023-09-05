testDict = {
    "entries": {
        "1": {
          "amount": 200,
          "tag" : "EXTRA",
          "date": "2023-09-05"
        }
    }
}

print("DEBUG: initial dict:", testDict)
entry = {

        "amount": 100,
        "tag": "FOOD",
        "date":  "2023-09-05"

}

testDict['2']=entry
print(testDict)