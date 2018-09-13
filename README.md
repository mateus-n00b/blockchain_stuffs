# Blockchain Stuffs

**Some useful documentations that I've been reading about blockchain and smart-contracts**
- https://blockgeeks.com/guides/ethereum/
- https://blockgeeks.com/guides/smart-contracts/
- https://remix.readthedocs.io/en/latest/quickstart_javascript_vm.html
- https://medium.com/aigang-network/how-ethereum-contract-can-communicate-with-external-data-source-2e32616ea180
- https://medium.com/@qmqlegal/what-you-need-to-know-about-blockchain-54df3291f834
- http://solidity.readthedocs.io/en/develop/security-considerations.html
- https://hackernoon.com/ethereum-development-walkthrough-part-2-truffle-ganache-geth-and-mist-8d6320e12269
- http://solidity.readthedocs.io/en/develop/miscellaneous.html?highlight=pure#modifiers
- http://remix.ethereum.org
- https://docs.oraclize.it/#background

**Solidity tutorials**
- https://learnxinyminutes.com/docs/solidity/
- https://blockgeeks.com/guides/solidity/

**Plattaforms**
- [Namecoin](https://namecoin.org/)
- [Ethereum](https://www.ethereum.org/)


## Installing [npm](https://www.npmjs.com/), [Truffle](https://github.com/trufflesuite/truffle), and [remix-ide](https://github.com/ethereum/remix-ide)

**First steps**

Run the following commands to install npm and nodejs

```
apt-get updade && \
apt-get install npm nodejs -y
```

Now as explained in https://stackoverflow.com/questions/30713136/strange-npm-behavior-when-installing-packages-like-grunt we have to create a symbolic link to the nodejs binary.

```
sudo ln -s /usr/bin/nodejs /usr/bin/node
```

**Configuring npm environment**

This step was based on https://docs.npmjs.com/getting-started/fixing-npm-permissions. To avoid permissions erros on npm
you must run the following commands:

* Back-up your computer before you start.

* Make a directory for global installations:

```
 mkdir ~/.npm-global
```

* Configure npm to use the new directory path:

```
npm config set prefix '~/.npm-global'
```

* Open or create a ~/.profile file and add this line:

```
export PATH=~/.npm-global/bin:$PATH
```

* Back on the command line, update your system variables:

```
source ~/.profile
```
* Test: Download a package globally without using sudo.

 In case of versioning erros,  follow this tutorial https://stackoverflow.com/questions/8191459/how-do-i-update-node-js

## Installing remix-ide and Truffle
Simple!!! Just execute:

```
npm install truffle -g
npm install remix-ide -g
```

**Your first Dapp**
- https://truffleframework.com/tutorials/pet-shop

**Interacting with your contracts**
- https://truffleframework.com/docs/truffle/getting-started/interacting-with-your-contracts

**Installing Web3.js API**

```
npm i web3
```

In case of erros such like: _github.com[0: 192.30.253.113]: errno=Conexão recusada_

See: https://stackoverflow.com/questions/1722807/how-to-convert-git-urls-to-http-urls


## Some interesting  discussion topics

- [Memory vs Storage](https://medium.com/loom-network/ethereum-solidity-memory-vs-storage-how-to-initialize-an-array-inside-a-struct-184baf6aa2eb)
- [Optimizing your Solidity contract’s gas usage](https://medium.com/coinmonks/optimizing-your-solidity-contracts-gas-usage-9d65334db6c7)

### Web3 APIs
- [Web3 Javascript API](https://github.com/ethereum/wiki/wiki/JavaScript-API)
- [Web3 Python API](https://github.com/ethereum/web3.py)

## END
