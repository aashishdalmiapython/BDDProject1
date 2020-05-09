Feature: This is for registration module testing

  @Smoke @Sanity
  Scenario: Registration using valid data
       Given user is on Registration page
       When  user enters username
       And   user enters email id
       And   user enters password
       And   user click on sign up button
       Then  user should get registered sucessfully

  @Regression @Smoke
  Scenario: Registration using duplicate data
       Given user is on Registration page
       When  user enters duplicate username
       And   user enters duplicate email id
       And   user enters password
       And   user click on sign up button
       Then  user should get registered sucessfully

  @Test
  Scenario: Registration using duplicate data
       Given user is on Registration page
       When  user enters duplicate username
       And   user enters duplicate email id
       And   user enters password
       And   user click on sign up button
       Then  user should get registered sucessfully

 #behave --tags=Smoke
 #behave --tags=Smoke,Test (This will execuete all scenarios from both tags)
 #behave --tags=Smoke --tags=Regression (This will execute scenarios having both the tags)