Feature: Target main page search tests

#  Scenario: User can search for a product on target
#    Given Open target main page
#    When  Search for tea
#    Then Verify search worked for tea
#    Then Verify correct search results URL opens for tea
#
#  Scenario: User can search for a product on target
#    Given Open target main page
#    When  Search for game
#    Then Verify search worked for game
#    Then Verify correct search results URL opens for tea

  Scenario Outline: User can search for a product on target
    Given Open target main page
    When  Search for <product>
    Then Verify search worked for <product>
    Then Verify correct search results URL opens for <product>
    Examples:
    |product   |product    |
    |tea       |tea        |
    |game      |game       |
    |iphone    |  iphone   |
