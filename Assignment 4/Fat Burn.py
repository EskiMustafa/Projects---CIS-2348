#Mustafa Eski
# PSID: 2046388
# Reference: https://stackoverflow.com/questions/61336073/im-having-trouble-with-this
def get_age():
    age = int(input())
    if age <= 18 or age >= 75:
        raise ValueError("Invalid age.")
    else:
        return age

def fat_burning_heart_rate(age):
    return (220 - age) * 0.7


if __name__ == "__main__":
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")
