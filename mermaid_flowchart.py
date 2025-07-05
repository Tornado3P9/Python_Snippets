import requests
import argparse
import re


def is_valid_bitcoin_address(address):
    # Regex for legacy (1, 3) and bech32 (bc1) addresses
    pattern = r'^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$'
    if re.match(pattern, address):
        return address
    else:
        raise argparse.ArgumentTypeError(f"Invalid Bitcoin address: {address}")


def commandLine() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a simple Mermaid FlowChart from Bitcoin Address Relations"
    )
    parser.add_argument("-V", "--version", action="version", version="%(prog)s 1.0")
    parser.add_argument(
        "-a",
        "--address",
        type=is_valid_bitcoin_address,
        required=True,
        help="your bitcoin address",
    )
    return parser.parse_args()


def fetch_transactions(address):
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/full"
    response = requests.get(url)
    return response.json()


def generate_mermaid(transactions, address):
    mermaid = "flowchart TD;\n"
    address_aliases = {}
    alias_counter = 0

    def get_alias(address):
        nonlocal alias_counter
        if address not in address_aliases:
            alias = chr(65 + alias_counter)  # Starting from 'A'
            address_aliases[address] = alias
            alias_counter += 1
            return f'{alias}["{address}"]'
        return address_aliases[address]

    if not transactions["txs"]:
        # No transactions, return the supplied address
        mermaid += f"    {get_alias(address)};\n"
    else:
        for tx in transactions["txs"]:
            for input in tx["inputs"]:
                input_alias = get_alias(input["addresses"][0])
                for output in tx["outputs"]:
                    output_alias = get_alias(output["addresses"][0])
                    mermaid += f"    {input_alias} --> {output_alias};\n"

    return mermaid


def main() -> None:
    parsed_args = commandLine()
    address: str = parsed_args.address
    transactions = fetch_transactions(address)
    mermaid_syntax = generate_mermaid(transactions, address)

    with open("mermaid_output.txt", "w") as file:
        file.write(mermaid_syntax)

    print("Created mermaid_output.txt")


if __name__ == "__main__":
    main()
