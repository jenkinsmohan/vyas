import requests, requests.utils
import json
import sys, getopt
from time import gmtime, strftime
from datetime import date, datetime
import ssl
import math

def mandatorGolive(mandUID, revUID):
    s = requests.session()
    loginResponse = s.post(url + "?{\"request\":\"postRequest\"}:", data=login_data).text
    #print (loginResponse)
    if loginResponse.find("LOGIN_FAILED") != -1:
        print ("Login failed, please check your credentials")
        sys.exit(2)
    print("Logged In Successfully")
    loginResponseJson = json.loads(loginResponse)
    downloadToken = loginResponseJson["downloadToken"]
    csrfToken = loginResponseJson["csrfToken"]
    headers = {'downloadToken': downloadToken, 'csrfToken': csrfToken}
    go_live_Check = "{\"request\":\"goliveCheckAndReport\", \"mandator\":" + str(mandUID) + ", \"revision\":" + str(revUID) + "}"
    #print(mandator_data)
    uidResponse = s.post(url + "?{\"request\":\"postRequest\"}:", headers=headers, data=go_live_Check).text
    #print(uidResponse)
    uidResponseJson = json.loads(uidResponse)
    if uidResponse.find("goliveReportWelcomeNew") != -1:
        print("*****GoLive Check Report for Mandator (UID: " + str(mandUID) + ") Revision with UID " + str(revUID) + " is successful*****")
    else:
        print("*****GoLive Check Report Failed for Mandator(UID: " + str(mandUID) + ") Revision with UID " + str(revUID) + " *****")
    s.close()
    s = requests.session()
    loginResponse = s.post(url + "?{\"request\":\"postRequest\"}:", data=login_data).text
    #print (loginResponse)
    if loginResponse.find("LOGIN_FAILED") != -1:
        print ("Login failed, please check your credentials")
        sys.exit(2)
    print("Logged In Successfully")
    loginResponseJson = json.loads(loginResponse)
    downloadToken = loginResponseJson["downloadToken"]
    csrfToken = loginResponseJson["csrfToken"]
    headers = {'downloadToken': downloadToken, 'csrfToken': csrfToken}
    go_live = "{\"request\":\"confirmGolive\", \"mandator\":" + str(mandUID) + ", \"revision\":" + str(revUID) + "}"
    #print(mandator_data)
    uidResponse = s.post(url + "?{\"request\":\"postRequest\"}:", headers=headers, data=go_live).text
    #print(uidResponse)
    uidResponseJson = json.loads(uidResponse)
    if uidResponse.find("OK") != -1:
        print("*****GoLive for Mandator (UID: " + str(mandUID) + ") Revision with UID " + str(revUID) + " is successful*****")
    else:
        print("*****GoLive Failed for Mandator(UID: " + str(mandUID) + ") Revision with UID " + str(revUID) + " *****")
    s.close()

    
