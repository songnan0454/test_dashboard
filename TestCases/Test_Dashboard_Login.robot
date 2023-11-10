*** Settings ***
Library    library/GetNameLibrary.py
Library    Selenium2Library
Resource   Resources/ElementPath.robot

*** Variables ***
${BROWSER}          firefox
${URL}              http://sf.myps188.com
${PAGE_COUNT}       ${100}
${START_TIME}       2023-11-05
${END_TIME}         2023-11-05

*** Keywords ***
#TC [1.0] Test Dashboard Login
#    Open Browser    ${URL}    ${BROWSER}
#    Maximize Browser Window
#    Title Should Be    RF Dashboard
#    Click Element    xpath=${HOME_LOGIN_BTN}
#    Wait Until Page Contains Element    xpath=${CANCEL_TXT}    timeout=5s
#    Input Text    xpath=${ID_INPUT}    jisong
#    Input Text    xpath=${PWD_INPUT}    py4r2*Rj
#    Click Element    xpath=${LOGIN_PAGE_LOGIN_BTN}
#    Wait Until Page Does Not Contain Element    xpath=${CANCEL_TXT}    timeout=8s
#    ${name}    Get Text    xpath=${LOGIN_NAME_TXT}
#    Should Be Equal    ${name}     Jimmy Song (NSB)
#    ${first_name}    Get The First Name    ${name}
#    Should Be Equal    ${first_name}    Song
#    [Teardown]    Close Browser

TC [1.0] Test Dashboard Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text    xpath=/html/body/div[2]/div[2]/label[1]/input    18367823720
    Input Text    xpath=/html/body/div[2]/div[2]/label[2]/input    xmy123456
    Click Element    xpath=/html/body/div[2]/div[2]/div[2]/p[1]
    Click Element    xpath=/html/body/div[2]/div[2]/div[1]
    Sleep    15s
    Click Element    xpath=/html/body/div[1]/div/div/div[2]/a[2]
    Sleep    15s
    Click Element    xpath=/html/body/div[4]/div[1]/form/input
    Input Text    xpath=//*[@id="fieldDate1"]    ${START_TIME}
    Input Text    xpath=//*[@id="fieldDate2"]   ${END_TIME}
    Click Element    xpath=/html/body/div[4]/div[1]/form/div[2]/div/label[1]/div/div/input
    Sleep    2s
    Click Element    xpath=/html/body/div[4]/div[1]/form/div[2]/div/label[1]/div/dl/dd[1]
    FOR  ${time}  IN RANGE  1  ${PAGE_COUNT}
        Sleep    15s
        ${count}    Get Element Count    xpath=//div[@id='orderList']/div
        ${count}    Evaluate    ${count} + 1
        FOR  ${index}  IN RANGE  1  ${count}
            ${order_time}    Get Text    xpath=/html/body/div[4]/div[1]/div[6]/div[${index}]/div[3]/div[2]/div[1]/div[1]
            ${order_time}    Get Order Time    ${order_time}
            ${order_status}    Get Text    xpath=/html/body/div[4]/div[1]/div[6]/div[${index}]/div[3]/div[2]/div[2]/div[@class='text state layui-hide-xs']
            ${order_status}    Get Order Status    ${order_status}
            ${order_id}    Get Text    xpath=/html/body/div[4]/div[1]/div[6]/div[${index}]/div[1]/div[1]
            ${order_name}    Get Text    xpath=/html/body/div[4]/div[1]/div[6]/div[${index}]/div[3]/div[2]/div[1]//div[@class='text']/span[text()='配送员：']/..
            ${order_name}    Get Order Name    ${order_name}
            IF    '${order_name}' == '无'
                ${order_phone}    Set Variable    空
            ELSE
                ${order_phone}    Get Text    xpath=/html/body/div[4]/div[1]/div[6]/div[${index}]/div[3]/div[2]/div[1]/div[3]/div[2]/p
            END
            Add Info To Txt    ${order_time}    ${order_id}    ${order_name}    ${order_status}    ${order_phone}    ${START_TIME}    ${END_TIME}
        END
        ${val}    Get Element Attribute    xpath=//div[@id='layui-laypage-1']/a[text()='下一页']    class
        Exit For Loop If    '${val}' != 'layui-laypage-next'
        Click Element    xpath=//a[@class='layui-laypage-next']
    END
    [Teardown]    Close Browser
