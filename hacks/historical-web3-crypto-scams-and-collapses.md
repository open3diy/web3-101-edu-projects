# Estafas y Colapsos Históricos en Web3 y Cripto

Este documento recoge los casos más significativos de fraudes, estafas y colapsos en el ecosistema cripto y Web3. No se trata de casos de hacking técnico, sino de esquemas fraudulentos, colapsos por diseño defectuoso o manipulación deliberada.

## Mt. Gox (2014)

El primer gran colapso de un exchange cripto.

Contexto: Mt. Gox manejaba el 70% de todas las transacciones de Bitcoin a nivel mundial en 2013-2014.

El problema:

- Entre 2011 y 2014, hackers robaron aproximadamente 850.000 BTC (7% de todo el Bitcoin existente en ese momento).
- El CEO Mark Karpelès no reportó los robos y continuó operando normalmente.
- Usó un sistema contable deficiente que no detectó las pérdidas durante años.

Colapso: Febrero 2014, suspendieron retiros y declararon bancarrota. 850.000 BTC desaparecidos (posteriormente recuperaron 200.000 BTC).

Resultado: Karpelès fue arrestado en Japón, aunque las acusaciones de malversación fueron desestimadas. Los acreedores siguen esperando distribución de fondos recuperados más de 10 años después.

Lección: Los exchanges centralizados son puntos únicos de fallo. La custodia centralizada contradice la filosofía de descentralización de cripto.

## OneCoin (2014-2017)

Uno de los esquemas Ponzi más grandes de la historia cripto.

Contexto: OneCoin se presentaba como una criptomoneda revolucionaria que superaría a Bitcoin. Prometía retornos masivos a los inversores que reclutaran más gente.

La realidad:

- No existía blockchain real. Era una base de datos centralizada controlada por la organización.
- Funcionaba como un esquema piramidal puro: los nuevos inversores pagaban a los anteriores.
- Vendían "paquetes educativos" que incluían tokens OneCoin sin valor real.
- Los tokens no se podían intercambiar libremente en ningún exchange real.

Resultado: Más de 4.000 millones de dólares robados a inversores de todo el mundo. Ruja Ignatova, la fundadora, desapareció en 2017 y sigue en la lista de los más buscados del FBI. Varios colaboradores fueron arrestados.

Lección: Si no puedes ver el código, auditar la blockchain o intercambiar libremente en exchanges reales, probablemente no sea una criptomoneda.

## Bitconnect (2016-2018)

Esquema Ponzi disfrazado de plataforma de préstamos con "bot de trading automático".

Contexto: Bitconnect prometía retornos del 1% diario (365% anual) mediante un "bot de trading volatility software" que nadie podía verificar.

Funcionamiento del fraude:

- Los usuarios compraban BCC (el token de Bitconnect) y lo bloqueaban en la plataforma.
- Prometían intereses diarios garantizados más bonos por referir nuevos usuarios.
- El "bot de trading" nunca existió. Los retornos provenían del dinero de nuevos inversores.
- Tenían un sistema de afiliados multinivel que incentivaba el reclutamiento agresivo.

Colapso: En enero de 2018, tras recibir órdenes de cese de autoridades regulatorias, cerraron abruptamente. El token BCC cayó de 400 USD a menos de 1 USD en días. Pérdidas estimadas en 2.000 millones de dólares.

Resultado: Varios promotores fueron arrestados. Demandas colectivas continúan. Se convirtió en el símbolo del esquema Ponzi cripto, generando el meme "Hey hey heyyy, Bitconneeeect!".

Lección: Promesas de retornos garantizados extraordinarios sin riesgo son siempre una bandera roja. En cripto no existen rendimientos sin riesgo.

## PlusToken (2018-2019)

Esquema Ponzi asiático masivo.

Contexto: Operaba principalmente en China y Corea del Sur, presentándose como una wallet cripto con funciones de trading.

El fraude: Prometían retornos del 10-30% mensual mediante "arbitraje entre exchanges". Funcionaba como MLM (multinivel marketing) incentivando reclutamiento.

Resultado: 2.900 millones de dólares robados a más de 3 millones de personas. Seis organizadores arrestados en China. Las ventas masivas de Bitcoin confiscado por autoridades chinas afectaron el mercado durante meses.

## Squid Game Token (2021)

Rug pull inspirado en la serie de Netflix.

Contexto: Token lanzado aprovechando la popularidad de la serie "Squid Game", sin afiliación oficial.

El fraude:

- El contrato inteligente tenía código malicioso que impedía a los usuarios vender el token.
- Solo el creador podía vender.
- Promoción agresiva en redes sociales y medios.

Colapso: El token subió de 0.01 USD a 2,856 USD en días. Los creadores vendieron todo, colapsando el precio a 0 USD en minutos. Robaron 3.3 millones de dólares.

Lección: Audita siempre el código del contrato inteligente. Si no puedes venderlo libremente, es una trampa.

## UST/LUNA - Terra Ecosystem (Mayo 2022)

El colapso de una stablecoin algorítmica que destruyó 40.000 millones de dólares en días.

Contexto: Terra era un ecosistema blockchain con dos tokens principales:

- UST: Una stablecoin algorítmica diseñada para mantener paridad 1:1 con el dólar.
- LUNA: El token de gobernanza y respaldo del ecosistema.

