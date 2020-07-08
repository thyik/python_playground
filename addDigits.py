class Solution:

    def add_digits(self, num: int) -> int:
        return 0 if num == 0 else 1 + (num - 1) % 9


if __name__ == "__main__":
    sln = Solution()
    res = sln.add_digits(998)

    print(res)