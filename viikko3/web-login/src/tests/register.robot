*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  test
    Set Password  12345678
    Set Password Confirmation  12345678
    Submit Credentials
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  12345678
    Set Password Confirmation  12345678
    Submit Credentials
    Page Should Contain  Username has to be only lowercase letters with minimum length of 3

Register With Valid Username And Too Short Password
    Set Username  test
    Set Password  1234
    Set Password Confirmation  1234
    Submit Credentials
    Page Should Contain  Password min length is 8 and can't consist only of letters

Register With Valid Username And Invalid Password
    Set Username  test
    Set Password  asdfasdf
    Set Password Confirmation  asdfasdf
    Submit Credentials
    Page Should Contain  Password min length is 8 and can't consist only of letters

Register With Nonmatching Password And Password Confirmation
    Set Username  test
    Set Password  asdfasdf1
    Set Password Confirmation  asdfasdf12
    Submit Credentials
    Page Should Contain  Password and its confirmation doesn't match!

Register With Username That Is Already In Use
    Set Username  test
    Set Password  asdfasdf1
    Set Password Confirmation  asdfasdf1
    Submit Credentials
    Go To Register Page
    Set Username  test
    Set Password  asdfasdf1
    Set Password Confirmation  asdfasdf1
    Submit Credentials
    Page Should Contain  Problem with registration

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

# jäin tän tunkkaamiseen, kun teen tehtävä 7:kaa. Pitäisi saada testi
# "Register With Too Short Username And Valid Password" toimimaan
# aja testit ja katso mikä ongelma!

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}