from populus.contracts import (
    deploy_contract,
    get_contract_address_from_txn,
)


def test_deployment_with_no_args(rpc_server, rpc_client, Math):
    deploy_txn_hash = deploy_contract(
        rpc_client,
        Math,
    )
    contract_addr = get_contract_address_from_txn(rpc_client, deploy_txn_hash)
    assert contract_addr


def test_deployment_with_endowment(rpc_server, rpc_client, Math):
    deploy_txn_hash = deploy_contract(
        rpc_client,
        Math,
        value=1000,
    )
    contract_addr = get_contract_address_from_txn(rpc_client, deploy_txn_hash)
    assert contract_addr
    math = Math(contract_addr, rpc_client)
    assert math.get_balance() == 1000


def test_deployment_with_args(rpc_server, rpc_client, Named):
    deploy_txn_hash = deploy_contract(
        rpc_client,
        Named,
        constructor_args=("John",),
    )
    contract_addr = get_contract_address_from_txn(rpc_client, deploy_txn_hash)

    named = Named(contract_addr, rpc_client)
    name = named.name.call()
    assert name == "John"