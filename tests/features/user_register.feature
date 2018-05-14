Feature: User registration
    
    Scenario: To register successfully
        Given that the user is on the page "http://localhost:5000/auth/register"
        When insert the "username" "Larry"
        And insert the "email" "larry12@gmail.com"
        And insert the "password" "matheuslindao"
        Then click the button "signUp"
        And the message should be displayed
            """
                Seu cadastro foi realizado com sucesso, Larry.
            """
