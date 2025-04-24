from collections import deque, defaultdict

def minimum_energy_to_exit(door_information, keycard_information, energy_activation_cost, override_activation_cost = 0 , override_activation_discount = 0):
    door_to_keys = {}
    door_requires_keys = defaultdict(list)

    final_door = "D0"
    for item in door_information:
        door, keys = item.split(":")
        door = door.strip()
        keys = keys.strip().split()
        door_to_keys[door] = set(keys)
        if int(final_door.strip("D")) < int(door.strip("D")):
            final_door = door  

    for item in keycard_information:
        key, door = item.split(":")
        key, door = key.strip(), door.strip()
        door_requires_keys[door].append(key)

    print(final_door)
    
    queue = deque()
    queue.append((door_requires_keys[final_door],final_door))  

    opened_door = set()
    energy_val = 0

    while queue:
        print(queue)
        keys,current_door = queue.popleft()
 
        if current_door not in opened_door:
            opened_door.add(current_door)
            current_energy = energy_activation_cost + len(door_requires_keys[current_door])
            energy_val += current_energy
            for key in keys:
                for door in door_to_keys:
                    if key in door_to_keys[door]:
                        queue.append((door_requires_keys[door],door))


    return energy_val


if __name__ == '__main__':
    door_information = {"D1: K1 K2 K3 K4 K5","D2: K6","D3: K7","D4: K8","D5: K9","D6: K10","D7:"}
    keycard_information = {"K1: D2", "K2: D3","K3: D4","K4: D5","K5: D6","K6: D7","K7: D7","K8: D7","K9: D7","K10: D7"}
    energy_activation_cost = 25

    # door_information = [
    # "D1: K1 K2 K3",
    # "D2: K4",
    # "D3: K5",
    # "D4:",
    # "D5:"
    # ]
    # keycard_information = [
    # "K1: D2",
    # "K2: D3",
    # "K3: D5",
    # "K4: D5",
    # "K5: D4"
    # ]
    # energy_activation_cost = 100
    print(minimum_energy_to_exit(door_information,keycard_information,energy_activation_cost))