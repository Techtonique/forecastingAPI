import forecastingapi as fapi

if __name__ == "__main__":
    
    ## 1 - create an account (once)
    res_create_account = fapi.create_account(username="user@example.com", 
                                             password="pwd") # choose a better password
    print(res_create_account)

    ## 2 - get a token 
    token = fapi.get_token(username = "user@example.com",
                                   password = "pwd")
    print(token)

    ## 3 - get forecast with prediction interval
    path_to_file = '/Users/t/Documents/datasets/time_series/univariate/nile.csv' # (examples:
#' https://github.com/Techtonique/datasets/tree/main/time_series/univariate)
     
    res_get_forecast = fapi.get_forecast(file=path_to_file, 
    token=token)

    print(res_get_forecast)

    res_get_forecast2 = fapi.get_forecast(file=path_to_file, 
    token=token, start_training = 2, n_training = 7, h = 4, level = 90)

    print(res_get_forecast2)

    res_get_forecast3 = fapi.get_forecast(file=path_to_file, 
    token=token, date_formatting="ms",
    start_training = 2, n_training = 7, h = 4, level = 90)

    print(res_get_forecast3)

    res_get_forecast4 = fapi.get_forecast(file=path_to_file, 
    token=token, method = "prophet")

    print(res_get_forecast4)