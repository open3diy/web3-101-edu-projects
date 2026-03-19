# Prácticas de salud en una DAO

> Este documento trata de mantener el equilibrio entre los tres factores que sostienen una DAO: utilidad real del protocolo, incentivos que motivan la participación hoy, y proyección a largo plazo. No describe cómo funcionan los mecanismos financieros —eso está en [gestión de tesorería](treasury-management.md)— ni cómo se estructura la gobernanza formal —eso está en [gobernanza de arquitectura](governance-architecture.md)—. Este documento responde a una pregunta diferente: ¿cómo sabes que algo va mal antes de que sea demasiado tarde para reaccionar?

Una DAO no colapsa de repente. Se deteriora. Los síntomas aparecen semanas o meses antes del colapso visible: la participación en votaciones cae, los contributors clave dejan de aparecer en el foro, las propuestas de gasto se vuelven más frecuentes sin resultados claros, el precio del token cae más que el mercado general. Cada uno de estos síntomas tiene causas específicas y respuestas posibles. El problema es que sin un sistema para observarlos sistemáticamente, los equipos suelen enterarse cuando ya es difícil revertir el daño.

Este documento ofrece tres cosas: un marco de diagnóstico para detectar problemas a tiempo, un cuadro de mandos con las métricas que realmente importan, y un conjunto de prácticas concretas para corregir desequilibrios antes de que se vuelvan crisis.

## Diagnóstico: señales de que algo va mal

El diagnóstico de salud en una DAO requiere observar simultáneamente tres dimensiones que corresponden al trilema de equilibrio: síntomas de pérdida de utilidad real, síntomas de desequilibrio en incentivos, y síntomas de deterioro en la proyección a largo plazo. La mayoría de los problemas aparecen primero en una sola dimensión y se propagan a las otras si no se atienden.

### Pérdida de utilidad real

El protocolo pierde utilidad cuando deja de responder a las necesidades de sus usuarios o cuando sus mecanismos de gobernanza se osifican y dejan de poder actualizarse. Las señales más tempranas son:

El TVL (total value locked) cae sostenidamente durante más de dos períodos consecutivos mientras competidores del mismo segmento crecen o se mantienen estables. Esto indica que los usuarios están eligiendo protocolos alternativos activamente, no simplemente que el mercado general está bajando.

El volumen de uso del protocolo —transacciones, fees generadas, usuarios únicos— cae mientras el precio del token se mantiene artificialmente sostenido por buybacks o staking rewards. Esta disociación entre actividad real y precio sostenido artificialmente es una señal de alerta severa: los incentivos financieros están compensando la falta de valor fundamental.

Las propuestas técnicas de mejora del protocolo tardan meses en llegar a votación formal o se rechazan sistemáticamente por quórum insuficiente. Si la DAO es incapaz de actualizar sus propios parámetros técnicos con fluidez, está congelada en una versión del producto que inevitablemente quedará obsoleta.

Los usuarios reportan problemas recurrentes en foros y redes sociales que no generan propuestas de respuesta en el foro de gobernanza. La desconexión entre feedback de usuarios y proceso de gobernanza es un síntoma de que la capa de gobernanza social está desconectada del producto real.

### Desequilibrio en incentivos

Los incentivos pueden desequilibrarse en dos direcciones opuestas: incentivos demasiado agresivos que atraen capital mercenario sin compromiso real, o incentivos insuficientes que no retienen participantes activos.

Los síntomas de incentivos demasiado agresivos incluyen: APYs de staking que superan significativamente la tasa de retorno del protocolo (los rewards se financian emitiendo tokens, no con ingresos reales); airdrops frecuentes sin criterios claros de mérito que generan bots y farming de airdrops en lugar de usuarios genuinos; propuestas de emisión de nuevos tokens que suman más del diez por ciento anual sobre el supply existente sin justificación clara de ingreso proporcional generado; concentración creciente de tokens en pocas wallets que venden consistentemente justo después de cada airdrop o distribución.

Los síntomas de incentivos insuficientes son los opuestos: caída en el número de tokens en staking durante más de dos períodos consecutivos; reducción del número de delegados activos en sistemas de gobernanza con delegación; foros de gobernanza donde las propuestas no reciben comentarios durante días; y contributors activos que anuncian su retirada citando explícitamente baja compensación o falta de reconocimiento.

