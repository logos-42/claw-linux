# Solana Test Wallet Instructions

## Create Solana Wallet

1. **Install Solana CLI** (if not installed):
   ```bash
   sh -c "$(curl -sSfL https://release.solana.com/stable/install)"
   ```

2. **Create new wallet**:
   ```bash
   solana-keygen new --outfile ~/solana-test-wallet.json
   ```

3. **Get wallet address**:
   ```bash
   solana address --keypair ~/solana-test-wallet.json
   ```

4. **Airdrop SOL** (Devnet):
   ```bash
   solana airdrop 1 --url https://api.devnet.solana.com --keypair ~/solana-test-wallet.json
   ```

5. **Check balance**:
   ```bash
   solana balance --url https://api.devnet.solana.com --keypair ~/solana-test-wallet.json
   ```

## Important Notes

- **Never share the private key file** (`~/solana-test-wallet.json`)
- **Testnet SOL has no real value**
- **Use only for testing and learning**
- **Mainnet requires real SOL for transactions**

## For Leo's Research Funding Project

Once comfortable with testnet, we can:
1. Deploy simple programs on Solana
2. Create NFTs for research funding
3. Participate in DeFi protocols
4. Explore yield farming opportunities

Current Solana DeFi yields on mainnet:
- Jito Liquid Staking: ~5.47% APY
- Binance Staked SOL: ~5.56% APY