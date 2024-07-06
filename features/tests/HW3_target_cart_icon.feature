Feature: Target main page cart test

  Scenario: User can navigate to cart
      Given Open target main page
      When  Click on Cart icon
      Then  Verify “Your cart is empty” message is shown

    # Enter steps here