# Tokenomics

## DISEÑO ECONÓMICO FUNDAMENTAL

### Supply Management (Gestión de Suministro)

#### Modelos de Emisión

- **Fixed Supply:** Suministro máximo definido desde inicio
  - Bitcoin (21M BTC), máxima escasez
  - Problemas: Falta de flexibilidad económica
- **Infinite Supply:** Sin cap máximo
  - ETH post-Merge (emisión dinámica)
  - Dogecoin (inflación constante)
- **Elastic Supply:** Ajuste algorítmico según demanda
  - Ampleforth (AMPL), rebasing tokens
  - RAI (Reflexer), controlador PID

#### Cronogramas de Desbloqueo (Vesting)

- **Cliff + Linear:** Lock inicial + liberación gradual
  - Team/Investors: 1 año cliff, 3-4 años vesting
  - Previene dumps tempranos
- **Token Generation Event (TGE):** % inicial circulante
  - Low float risk: <10% circulante causa alta volatilidad
  - Healthy launch: 15-30% circulante en TGE
- **Unlock Schedules:** Calendario público y transparente
  - Herramienta: Token Unlocks trackers
  - Riesgo: Overhang (presión vendedora futura)

#### Burning y Deflación

- **Buyback & Burn:** Protocolo compra y destruye tokens
  - BNB: Quarterly burns hasta alcanzar 100M supply
  - Binance usa 20% de profits para buyback
- **Fee Burning:** Parte de fees destruye tokens
  - ETH: EIP-1559, fee base quemada
  - Reduce supply en proporción al uso
- **Deflationary Spirals:** Riesgo de burning excesivo
  - Incentiva holding extremo
  - Puede matar la economía del protocolo

### Utilidad Real del Token

#### Casos de Uso Legítimos

- **Governance (Gobernanza):**
  - Votar propuestas on-chain (Snapshot, Tally)
  - MKR vota parámetros de riesgo en MakerDAO
  - Delegación: No necesitas participar directamente
- **Staking (Security/Revenue):**
  - Securing the network: ETH, SOL, DOT
  - Revenue sharing: GMX, CVX
  - Sin utilidad real: Solo bloquear tokens ≠ valor
- **Gas (Transaction Fees):**
  - Token como medio de pago interno
  - ETH en Ethereum, SOL en Solana
  - Crea demanda orgánica constante
- **Collateral (Garantía):**
  - Préstamos: Aave, Compound
  - Minting stablecoins: DAI con ETH/WBTC
  - Derivados: GMX, Synthetix (SNX)

#### Tokens Sin Utilidad Real (Red Flags)

- **Pure Speculation:** Solo "to the moon"
- **Governance vacía:** No hay decisiones importantes que votar
- **Staking sin fuente de revenue:** ¿De dónde vienen los rewards?
- **Promesas vagas:** "Utility coming soon™"

## PROTOCOLOS DE TOKENOMICS

### Captura de Valor

#### Fee Switch (Protocol Revenue)

- Patrón: Una parte de fees va a token holders
- Uniswap: Potencial fee switch (no activado)
- Aave: Safety module stakers
- GMX: 70% de fees a stakers (esGMX)

#### Productive Assets (Yield-Bearing)

- Patrón: Token genera yield automáticamente
- stETH (Lido): Rebasing o wrapped
- rETH (Rocket Pool): Appreciate vs ETH
- sDAI (Spark): DAI + DSR yield

### Mecanismos de Alineación

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

## VALORACIÓN DE MERCADO

### Métricas Clave de Valoración

#### Market Cap vs FDV (Fully Diluted Valuation)

- **Market Cap:** Precio × Circulante
  - Lo que puedes "comprar hoy"
  - Ej: 100M tokens × $10 = $1B market cap
- **FDV:** Precio × Supply Total
  - Valoración si todos los tokens existieran
  - Ej: 1B tokens × $10 = $10B FDV
- **FDV/Market Cap Ratio:** Indicador de dilución
  - Ratio >3x: Alto riesgo de dilución futura
  - Ratio <2x: Distribución más saludable

#### Protocol Revenue y Valoración

- **P/F Ratio (Price-to-Fees):**
  - Similar a P/E en acciones tradicionales
  - FDV / Annual Protocol Fees
  - Ej: $1B FDV / $50M fees = 20x P/F
  - Comparación: Uniswap vs GMX vs Aave
- **Revenue Share:** ¿Cuánto va a token holders?
  - GMX: 70% de fees a stakers
  - Uniswap: 0% (fee switch no activado)
  - Sin revenue share → Token es governance puro
- **Fee Generation Sustainability:**
  - Real users paying fees vs subsidized activity
  - Wash trading puede inflar métricas falsas

#### Token Incentives (Emisiones)

- **Emission Rate:** Inflación anualizada del token
  - Ej: 10% annual inflation
  - Reduce valor si no hay demand equivalente
- **Incentives vs Real Revenue:**
  - Protocol paga $100M en tokens, genera $10M fees
  - Ratio 10:1 incentives/revenue = Insostenible
