from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()

    if network.show_active() != "development":
        price_feed_address = config[network][network.show_active()][
            "eth_usd_price_feed_address"
        ]
    else:
        # print(network.show_active())
        print(f"the active network is {network.show_active()}")
        print("Deploying Mocks...\n")
        mock_aggregator = MockV3Aggregator.deploy(
            18, 2000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address
        print("mock deployed")

    fund_me = FundMe.deploy(price_feed_address, {"from": account})
    print(f"contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
