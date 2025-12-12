# Tokenomics

## VII. PROTOCOLOS DE TOKENOMICS

### 1. Captura de Valor

#### Fee Switch (Protocol Revenue)

- Patrón: Una parte de fees va a token holders
- Uniswap: Potencial fee switch (no activado)
- Aave: Safety module stakers
- GMX: 70% de fees a stakers (esGMX)

#### Token Sinks (Deflación)

- Burning: Destruir tokens permanentemente
  - ETH post-EIP-1559, BNB quarterly burns
- Buyback: Protocolo compra tokens del mercado
  - MKR (MakerDAO surplus auctions)
- Lockup: Requiere lock para utilidad
  - veCRV (Curve), veBAL (Balancer)

#### Productive Assets (Yield-Bearing)

- Patrón: Token genera yield automáticamente
- stETH (Lido): Rebasing o wrapped
- rETH (Rocket Pool): Appreciate vs ETH
- sDAI (Spark): DAI + DSR yield

### 2. Mecanismos de Alineación

#### Vote-Escrowed Tokens (ve-model)

- Patrón: Lock tokens por tiempo → voting power + rewards
- Curve veCRV: Lock CRV hasta 4 años → boost + fees
- Balancer veBAL: 80/20 BPT locked
- Velodrome veVELO: Solidly fork en Optimism

#### Dual-Token Models

- Governance + Utility separados
- Olympus: OHM (tradeable) + gOHM (wrapped)
- GMX: GMX (gov) + GLP (liquidity pool)
- THORChain: RUNE (settlement) + synthetic assets

### 3. Bootstrapping de Liquidez

#### Protocol-Owned Liquidity (POL)

- Patrón: Bonding en lugar de renting (liquidity mining)
- Olympus Pro: Vende tokens con descuento por LP tokens
- Ventaja: Liquidez permanente, no mercenaria

#### Liquidity Mining

- Patrón: Emisiones de tokens a LPs
- Curve Gauge System: Votos dirigen emissions
- SushiSwap Onsen: Temporary farms
- Problema: Sell pressure, liquidez mercenaria