- **Ponzinomics:** Nuevos usuarios pagan rewards de viejos
  - Terra/Luna: 20% APY en Anchor sin fuente real
  - OlympusDAO: (3,3) meme sin fundamentals

### Token Distribution (Distribución)

#### Fairness del Launch

- **Community Allocation:** % para usuarios reales
  - >50% community = Descentralizado
  - <20% community = Red flag (pump & dump)
- **Team & Investors Allocation:**
  - 15-25% reasonable para team + advisors
  - >40% team/VCs = High centralization risk
  - Vesting largo (4 años) = Alineación
- **Treasury:** Fondos para desarrollo futuro
  - 20-30% razonable
  - Governance decide cómo gastarlo

#### Modelos de Lanzamiento

- **Fair Launch:** Sin pre-venta, todos entran igual
  - Yearn Finance (YFI), Uniswap
  - Solo liquidity mining desde día 1
- **ICO/IDO:** Venta pública/descentralizada
  - ICO: Ethereum 2014, Polkadot 2017
  - IDO: En DEXs, más accesible (menos regulación)
- **Airdrop:** Distribución gratis basada en criterios
  - Uniswap: 400 UNI por usuario histórico
  - Arbitrum: Basado en actividad on-chain
  - Sybil farming: Problema de bots múltiples wallets

## LANZAMIENTO DE TOKENS (ICO/IDO/TGE)

### Preparación Pre-Lanzamiento

#### Aspectos Legales y Regulatorios

- **Security vs Utility Token:**
  - Howey Test (USA): ¿Es un security?
  - MiCA (EU 2024): Regulación crypto unificada
  - CNMV (España): Obligaciones de registro
- **KYC/AML Requirements:**
  - IDOs centralizados: ByBit, Binance Launchpad
  - IDOs descentralizados: Riesgos legales
- **Whitepaper y Documentación:**
  - Tokenomics completa y transparente
  - Roadmap realista, no promesas imposibles
  - Auditorías: CertiK, Trail of Bits, OpenZeppelin

#### Auditorías Técnicas

- **Smart Contract Audits:**
  - Múltiples auditorías (no solo una)
  - Publicar reportes completos
  - Bug bounties: Immunefi, HackerOne
- **Economic Audits:**
  - Simulaciones de Game Theory
  - Análisis de vectores de ataque económico
  - Herramientas: Gauntlet, Chaos Labs

### Estrategias de Lanzamiento

#### Bootstrapping de Liquidez

- **Liquidity Pools (LPs):**
  - Pairing: TOKEN/ETH o TOKEN/USDC
  - Lockup: Team liquidity locked 1+ año
  - Herramientas: Unicrypt, Team Finance
- **Bonding Curves:**
  - Precio aumenta automáticamente con supply
  - Bancor, Polkadot parachain auctions
- **LBP (Liquidity Bootstrapping Pool):**
  - Balancer: Peso cambia 95/5 → 50/50
  - Previene bots y snipers
  - Precio descubre demand orgánicamente

#### Marketing y Community Building

- **Education-First Marketing:**
  - Contenido técnico: Docs, videos, AMAs
  - No solo hype: Explicar el "por qué"
  - Embajadores y evangelistas técnicos
- **Incentivos para Early Adopters:**
  - Testnet rewards, NFTs conmemorativos
  - Puntos que se convierten en tokens
  - Evitar mercenarios: Criterios de calidad
- **Transparencia Total:**
  - Public dashboards: Dune Analytics
  - Multisig transparency: Gnosis Safe
  - Comunicación constante en Discord/Forum

### Post-Lanzamiento

#### Gestión de Mercado Secundario

- **Market Making:** Proveer liquidez profesional
  - Wintermute, GSR, Jump Trading
  - Evitar manipulación y wash trading
- **CEX Listings:** Intercambios centralizados
  - Timing: No demasiado pronto (volumen real primero)
  - Costs: $50k-$500k+ listing fees
  - Top tier: Binance, Coinbase (requieren traction)
- **Token Buybacks:** Protocolo compra del mercado
  - Reduce supply, aumenta precio
  - Solo con revenue real, no con treasury

#### Monitoring y Ajustes

- **On-Chain Analytics:**
  - Holder distribution: ¿Centralizado en pocas wallets?
  - Active users: ¿Crecimiento real o bots?
  - Token velocity: ¿Se usa o solo se holdea?
- **Governance Evolution:**
  - Progressive decentralization
  - Inicio: Team control con training wheels
  - Futuro: Full community governance
- **Incentives Optimization:**
  - Reducir emisiones gradualmente
  - Mover de liquidity mining a protocol revenue
  - Sustainable tokenomics = Long-term success

## RED FLAGS Y ERRORES COMUNES

### Señales de Alarma (Red Flags)

