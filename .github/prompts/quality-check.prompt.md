# Checklist de conocimiento técnico avanzado Web3

> Este checklist separa el conocimiento superficial (explicaciones simplistas de DAO/DeFi, maximalismo Bitcoin) del conocimiento técnico profundo que demuestra comprensión real del ecosistema Web3.

## Economía y Tokenomics

- [ ] **Ownership Economy** - Token de captura de valor vs participación, diferencias críticas con equity tradicional
- [ ] **Bonding Curves** - Alternativa matemática a pools de liquidez, casos de uso (Protocol-Owned Liquidity, fair launch)
- [ ] **ve-Tokenomics** (vote-escrowed) - Vote locking, time-weighted voting power, Curve Wars
- [ ] **Liquid Staking Derivatives (LSD)** - stETH, rETH, riesgos de centralización (Lido >30%), LSD-Fi
- [ ] **Restaking & EigenLayer** - AVS (Actively Validated Services), seguridad compartida, capital efficiency, riesgos de cascading slashing

## Identidad, Reputación y Gobernanza

- [ ] **Soulbound Tokens (SBT)** - EIP-4973, Account-bound tokens, no-transferible credentials
- [ ] **ERC-6551 (Token Bound Accounts)** - NFTs con wallets propias que acumulan reputación componible
- [ ] **Attestations & Verifiable Credentials** - EAS (Ethereum Attestation Service), W3C VCs, DID (Decentralized Identifiers)
- [ ] **EIP-712 (Typed Structured Data)** - Prevención de phishing, legibilidad de firmas, typed data signing
- [ ] **Proof of Personhood** - Sybil resistance sin sacrificar privacidad (Worldcoin, BrightID, Gitcoin Passport)
- [ ] **Futarchy** - "Vote on values, bet on beliefs", prediction markets para gobernanza DAO
- [ ] **Quadratic Voting/Funding** - Mitigación de plutocracy, optimización de bienes públicos

## Arquitectura y Escalabilidad

- [ ] **Account Abstraction (ERC-4337)** - UserOperations, Bundlers, Paymasters, EntryPoint, session keys, social recovery
- [ ] **Optimistic vs ZK Rollups** - Fraud proofs, validity proofs, trade-offs de finalidad (7 días vs minutos), Data Availability
- [ ] **PBS/ePBS (Proposer-Builder Separation)** - MEV extraction, Builders, PTC (Payload Timeliness Committee), EIP-7732
- [ ] **Danksharding & Proto-Danksharding** - EIP-4844, blobs, Data Availability Sampling (DAS), capa modular
- [ ] **Single Slot Finality (SSF)** - Propuesta Ethereum para reducir finalidad a 12 segundos vs 15 minutos actuales
- [ ] **RANDAO** - Fuente de aleatoriedad en Ethereum PoS, beacon chain randomness, VDF
- [ ] **Verkle Trees** - Reemplazo de Merkle Patricia Trees, stateless clients, witness size reduction
- [ ] **Modular Blockchain** - Separación de execution/consensus/DA, Celestia, OP Stack/Superchain, zkStack
- [ ] **Cross-Chain Intents (ERC-7683)** - Abstracción de bridges, solvers compitiendo por ejecutar cross-chain orders

## DeFi Avanzado

Dynamic AMMs** - Balancer v2 pools, variable weights, custom curves, multi-token pools
- [ ] **vAMMs (Virtual AMMs)** - Perpetual Protocol, synthetic liquidity, funding rates, oracle-based pricing
- [ ] **MEV (Maximal Extractable Value)** - Sandwich attacks, frontrunning, Flashbots, builder market
- [ ] **TWAP Oracles** - Time-weighted average price, resistencia a manipulación vs spot price
- [ ] **Impermanent Loss avanzado** - Estrategias de range management, hedging con perpetuals
- [ ] **DeFi 2.0 Anti-patterns** - Ponzinomics taxonomy, rebase tokens insostenibles, yield farming extractivo, (3,3) memeional
- [ ] **MEV (Maximal Extractable Value)** - Sandwich attacks, frontrunning, Flashbots, builder market
- [ ] **TWAP Oracles** - Time-weighted average price, resistencia a manipulación vs spot price
- [ ] **Impermanent Loss avanzado** - Estrategias de range management, hedging con perpetuals

## Criptografía y Privacidad

- [ ] **MPC Wallets (Multi-Party Computation)** - Threshold signatures, distributed key generation vs multisig tradicionallications
- [ ] **BLS Signatures** - Signature aggregation en Ethereum PoS, efficiency para validar múltiples attestations
- [ ] **Schnorr Signatures & MuSig** - Signature aggregation Bitcoin Taproot, privacy en multisig
- [ ] **Verkle Trees** - Reemplazo de Merkle Patricia Trees, stateless clients, witness size reduction
- [ ] **Commit-Reveal Schemes** - Fair NFT mints, voting, time-locked secrets on-chain

## Tendencias 2025-2026

- [ ] **RWA (Real World Assets)** - Tokenización institucional, Blackrock BUIDL, Ondo Finance, regulación MiCA
- [ ] **Account Abstraction UX** - Passkeys (WebAuthn), social login, gasless transactions, session keys
- [ ] **EigenLayer AVS Ecosystem** - Oráculos descentralizados, sequencer networks, DA layers como AVS

---
