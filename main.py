from api import API


def main():
    print("Welcome to the Learnbeat API caller 9000!")
    print("----------------------------------------------")

    api = API()
    api.set_token()
    use_api(api)


def use_api(api):
    print("The following routes are available on our api:\n")
    for x, route in enumerate(api.get_routes()):
        print(f"({x}) {route.value}")
    print("(q) Quit the API caller 9000")

    choice = input("\nWhat route do you want to call? ")
    if choice == "q":
        exit()
    try:
        choice = int(choice)
        route = api.get_route_by_index(choice)
    except IndexError:
        print('invalid choice!')

    api.set_route(route)
    api.provide_parameters()
    api.make_request()

    # Call ourselves recursively until the user is done (and enters 'q')
    use_api(api)


if __name__ == "__main__":
    main()
