*** Settings ***
Library    library/GetNameLibrary.py
Library    SeleniumLibrary
Library    MongoDBLibrary

*** Variables ***
${BROWSER}          firefox
${URL}              https://rf-dashboard.ext.net.nokia.com/DashBoard

*** Keywords ***
TC [1.0] Test Dashboard Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    RF Dashboard
    Click Element    xpath=//*[@id="app"]/div[1]/header/div/button[2]
    Wait Until Page Contains Element    xpath=//button[@class='el-button el-button--primary']/span[text()=' Close ']    timeout=5s
    Input Text    xpath=//*[@id="input-64"]    jisong
    Input Text    xpath=//*[@id="input-67"]    py4r2*Rj
    Click Element    xpath=//*[@id="app"]/div[3]/div/div/div[2]/button[1]
    Wait Until Page Does Not Contain Element    xpath=//button[@class='el-button el-button--primary']/span[text()=' Close ']    timeout=8s
    ${name}    Get Text    xpath=//button[@class='el-button el-button--primary']/span[text()=' Jimmy Song (NSB) ']
    Should Be Equal    ${name}     Jimmy Song (NSB)
    ${first_name}    Get The First Name    ${name}
    Should Be Equal    ${first_name}    Song
    [Teardown]    Close Browser