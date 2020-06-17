Feature: This is for Login module testing

  #@Smoke @Sanity
  Scenario: Login using valid data
       Given user is on Login page
       When  user enters Login ID
       And   user enters Login Password
       And   user click on SignIn button
       Then  user should get redirected to Dashboard
       And   user should get logout on clicking logout button