'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur
within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if not word or len(word) < 2:
        return 0

    def count(index):
        if index >= len(word) - 1:
            return 0
        if word[index] + word[index + 1] == "th":
            return 1 + count(index + 2)
        else:
            return count(index + 1)
    return count(0)


print(count_th("thehthehe"))
