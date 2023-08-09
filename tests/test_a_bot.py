import sys

try:
    sys.path.append("./")  
    from assistant_bot.class_assistant_bot import Assistant_bot
    from assistant_bot.main import cli      
except ImportError :
    sys.path.append("../")  
    from assistant_bot.class_assistant_bot import Assistant_bot
    from assistant_bot.main import cli


def pre_init(assistant: Assistant_bot) -> None:
    if True:
        verbose = True
        assistant.api("add address book", "Jon-00", "+380447776661", "4400",
                    verbose=verbose)
        assistant.api("add email", "Jon-00", "jon05@example.com", verbose=verbose)
        assistant.api("add address", "Jon-00",
                "вул. Ворота Гетьмана, буд. 02, офіс. 121-344", verbose=verbose)

        

        assistant.api("add birthday", "Jon-00", "1999-08-11", verbose=verbose)
        assistant.api("add address book", "Jon-01", "+380447776661", "4401",
                    verbose=verbose)
        assistant.api("add address book", "Jon-02", "+380447776661", "4402",
                    verbose=verbose)               

        assistant.api("add address book", "Mike", "+380447777661", "4402",
                    verbose=verbose)  
        assistant.api("add address book", "Mike Svarovsky", "+380447786661",
                    verbose=verbose)                                                     
        assistant.api("add note", "Note 1", "#tag1", "#tag2", verbose=verbose)
        assistant.api("add note", "Note 2", "#tag1", "#tag2", verbose=verbose)
        assistant.api("add note", "Note 1", "#tag1", "#tag2", verbose=verbose)
        assistant.api("add note", "Note 1", "#tag2", "#tag3", verbose=verbose)


if __name__ == "__main__":
    # args = argument_parse()
    # username = args.username
    # assistant = Assistant_bot(id=username, auto_restore=True, auto_backup=True)
    # if not arg_action(assistant, args):
    #    exit()
    # assistant.main()
    cli(pre_init=pre_init)



