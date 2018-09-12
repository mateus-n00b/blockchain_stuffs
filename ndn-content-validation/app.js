module.paths.push('/home/mateus/.npm_global/lib/node_modules');
var Web3 = require('web3');
// const solc = require("solc");

App = {
  web3Provider: null,

  initWeb3: function () {
    App.web3Provider = new Web3.providers.HttpProvider('http://localhost:7545');
    web3 = new Web3(App.web3Provider);
    return App.initContract("0x9359900a8b0493d1d440ed0c19c33da9b0c7da68");
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
      ContentValidation.methods.registerContent("dado2", accounts[1]).send({from:account, gas:1000000}).then(function(receipt) {
        console.log(receipt);
      }).catch(console.log);
      //
      // // Verificacao do conteudo fornecido
      // ContentValidation.methods.verify_name("dado2",accounts[3]).send({from:account}).then(function(result) {
      //   console.log(result);
      // }).catch(console.log);

      // // Dono do conteudo solicita o cadastramento de um novo distribuidor de conteudo
      // ContentValidation.methods.registerAllowedProviders("dado2", accounts[3]).call({from:account, gas:1000000}).then(function(receipt) {
      //   console.log(receipt);
      // }).catch(console.log);


      ContentValidation.methods.getBadNodes().call({from:account}).then(console.log);
      // ContentValidation.methods.myFunction().call({from:account}).then(console.log);

    });
  }
}

App.initWeb3();
