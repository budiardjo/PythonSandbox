
# 0(n) time | O(1) space

def validateSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

if __name__ == '__main__':
    print(validateSubsequence([5,1,22,25,6,-1,8,10], [1,6,-1,10]))

# def validateSubsequence(array, sequence):
#     seqIdx = 0
#     for value in array:
#         if seqIdx == len(sequence):
#             break
#         if sequence(seqIdx) == value:
#             seqIdx += 1
#     return seqIdx == len(sequence)


# def validateSubsequence(array, sequence):
#     # Write your code here.
#     # O(N) time and O(1) space
#     if not sequence:
#         return False
#
#     index = 0
#     for x in array:
#         if x == sequence[index]:
#             if index == len(sequence) - 1:
#                 return True
#             index += 1
#
#     return False

