Feature: help page
  # Enter feature description here

  Scenario: Verify help page ui displays
    Given Open target help page
    When Target Help, text displays
    And Search field displays
    And Magnify button displays
    And Div block 1 elements display
    And Manage my, cell elements display
    And Div block 2 elements display
    And Browse all Help pages, text displays
    Then Verify help page ui link displays

