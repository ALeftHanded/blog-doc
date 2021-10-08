def maxArea_for_test(height):
    ans = 0
    for i in range(len(height) - 1):
        for j in range(i + 1, len(height)):
            area = (j-i)*min(height[i], height[j])
            if area > ans:
                ans = area
    return ans


def maxArea(height):
    i, j = 0, len(height) - 1
    ans = (j-i) * min(height[i], height[j])
    while i < j:
        if height[i] > height[j]:
            j -= 1
            ans = (j-i) * min(height[i], height[j]) if (j-i) * min(height[i], height[j]) > ans else ans
        elif height[i] < height[j]:
            i += 1
            ans = (j - i) * min(height[i], height[j]) if (j - i) * min(height[i], height[j]) > ans else ans
        else:
            i += 1
    return ans