- **FDV/Market Cap >5x:** Dilución masiva pendiente
- **Team tokens sin vesting:** Rugpull inminente
- **Anonymous team:** Sin accountability
- **Copied code sin auditoría:** Vulnerabilidades conocidas
- **Promesas imposibles:** "100x guaranteed", "Risk-free"
- **Pressure tactics:** "Last chance", "Only today"
- **Sin product-market fit:** Token antes que producto

### Errores de Diseño Tokenómico

- **Incentivos mal alineados:**
  - Rewards para comportamiento dañino
  - Ej: Pagar por volumen → wash trading
- **Death spirals:**
  - Selling pressure perpetua
  - Ej: High inflation + no utility
- **Governance centralizada:**
  - Whale control (ballenas controlan votos)
  - Solución: Cuadratic voting, delegación
- **Sin mecanismo de captura de valor:**
  - Protocol exitoso pero token sin valor
  - Ej: Uniswap pre-fee switch

## RECURSOS Y HERRAMIENTAS

### Análisis y Research

- **DefiLlama:** TVL, fees, revenue de todos los protocolos
- **Token Terminal:** Financial metrics (P/F, P/S ratios)
- **Messari:** Research reports profesionales
- **Dune Analytics:** Dashboards custom on-chain
- **Nansen:** Token god mode, smart money tracking

### Valoración y Modelado

- **TokenomicsDAO:** Frameworks de diseño
- **Gauntlet:** Economic simulations
- **Outlier Ventures:** Token design workshops
- **CoinGecko/CMC:** Market data básica

#### Simuladores de Tokenomics

Herramientas para modelar y visualizar la economía del token antes del lanzamiento:

- **[Cenit Finance Tokenomics Simulator](https://www.cenit.finance/tokenomics-simulator-template):** Simulador interactivo basado en Google Sheets/Excel. Permite modelar supply schedules, vesting, emisiones, burns, staking rewards, y visualizar proyecciones de precio/market cap bajo diferentes escenarios. **Freemium model:** Versión básica gratuita con funcionalidades limitadas, versión completa de pago (~$99-299) con features avanzadas y templates customizables. Ideal para founders sin background financiero que necesitan validar tokenomics antes de launch.

- **[Outlier Ventures Token Designer](https://github.com/OutlierVentures/TokenDesigner):** Framework open-source en Python para diseño y simulación de tokenomics. Permite modelar agentes económicos, comportamientos de mercado, y ejecutar simulaciones Monte Carlo. Más técnico que Cenit, requiere conocimientos de Python pero ofrece mayor flexibilidad y es completamente gratuito. Usado en workshops de Outlier Ventures para startups Web3.

- **[TokenSPICE](https://github.com/tokenspice/tokenspice):** Simulador open-source avanzado basado en agent-based modeling (ABM) desarrollado originalmente por Ocean Protocol. Modela comportamientos complejos de múltiples agentes (traders, stakers, liquidity providers) en economías token. Curva de aprendizaje alta pero permite validar sostenibilidad económica bajo condiciones adversas. Requiere Python y conocimientos de simulación. **100% gratuito y open-source.**

- **[Machinations](https://machinations.io/):** Plataforma visual de game economy design adaptada para tokenomics. Sistema de diagramas de flujo para modelar circulación de tokens, pools, incentivos. **Freemium:** Versión gratuita muy limitada (pocos diagramas, sin exportación avanzada), planes pagos ($19-99/mes) para features completas. No open-source pero muy intuitivo para diseño iterativo.

- **[CadCAD](https://cadcad.org/):** Framework open-source de simulación de sistemas complejos usado por proyectos DeFi serios (MakerDAO, BlockScience). Permite modelar políticas, parámetros y comportamientos emergentes. Extremadamente potente pero requiere expertise en ciencia de datos y Python. **100% gratuito y open-source.** Overkill para proyectos pequeños, esencial para protocolos complejos con riesgos sistémicos.

**Recomendaciones según presupuesto y experiencia:**

- **Sin presupuesto + no-técnicos:** Cenit Finance versión gratuita (limitada) o Machinations free tier
- **Sin presupuesto + técnicos:** TokenSPICE o Outlier Ventures Token Designer (100% gratis, open-source)
- **Con presupuesto + no-técnicos:** Cenit Finance versión completa ($99-299 one-time) o Machinations Pro ($19-99/mes)
- **Protocolos DeFi complejos:** CadCAD (gratis pero complejo) + consultoría especializada (Gauntlet, BlockScience)

**Recursos complementarios:**

- [TokenEngineering Academy](https://www.tokenengineering.net/): Cursos y recursos sobre diseño de sistemas económicos
- [TE Commons Library](https://library.tokenengineering.net/): Papers y frameworks de token engineering
- [Awesome Token Engineering](https://github.com/token-engineering-commons/awesome-token-engineering): Lista curada de recursos open-source

### Compliance y Legal

- **CNMV:** Regulación española (Sandbox)
- **MiCA:** Marco europeo (2024+)
- **Howey Test:** Framework USA para securities
- **Token Taxonomy Framework:** Estándares internacionales