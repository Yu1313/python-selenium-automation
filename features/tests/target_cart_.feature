Feature: Target main page cart test
##
#  Scenario: User can navigate to empty cart
#      Given Open target main page
#      When  Click on Cart icon
#      Then  Verify “Your cart is empty” message is shown

  Scenario: User can add product to cart
    Given Open target main page
    When  Search for tea
    When  Add item to cart
    When Store product name
    When  Add to cart from side nav
    When View cart & checkout
    Then Verify cart has 1 item(s)
    And  Verify cart has correct tea
    # Enter steps here