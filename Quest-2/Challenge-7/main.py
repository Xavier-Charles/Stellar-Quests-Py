"""
Challenge 7: End Sponsoring Reserves
"""
from stellar_sdk import Server, Keypair, TransactionBuilder, Network, FeeBumpTransaction, ClaimPredicate, Claimant, Asset
import requests

# 1. Load Keys
server = Server("https://horizon-testnet.stellar.org")
stellar_quest_keypair = Keypair.from_secret("SBGMYUBQ...")
quest_account_pub_key = stellar_quest_keypair.public_key
quest_account_priv_key = stellar_quest_keypair.secret

other_account = server.load_account("GAT5HZQKWP3S...")

# 2. Create Transaction
print("Building Transaction...")

base_fee = server.fetch_base_fee()
account = server.load_account(quest_account_pub_key)


transaction = TransactionBuilder(
    source_account=account,
    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee=base_fee,
).append_payment_op(
    destination="GAT5HZQKWP3SEMOGDVO7NX3D3JNQHKCBR32FAI45V7V4YVPAGTPRWKUY", 
    amount="10",
    asset_code="XLM",
).append_revoke_account_sponsorship_op(
	account_id="GAT5HZQKWP3SEMOGDVO7NX3D3JNQHKCBR32FAI45V7V4YVPAGTPRWKUY",
).build()


transaction.sign(quest_account_priv_key)
response = server.submit_transaction(transaction)

print(f"This is the final response: {response}")
