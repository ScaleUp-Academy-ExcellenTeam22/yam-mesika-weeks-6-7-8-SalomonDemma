from turtle_sent_2 import PostOffice


def show_example():
    """Show example of using the PostOffice class."""
    users = ('Newman', 'Mr. Peanutbutter')
    post_office = PostOffice(users)

    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Hello, Newman.',
    )
    print(f"Successfuly sent message number {message_id}.")

    message_id = post_office.send_message(
        sender='Mr. Peanutbutter',
        recipient='Newman',
        message_body='Bye, Newman.',
    )
    print(f"Successfuly sent message number {message_id}.")

    #  tests:
    # print(post_office.boxes['Newman'])
    # print(post_office.read_inbox('Newman', 2))
    # s = post_office.search_inbox('Newman', 'Hello')
    # print(s)
    # print(len(s[0]))


if __name__ == "__main__":
    show_example()
