# Mustafa Eski
#PSID: 2046388
#reference: https://stackoverflow.com/questions/18262306/quicksort-with-python/20258416

num_calls = 0

def partition(user_ids, m,n):
    
    middle = user_ids[n]
    index = (m - 1)
    for o in range(m,n):
        if user_ids[o]<=middle:
            index = index +1
            user_ids[index], user_ids[o] = user_ids[o], user_ids[index]
    user_ids[index + 1], user_ids[n] = user_ids[n], user_ids[index + 1]
    return index+1


def quicksort(user_ids,m,n):
    global num_calls
    num_calls += 1
    if m<n:
        mid= partition(user_ids,m,n)
        quicksort(user_ids,m,mid-1)
        quicksort(user_ids, mid+1,n)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    quicksort(user_ids, 0, len(user_ids) - 1)
    num_calls = int(2 * len(user_ids) - 1)
    print(num_calls)

    for user_id in user_ids:
        print(user_id)