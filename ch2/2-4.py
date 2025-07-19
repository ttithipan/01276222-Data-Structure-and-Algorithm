def three_num_zero_sum(arr):
    arr.sort()
    triplets = []
    n = len(arr)

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if abs(total) < 1e-9:
                triplet = [int(arr[i]), int(arr[left]), int(arr[right])]
                if triplet not in triplets:
                    triplets.append(triplet)
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets

nums = [float(e) for e in input("Enter Your List : ").split()]
if len(nums) < 3:
    print("Array Input Length Must More Than 2")
else:
    print(three_num_zero_sum(nums))
