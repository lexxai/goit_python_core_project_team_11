import sys

try:
    sys.path.append("./")  
    from assistant_bot.class_assistant_bot import Assistant_bot
except ImportError :
    sys.path.append("../")  
    from assistant_bot.class_assistant_bot import Assistant_bot


if __name__ == "__main__":
    session = "user-session-000001"
    assistant = Assistant_bot(id=session)

    if True:
        verbose = True
        assistant.api("add address book", "Jon-00", "+38044333223", "+38044333221",
                       verbose=verbose)
        assistant.api("add email", "Jon-00", "jon05@example.com", verbose=verbose)
        assistant.api("add address", "Jon-00",
                "вул. Ворота Гетьмана, буд. 02, офіс. 121-344", verbose=verbose)
        assistant.api("add birthday", "Jon-00", "1999-08-11", verbose=verbose)
        assistant.api("add note", "Note 1", "#tag1", "#tag2", verbose=verbose)
        assistant.api("add note", "Note 2", "#tag1", "#tag2", verbose=verbose)
        assistant.api("add note", "Note 1", "#tag1", "#tag2", verbose=verbose)
        assistant.api("add note", "Note 1", "#tag2", "#tag3", verbose=verbose)

    assistant.main()


