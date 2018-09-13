#!/usr/bin/env python3.7
from web3 import Web3, HTTPProvider
import json

w3Provider = HTTPProvider('http://localhost:7545')
w3 = Web3(w3Provider)

accounts = w3.eth.accounts

abi_file = open("../../build/contracts/ContentValidation.json","r")
abi_file = json.loads(abi_file.read())

contract_address = w3.toChecksumAddress("0x60969902a3c17b5243aad850481149ead1cc0982") # Here goes the contract address
contract_instance = w3.eth.contract(address=contract_address,abi=abi_file['abi'])

def _verifyContent(content_name, provider_acount):
    try:
        contract_instance.functions.verifyContent(content_name,provider_acount).transact({'from':accounts[0],'gas':410000})
        status = contract_instance.functions.verifyContent(content_name,provider_acount).call()
        if (bool(status)):
            print("Provider '{0}' is allowed to provide content '{1}'!".format(provider_acount,content_name))
        else:
            print("node '{0}' is an invalid provider for content '{1}'! Call the cops.".format(provider_acount,content_name))
    except Exception as err:
        print(err)

def _registerProvider(content_name,provider_acount):
    try:
        contract_instance.functions.registerAllowedProviders(content_name,provider_acount).transact({'from':accounts[0], 'gas': 410000})
        print("New provider for content '{0}' registered successfully!".format(content_name))
    except Exception as err:
        print(err)

def _registerContent(content_name,producer_account):
    # print(contract_instance.functions.myFunction().call())
    # address = w3.toChecksumAddress("0x85e20912ed9cab54e5712e5d1b39b77e593b9067")
    try:
        contract_instance.functions.registerContent(content_name,producer_account).transact({'from':accounts[0], 'gas': 410000})
        status = contract_instance.functions.checkContentStatus(content_name).call()
        if (bool(status)):
            print("Content '{0}' owned by {1} registered successfully!".format(content_name,producer_account))
        else:
            print("Error on register content! Try again later.")
    except Exception as err:
        print(err)

# address = w3.toChecksumAddress("0x85e20912ed9cab54e5712e5d1b39b77e593b9067")
address = accounts[0]
fake = accounts[3]
_registerContent("data1",address)
_verifyContent("data1",fake)
_registerProvider("data1",fake)
_verifyContent("data1",fake)
