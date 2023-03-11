def smart_device_budget():
    # input from the user
    num_rooms = int(input("Enter the number of Bedrooms: "))
    room_areas = []
    for i in range(num_rooms):
        area = int(input("Enter the area of Bedroom {} (in square feet): ".format(i + 1)))
        room_areas.append(area)
    num_kitchens = int(input("Enter the number of kitchens: "))
    kitchen_areas = []
    for i in range(num_kitchens):
        area = int(input("Enter the area of Kitchen {} (in square feet): ".format(i + 1)))
        kitchen_areas.append(area)
    num_bathrooms = int(input("Enter the number of bathrooms: "))
    bathroom_areas = []
    for i in range(num_bathrooms):
        area = int(input("Enter the area of Bathroom {} (in square feet): ".format(i + 1)))
        bathroom_areas.append(area)
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

    # total area of the house
    total_area = sum(room_areas) + sum(kitchen_areas) + sum(bathroom_areas)

    # total number of sockets in the house
    total_sockets = sum(sockets_per_room)

    # max amount of each type of device that can be installed
    max_devices = {}
    for device, specs in device_types.items():
        if specs["Room"] == "All":
            max_devices[device] = int((total_area * 0.2 - total_sockets * 2) / specs["Area"])
        elif specs["Room"] == "Kitchen":
            max_devices[device] = int(
                (sum(kitchen_areas) * 0.2 - num_kitchens * sockets_per_room[-(num_bathrooms + num_kitchens + 1)] * 2) /
                specs["Area"])
        elif specs["Room"] == "Bathroom":
            max_devices[device] = int((num_bathrooms * sockets_per_room[-1] * (total_area - sum(room_areas))) / (
                    specs["Power"] * specs["Area"]))
        elif specs["Room"] == "Bedroom":
            max_devices[device] = int((num_rooms * sum(sockets_per_room[:num_rooms]) * (
                    total_area - sum(kitchen_areas) - sum(bathroom_areas))) / (
                                              specs["Power"] * specs["Area"] * 0.2 * room_areas[:num_rooms].count(
                                          1)))

    # max amount of each type of device that can be installed in each room
    # Calculate devices per room
    devices_per_room = {}
    for device, specs in device_types.items():
        if specs["Room"] == "All":
            devices_per_room[device] = int((total_area * 0.2 - total_sockets * 2) / specs["Area"]) // (
                    num_rooms + num_kitchens + num_bathrooms)
        elif specs["Room"] == "Kitchen":
            devices_per_room[device] = int(
                (sum(kitchen_areas) * 0.2 - num_kitchens * sockets_per_room[-(num_bathrooms + num_kitchens + 1)] * 2) /
                specs["Area"]) // num_kitchens
        elif specs["Room"] == "Bathroom":
            devices_per_room[device] = int((num_bathrooms * sockets_per_room[-1] * (total_area - sum(room_areas))) / (
                    specs["Power"] * specs["Area"])) // num_bathrooms
        elif specs["Room"] == "Bedroom":
            devices_per_room[device] = int((num_rooms * sum(sockets_per_room[:num_rooms]) * (
                    total_area - sum(kitchen_areas) - sum(bathroom_areas))) / (
                                                   specs["Power"] * specs["Area"] * 0.2 * room_areas.count(
                                               1))) // num_rooms

    print("Maximum number of smart devices that can be installed in each room:")
    for device, count in devices_per_room.items():
        print("{}: {}".format(device, count))


smart_device_budget()
