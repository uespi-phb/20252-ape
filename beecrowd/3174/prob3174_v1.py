hours_drawers = 0
hours_musicians = 0
hours_archs = 0
hours_dolls = 0

worker_count = int(input())
while worker_count > 0:
    worker_count -= 1

    data = input().split()
    group = data[1]
    hours = int(data[2])

    if group == 'desenhistas':
        hours_drawers += hours
    elif group == 'musicos':
        hours_musicians += hours
    elif group == 'bonecos':
        hours_dolls += hours
    elif group == 'arquitetos':
        hours_archs += hours

gift_count = 0
gift_count += hours_drawers // 12
gift_count += hours_dolls // 8
gift_count += hours_musicians // 6
gift_count += hours_archs // 4

print(gift_count)
