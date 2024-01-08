class FilterNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class FilterList:
    def __init__(self):
        self.first_node = None
        self.length = 0

    def append(self, data):
        current_node = self.first_node
        self.length += 1

        if current_node is None:
            self.first_node = FilterNode(data)
            return

        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = FilterNode(data)

    def test_message(self, message):
        current_node = self.first_node
        if current_node is None:
            return False
        while current_node is not None:
            if current_node.data in message:
                return True
            current_node = current_node.next_node
        return False

    def initialisation(self):
        self.append("tg")
        self.append("ta gueule")
        self.append("merde")
        self.append("connard")
        self.append("fdp")
        self.append("fils de pute")
        self.append("fille de pute")
