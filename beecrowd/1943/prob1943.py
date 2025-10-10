
def get_category(rank):
    categories = (1, 3, 5, 10, 25, 50, 100)
    for category in categories:
        if rank <= category:
            return category
    return None


rank = int(input())
top_rank = get_category(rank)
print(f'Top {top_rank}')
