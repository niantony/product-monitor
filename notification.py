from discord_webhook import DiscordWebhook, DiscordEmbed
import os
from dotenv import load_dotenv

load_dotenv()

webhook = DiscordWebhook(url=os.getenv('WEBHOOK_URL'))

def sendBestBuyNotification(sku, url, name, image, price, addToCart):
    print(name + ' (' + sku + ') in stock!')
    embed = DiscordEmbed(title="<:bestbuy:877291905954750464> Best Buy Restock!", url=url, color='0046BE')
    embed.set_timestamp()
    embed.add_embed_field(name='Product', value=name, url=url, inline=False)
    embed.add_embed_field(name='Price', value=price)
    embed.add_embed_field(name='SKU', value=sku)
    embed.add_embed_field(name='Add to cart', value=addToCart, inline=False)
    embed.set_thumbnail(url=image)

    webhook.add_embed(embed)
    webhook.execute()