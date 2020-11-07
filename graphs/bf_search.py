# Breadth First Search code.
# From Grokking Algorithms.

from collections import deque

def bf_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print("{} is a mango seller!".format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == "m"

# Implement the graph of yourself and network and test.
graph = {}
graph ["Self"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Anuj", "Peggy"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["Tom", "Johnny"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Tom"]= []
graph["Johnny"] = []

bf_search("Self")
