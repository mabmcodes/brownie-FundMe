from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3, IPCProvider


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DICIMLS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print("deploying mocks ...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DICIMLS, STARTING_PRICE, {"from": get_account()})
    print("mocks deployed!")
