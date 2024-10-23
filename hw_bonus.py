"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""

def longest_consecutive(my_list: list[int]) -> int:
    if not my_list:
        return 0

    my_list.sort()
    cnt = 1
    ans = 0

    for i in range(1, len(my_list)):
        if my_list[i-1]+1!=my_list[i]:
            if my_list[i-1]==my_list[i]:
                continue
            ans = max(ans, cnt)
            cnt=1
        else:
            cnt+=1

    return max(ans, cnt)


"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""

def find_missing(my_list: list[int]) -> int:
    if not my_list:
        return 0

    my_list.sort()


    for i in range(1, len(my_list)+1):
        if i!=my_list[i-1]:
            return i

    return None


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""


def find_duplicate(my_list: list[int]) -> int:
    # Use Floyd's Tortoise and Hare algorithm (cycle detection)
    slow = fast = my_list[0]

    # Phase 1: Detect the cycle
    while True:
        slow = my_list[slow]
        fast = my_list[my_list[fast]]
        if slow == fast:
            break

    # Phase 2: Find the entry point of the cycle
    slow = my_list[0]
    while slow != fast:
        slow = my_list[slow]
        fast = my_list[fast]

    return slow


"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""

from collections import defaultdict
def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_groups = defaultdict(list)

    for word in words:
        # Sort the word and use it as a key
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    # Return the grouped anagrams as a list of lists
    return list(anagram_groups.values())


if __name__ == '__main__':
    pass