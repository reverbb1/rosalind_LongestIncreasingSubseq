with open("file.txt","r") as file:
    seq0 = "".join(file.readlines()[1:])

seq1 = seq0.split()
seq2 = [int(num) for num in seq1]



def inc_subsequence(seq2):
    if not seq2:
        return seq2

    m = [1] * len(seq2)
    p = [-1] * len(seq2)

    for i in range(1, len(seq2)):
        for j in range(i):
            if seq2[i] > seq2[j] and m[j] + 1 > m[i]:
                m[i] = m[j] + 1
                p[i] = j 

    max_index = max(range(len(seq2)), key=lambda x: m[x])

    longest = []
    current_index = max_index

    while current_index != -1:
        longest.append(seq2[current_index])  
        current_index = p[current_index]

    return longest[::-1]

def dec_subsequence(seq2):
    if not seq2:
        return seq2

    m = [1] * len(seq2)
    p = [-1] * len(seq2)

    for i in range(1, len(seq2)):
        for j in range(i):
            if seq2[j] > seq2[i] and m[j] + 1 > m[i]:
                m[i] = m[j] + 1
                p[i] = j 

    max_index = max(range(len(seq2)), key=lambda x: m[x])

    longest = []
    current_index = max_index

    while current_index != -1:
        longest.append(seq2[current_index])  
        current_index = p[current_index]

    return longest[::-1]

a=inc_subsequence(seq2)
b=dec_subsequence(seq2)

print(" ".join(str(num) for num in a))
print(" ".join(str(num) for num in b))