def mandatorCreation(mandNum):
    #print(mandNum)
    s = requests.session()
    loginResponse = s.post(url + "?{\"request\":\"postRequest\"}:", data=login_data).text
    #print (loginResponse)
    if loginResponse.find("LOGIN_FAILED") != -1:
        print ("Login failed, please check your credentials")
        sys.exit(2)
    print("Logged In Successfully")
    loginResponseJson = json.loads(loginResponse)
    downloadToken = loginResponseJson["downloadToken"]
    csrfToken = loginResponseJson["csrfToken"]
    headers = {'downloadToken': downloadToken, 'csrfToken': csrfToken}
    mandator_data = "{\"request\":\"save\",\"uid\":-1,\"mandator\":997,\"data\":{\"streamType\":\"mandator\",\"uid\":-1,\"head\":997,\"name\":\"Test Mandator " + str(mandNum) + "\",\"comment\":\"Main Mandator for Banking Group \",\"fraudFlagIndex\":-1,\"mayDefineFinalRulesets\":false,\"allowInvestigationReport\":false,\"maxMemoryForSimulationGB\":1,\"saiExplanation\":\"\",\"saiTooltip\":\"\",\"saiOnlineHelpType\":\"NoOnlineHelp\",\"saiOnlineHelp\":\"\",\"conditions\":[{\"attribute\":1003,\"operator\":\"EqualTo\",\"caseSensitive\":false,\"minConsecutiveDigits\":false,\"maxConsecutiveDigits\":false,\"countNumberOfSingleCharacter\":false,\"character\":\"\",\"digits\":\"0\",\"distance\":\"0\",\"tolerance\":\"0\",\"toleranceUnit\":\"percent\",\"expressionStructed\":{\"type\":\"Interval\",\"parameters\":[{\"type\":\"Constant\",\"value\":\"" + str(min) + "\"},{\"type\":\"Delimiter\",\"value\":\"~\"},{\"type\":\"Constant\",\"value\":\"" + str(max) +"\"}],\"value\":\"21~25\"}}],\"pythonCodeExecutionEnabled\":false,\"pythonModules\":[],\"doubletDetectionEnabled\":false,\"doubletDetectionIncludeDdc\":false,\"doubletDetectionIndex\":-1,\"doubletDetectionAttributes\":[],\"doubletDetectionSendOutput\":false,\"customCss\":\"\",\"relationalDatabase\":{\"rdiEnabledTransactions\":false,\"databaseFormat\":\"Db2\",\"deliveryPath\":\"\",\"writeInterval\":\"Hours\",\"rdiAttributes\":[],\"maskEncryptedAttributes\":true,\"tableName\":\"DEFAULT_TRANSACTIONS\",\"rdiEnabledCases\":false,\"rdiDeliveryPathCases\":\"\",\"rdiTableNameCases\":\"DEFAULT_CASES\",\"rdiLinebreaks\":0}}}{\"request\":\"save\",\"uid\":-1,\"mandator\":997,\"data\":{\"streamType\":\"mandator\",\"uid\":-1,\"head\":997,\"name\":\"Test Mandator 1\",\"comment\":\"Main Mandator for Banking Group \",\"fraudFlagIndex\":-1,\"mayDefineFinalRulesets\":false,\"allowInvestigationReport\":false,\"maxMemoryForSimulationGB\":1,\"saiExplanation\":\"\",\"saiTooltip\":\"\",\"saiOnlineHelpType\":\"NoOnlineHelp\",\"saiOnlineHelp\":\"\",\"conditions\":[{\"attribute\":1003,\"operator\":\"EqualTo\",\"caseSensitive\":false,\"minConsecutiveDigits\":false,\"maxConsecutiveDigits\":false,\"countNumberOfSingleCharacter\":false,\"character\":\"\",\"digits\":\"0\",\"distance\":\"0\",\"tolerance\":\"0\",\"toleranceUnit\":\"percent\",\"expressionStructed\":{\"type\":\"Interval\",\"parameters\":[{\"type\":\"Constant\",\"value\":\"21\"},{\"type\":\"Delimiter\",\"value\":\"~\"},{\"type\":\"Constant\",\"value\":\"25\"}],\"value\":\"21~25\"}}],\"pythonCodeExecutionEnabled\":false,\"pythonModules\":[],\"doubletDetectionEnabled\":false,\"doubletDetectionIncludeDdc\":false,\"doubletDetectionIndex\":-1,\"doubletDetectionAttributes\":[],\"doubletDetectionSendOutput\":false,\"customCss\":\"\",\"relationalDatabase\":{\"rdiEnabledTransactions\":false,\"databaseFormat\":\"Db2\",\"deliveryPath\":\"\",\"writeInterval\":\"Hours\",\"rdiAttributes\":[],\"maskEncryptedAttributes\":true,\"tableName\":\"DEFAULT_TRANSACTIONS\",\"rdiEnabledCases\":false,\"rdiDeliveryPathCases\":\"\",\"rdiTableNameCases\":\"DEFAULT_CASES\",\"rdiLinebreaks\":0}}}"
    #print(mandator_data)
    uidResponse = s.post(url + "?{\"request\":\"postRequest\"}:", headers=headers, data=mandator_data).text
    #print(uidResponse)
    uidResponseJson = json.loads(uidResponse)
    if uidResponse.find("SAVED_SUCCESSFULLY") != -1:
        print("***** Test Mandator " + str(mandNum) + " created successfully with UID " + str(uidResponseJson["uid"]) + " ******")
    else:
        print("***** Failed to create mandator *****")
    s.close()
    mandUID = uidResponseJson["uid"]
    revUID = uidResponseJson["uid"] + 1
    mandatorGolive(mandUID, revUID)

    
user="user" #Enter your username
password="SaferPayments1" #Enter your password
url="http://192.168.0.111:8001/" #Enter your URL
login_data = "{\"request\":\"login\",\"data\":{\"login\":\"" + user + "\",\"password\":\"" + password + "\"}}"
min = 18521
print (login_data)
for x in range(3801, 4001):
    #print(x)
    max = min + 4
    mandatorCreation(x)
    min = max + 1
