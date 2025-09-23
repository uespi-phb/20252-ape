
group_time = {
    'arquitetos': 4,
    'musicos': 6,
    'bonecos': 8,
    'desenhistas': 12,
}
group_hours = {}

worker_count = int(input())
while worker_count > 0:
    worker_count -= 1

    data = input().split()
    group = data[1]
    hours = int(data[2])

    group_hours[group] = group_hours.get(group, 0) + hours

gift_count = 0
for group, hours in group_hours.items():
    gift_count += hours // group_time[group]

print(gift_count)
