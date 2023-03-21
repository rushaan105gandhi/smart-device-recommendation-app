def smart_device_budget():
    max_devices = {
        "Smart Bulbs": 0,
        "Smart Plugs": 0,
        "Smart Switches": 0,
        "Smart Locks": 0,
        "Smart Thermostats": 0,
        "Smart Speakers": 0,
        "Smart Displays": 0,
        "Smart Cameras": 0
    }

    num_rooms = int(input("Enter the number of Bedrooms: "))

    sockets_per_room = []

    for i in range(1, num_rooms + 1):
        room_sockets = int(input("Enter the number of sockets in room {}: ".format(i)))
        sockets_per_room.append(room_sockets)

    total_socket_count = sum(sockets_per_room)

    room_areas = []

    for i in range(1, num_rooms + 1):
        room_area = int(input("Enter the area of Bedroom {} (in square feet): ".format(i)))
        room_areas.append(room_area)

    kitchen_count = int(input("Enter the number of kitchens: "))

    for i in range(1, kitchen_count + 1):
        kitchen_sockets = int(input("Enter the number of sockets in kitchen {}: ".format(i)))
        total_socket_count += kitchen_sockets
        kitchen_area = int(input("Enter the area of Kitchen {} (in square feet): ".format(i)))
        room_areas.append(kitchen_area)

    bathroom_count = int(input("Enter the number of bathrooms: "))

    for i in range(1, bathroom_count + 1):
        bathroom_sockets = int(input("Enter the number of sockets in bathroom {}: ".format(i)))
        total_socket_count += bathroom_sockets
        bathroom_area = int(input("Enter the area of Bathroom {} (in square feet): ".format(i)))
        room_areas.append(bathroom_area)

    total_area = sum(room_areas)

    budget = int(input("Enter your budget (in dollars): "))

    if total_socket_count > 0:
        max_devices["Smart Plugs"] = int(total_socket_count * 0.25)

    if num_rooms > 0:
        max_devices["Smart Bulbs"] = num_rooms * 2

    if total_area > 0:
        max_devices["Smart Thermostats"] = 1

        if total_area < 1000:
            max_devices["Smart Speakers"] = 1
            max_devices["Smart Displays"] = 0

        else:
            max_devices["Smart Speakers"] = 2
            max_devices["Smart Displays"] = 1

    if kitchen_count > 0:
        max_devices["Smart Switches"] = 1

    if bathroom_count > 0:
        max_devices["Smart Locks"] = 1

    for device, count in max_devices.items():
        print("Maximum number of {} you can buy: {}".format(device, count))

        if count > 0:
            cost_per_device = int(budget / count)
            print("Cost per device: {} dollars".format(cost_per_device))


smart_device_budget()
