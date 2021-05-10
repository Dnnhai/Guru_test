Feature: Create new customer successful

  Background: common steps
    Given I launch browser
    When I open the hompage
    And enter username "mngr324520" and password "Ynymeta" and click on login button
    And clik on New Customer tag

  Scenario: create 1 user
    When I click to customer name field and enter my name "NguyenHai" to name field
    And I enter day of birth "11111991" to day of birth field
    And enter addresss "Vo Van Ngan" to address feild
    And enter city "Ho Chi Minh" to city feild
    And enter state "Thu Duc" to state feild
    And enter PIN "122133" to PIN feild
    And enter Mobile Number "0987654321" to Mobile Number feild
    And enter email "a123@a.aa" to email feild
    And enter Password "1234567890" to Password feild
    And click submit button
    Then message "Customer Registered Successfully!!!" must be show

    When I have user ID after that i click to New Account Tag
    And I enter user ID to customer field
    And I enter Initial deposit "123455" to deposit field
    And I click submit account button
    Then message "Account Generated Successfully!!!" must be show

    When I have account ID after that i click to Deposite Tag
    And I enter account ID to account No field
    And I enter Initial deposit "12000" to deposit field and fill description "demo deposite"
    And I click submit deposite button
    Then message "Transaction details of Deposit for Account <Acc_No>" must be show

