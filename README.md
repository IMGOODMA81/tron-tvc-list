import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import '@okxweb3/hardhat-explorer-verify';  // Import the plugin

const config: HardhatUserConfig = {
    solidity: "0.8.24",
    sourcify: {
        enabled: true,
    },
    networks: {
        xlayer: {
            url: "https://xlayerrpc.example.com",
            accounts: ["<Your Wallet Private Key>"],
        },
    },
    etherscan: {
        apiKey: '...',
    },
    okxweb3explorer: {
        apiKey: "<Your API Key>",
        customChains: [
            {
                network: "Fractal Bitcoin Mainnet",
                chainId: 70000061,
                urls: {
                    apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/FRACTAL",
                    browserURL: "https://www.oklink.com/fractal",
                },
            },
        ],
    },
};

export default config;import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import '@okxweb3/hardhat-explorer-verify';  // Import the plugin

const config: HardhatUserConfig = {
    solidity: "0.8.24",
    sourcify: {
        enabled: true,
    },
    networks: {
        xlayer: {
            url: "https://xlayerrpc.example.com",
            accounts: ["<Your Wallet Private Key>"],
        },
    },
    etherscan: {
        apiKey: '...'
    },
    okxweb3explorer: {
        apiKey: "<Your API Key>",
        customChains: [
            {
                network: "Fractal Bitcoin Mainnet",
                chainId: 70000061,
                urls: {
                    apiURL: "https://www.oklink.com/api/v5/explorer/contract/verify-source-code-plugin/FRACTAL",
                    browserURL: "https:/POST /api/v5/explorer/contract/check-proxy-verify-result
body
{
    "chainShortName":"ETH",
    "guid":"4f2e75682f75410f958c0a3bbf754358"
}POST /api/v5/explorer/contract/verify-proxy-contract
body
{
    "chainShortName": "ETH",
    "proxyContractAddress": "0xfeee12d53ddb7ce61ee467ddf7243212a953174a",
    "expectedImplementation": "0x0ecbefc71524068cf18f9d4e50d787e134ee70b8"
}8dd085d159cb123f545c272c0d871a5339550e79function transfer(address to, uint256 tokenId) public virtual returns (bool success) {
    // Only the owner can transfer the token
    require(msg.sender == ownerOf[tokenId], "NOT_OWNER");

    unchecked {
        balanceOf[msg.sender]--; // Decrease owner's token balance
        balanceOf[to]++;         // Increase recipient's token balance
    }

    delete getApproved[tokenId]; // Remove any prior approval

    ownerOf[tokenId] = to;       // Update the owner mapping

    emit Transfer(msg.sender, to, tokenId); // Emit the ERC-721 Transfer event

    success = true;
}# Adding new token
The JSON schema for the tokens includes: address, name, decimals, symbol, logoURI, official homepage, MarketCap link, existing Markets.

Follow the steps below to add a new token：
1) Fork this repo.
2) change the JSON file `tokenlist.json`, adding such as: (PLEASE DO NOT REMOVE EXISITING TOKENS)
```
{
      "address": "TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7",
      "symbol": "WIN",
      "name": "WINkLink",
      "decimals": 6,
      "logoURI": "https://coin.top/profile_images/JKtJTydD_400x400.jpg",
      "homepage": "https://winklink.org/",
      "MarketCapLink": "https://coinmarketcap.com/currencies/wink/",
      "existingMarkets": [
          {
              "source": "Binance",
              "pairs": [
                  "WIN/USDT",
                  "WIN/BUSD",
                  "WIN/BNB",
                  "WIN/USDC"
              ]
          },
          {
              "source": "Poloniex",
              "pairs": [
                  "WIN/USDT"
              ]
          },
          {
              "source": "KuCoin",
              "pairs": [
                  "WIN/USDT"
              ]
          }
    ]
}
```
* `address`[Required]: your token address.
* `symbol`[Required]: your token symbol.
* `name`[Required]: your token name.
* `logoURI`[Required]: the logo URI of your token.
* `homepage`[Required]: the home page of your token.
* `MarketCapLink`[Optional]: the coinmarketcap or coingecko link for your token.
* `existingMarkets`[Required]: where to trade with your token.
3) Submit PR with the changed JSON file.


