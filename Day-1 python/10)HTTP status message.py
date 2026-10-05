http_code = int(input("Enter a http code:"))
match http_code:
    case 200:
        print("OK Successful")
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 500:
        print("Internal server error")
    case _:
        print("Invalid Status Code")
    