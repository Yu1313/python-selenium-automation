Feature: Target main page signin test

#  Scenario: logged out user can Sign In
#    Given Open target main page
#    When Click Sign In
#    When From right side navigation menu, click Sign In
#    Then Verify Sign In form opened

  Scenario: User can signin successfully
    Given Open target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    When input email and password on SignIn page
    When Click Sign in with password
    Then Verify user is logged in