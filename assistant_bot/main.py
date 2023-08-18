from .class_assistant_bot import Assistant_bot
from .class_console_output import Terminals
from argparse import ArgumentParser
import hashlib


def argument_parse():
    default_user = "user-session-100001"
    parser = ArgumentParser(
        prog=__package__,
        description="Assistant bot of GoIT project team 11",
        epilog="GoIT. Python Core 15. Project team 11. Aug-2023",
    )

    parser.add_argument(
        "-u",
        "--username",
        type=str,
        required=False,
        default=default_user,
        help="user name of the Assistant bot",
    )
    parser.add_argument(
        "-sort",
        "--sorting",
        type=str,
        required=False,
        metavar="PATH",
        help="run sorting commands for selected folder. "
        "Use path to folder as argument ",
    )
    parser.add_argument("-V", "--version", action="store_true", help="show version")
    parser.add_argument(
        "-dar",
        "--disable_auto_restore",
        action="store_true",
        help="disable auto_restore",
    )
    parser.add_argument(
        "-dab", "--disable_auto_backup", action="store_true", help="disable auto_backup"
    )

    list_output = []
    list_output_help = []
    for t in Terminals:
        list_output.append(t.value)
        list_output_help.append(f"{t.value}: {t.name}")
    list_output_help_str = ", ".join(list_output_help)

    parser.add_argument(
        "--output_console",
        type=int,
        choices=list_output,
        help=f"Output console ({list_output_help_str}), \
              default: {Terminals.TERMINAL_RICH.value}",
        default=Terminals.TERMINAL_RICH,
    )

    args = parser.parse_args()
    if args.username:
        bin_name = bytearray(args.username, encoding="utf-8")
        args.username = hashlib.sha1(bin_name).hexdigest()
    if args.sorting or args.version:
        args.disable_auto_restore = True
        args.disable_auto_backup = True
    # print(args)
    return args


def arg_action(assistant, args):
    if args.version:
        print(assistant.api("version", verbose=False))
    elif args.sorting:
        print(assistant.api("sorting", args.sorting, verbose=False))
    else:
        return True


def cli(pre_init: object = None) -> None:
    args = argument_parse()
    username = args.username
    auto_restore = not args.disable_auto_restore
    auto_backup = not args.disable_auto_backup

    output_terminal = Terminals(args.output_console)

    assistant = Assistant_bot(
        id=username,
        auto_restore=auto_restore,
        auto_backup=auto_backup,
        output_terminal=output_terminal,
    )

    if arg_action(assistant, args):
        if pre_init:
            pre_init(assistant)
        assistant.main()


if __name__ == "__main__":
    cli()
