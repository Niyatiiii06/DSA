def largest(arr):
    largest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
    print("Largest element is:", largest)
def second_l(arr):
    largest=arr[0]
    sec= None
    for i in arr:
        if i>largest:
            sec=largest
            largest=i
        elif i<largest and (sec is None or i>sec):
            sec=i
    return sec if sec is not None else "No second largest element"

def smallest(arr):
    smallest=arr[0]
    for i in arr:
        if i<smallest:
            smallest=i
    print("Smallest element is:", smallest)
def second_s(arr):
    smallest=arr[0]
    sec= None
    for i in arr:
        if i<smallest:
            sec=smallest
            smallest=i
        elif i>smallest and (sec is None or i<sec):
            sec=i
    return sec if sec is not None else "No second smallest element"



largest([1, 2, 0, 9, 4, 5])
smallest([1, 2, 0, 9, 4, 5])
print(second_l([-1, -2, 0, -5, -4, -5]))
print(second_s([5,5,5,5,5]))