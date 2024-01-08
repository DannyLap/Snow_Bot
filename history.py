class HistoryNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class HistoryList:
    def __init__(self):
        self.first_node = None
        self.length = 0

    def append(self, data):
        current_node = self.first_node
        self.length += 1

        if current_node is None:
            self.first_node = HistoryNode(data)
            return

        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = HistoryNode(data)

    def show_all(self):
        if self.length == 0:
            return "```L'historique est vide !!!```"
        else:
            ret = "```"
            index = 0
            current_node = self.first_node
            while current_node.next_node is not None:
                ret += str(index) + " : " + current_node.data + "\n"
                current_node = current_node.next_node
                index += 1
            ret += str(index) + " : " + current_node.data
            ret += "```"
            return ret

    def show_last(self):
        if self.length == 0:
            return "```L'historique est vide !!!```"
        else:
            current_node = self.first_node
            while current_node.next_node is not None:
                current_node = current_node.next_node
            return "```" + current_node.data + "```"

    def clear(self):
        self.first_node = None
        self.length = 0
        return "```L'historique a bien été vidé !```"
