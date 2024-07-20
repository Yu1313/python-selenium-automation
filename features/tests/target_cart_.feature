Feature: Target main page cart test

#  Scenario: User can navigate to empty cart
#      Given Open target main page
#      When  Click on Cart icon
#      Then  Verify “Your cart is empty” message is shown

  Scenario: User can add product to cart
    Given Open target main page
    When  Search for MILK
    When  Add milk to cart
    When  Add to cart
    When View cart & checkout
    Then Verify 1 item text is shown

    # Enter steps here