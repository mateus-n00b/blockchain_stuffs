pragma solidity ^0.4.23;

// A example of reliable math library
library Math{
  function sum(uint a, uint b) public returns (uint256){
    return a+b;
  }
}

contract ContentValidation {

  address admin;
  address[] private good_nodes;
  address[] private bad_nodes;

  mapping (string => Provider) private registeredContents;

  struct Provider{
    string name;
    mapping (address => bool) allowed_producers;
    address contentOwner;
    bool exists;
  }

  // constructor () {admin = msg.sender; }
  // Here the node ask for a producer name Validation on blockchain
  // But if the clients were the bad guys?
  function verify_name(string contentName, address holder) public returns (bool success){
    require(registeredContents[contentName].exists);
    if (registeredContents[contentName].contentOwner == holder ||
      registeredContents[contentName].allowed_producers[holder]){
        return true;
      }else{
        bad_nodes.push(holder);
        return false;
      }
    }

    // modifier onlyOwner {
    //     require(
    //         msg.sender == owner,
    //         "Only owner can call this function."
    //     );
    //     _;
    // }

    function registerAllowedProviders(string contentName, address producer) public returns (bool success){
        require(msg.sender == registeredContents[contentName].contentOwner);

        if (registeredContents[contentName].exists &&
            !registeredContents[contentName].allowed_producers[producer]){
                registeredContents[contentName].allowed_producers[producer] = true;
                return true;
            }else{
                return false;
            }
    }

    function registerContent (string contentName, address contentOwner) public returns (bool success){
      address senderAddress = msg.sender;
      require(bytes(contentName).length > 0);
      if (bytes(contentName).length > 0 && !registeredContents[contentName].exists){
        registeredContents[contentName].name = contentName;
        registeredContents[contentName].allowed_producers[senderAddress] = true;
        registeredContents[contentName].contentOwner = contentOwner;
        registeredContents[contentName].exists = true;
        // Is not necessary to keep the good_nodes
        // good_nodes.push(senderAddress);
        return true;
      }else{
        return false;
      }
    }

    function checkContentStatus(string contentName) public view returns (bool exists){
        if (registeredContents[contentName].exists){
          return true;
        }else{
          return false;
        }
    }

    function getBadNodes() public view returns (address[]) {
      return bad_nodes;
    }

    function getGoodNodes() public view returns (address[]){
      return good_nodes;
    }

    // Just a debug function
    function myFunction() public view returns(uint256 myNumber) {
      return (1999);
    }
  }
