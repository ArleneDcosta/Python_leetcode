
def carFleet(target, position, speed):
    print(sorted(zip(position,speed))[::-1])
    stack = []
    for pos, vel in sorted(zip(position, speed))[::-1]:
        dist = target - pos
        if not stack:
            stack.append(dist / vel)
        elif dist / vel > stack[-1]:
            stack.append(dist / vel)
    return len(stack)

if __name__ == '__main__':
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(carFleet(target,position,speed))
    target = 10
    position = [3]
    speed = [3]
    print(carFleet(target,position,speed))
    target = 100
    position = [0,2,4]
    speed = [4,2,1]
    print(carFleet(target,position,speed))
    target = 10
    position = [6,8]
    speed = [3,2]
    print(carFleet(target,position,speed))