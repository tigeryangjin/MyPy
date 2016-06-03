grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for i in grades:
        print(i)


def grades_sum(scores):
    total = 0
    for i in scores:
        total += i
    return total


def grades_average(grades):
    average = grades_sum(grades) / float(len(grades))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance = variance / float(len(scores))
    return variance


def grades_std_deviation(variance):
    std = grades_variance(variance) ** 0.5
    # std=1
    return std


print(grades_sum(14.2222222222))
