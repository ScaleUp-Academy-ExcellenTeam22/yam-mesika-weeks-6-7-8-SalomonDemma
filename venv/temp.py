from turtle_sent import PostOffice


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

    print(post_office.boxes['Newman'])
    #print(post_office.read_inbox('Newman', 2))
    #print(post_office.search_inbox('Newman', 'Hello'))



if __name__ == "__main__":

    show_example()
