# Step 01
# Getting the data from the input.json

import json

with open("input_test.json") as file:
    dataInput = json.load(file)


dataKey = (dataInput["Car"][0]['DataKey'])
dataValue = (dataInput["Car"][1]['DataValue'])


varLen = len(dataKey)
for y in range(0, varLen):
    print(dataKey[y]["VarCharValue"],":",dataValue[y]["VarCharValue"])






# Step 02
# Getting the data from the output.json

import json

with open("output.json") as file:
    dataOut = json.load(file)
    print(dataOut)




#
# Step 03
# Iterating all the element of the output.json

import json

with open("output.json") as file:
    dataOut = json.load(file)
    # print(data)


def iterate(outputDict):
    for key in outputDict:
        if not isinstance(outputDict[key], dict):
            print("Element found")
        else:
            print("Element not found")
            iterate(outputDict[key])

iterate(dataOut["VehicleInsurance"])








# Step 04
# Elements name while Iterating all the element of the output.json and their value

import json

with open("input_test.json") as file:
    dataInput = json.load(file)

with open("output.json") as file:
    dataOut = json.load(file)


def search(keyToSearch):
    dataKey = (dataInput["Car"][0]['DataKey'])
    dataValue = (dataInput["Car"][1]['DataValue'])

    varLen = len(dataKey )
    print(keyToSearch)
    # for y in range(0, varLen):
    #     if dataKey[y]["VarCharValue"].lower() == keyToSearch.lower():
    #         print(" ")
    #         print(" ")
    #         return dataValue[y]["VarCharValue"]


def iterate(outputDict):
    for key in outputDict:
        if not isinstance(outputDict[key], dict):
            print("Element found")
            print(search(key))
        else:
            print("Element not found")
            iterate(outputDict[key])


iterate(dataOut["VehicleInsurance"])







# Step 05
# Creating new dictionary with found values of respective keys and parsing that
# all values into a newly generated .txt file

import json

with open("input_test.json") as file:
    dataInput = json.load(file)

with open("output.json") as file:
    dataOut = json.load(file)


def search(keyToSearch):
    dataKey = (dataInput["Car"][0]['DataKey'])
    dataValue = (dataInput["Car"][1]['DataValue'])

    varLen = len(dataKey)
    print(keyToSearch)
    for y in range(0, varLen):
        if dataKey[y]["VarCharValue"].lower() == keyToSearch.lower():
            print(" ")
            print(" ")
            return dataValue[y]["VarCharValue"]


def iterate(outputDict):
    for key in outputDict:
        if not isinstance(outputDict[key], dict):
            print("Element found")
            outputDict[key] = search(key)
            print(outputDict[key])
        else:
            print("Element not found")
            outputDict[key] = iterate(outputDict[key])
    return outputDict


dataOut["VehicleInsurance"] = iterate(dataOut["VehicleInsurance"])

print(dataOut["VehicleInsurance"])


finalJson = json.dumps(dataOut)


def main():
    f = open("FinalOutput.txt", "w+")
    f.write(finalJson)
    f.close()


if __name__ == "__main__":
    main()









# #practice code
# import json
#
# # with open("input_test.json") as file:
# #     data = json.load(file)
#
#
# try:
#     with open("input_test.json") as file:
#         data = json.load(file)
#     print("Equipment data has been retrieved")
#     # print(data)
# except json.decoder.JSONDecodeError:
#     print("Problem accessing the data")
#
#
#
# for item in data["Car"]:
#     print(item["Data"][0]["VarCharValue"])
#
#
#
# for item in data["Car"]:
#     varLen = len(item["Data"])
#     for y in range(0, varLen):
#         print(item["Data"][y]["VarCharValue"])
#
#
# import json
#
# with open("input_test.json") as file:
#     data = json.load(file)
#
# for item in data["Car"]:
#     varLen = len(item['Data'])
#     for y in range(0, varLen):
#         print(item['Data'][y]["VarCharValue"],":",item['Data'][y]["VarCharValue"])
#
#
# for item in data["Car"]:
#     varLen = len(item['Data'])
#     for y in range(0, varLen):
#         print(item['Data'][y]["VarCharValue"])
#
#
#
# import json
#
# with open("input_test.json") as file:
#     data = json.load(file)
#
#
# a = (data["Car"][0]['Data1'])
# b = (data["Car"][1]['Data2'])
#
#
# varLen = len(a)
# for y in range(0, varLen):
#     print(a[y]["VarCharValue"],":",b[y]["VarCharValue"])
#     if(a[y]["VarCharValue"] == key):
#         return (b[y]["VarCharValue"])
#
#
#
# //key --- dictionary keyword
# //keytoseach----- iterate
#
#
# import json
#
# with open("input_test.json") as file:
#     data = json.load(file)
#
# with open("output.json") as file:
#     dataOut = json.load(file)
#
#
# def func1(keyToSearch):
#     a = (data["Car"][0]['Data1'])
#     b = (data["Car"][1]['Data2'])
#
#     varLen = len(a)
#     print(keyToSearch)
#     # for y in range(0, varLen):
#     #     if a[y]["VarCharValue"].lower() == keyToSearch.lower():
#     #         print(" ")
#     #         print(" ")
#     #         return b[y]["VarCharValue"]
#
#
#
#
# def iterate(dict1):
#     for key in dict1:
#         if not isinstance(dict1[key], dict):
#             print("Element found")
#             print(func1(key))
#         else:
#             print("Element not found")
#             iterate(dict1[key])
#
#
# iterate(dataOut["VehicleInsurance"])
#
#
# import json
#
# with open("input_test.json") as file:
#     data = json.load(file)
#
# def func1(keyToSearch):
#     a = (data["Car"][0]['Data1'])
#     b = (data["Car"][1]['Data2'])
#
#     varLen = len(a)
#     print(keyToSearch)
#     for y in range(0, varLen):
#         # print(a[y]["VarCharValue"], ":", b[y]["VarCharValue"])
#         if (a[y]["VarCharValue"].lower() == keyToSearch.lower()):
#             print("inside if")
#             return (b[y]["VarCharValue"])
#
#
# with open("output.json") as file:
#     dataOut = json.load(file)
#     # print(data)
#
# def iterate(dict1):
#     for key in dict1:
#         if not isinstance(dict1[key], dict):
#             print("Element found")
#             dict1[key] = func1(key)
#             print(dict1[key])
#         else:
#             print("Element not found")
#             dict1[key] = iterate(dict1[key])
#     return(dict1)
#
# # iterate(dataOut["VehicleInsurance"])
# dataOut["VehicleInsurance"] = iterate(dataOut["VehicleInsurance"])
#
# print(dataOut["VehicleInsurance"])
# myString = json.dumps(dataOut)
#
#
# def main():
#     f = open("guru99.txt", "w+")
#     f.write(myString)
#     f.close()
#
# if __name__ == "__main__":
#     main()
