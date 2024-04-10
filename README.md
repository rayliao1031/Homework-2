# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Swap 1: BA - amountIn: 5, amountOut: 5.655321988655322
> 
> Swap 2: AD - amountIn: 5.655321988655322, amountOut: 2.4587813170979333
> 
> Swap 3: DC - amountIn: 2.4587813170979333, amountOut: 0.9064895557558128
> 
> Swap 4: CB - amountIn: 0.9064895557558128, amountOut: 6.6348386154671175
> 
>Path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129888944077443

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Slippage in AMMs like Uniswap V2 refers to the difference between the expected price of a trade and the price at which the trade is executed. This often occurs due to price movements between the time a trade is submitted and when it's executed, especially in volatile or low-liquidity markets.
>
>Uniswap V2 addresses slippage by:
>
>Using the Constant Product Formula (x * y = k), which naturally increases the price impact of larger trades, discouraging large orders that can cause significant slippage.
> 
>Allowing users to set a Slippage Tolerance, which is the maximum allowed deviation between the expected and actual prices. Trades exceeding this tolerance will fail.
> 
>Permitting a Transaction Deadline, where trades must be executed before this time, reducing the risk of executing at an undesirable price due to delay.
```solidity
// Assuming a function to swap tokens with slippage control
function swapTokens(uint amountIn, uint minAmountOut, address[] path, uint deadline) external {
    require(block.timestamp <= deadline, "Trade expired"); // Checks the deadline
    uint amountOut = getAmountOut(amountIn, path); // Calculates output based on Uniswap formula
    require(amountOut >= minAmountOut, "Slippage too high"); // Checks for slippage tolerance
    // Proceed with the swap if conditions are met
}

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

