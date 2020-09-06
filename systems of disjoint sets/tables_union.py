_, num_of_quaries = input().split(' ')
table_sizes = [int(i) for i in input().split(' ')]
table_links = [i for i in range(len(table_sizes))]
max_table_size = max(table_sizes)
symlinc_indexes = []


def relative_check(link):
    if link == table_links[link]:
        return link
    symlinc_indexes.append(link)
    return relative_check(table_links[link])


def link_swapper(changer):
    if symlinc_indexes:
        for ind in symlinc_indexes:
            table_links[ind] = changer
        symlinc_indexes.clear()


for _ in range(int(num_of_quaries)):
    query_input = input().split(' ')
    destination = relative_check(int(query_input[0]) - 1)
    link_swapper(destination)
    source = relative_check(int(query_input[1]) - 1)
    link_swapper(source)
    if destination != source:
        table_sizes[destination] += table_sizes[source]
        table_links[source] = destination
        if table_sizes[destination] >= max_table_size:
            max_table_size = table_sizes[destination]
    print(max_table_size)