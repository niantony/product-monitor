# Website Product Monitor
A Python application that monitors for product restocks. Currently supports BestBuy.

## Get started
You can get started by cloning this repository and creating a `.env` file. In the `.env` file, create a variable `WEBHOOK_URL` and set it equal to your Discord Webhook Url where you want your notifications to appear, for example `WEBHOOK_URL="YOUR WEBHOOK URL"`. Next edit the `bestBuySkus.txt` file with the skus of the products you would like to monitor. Finally, you can start the program by typing `python bestBuy.py` in your terminal, otherwise if you have any proxies, just insert them in `proxies.txt` and then type `python bestBuy.py` in your terminal.

## Examples
![mon1](https://user-images.githubusercontent.com/66891025/129939988-957c823b-c602-46f4-a679-ede13b1a06ce.png)
![mon2](https://user-images.githubusercontent.com/66891025/129939994-9a9d78f4-c689-49f5-bb6b-920f04b8f1f7.png)
