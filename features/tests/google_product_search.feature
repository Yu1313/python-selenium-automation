Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown

  # Feature: Test Scenarios for Search functionality  # multiple scenarios, 1 feature per file
  #   Scenario: User can search for a product   # same as a test case
  #     Given Open Google page                  # preconditions what to do before starting test
  #     When Input Car into search field        # Actions done during test
  #     And Click on search icon                # Action copy of step before: then/when DO NOT PUT AND IN STEPS WILL BRK
  #     Then Product results for Car are shown  # verification done
    # Steps used in Given, When, And, Then will be implemented in step directory
    # So they must be unique