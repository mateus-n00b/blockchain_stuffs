#!/usr/bin/env python3.7
from web3 import Web3, HTTPProvider
import json

w3Provider = HTTPProvider('http://localhost:7545')
w3 = Web3(w3Provider)

accounts = w3.eth.accounts

abi_file = open("../../build/contracts/ContentValidation.json","r")
abi_file = json.loads(abi_file.read())

contract_address = w3.toChecksumAddress("0x321541d523713102076436240a74d2b6440fe582")
contract_instance = w3.eth.contract(address=contract_address,abi=abi_file['abi'])


def _registerContent(content_name,producer_account):
    # print(contract_instance.functions.myFunction().call())
    # address = w3.toChecksumAddress("0x85e20912ed9cab54e5712e5d1b39b77e593b9067")
    try:
        contract_instance.functions.registerContent(content_name,producer_account).transact({'from':accounts[0], 'gas': 410000})
        status = contract_instance.functions.checkContentStatus(content_name).call()
        if (bool(status)):
            print("Content registered sucessfully!")
        else:
            print("Error on register content! Try again later.")
    except Exception as err:
        print(err)

address = w3.toChecksumAddress("0x85e20912ed9cab54e5712e5d1b39b77e593b9067")
_registerContent("data1",address)
