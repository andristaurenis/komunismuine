
message_dict = {
        'en': """
Hello!
        """,
        }
def get_email_message(lang):
    return message_dict.get(lang, message_dict['en'])

