import urllib.request
import urllib.error
import time
import os


# ==========================================
#                  COLORS
# ==========================================

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


# ==========================================
#               PLATFORMS
# ==========================================

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "X": "https://x.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Steam": "https://steamcommunity.com/id/{}",
}


# ==========================================
#                  LOGO
# ==========================================

def show_logo():

    print(GREEN + r"""
███╗   ██╗ █████╗ ███╗   ███╗███████╗ █████╗ ██╗    ██╗
████╗  ██║██╔══██╗████╗ ████║██╔════╝██╔══██╗██║    ██║
██╔██╗ ██║███████║██╔████╔██║█████╗  ███████║██║ █╗ ██║
██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██║██║███╗██║
██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗██║  ██║╚███╔███╔╝
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══╝╚══╝

                    Searcher by Aspect
""" + RESET)


# ==========================================
#              CHECK PROFILE
# ==========================================

def check_profile(url):

    try:

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response = urllib.request.urlopen(
            request,
            timeout=8
        )

        if 200 <= response.status < 400:
            return True

        return False

    except urllib.error.HTTPError as error:

        if error.code == 404:
            return False

        return None

    except Exception:
        return None


# ==========================================
#              USERNAME SEARCH
# ==========================================

def search_username(username):

    results = []

    print()
    print(GREEN + f"Searching for: {username}" + RESET)
    print()

    for platform, url_template in PLATFORMS.items():

        url = url_template.format(username)

        print(
            f"[*] Checking {platform}...",
            end=" ",
            flush=True
        )

        time.sleep(0.3)

        result = check_profile(url)

        if result is True:

            print(GREEN + "FOUND" + RESET)
            results.append((platform, url))

        elif result is False:

            print(RED + "NOT FOUND" + RESET)

        else:

            print("UNKNOWN")

    print()
    print("RESULTS")
    print()

    if not results:

        print("No public profiles were found.")

    else:

        print(f"Found {len(results)} possible profile(s):")
        print()

        for platform, url in results:

            print(GREEN + f"[+] {platform}" + RESET)
            print(f"    {url}")
            print()

    print()
    print("Developped by Aspect")


# ==========================================
#             DISCORD USERNAME
# ==========================================

def discord_username():

    print()
    print("DISCORD USERNAME")
    print()

    print("Enter a Discord username you already know.")
    print("Type 'back' to return to the main menu.")
    print()

    try:

        username = input("Discord username: ").strip()

    except KeyboardInterrupt:

        return

    if username.lower() == "back":
        return

    if username.lower() == "quit":
        raise SystemExit

    if username == "":

        print()
        print("Please enter a username.")
        time.sleep(1)
        return

    username = username.lstrip("@")

    discord_link = f"https://discord.com/users/{username}"

    print()
    print("Discord profile link:")
    print()
    print(discord_link)
    print()


# ==========================================
#                SEARCH MENU
# ==========================================

def search_menu():

    while True:

        os.system("cls")
        show_logo()

        print("SEARCHER")
        print()
        print("Type a username to search.")
        print("Type 'back' to return to the main menu.")
        print("Type 'quit' to close NAMESAW.")
        print()
        print("Press Ctrl+C to go back to the menu.")
        print()

        try:

            username = input("Username: ").strip()

        except KeyboardInterrupt:

            return

        if username.lower() == "quit":

            raise SystemExit

        if username.lower() == "back":

            return

        if username == "":

            print()
            print("Please enter a username.")
            time.sleep(1)
            continue

        username = username.lstrip("@")

        try:

            search_username(username)

        except KeyboardInterrupt:

            return

        print()
        print("Press ENTER to return to the menu.")
        print("Press Ctrl+C to return to the menu.")

        try:

            input()

        except KeyboardInterrupt:

            return


# ==========================================
#              DISCORD MENU
# ==========================================

def discord_menu():

    while True:

        os.system("cls")
        show_logo()

        try:

            discord_username()

        except KeyboardInterrupt:

            return

        except SystemExit:

            raise

        print()
        print("Press ENTER to return to the menu.")
        print("Press Ctrl+C to return to the menu.")

        try:

            input()

        except KeyboardInterrupt:

            return


# ==========================================
#                MAIN MENU
# ==========================================

def main():

    while True:

        os.system("cls")

        show_logo()

        print("    1. Searcher")
        print("    2. Discord username")
        print()
        print("Type 1 or 2.")
        print("Type quit to close NAMESAW.")
        print("Press Ctrl+C to go back to the menu.")
        print()

        try:

            choice = input("> ").strip()

        except KeyboardInterrupt:

            continue

        if choice == "1":

            search_menu()

        elif choice == "2":

            discord_menu()

        elif choice.lower() == "quit":

            os.system("cls")

            print()
            print("NAMESAW closed.")
            print()
            break

        else:

            print()
            print("Invalid choice. Type 1 or 2.")
            time.sleep(1)


# ==========================================
#                  START
# ==========================================

try:

    main()

except SystemExit:

    os.system("cls")

    print()
    print("NAMESAW closed.")
    print()

except KeyboardInterrupt:

    os.system("cls")

    print()
    print("NAMESAW closed.")
    print()