Feature: GURU login

  Scenario: Login with valid ID and valid password
    Given I launch browser
    When I open the hompage
    And enter username "mngr324520" and password "Ynymeta" and click on login button
    Then I login to managers homepage

  Scenario Outline: Login with multiple ID and password
    Given I launch browser
    When I open the hompage
    And enter username "<username>" and password "<password>" and click on login button
    Then I login to managers homepage

    Examples:
      | username	| password  |
	  | mngr324520  | Ynymeta   |
	  | nguyenhai   | Ynymeta   |
	  | mngr324520  | 123456    |
	  | nguyenhai   | 123456    |
