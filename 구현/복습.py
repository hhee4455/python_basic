n , m = map(int, input().split())

x, y, direction = map(int,input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

dx = [-1,0,1,0]
dy = [0,-1,0,1]

map_arr = [list(map(int, input().split())) for _ in range(m)]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 0
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and map_arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        count += 1
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map_arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
