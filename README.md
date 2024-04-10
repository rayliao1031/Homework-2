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

> The Uniswap V2 protocol, when minting initial liquidity for a new pair, subtracts a minimum liquidity amount of 1000 units. This design serves several purposes, both technical and economic:

> 1. Preventing Zero-Total-Supply Issues
At the very start, before any liquidity is added, the total supply of the liquidity tokens (LP tokens) for a pair is zero. The first liquidity provider must not be allowed to end up with zero LP tokens after their contribution because their share of the pool would be undefined, and it could introduce division by zero errors in calculations. Subtracting a minimum amount when the first liquidity is added ensures that the first liquidity provider receives an amount of LP tokens that correctly represents their share of the pool, excluding the very small amount subtracted.
> 
> 2. Creating a Non-withdrawable Minimum Liquidity
The minimum liquidity subtracted and permanently locked in the contract ensures that there's always some residual value. This makes the pool resistant to being completely drained through withdrawals. It's a safeguard that ensures the pool can continue to function, even if liquidity levels fall very low.
> 
> 3. Protection Against Certain Attacks
This design can offer protection against potential manipulation or attack vectors. By ensuring that a tiny portion of liquidity cannot be withdrawn, it prevents someone from completely resetting the pool's state through strategic withdrawals and deposits, which could potentially be used to manipulate prices or extract value from other liquidity providers.
> 
>  Technical Rationale
When the first liquidity provider contributes liquidity, they set the initial price of the assets in the pool based on the ratio of their deposited assets. The initial mint function needs to carefully issue LP tokens to ensure that the pool's initial state and the LP tokens' distribution accurately reflect the value contributed by this liquidity provider, minus the tiny, non-withdrawable part that serves the purposes outlined above.
> 
>  Example from the UniswapV2Pair Contract:
When the first liquidity provider adds liquidity, the Uniswap V2 contract mints LP tokens based on the square root of the product of the amounts of the two assets deposited, minus the 1000 units of minimum liquidity. This approach ensures that the ratio of assets in the pool accurately reflects the market's consensus value of these assets relative to each other, while also seeding the pool with an initial amount of liquidity that remains locked.
> 
In summary, subtracting a minimum liquidity amount upon the initial liquidity minting in Uniswap V2 serves to prevent mathematical issues, ensure ongoing pool operation, protect against certain types of economic attacks, and establish an initial state that accurately reflects the value and price ratios contributed by the first liquidity provider.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

