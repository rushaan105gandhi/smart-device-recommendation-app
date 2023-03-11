def smart_device_budget():
    # input from the user
    size_of_house = int(input("Enter the size of the house (in square feet): "))
    num_rooms = int(input("Enter the number of Bedrooms: "))
    num_kitchens = int(input("Enter the number of kitchens: "))
    num_bathrooms = int(input("Enter the number of bathrooms: "))
    sockets_per_room = []
    for i in range(num_rooms + num_kitchens + num_bathrooms):
        sockets = int(input("Enter the number of sockets in room {}: ".format(i + 1)))
        sockets_per_room.append(sockets)
    budget = int(input("Enter your budget (in dollars): "))

    # types of smart devices and power consumption
    device_types = {
        "Smart Bulb": {"Power": 10, "Room": "All", "Area": 1},
        "Smart Speaker": {"Power": 30, "Room": "All", "Area": 1},
        "Smart Thermostat": {"Power": 20, "Room": "All", "Area": 1},
        "Smart Lock": {"Power": 5, "Room": "All", "Area": 1},
        "Smart Camera": {"Power": 15, "Room": "All", "Area": 1},
        "Smart Plug": {"Power": 5, "Room": "All", "Area": 1},
        "Smart TV": {"Power": 100, "Room": "Bedroom", "Area": 10},
        "Smart Fridge": {"Power": 50, "Room": "Kitchen", "Area": 15},
        "Smart Oven": {"Power": 40, "Room": "Kitchen", "Area": 10},
        "Smart Mirror": {"Power": 10, "Room": "Bathroom", "Area": 2}
    }

    # total number of sockets in the house
    total_sockets = sum(sockets_per_room)

    # total area occupied by the sockets
    total_area = total_sockets * 2  # assuming 2 square feet for each socket

    # max amount of each type of device that can be installed
    max_devices = {}
    for device, specs in device_types.items():
        if specs["Room"] == "All":
            max_devices[device] = int((size_of_house - total_area) / specs["Area"])
        elif specs["Room"] == "Kitchen":
            max_devices[device] = int((num_kitchens * sockets_per_room[-(num_bathrooms + num_kitchens + 1)] * (
                    size_of_house - total_area)) / (specs["Power"] * specs["Area"]))
        elif specs["Room"] == "Bathroom":
            max_devices[device] = int((num_bathrooms * sockets_per_room[-1] * (size_of_house - total_area)) / (
                    specs["Power"] * specs["Area"]))
        elif specs["Room"] == "Bedroom":
            max_devices[device] = int((num_rooms * sum(sockets_per_room[:num_rooms]) * (size_of_house - total_area)) / (
                    specs["Power"] * specs["Area"]))

    # max amount of each type of device that can be installed in each room
    devices_per_room = {}
    for device, specs in device_types.items():
        if specs["Room"] == "All":
            devices_per_room[device] = int((size_of_house - total_area) / specs["Area"]) // (
                    num_rooms + num_kitchens + num_bathrooms)
        elif specs["Room"] == "Kitchen":
            devices_per_room[device] = int((num_kitchens * sockets_per_room[-(num_bathrooms + num_kitchens + 1)] * (
                    size_of_house - total_area)) / (specs["Power"] * specs["Area"])) // num_kitchens
        elif specs["Room"] == "Bathroom":
            devices_per_room[device] = int((num_bathrooms * sockets_per_room[-1] * (size_of_house - total_area)) / (
                    specs["Power"] * specs["Area"])) // num_bathrooms
        elif specs["Room"] == "Bedroom":
            devices_per_room[device] = int(
                (num_rooms * sum(sockets_per_room[:num_rooms]) * (size_of_house - total_area)) / (
                        specs["Power"] * specs["Area"])) // num_rooms

    print("Maximum number of smart devices that can be installed in each room:")
    for device, count in devices_per_room.items():
        print("{}: {}".format(device, count))


smart_device_budget()
