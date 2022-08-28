import sys
import requests


def main():
    URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    numof_btc = input_numof_btc()
    # print(f"numof_btc: {numof_btc}")
    response = get_btc_price(URL)
    # print(json.dumps(response, indent=2))
    USD_price = get_usd(response, numof_btc)
    print(f"${USD_price}")
    # print("$"+"{:,.4f}".format(USD_price))



def input_numof_btc():
    # numof_btc = input("numof:")
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            numof_btc = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            return numof_btc

def get_btc_price(URL):
    try:
        response = requests.get(URL)
    except requests.RequestException:
        sys.exit("req excptn")
    else:
        r = response.json()
        return r

def get_usd(rspns, numof_btc):
    results = rspns["bpi"]["USD"]["rate_float"] * numof_btc
    # return results
    return '{:,.4f}'.format(results)

main()


