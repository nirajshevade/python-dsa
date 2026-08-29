class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:

            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]


def main():

    capacity = int(input("Enter cache capacity: "))

    cache = LRUCache(capacity)

    print("\nCommands:")
    print("put key value")
    print("get key")
    print("exit")

    while True:

        command = input("\nEnter command: ").split()

        if not command:
            continue

        if command[0].lower() == "put":

            if len(command) != 3:
                print("Usage: put key value")
                continue

            key = int(command[1])
            value = int(command[2])

            cache.put(key, value)

            print("Added:", key, "->", value)

        elif command[0].lower() == "get":

            if len(command) != 2:
                print("Usage: get key")
                continue

            key = int(command[1])

            result = cache.get(key)

            print("Result:", result)

        elif command[0].lower() == "exit":
            print("Exiting...")
            break

        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()