El desequilibrio más peligroso no es ninguno de estos dos extremos por separado, sino la combinación de incentivos agresivos en staking con caída en utilidad real. Indica que el protocolo está pagando a la gente para que se quede, no para que use el protocolo. Es insostenible.

### Deterioro en la proyección a largo plazo

La proyección se deteriora cuando los recursos colectivos se erosionan gradualmente sin que nadie tome consciencia del problema, o cuando la capacidad de la DAO para tomar decisiones de largo plazo queda bloqueada.

La señal más clara de erosión financiera es el runway de la tesorería: si al ritmo de gasto actual los fondos se agotan en menos de doce meses y no hay ingresos recurrentes claros que cambien esa tendencia, la DAO enfrenta un problema existencial aunque nadie hable de ello. El porcentaje de tesorería en el token nativo es también indicativo: si más del setenta por ciento de la tesorería está en el propio token, una caída de mercado del cincuenta por ciento destruye también el cincuenta por ciento de la capacidad operativa.

El deterioro en la capacidad de tomar decisiones aparece cuando las propuestas importantes quedan bloqueadas indefinidamente sin votación concluyente, cuando los quórums mínimos no se alcanzan repetidamente, o cuando las mismas propuestas se rechazan y re-presentan en ciclos sin resolución. Esto indica que existe un bloqueo político no resuelto que paraliza la gobernanza.

La concentración creciente de poder en pocos delegados o una sola wallet que controla más del veinticinco por ciento del supply con derechos de voto es una señal de captura progresiva. No tiene que ser maliciosa para ser peligrosa: un holder con buenas intenciones pero criterio diferente a la comunidad puede bloquear decisiones por años.

La pérdida de contributors clave es quizás la más difícil de detectar porque ocurre gradualmente. Cuando en seis meses el equipo activo ha rotado completamente y el conocimiento histórico del protocolo se ha perdido, reconstruirlo es extraordinariamente costoso.

## Cuadro de mandos

Un cuadro de mandos de salud no debe intentar monitorizar todo. Debe concentrarse en los indicadores que cambian antes de que los síntomas sean evidentes y que tienen causalidad clara con la salud del protocolo. La siguiente clasificación separa métricas de producto, de gobernanza, de tesorería y de comunidad, porque los problemas tienden a aparecer primero en una dimensión específica.

### Métricas de producto

Las métricas de producto miden si el protocolo está generando valor real para sus usuarios. Son las más importantes porque sin utilidad real, ningún mecanismo financiero sostiene una DAO indefinidamente.

El TVL es el indicador más directo de confianza del mercado en el protocolo, pero debe analizarse en relación con competidores del mismo segmento, no en términos absolutos. Una caída del veinte por ciento en TVL durante una caída general del mercado del treinta por ciento es señal positiva. La misma caída durante un mercado alcista es una señal de alarma grave.

Las fees generadas por el protocolo son el indicador más honesto de utilidad real porque requieren que alguien use activamente el protocolo y pague por ello. Trazar la tendencia de fees mensuales durante al menos seis meses revela si el protocolo está creciendo, estabilizándose o decayendo con independencia del precio del token.

El número de usuarios únicos activos mensualmente (MAU en terminología Web2, dirección únicas que interactúan con el protocolo) complementa al TVL porque captura uso distribuido: un protocolo con alto TVL concentrado en cinco wallets y bajo número de usuarios es más frágil que uno con TVL similar distribuido en miles.

