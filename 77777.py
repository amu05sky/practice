from collections import deque

def find_min_clicks(N, links, start_page, end_page):
    # Create an adjacency list to represent the links between web pages
    adjacency_list = [[] for _ in range(N)]
    for i, link in enumerate(links):
        for linked_page in link:
            adjacency_list[i].append(linked_page - 1)  # Convert 1-based index to 0-based index

    # Initialize a queue for BFS and a visited set to keep track of visited pages
    queue = deque([(start_page - 1, 0)])  # Start from the 0-based index of the start page
    visited = set()

    while queue:
        current_page, clicks = queue.popleft()

        if current_page == end_page - 1:  # Found the end page
            return clicks

        if current_page not in visited:
            visited.add(current_page)
            for linked_page in adjacency_list[current_page]:
                queue.append((linked_page, clicks + 1))

    # If end page cannot be reached
    return -1

# Input
N = int(input())
links = []
for _ in range(N):
    links.append(list(map(int, input().split())))

start_page, end_page = map(int, input().split())

# Output
result = find_min_clicks(N, links, start_page, end_page)
print(result)
