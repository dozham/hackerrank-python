# def merge_the_tools(string, k):
#     n: int = len(string)
#     chunks: int = n // k
#
#     u_chunks_list = []
#     for c in range(chunks):
#         chunk_start_index = c * k
#         chunk_end_index = c * k + k
#         chunk = string[chunk_start_index:chunk_end_index]
#         u_chunks_list.append(dedup_string(chunk))
#
#     return u_chunks_list

# def dedup_string(s: str):
#     seen_set = set()
#     dedupped_str = ''
#     for ch in s:
#         if ch not in seen_set:
#             seen_set.add(ch)
#             dedupped_str += ch
#
#     return dedupped_str
#

def merge_the_tools(string, k):
    uchunks = []
    for i in range(0, len(string), k):  # TIP: using range step to chunk the input
        chunk = string[i:i + k]
        unique_chunk = ''

        for ch in chunk:
            if ch not in unique_chunk:
                unique_chunk += ch
        # print(unique_chunk)
        uchunks.append(unique_chunk)

    return uchunks


if __name__ == '__main__':
    # string, k = input(), int(input())
    string, k = "AABCDEABCBBC", 3
    print("Input:", string)
    [print(c) for c in merge_the_tools(string, k)]

