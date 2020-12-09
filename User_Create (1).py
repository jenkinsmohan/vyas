import requests, requests.utils
import json
import sys, getopt
from time import gmtime, strftime
from datetime import date, datetime
import ssl
import math

def userCreation(userNum):
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
    user_data = "{\"request\":\"save\",\"uid\":-1,\"mandator\":997,\"data\":{\"streamType\":\"user\",\"uid\":-1,\"enabled\":true,\"login\":\"test.analyst"+str(userNum)+"\",\"name\":\"Analyst User "+str(userNum)+"\",\"comment\":\"Annie Analyst is the fraud analyst for the Savings & Loans division\",\"authSms\":\"\",\"email\":\"\",\"phone\":\"\",\"location\":\"\",\"extraLdapOu\":\"\",\"mandator\":997,\"globalPrivileges\":{\"userAccount\":\"Change\",\"systemConfiguration\":\"No\",\"retention\":\"No\",\"realtimeInterceptionCodes\":\"View\",\"messages\":\"No\",\"cluster\":\"No\",\"inboundEndpoint\":\"No\",\"eventLogMessageAdministration\":\"No\",\"job\":\"No\",\"passwordSafes\":\"No\",\"keyEntry\":\"No\",\"keyManagement\":\"No\",\"complianceList\":\"No\",\"viewSystemInternals\":true,\"maskValuesLevel\":\"MaySeeClearValues\",\"changeMemoryLimits\":false,\"exportConfig\":false,\"viewSystemLogMessages\":false,\"viewAuditLogMessages\":false,\"viewMessageReport\":false,\"viewRulesFiredInCases\":true,\"viewRuleConditionsInCases\":true,\"viewManualButton\":false,\"viewPrivateWorkingQueue\":false,\"setDefaultPreferences\":false,\"maintenanceFunctions\":false,\"maintenanceIndexFunctions\":false,\"maintenanceResetAllUserPreferences\":false,\"maintenanceRewriteElementToDisk\":false,\"maintenanceCleanoutRevisions\":false,\"maintenanceSetXdcSizes\":false,\"maintenanceCheckHealthOfIndex\":false,\"maintenanceRewindFliBuffer\":false,\"maintenanceConclusionExpressionValuePairs\":false,\"maintenanceCancelMasterKeyChange\":false,\"maintenanceConvertAttributeData\":false,\"maintenanceRewriteRiskLists\":false,\"selfService\":\"EditPreferencesOnly\"},\"grants\":[{\"mandator\":997,\"role\":1048,\"passOnToSubMandators\":true}],\"memoryLimits\":[{\"mandator\":1042,\"value\":1},{\"mandator\":1044,\"value\":1},{\"mandator\":1046,\"value\":1}],\"initialPassword\":\"SaferPayments1\",\"startTab\":\"Model\",\"language\":\"en\",\"timeZoneOffset\":0,\"useSystemTimezone\":true,\"dateTimeFormat\":\"ISO\",\"decimal\":\"dot\",\"digitGroup\":\"comma\",\"fieldSeparator\":\"semicolon\",\"dataSelectionPeriodType\":\"TimeAbsolute\",\"extendedSelectDialog\":true,\"searchInSelections\":true,\"expandCheckboxList\":10,\"expandMultipleRelationsItems\":10,\"showExplanation\":false,\"showUncomputedElementsInSimulationReport\":false,\"showUnchangedElementsInComparisonReport\":false,\"showUids\":false,\"showElementPrintView\":false,\"showConditionCopyView\":false,\"ignoreCasesAsDefault\":false,\"ignoreCasesInSearch\":false,\"enforcePasswordChanges\":false,\"systemUser\":false,\"tickerHighlightInterval\":15,\"tickerRefreshInterval\":30,\"tickerShown\":true,\"numberFailedLogins\":0,\"lastPasswordChange\":-549755813888,\"lastSuccessfulLogin\":1607016474,\"lastLogOut\":1607016486,\"lastAction\":-549755813888,\"oldPassword\":\"\",\"newPassword\":\"\",\"confirmPassword\":\"\",\"extendedAuthentication\":false,\"enabledSystemUser\":false}}{\"request\":\"save\",\"uid\":-1,\"mandator\":997,\"data\":{\"streamType\":\"user\",\"uid\":-1,\"enabled\":true,\"login\":\"a2.analyst\",\"name\":\"Analyst User 2\",\"comment\":\"Annie Analyst is the fraud analyst for the Savings & Loans division\",\"authSms\":\"\",\"email\":\"\",\"phone\":\"\",\"location\":\"\",\"extraLdapOu\":\"\",\"mandator\":997,\"globalPrivileges\":{\"userAccount\":\"Change\",\"systemConfiguration\":\"No\",\"retention\":\"No\",\"realtimeInterceptionCodes\":\"View\",\"messages\":\"No\",\"cluster\":\"No\",\"inboundEndpoint\":\"No\",\"eventLogMessageAdministration\":\"No\",\"job\":\"No\",\"passwordSafes\":\"No\",\"keyEntry\":\"No\",\"keyManagement\":\"No\",\"complianceList\":\"No\",\"viewSystemInternals\":true,\"maskValuesLevel\":\"MaySeeClearValues\",\"changeMemoryLimits\":false,\"exportConfig\":false,\"viewSystemLogMessages\":false,\"viewAuditLogMessages\":false,\"viewMessageReport\":false,\"viewRulesFiredInCases\":true,\"viewRuleConditionsInCases\":true,\"viewManualButton\":false,\"viewPrivateWorkingQueue\":false,\"setDefaultPreferences\":false,\"maintenanceFunctions\":false,\"maintenanceIndexFunctions\":false,\"maintenanceResetAllUserPreferences\":false,\"maintenanceRewriteElementToDisk\":false,\"maintenanceCleanoutRevisions\":false,\"maintenanceSetXdcSizes\":false,\"maintenanceCheckHealthOfIndex\":false,\"maintenanceRewindFliBuffer\":false,\"maintenanceConclusionExpressionValuePairs\":false,\"maintenanceCancelMasterKeyChange\":false,\"maintenanceConvertAttributeData\":false,\"maintenanceRewriteRiskLists\":false,\"selfService\":\"EditPreferencesOnly\"},\"grants\":[{\"mandator\":997,\"role\":1048,\"passOnToSubMandators\":true}],\"memoryLimits\":[{\"mandator\":1042,\"value\":1},{\"mandator\":1044,\"value\":1},{\"mandator\":1046,\"value\":1}],\"initialPassword\":\"SaferPayments1\",\"startTab\":\"Model\",\"language\":\"en\",\"timeZoneOffset\":0,\"useSystemTimezone\":true,\"dateTimeFormat\":\"ISO\",\"decimal\":\"dot\",\"digitGroup\":\"comma\",\"fieldSeparator\":\"semicolon\",\"dataSelectionPeriodType\":\"TimeAbsolute\",\"extendedSelectDialog\":true,\"searchInSelections\":true,\"expandCheckboxList\":10,\"expandMultipleRelationsItems\":10,\"showExplanation\":false,\"showUncomputedElementsInSimulationReport\":false,\"showUnchangedElementsInComparisonReport\":false,\"showUids\":false,\"showElementPrintView\":false,\"showConditionCopyView\":false,\"ignoreCasesAsDefault\":false,\"ignoreCasesInSearch\":false,\"enforcePasswordChanges\":false,\"systemUser\":false,\"tickerHighlightInterval\":15,\"tickerRefreshInterval\":30,\"tickerShown\":true,\"numberFailedLogins\":0,\"lastPasswordChange\":-549755813888,\"lastSuccessfulLogin\":1607016474,\"lastLogOut\":1607016486,\"lastAction\":-549755813888,\"oldPassword\":\"\",\"newPassword\":\"\",\"confirmPassword\":\"\",\"extendedAuthentication\":false,\"enabledSystemUser\":false}}"
    #print(mandator_data)
    uidResponse = s.post(url + "?{\"request\":\"postRequest\"}:", headers=headers, data=user_data).text
    #print(uidResponse)
    uidResponseJson = json.loads(uidResponse)
    if uidResponse.find("SAVED_SUCCESSFULLY") != -1:
        print("Analyst User " + str(userNum) + " created successfully with UID " + str(uidResponseJson["uid"]) + "")
    else:
        print("Failed to create user")
    s.close()

    
user="user" #Enter your username
password="SaferPayments1" #Enter your password
url="http://192.168.0.111:8001/" #Enter your URL
login_data = "{\"request\":\"login\",\"data\":{\"login\":\"" + user + "\",\"password\":\"" + password + "\"}}"
print (login_data)
for x in range(8001, 10001):
    #print(x)
    userCreation(x)
