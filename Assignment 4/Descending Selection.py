#Mustafa Eski
#PSID: 2046388
#reference: https://learn.zybooks.com/zybook/UHCIS2348Fall2021/chapter/14/section/6?content_resource_id=49220580

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        n = i
        for j in range(i + 1, len(numbers)):
            if numbers[n] < numbers[j]:
                n = j
        numbers[i], numbers[n] = numbers[n], numbers[i]
        for value in numbers:
            print(value,end=" ")
        print()
    return numbers

if __name__ == "__main__":
    numbers = []

    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)