Diseño del sistema:

- UST no estaba respaldado por dólares reales, sino por un mecanismo algorítmico.
- Para mantener el precio de 1 USD, podías quemar 1 UST y acuñar 1 dólar en LUNA (y viceversa).
- Anchor Protocol ofrecía 20% APY por depositar UST, atrayendo miles de millones.

El problema fundamental:

- Era un sistema reflexivo: UST dependía del valor de LUNA, y LUNA dependía de la demanda de UST.
- No había respaldo real. Todo el valor dependía de la confianza en que el mecanismo funcionaría.
- El 20% APY era insostenible y provenía principalmente de inversión de capital de riesgo (Terraform Labs).

El colapso (9-13 mayo 2022):

- Grandes ventas de UST desestabilizaron el precio a 0.98 USD.
- El mecanismo de arbitraje empezó a acuñar LUNA masivamente para restaurar la paridad.
- Esto diluyó el valor de LUNA, creando una espiral de muerte.
- En 3 días, LUNA pasó de 80 USD a 0.00001 USD. UST colapsó a 0.10 USD.
- El supply de LUNA pasó de millones a trillones de tokens (hiperinflación).

Resultado: 40.000 millones de dólares evaporados. Miles de inversores perdieron ahorros de vida. Do Kwon, el fundador, fue buscado internacionalmente y arrestado en Montenegro en 2023. Enfrenta cargos de fraude en Corea del Sur y Estados Unidos.

Lección: Las stablecoins algorítmicas sin respaldo real son extremadamente frágiles. La confianza puede colapsar instantáneamente, creando espirales de muerte. No confíes en APYs insostenibles.

## FTX / Alameda Research (Noviembre 2022)

El colapso del segundo exchange centralizado más grande del mundo.

Contexto: FTX era un exchange cripto fundado por Sam Bankman-Fried (SBF), valorado en 32.000 millones de dólares. SBF era considerado el "niño prodigio" de cripto, con conexiones políticas y respaldo de grandes fondos.

El fraude:

- FTX usaba fondos de clientes (que deberían estar segregados) para financiar operaciones de trading de Alameda Research, la firma de trading propiedad de SBF.
- Alameda tenía una línea de crédito ilimitada en FTX, permitiéndole retirar fondos de clientes sin restricciones.
- Parte de las reservas de FTX estaban en FTT, el token nativo del exchange (conflicto de interés circular).
- Alameda usó dinero de clientes para inversiones de riesgo, préstamos a ejecutivos y compras de propiedades.

El colapso:

- CoinDesk publicó el balance de Alameda mostrando dependencia excesiva del token FTT (noviembre 2022).
- Binance anunció que vendería sus holdings de FTT, causando pánico.
- Inicio de bank run: los clientes intentaron retirar fondos masivamente.
- FTX congeló retiros al descubrir un "agujero" de 8.000 millones de dólares.
- Declararon bancarrota días después.

Resultado: 8.000 millones de dólares en fondos de clientes desaparecidos. SBF arrestado en Bahamas, extraditado a EEUU y condenado a 25 años de prisión por fraude, conspiración y lavado de dinero (2024). Colapso total del ecosistema FTX/Alameda.

Impacto: Destruyó la confianza en exchanges centralizados. Reforzó la importancia de "not your keys, not your coins" y la necesidad de pruebas de reservas auditadas.

Lección: Nunca confíes ciegamente en exchanges centralizados, sin importar quién los respalde. La falta de transparencia y auditorías independientes es una bandera roja.

## Celsius Network (2022)

Plataforma de préstamos cripto que colapsó.

Contexto: Celsius ofrecía hasta 18% APY por depositar criptomonedas, usando los fondos para préstamos y trading.

El problema:

- Gestión de riesgo terrible: invertían en proyectos de alto riesgo sin cobertura adecuada.
- No tenían liquidez suficiente para honrar retiros en momentos de estrés.
- El modelo de negocio dependía de mercados alcistas continuos.

Colapso: Junio 2022, congelaron retiros citando "condiciones extremas de mercado". Declararon bancarrota en julio. 4.700 millones de dólares en deuda.

Resultado: El CEO Alex Mashinsky renunció y enfrenta cargos de fraude. Usuarios perdieron acceso a sus fondos.

Lección: Alto rendimiento = alto riesgo. Las plataformas CeFi (finanzas centralizadas) pueden colapsar como bancos tradicionales, pero sin seguro de depósitos.

## Patrones Comunes

Todas estas estafas comparten características:

1. Promesas de retornos extraordinarios sin riesgo aparente
2. Falta de transparencia en el funcionamiento real
3. Incentivos para reclutar nuevos inversores
4. Imposibilidad de auditar reservas o código
5. Figuras carismáticas que generan confianza irracional
6. Presión social y FOMO (fear of missing out)

## Cómo Protegerse

- Desconfía de retornos garantizados superiores al 10-15% anual.
- Verifica que el código sea open source y auditado.
- Confirma que puedes retirar fondos libremente en cualquier momento.
- No confíes en proyectos que dependen exclusivamente de reclutamiento.
- Investiga al equipo: ¿Son anónimos? ¿Tienen historial verificable?
- Si suena demasiado bueno para ser verdad, probablemente lo sea.
- Nunca inviertas más de lo que puedes permitirte perder.

---
