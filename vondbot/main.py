import os
from vondbot import Von


def main() -> None:
    bot = Von()

    token = os.getenv("DISCORD_TOKEN")
    if token:
        bot.run(token)
    else:
        print("can't found discord token inside .env")


if __name__ == "__main__":
    main()
