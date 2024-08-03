Feature: Target main page signin test
#
#  Scenario: logged out user can Sign In
#    Given Open target main page
#    When Click Sign In
#    When From right side navigation menu, click Sign In
#    Then Verify Sign In form opened
#
#  Scenario: User can signin successfully
#    Given Open target main page
#    When Click Sign In
#    When From right side navigation menu, click Sign In
#    When input email and password on SignIn page
#    When Click Sign in with password
#    Then Verify user is logged in

#  Scenario: User can open and close Terms and Conditions from sign in page
#   Given Open target main page
#    When Click Sign In
#    When From right side navigation menu, click Sign In
#    When Store original window
#    And Click on Target terms and conditions link
#    And Switch to the newly opened window
#    Then Verify Terms and Conditions page is opened
#    And User can close new window and switch back to original

  Scenario: Verify entering incorrect username/password prevents user from logging on
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    When Enter incorrect email and password combination
    When Click Sign in with password
    Then Verify that 'We can't find your account.' message is shown