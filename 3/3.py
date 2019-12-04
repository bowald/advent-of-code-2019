def occupie(path, coords):
    current_coord = [0,0]

    for p in path:
        direction = p[0]
        steps = int(p[1:])

        if direction == 'R':
            for v in range(1,steps + 1):
                key = f'{current_coord[0]},{current_coord[1] + v}'
                coords[key] = 1
            current_coord[1] += steps
            
        elif direction == 'L':
            for v in range(1, steps + 1):
                key = f'{current_coord[0]},{current_coord[1] - v}'
                coords[key] = 1
            current_coord[1] -= steps
        elif direction == 'U':
            for u in range(1, steps + 1):
                key = f'{current_coord[0] + u},{current_coord[1]}'
                coords[key] = 1
            current_coord[0] += steps
        elif direction == 'D':
            for u in range(1, steps + 1):
                key = f'{current_coord[0] - u},{current_coord[1]}'
                coords[key] = 1
            current_coord[0] -= steps
        else:
            print('ERROR')


def calc(path, goal):
    total_steps = 0
    current_coord = [0,0]

    for p in path:
        direction = p[0]
        steps = int(p[1:])

        if direction == 'R':
            for v in range(1,steps + 1):
                total_steps += 1
                key = f'{current_coord[0]},{current_coord[1] + v}'
                if key == goal:
                    return total_steps
            current_coord[1] += steps
            
        elif direction == 'L':
            for v in range(1, steps + 1):
                total_steps += 1
                key = f'{current_coord[0]},{current_coord[1] - v}'
                if key == goal:
                    return total_steps
            current_coord[1] -= steps
        elif direction == 'U':
            for u in range(1, steps + 1):
                total_steps += 1
                key = f'{current_coord[0] + u},{current_coord[1]}'
                if key == goal:
                    return total_steps
            current_coord[0] += steps
        elif direction == 'D':
            for u in range(1, steps + 1):
                total_steps += 1
                key = f'{current_coord[0] - u},{current_coord[1]}'
                if key == goal:
                    return total_steps
            current_coord[0] -= steps
        else:
            print('ERROR')
    print('BAAAD')
    return -1 

paths = [p.split(',') for p in open('input.txt')]
coords0 = {}
coords1 = {}

occupie(paths[0], coords0)
occupie(paths[1], coords1)

a = set(coords0.keys())
b = set(coords1.keys())

intersections = a.intersection(b)

# part 1
# p = [k.split(',') for k in intersections]
# print(min([abs(int(cs[0])) + abs(int(cs[1])) for cs in p]))

min_steps = 9999999999999999999999
for intersection in intersections:
    steps_to_intersection = calc(paths[0], intersection) + calc(paths[1], intersection)
    min_steps = min(min_steps, steps_to_intersection)

print(min_steps)