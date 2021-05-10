Feature: Create new customer

  Background: common steps
    Given I launch browser
    When I open the hompage
    And enter username "mngr324520" and password "Ynymeta" and click on login button
    And clik on New Customer tag

  Scenario: username is empty
    When I do not enter value name field
    And press TAB button
    Then Error message "Customer name must not be blank" must be show
#
  Scenario: username is numberic
    When I enter a number to value name field
    Then Error message "Numbers are not allowed" must be show

#     Scenario: username is special chracter
#    When I enter special chracter to value name field
#    Then Error message "Special characters are not allowed" must be show
