Feature: Target main page search tests
#
##  Scenario: User can search for a product on target
##    Given Open target main page
###    When  Search for tea
###    Then Verify search worked for tea
###    Then Verify correct search results URL opens for tea
###
#  Scenario: User can search for a product on target
#    Given Open target main page
#    When  Search for milk
#    Then Verify search worked for milk
#    Then Verify correct search results URL opens for milk

##  Scenario Outline: User can search for a product on target
##    Given Open target main page
##    When  Search for <product>
##    Then Verify search worked for <product>
##    Then Verify correct search results URL opens for <product>
##    Examples:
##    |product   |product    |
##    |tea       |tea        |
##    |game      |game       |
##    |iphone    |  iphone   |
#
#  Scenario: Verify that user can see product names and images
#    Given Open target main page
#    When Search for iphone
#    Then Verify that every product has a name and an image

  Scenario: User can see favorite tooltip for search results
    Given Open target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown