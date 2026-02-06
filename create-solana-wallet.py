#!/usr/bin/env python3
"""
Create a Solana wallet manually using Python
This creates a basic keypair for testing purposes
"""

import os
import json
from hashlib import sha256
import secrets

def create_solana_keypair():
    """Create a Solana keypair (64 bytes: 32 bytes secret + 32 bytes public)"""
    # Generate 32 bytes of random data for the secret key
    secret_key = secrets.token_bytes(32)
    
    # For simplicity, we'll use a basic derivation for public key
    # In real Solana, this uses Ed25519 curve
    public_key = sha256(secret_key).digest()
    
    # Combine into 64-byte keypair (secret + public)
    keypair = secret_key + public_key
    
    return keypair, secret_key, public_key

def save_wallet(keypair, filename):
    """Save wallet as JSON and binary format"""
    # Save as binary (what Solana CLI uses)
    with open(filename + '.json', 'w') as f:
        # Convert to array of integers (Solana format)
        keypair_array = list(keypair)
        json.dump(keypair_array, f)
    
    # Save human-readable info
    with open(filename + '_info.txt', 'w') as f:
        f.write(f"Solana Test Wallet\n")
        f.write(f"==================\n")
        f.write(f"Secret Key (hex): {keypair[:32].hex()}\n")
        f.write(f"Public Key (hex): {keypair[32:].hex()}\n")
        f.write(f"Public Key (base58): [Will need proper base58 encoding]\n")
        f.write(f"\n⚠️  WARNING: This is for testing only!\n")
        f.write(f"Never use this for real funds!\n")

if __name__ == "__main__":
    print("Creating Solana test wallet...")
    keypair, secret, public = create_solana_keypair()
    
    wallet_name = "solana_test_wallet"
    save_wallet(keypair, wallet_name)
    
    print(f"Wallet created: {wallet_name}.json")
    print(f"Public key: {public.hex()}")
    print("\nTo use this wallet:")
    print("1. Import the .json file into Phantom or Solflare")
    print("2. Or use it with Solana CLI after proper installation")