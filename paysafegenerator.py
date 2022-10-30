import random, discord_webhook, time, os, fade, colorama
from discord_webhook import DiscordWebhook, DiscordEmbed





input_webhook = input("Webhook URL: ")
def main():
    while True:
        code = random.randint(1000000000000000,9999999999999999)
        print(f"                     [{green}+{reset}] New Code: {blue}{code}{reset}")
        time.sleep(0.5)
        webhook = DiscordWebhook(url=input_webhook)
        embed = DiscordEmbed(title='PaySafeCard Generator', description=f"`➕` Code: {code}", color=random.choice(colors_list))
        webhook.add_embed(embed)
        time.sleep(0.5)
        response = webhook.execute() 
main()

