from collections import deque

graph = {}
graph["you"] = ["alice","Bob", "cindy", "dell"]
graph["Bob"] = ["To", "bobm", "bobm", "Abigailm"]

def search_person(name):
    return name[-1] == 'm'

def start_find(name):

    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if search_person(person):
                print(person + "I find him who is")
                return True
            else:
                search_queue += graph[name]
                searched.append(person)
    return False

start_find("you")