Herramientas para monitorizar estas métricas: [Dune Analytics](https://dune.com/) permite crear dashboards personalizados consultando directamente datos on-chain; [DefiLlama](https://defillama.com/) ofrece comparativas de TVL entre protocolos con histórico; [Token Terminal](https://tokenterminal.com/) normaliza métricas financieras de protocolos DeFi en formato comparable.

### Métricas de gobernanza

Las métricas de gobernanza miden la salud del proceso de toma de decisiones. Una gobernanza inactiva o bloqueada no puede responder a cambios en el mercado ni corregir problemas que ya se detectaron.

La tasa de participación en votaciones es el indicador más básico. Calculada como porcentaje de tokens en circulación que participan en el promedio de las últimas diez votaciones, da la temperatura real de engagement. Por debajo del cinco por ciento es señal de alerta. Por encima del veinte por ciento es saludable para una DAO madura con gran número de holders.

El tiempo promedio desde que una propuesta se publica en el foro hasta que llega a votación formal mide la fluidez del proceso. Tiempos superiores a treinta días para propuestas técnicas rutinarias indican fricción disfuncional. Tiempos inferiores a cinco días para propuestas importantes indican que el proceso de deliberación no está ocurriendo.

La tasa de aprobación de propuestas es un indicador contraintuitivo: tanto tasas muy altas (más del noventa por ciento de propuestas aprobadas) como muy bajas (menos del treinta por ciento) pueden indicar problemas. La primera puede señalar que solo llegan a votación propuestas pre-acordadas en círculos cerrados, excluyendo participación real. La segunda puede indicar parálisis política.

La concentración de poder de voto, medida como el porcentaje de las últimas veinte votaciones donde el resultado habría cambiado si las cinco wallets más grandes hubieran votado diferente, es el indicador más directo de plutarquía real versus descentralización real.

Herramientas: [Tally](https://www.tally.xyz/) agrega votaciones on-chain de múltiples DAOs con histórico y métricas de participación; [Boardroom](https://boardroom.io/) ofrece dashboards de gobernanza con análisis de delegados y propuestas; [DeepDAO](https://deepdao.io/) proporciona comparativas de salud de gobernanza entre DAOs.

### Métricas de tesorería

Las métricas de tesorería miden la sostenibilidad financiera y la capacidad de la organización de financiar su propia operación.

El runway es la métrica más urgente: a ritmo de gasto mensual promedio de los últimos seis meses, ¿cuántos meses puede operar la DAO con los fondos actuales sin ingresos adicionales? Menos de doce meses requiere acción inmediata. Entre doce y veinticuatro meses requiere atención activa. Más de veinticuatro meses permite planificación estratégica tranquila.

La diversificación de la tesorería se mide como porcentaje de activos en stablecoins o activos de baja volatilidad versus el token nativo. Un ratio inferior al veinte por ciento en stablecoins significa que una caída de mercado del cincuenta por ciento también destruye la mitad de la capacidad operativa.

La relación entre ingresos de protocolo (fees) y gastos operativos (pagos a contributors, infraestructura, grants) determina si la DAO es económicamente sostenible o si está quemando tesorería acumulada. Una DAO que genera el ciento por ciento de sus gastos en fees es completamente autosustentable. Una que genera cero y vive de la tesorería inicial tiene vida útil finita.

Herramientas: [Llama](https://llama.xyz/) y [Parcel](https://parcel.money/) ofrecen dashboards de tesorería en tiempo real con análisis de runway; [Safe](https://safe.global/) proporciona vistas de saldo y transacciones de multisigs de tesorería; [Dune Analytics](https://dune.com/) permite construir dashboards de cashflow on-chain personalizados.

### Métricas de comunidad

Las métricas de comunidad son las más difíciles de cuantificar pero frecuentemente capturan problemas antes de que aparezcan en los datos on-chain.

El número de contribuidores activos únicos —definidos como personas que han publicado al menos un mensaje en el foro de gobernanza o completado al menos un bounty en los últimos treinta días— mide la amplitud real de participación más allá de los grandes holders. Una comunidad saludable tiene crecimiento o estabilidad en esta métrica; una en deterioro muestra declive constante independientemente del número de holders de token.

La diversidad de origen de las propuestas indica si la agenda la controla un círculo cerrado o si existe participación real. Si más del ochenta por ciento de las propuestas que llegan a votación provienen de menos de cinco wallets o entidades, la gobernanza es plutocrática en la práctica aunque sea formalmente abierta.

La retención de contributors medida como porcentaje de contributors activos hace seis meses que siguen activos hoy revela si la DAO es capaz de retener talento. Una rotación superior al cincuenta por ciento en seis meses implica pérdida continua de conocimiento organizacional.

Herramientas: [Karma](https://www.karmahq.xyz/) rastrea actividad de gobernanza de wallets individuales; [Coordinape](https://coordinape.com/) genera datos de contribución entre pares; [Discourse](https://www.discourse.org/) y Discord ofrecen métricas de actividad de sus propias plataformas.

## Mejores prácticas

Las mejores prácticas en salud de una DAO no son reglas absolutas. Son heurísticas desarrolladas a partir de patrones observados en protocolos que sobrevivieron a múltiples ciclos de mercado y en protocolos que colapsaron. Para cada mecanismo —airdrops, reemisión de tokens, staking, buybacks, diversificación de tesorería— hay patrones que tienden a funcionar y patrones que tienden a destruir valor.

### Airdrops: distribuir sin crear mercenarios

El error más común en diseño de airdrops es optimizar para cantidad de wallets alcanzadas en lugar de calidad de destinatarios. Un airdrop que llega a cien mil wallets de las cuales noventa y cinco mil venden en las primeras setenta y dos horas no distribuye gobernanza: genera presión de venta masiva que daña el precio y desmoraliza a los holders a largo plazo.

Los criterios de elegibilidad deben medir compromiso real, no actividad técnica superficial. Haber interactuado con el protocolo al menos tres veces en períodos separados de tiempo demuestra más compromiso que haber hecho una sola transacción de alto valor para calificar. Los criterios basados en antigüedad —llevar más de seis meses usando el protocolo o el ecosistema relacionado— filtran mejor el capital mercenario que criterios basados únicamente en volumen.

El vesting parcial de los tokens del airdrop, donde el destinatario recibe un porcentaje inmediatamente y el resto se libera durante tres a seis meses, reduce la presión de venta inicial sin que sea tan restrictivo que disuada la participación. [Optimism](https://www.optimism.io/) ha iterado su modelo RetroPGF con este aprendizaje: las distribuciones retroactivas a contribuidores verificados, con criterios públicos y auditables, generan mucho menos mercenarios que airdrops basados en uso técnico.

Antes de cada airdrop, simular el impacto en el supply circulante. Si el airdrop añade más del cinco por ciento al supply circulante de golpe, el impacto en precio puede ser severo incluso si los destinatarios no venden masivamente.

### Programas de staking: recompensar permanencia sin inflación insostenible

El diseño incorrecto más frecuente en staking es fijar APYs atractivos sin calcular de dónde vienen esos rendimientos. Si los rewards de staking se financian con emisión de nuevos tokens y no con ingresos reales del protocolo, el APY es ilusorio: estás pagando a los stakers con la dilución de todos los demás holders.

La práctica saludable es que los rewards de staking provengan de fees reales del protocolo o de rendimientos generados por la tesorería. Cuando el protocolo no genera suficientes fees para financiar el APY prometido, la alternativa correcta no es emitir más tokens sino reducir el APY hasta que sea sostenible con ingresos reales.

Los períodos de bloqueo deben tener sentido económico para el participante. Bloqueos de cuatro años como en el modelo veCRV de [Curve](https://curve.fi/) tienen sentido cuando el participante recibe beneficios proporcionales al compromiso: mayor peso de voto, mayor porcentaje de fees. Bloqueos largos con recompensas escasas solo crean fricción sin beneficio.

Revisar los parámetros de staking al menos cada dos períodos de renovación. Si la tasa de participación en staking cae sostenidamente, los parámetros están mal calibrados. Si la tasa sube dramáticamente solo durante épocas de alto APY y cae igual de rápido, estás atrayendo capital oportunista, no holders comprometidos.

### Reemisión de tokens: solo con propósito demostrable

La reemisión de tokens es la decisión financiera con mayor potencial de destruir confianza en una DAO porque altera retroactivamente las expectativas de todos los holders. Debe tratarse con la misma seriedad que una empresa cotizada trataría una ampliación de capital dilutiva.

Las condiciones que justifican una reemisión son restrictivas: financiar desarrollo crítico que no puede cubrirse con la tesorería actual sin comprometer la supervivencia del protocolo, o aprovechar una oportunidad estratégica de crecimiento con retorno demostrable cuyos beneficios superan el costo de dilución. "Necesitamos cash" sin contexto específico no es justificación suficiente.

La transparencia en la comunicación es no negociable. La propuesta debe incluir el impacto exacto de dilución en términos porcentuales sobre el supply total y circulante, el uso específico de los fondos con cronograma y entregables verificables, y la proyección de cómo el gasto generará valor superior a la dilución. Publicar proyecciones optimistas sin rangos de incertidumbre honesta destruye credibilidad cuando los resultados reales divergen.

El límite anual de reemisión debe estar codificado en los estatutos o smart contracts de gobernanza. Una regla práctica es que reemisiones que superen el cinco por ciento anual sobre el supply total requieran supermayoría del sesenta y seis por ciento con quórum extendido. Esto no impide reemisiones necesarias pero sí requiere consenso genuino.

### Diversificación de tesorería: el runway es sagrado

La regla más simple y más frecuentemente ignorada: la tesorería siempre debe mantener suficientes stablecoins para cubrir al menos doce meses de gastos operativos al ritmo actual. No importa cuánto valga el token nativo en ese momento. Esta reserva debe ser intocable excepto en emergencias declaradas formalmente.

El momento de diversificar no es durante el mercado bajista, cuando el token nativo ya ha perdido valor. Es durante el mercado alcista, cuando vender una fracción del token nativo tiene el menor impacto porcentual y la mayor valoración. Las DAOs que implementan ventas programáticas automáticas —convertir un porcentaje fijo mensual de tokens nativos en stablecoins al margen del precio— eliminan la tentación de hacer timing del mercado y garantizan diversificación continua sin fricción de gobernanza.

La diversificación más allá de stablecoins debe someterse a límites de exposición explícitos. Ningún protocolo externo debería recibir más del diez al quince por ciento de la tesorería, por reputado que sea. La historia de DeFi tiene demasiados ejemplos de protocolos con múltiples auditorías que fueron hackeados o colapsaron. La concentración en un solo protocolo externo es riesgo de ruina total para esa porción.

### Buybacks: señal de fortaleza, no de soporte de precio

Los buybacks funcionan cuando son financiados con excedentes reales del protocolo y ejecutados consistentemente en el tiempo. Fallan cuando se usan reactivamente para "defender" un precio que está cayendo por razones fundamentales. Comprar tokens propios cuando el protocolo está perdiendo usuarios y fees solo retrasa la caída a costa de agotar la tesorería.

La disciplina operativa correcta es establecer en los estatutos una regla clara: X porcentaje de las fees mensuales del protocolo se destina automáticamente a buybacks, independientemente del precio del token. Esto convierte los buybacks en consecuencia natural de la actividad del protocolo, no en decisión política reactiva.

Si los buybacks deben suspenderse porque el protocolo no genera suficientes fees, la señal honesta para la comunidad no es suspender los buybacks silenciosamente sino comunicar explícitamente que el protocolo necesita aumentar ingresos. Usar tesorería acumulada para continuar buybacks cuando no hay ingresos reales que los justifiquen es exactamente el tipo de decisión que destruye la tesorería gradualmente sin que nadie hable de ello.

### Revenue sharing: solo cuando el protocolo puede sostenerlo

El error en revenue sharing es activarlo prematuramente, cuando el protocolo todavía necesita retener capital para desarrollo y crecimiento. Distribuir el cincuenta por ciento de fees cuando el runway de la tesorería cubre solo seis meses es una decisión que optimiza para el corto plazo a costa de la supervivencia.

La condición mínima antes de activar revenue sharing es que el runway de la tesorería supere los veinticuatro meses al ritmo de gasto actual, o que los ingresos recurrentes superen los gastos operativos con margen suficiente para continuar creciendo. Cualquiera de las dos condiciones garantiza que la distribución no compromete la capacidad de operación.

Una vez activo, el porcentaje de distribución debe revisarse explícitamente en cada ciclo de presupuesto y ajustarse según la situación financiera real del protocolo. Un fee switch que se activa y nunca se revisa se convierte en obligación fija que limita la flexibilidad financiera en momentos de estrés.

## Revisión periódica del equilibrio

El cuadro de mandos y las mejores prácticas solo tienen valor si existe un proceso formal y recurrente para revisarlos. La práctica más efectiva observada en DAOs que sobreviven múltiples ciclos de mercado es la revisión trimestral de salud: un informe público, preparado por el equipo o working group responsable de operaciones, que presenta el estado actual de todas las métricas con tendencia de los últimos doce meses y una evaluación explícita de los riesgos identificados.

Este informe no reemplaza la transparencia continua on-chain. La complementa con interpretación contextual. Cualquiera puede ver en Dune que el TVL cayó un quince por ciento, pero el informe de salud trimestral explica si eso es preocupante o esperado, qué causas específicas se identificaron, y qué acciones se proponen.

El informe debe generar al menos una propuesta de gobernanza por trimestre si se identifican métricas que requieren ajuste. Una DAO que detecta problemas pero no propone correcciones tiene información sin acción, lo cual es tan peligroso como no tener información.

Los modelos más completos para aprender son [MakerDAO Endgame Health Reports](https://forum.makerdao.com/), los informes periódicos de [Uniswap Foundation](https://www.uniswap.foundation/), y los quarterly reports de [Aave Grants DAO](https://aavegrants.org/). Los tres publican en foros de gobernanza con datos, análisis y propuestas, estableciendo el estándar de transparencia que hace que sus comunidades confíen en la dirección del protocolo incluso en momentos de incertidumbre.

---
