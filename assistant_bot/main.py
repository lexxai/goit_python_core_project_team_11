from .class_assistant_bot import Assistant_bot

def cli():
    session = "user-session-000001"
    assistant = Assistant_bot(id=session)
    assistant.main()    


if __name__ == "__main__":
    cli()
    



