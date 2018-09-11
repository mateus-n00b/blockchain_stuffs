module.paths.push('/home/mateus/.npm_global/lib/node_modules');
var Web3 = require('web3');
// const solc = require("solc");

App = {
  web3Provider: null,

  initWeb3: function () {
    App.web3Provider = new Web3.providers.HttpProvider('http://localhost:7545');
    web3 = new Web3(App.web3Provider);
    return App.initContract("0xc2b19ffb74e11536c5ecf50880816153119b068d");
  },

  initContract: function(contract_address){
    var abi = require('./build/contracts/ContentValidation.json');

    web3.eth.getAccounts(function(error, accounts) {
      if (error) {
        console.log(error);
      }

      var account = accounts[0];
      var ContentValidation = new web3.eth.Contract(JSON.parse(JSON.stringify(abi.abi)),contract_address); //,{gasPrice: '2000', from: account});
      // console.log(Object.getOwnPropertyNames(web3.eth));
      ContentValidation.methods.registerProviders("dado2", account).send({from:account, gas:1000000}).then(function(receipt) {
        console.log("HI");
      }).catch(console.log);

      ContentValidation.methods.verify_name("dado2",accounts[2]).call().then(function(result) {
        console.log(result);
      }).catch(console.log);

      ContentValidation.methods.getBadNodes().call({from:account}).then(console.log);
      // ContentValidation.methods.myFunction().call({from:account}).then(console.log);

    });
  }
}

App.initWeb3();
