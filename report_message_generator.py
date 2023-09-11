from random import choice


def generate_report_message():
    First_part = [
        "Copyright Movies. ",
        "Copyright Netflix series. ",
        "Copyright Amharic Movies. ",
        "Copyright Amharic Films. ",
        "Copyright Music. ",
        "Copyright Amharic Music. ",
        "dangerous for film Industry. ",
    ]
    second_part = [
        "Block the channel! ",
        "Block it as soon as possible! ",
        "Ban this channel please ",
        "It would be helpful if you ban this channel ",
        "This channel is violating Telegram rules and must be stopped ",
    ]
    return (
            choice(First_part) + choice(second_part)
    )
