class Message:
    """ A Message Class that contain a message and is details """

    def __init__(self, msg_id: int, sender: str, msg_body=''):
        """
        init the Message body and details
        :param msg_id: the id number of message
        :param sender: from whom send the message
        :param msg_body: the message
        """
        self.msg_id = msg_id
        self.sender = sender
        self.msg_body = msg_body

    def __str__(self):
        """
        :return: the data as a string
        """
        return '\nMessage ID: ' + str(self.msg_id) + '\n' \
                'Sender: ' + self.sender + '\n' \
                'Message_body:' + self.msg_body + '\n'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        """
        :return: the length of the body message
        """
        return len(self.msg_body)
