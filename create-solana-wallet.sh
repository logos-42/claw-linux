#!/bin/bash

# Create Solana wallet for testing
echo "Creating Solana wallet for Leo/觉者..."

# Install Solana CLI if not exists
if ! command -v solana &> /dev/null; then
    echo "Installing Solana CLI..."
    sh -c "$(curl -sSfL https://release.solana.com/stable/install)"
    source ~/.bashrc
fi

# Create new wallet
solana-keygen new --outfile ~/solana-test-wallet.json

# Display public key
echo "Solana Wallet Public Key:"
solana address

echo "Wallet created successfully!"
echo "Private key stored in: ~/solana-test-wallet.json"
echo "Remember: NEVER share the private key file!"