# El ciclo de vida de un token

Un token no nace cuando aparece en tu wallet. Para entonces ya ha vivido media vida: alguien decidió cuántos habría, quién se llevaría los primeros, durante cuánto tiempo estarían bloqueados y qué se podría hacer con ellos. Cuando tú lo compras, estás entrando en una película que empezó hace tiempo, y para entender por qué sube, por qué se hunde o por qué un día simplemente deja de importar, hay que verla desde el principio.

Eso es lo que vamos a hacer aquí. Seguir a un token a lo largo de toda su vida, fase por fase, desde que es solo una idea en un documento hasta que muere. Y verás que cada etapa condiciona la siguiente: cómo se reparte al principio decide quién manda después; cómo se emite decide si sobrevive a su propia inflación; cómo promete devolver valor decide si alguien querrá tenerlo dentro de cinco años.

No hace falta que seas experto. Sí ayuda que te suenen las piezas básicas de DeFi —wallets, contratos, *pools* de liquidez— porque a partir de ahí construimos. Cada palabra nueva la explico cuando aparece, con un ejemplo, y la dejo enlazada por si quieres tirar del hilo.

## Antes de existir: el diseño

Todo token empieza siendo un documento. Se llama [tokenómica](https://academy.binance.com/es/articles/what-is-tokenomics-and-why-does-it-matter), y es donde el equipo decide las reglas del juego antes de que haya un solo jugador: cuántas unidades existirán, cómo se crean, qué se puede hacer con ellas y quién se lleva las primeras.

Parece papeleo. No lo es. Algunas de estas decisiones son imposibles de deshacer, y casi todas las demás marcan la trayectoria durante años.

Lo primero que se decide es **cuántos tokens habrá**. Y aquí hay tres números que la gente confunde todo el rato, así que vamos despacio.

El *suministro máximo* es el techo: cuántas unidades pueden llegar a existir como mucho. Bitcoin tiene un techo de veintiún millones grabado en el código; nadie puede crear el número 21.000.001. Otros tokens no tienen techo y pueden crecer para siempre.

El *suministro total* es cuántos se han creado ya, estén donde estén, incluidos los que están guardados y nadie puede vender todavía.

El *suministro circulante* es solo la parte suelta, la que de verdad está en el mercado y alguien puede vender hoy.

La distancia entre el circulante y el total es la clave de casi todo lo que viene después. Imagina un token donde solo el 10% está suelto y el 90% está guardado esperando salir. El precio de hoy lo fija ese 10%, pero ese 90% existe y un día llegará. Es oferta futura ya comprometida, y se le llama *overhang*: una sombra colgando sobre el precio.

Esa diferencia se ve en dos cifras que tampoco son lo mismo. La *capitalización de mercado* es el precio por el suministro circulante: cuánto vale lo que de verdad circula. La [valoración totalmente diluida](https://www.coingecko.com/learn/fully-diluted-valuation-crypto) o FDV es el precio por el suministro total: cuánto valdría todo si ya estuviera suelto. Cuando la FDV es diez veces la capitalización, te están avisando de algo: hay diez veces más tokens esperando a salir de los que circulan ahora. Un token puede parecer barato y ser carísimo a la vez, según qué número mires.

Decidido cuántos, se decide **cómo cambia ese número con el tiempo**. Un token puede tener suministro *fijo*, como Bitcoin, donde la escasez está garantizada pero el protocolo tiene que buscarse la vida para premiar a sus participantes sin imprimir más. O puede ser *variable*, y entonces puede ir hacia arriba —*inflacionario*, se crean unidades nuevas, lo que en inglés se dice *mint*— o hacia abajo —*deflacionario*, se destruyen unidades, lo que se llama *burn*, quemar—.

La inflación tiene una ventaja y un peligro. La ventaja: te da tokens nuevos con los que pagar a la gente cuando todavía no ganas dinero. El peligro: cada token nuevo *diluye* a los que ya existen, igual que imprimir billetes le quita valor a los que tienes en el bolsillo.

Hay incluso tokens donde el saldo de tu wallet cambia solo, sin que tú hagas nada: los [tokens *rebase*](https://academy.binance.com/en/articles/what-are-rebase-tokens). Si el precio sube, amanecen más tokens en tu cuenta; si baja, desaparecen. Son una rareza, pero conviene saber que existen para no asustarte si un día ves que tu saldo se ha movido solo.

La tercera gran decisión es **para qué sirve el token**. Porque un token sin uso es solo un número en un contrato. Lo que le da sentido es lo que el protocolo te deja hacer con él, y hay cinco usos típicos.

Puede ser una *llave*: sin él no entras a cierta función o cierto servicio. Puede ser un *voto*: con él decides el rumbo del protocolo. Puede ser un *derecho a cobrar*: te da una parte de lo que el protocolo factura. Puede ser un *aval*: lo depositas como garantía para pedir prestado. Y puede ser una *semilla*: lo bloqueas y genera más tokens.

Aquí hay una pregunta que te ahorra muchos disgustos. ¿El uso es real o es circular? Hay tokens cuyo único uso es que, si los bloqueas, te dan más del mismo token. Eso no es utilidad: es un sistema de reparto que solo funciona mientras siga entrando gente nueva. Es, básicamente, la mecánica de un esquema Ponzi con una interfaz bonita. Saber distinguir las dos cosas es saber distinguir un protocolo de una estafa elegante.

Y la última decisión del diseño, la más difícil de deshacer, es **quién se lleva los primeros tokens**. A eso lo vemos ahora con calma, porque de ahí sale casi todo el poder que se reparte después.

## El reparto: quién se lleva los primeros tokens

Antes de que exista mercado, alguien hace una tarta y la corta. Ese reparto —en inglés, *allocation*— decide quién arranca con qué, y como verás más adelante, decide también quién mandará en el protocolo durante años.

Las porciones suelen ser parecidas en casi todos los proyectos. Una parte para el *equipo* fundador y los primeros empleados. Una parte para los *inversores* que pusieron dinero pronto, en las rondas llamadas *semilla* y *privada*, normalmente con un buen descuento por llegar antes que nadie. Una parte para el *ecosistema*, una bolsa para repartir entre desarrolladores y proyectos que construyan encima. Una parte para la *tesorería*, el cofre común que en teoría gestiona la comunidad. Y una parte para el *público*, los que compran cuando el token ya está a la venta para todos.

¿Cuánto se llevan equipo e inversores juntos? Históricamente, entre un 20% y un 40% del total en los proyectos de 2020 a 2024. Cuando ves a un equipo quedándose con el 40% antes de que exista nada, ya sabes algo importante sobre quién va a tener la sartén por el mango.

Hay una forma muy de moda de repartir parte de la tarta: el [*airdrop*](https://academy.binance.com/es/articles/what-is-a-crypto-airdrop), regalar tokens a quien ya usaba el protocolo. El caso famoso es Uniswap en 2020: a todo el que había usado el intercambio le cayeron 400 tokens UNI del cielo, que llegaron a valer miles de dólares. La idea es premiar a los usuarios de verdad y repartir el poder entre mucha gente.

Pero los airdrops crearon su propio monstruo. Cuando se corrió la voz de que usar un protocolo nuevo podía traer un regalo futuro, apareció el *granjeo de airdrops*: gente usando protocolos no porque le interesen, sino para cobrar el premio. Y de ahí al *ataque sybil*: una sola persona creando cientos de wallets para hacerse pasar por cientos de usuarios y multiplicar su regalo. Hoy media industria se dedica a intentar distinguir al usuario real del granjero disfrazado.

Pero el porcentaje que se lleva cada uno no es lo más importante. Lo más importante es **cuándo puede venderlo**. Y aquí entra la palabra que más te conviene entender de toda esta fase: el *vesting*.

[Vesting](https://www.coingecko.com/learn/what-is-crypto-vesting) significa que los tokens que te asignan no te los dan de golpe, sino poco a poco a lo largo del tiempo. Viene del mundo de las empresas: si a un fundador le das todas sus acciones el primer día, ¿qué le impide marcharse al día siguiente? El vesting lo ata. Solo cobra del todo si se queda y cumple.

En cripto el vesting hace lo mismo, pero tiene un efecto extra que en las empresas normales no existe: pega directo al precio. En una empresa privada las acciones del fundador no cotizan en ningún sitio, así que da igual cuándo las reciba. En cripto el token cotiza desde el primer día, así que cada vez que a alguien se le liberan tokens, esa persona puede venderlos esa misma tarde. El vesting deja de ser solo una correa para el equipo y se convierte en un calendario de futura oferta cayendo sobre el mercado.

El vesting viene en dos sabores, y la diferencia importa mucho.

El *vesting lineal* suelta un poquito cada día, de forma constante. Como un grifo abierto a poco caudal: la oferta nueva gotea, suave y previsible.

El *cliff* —que en inglés es "acantilado"— es lo contrario: un periodo en el que no sueltas absolutamente nada, y al final, de golpe, cae todo lo acumulado. Un cliff de un año significa que durante doce meses esa persona no toca ni un token, y en el mes trece le caen de golpe los doce meses juntos.

¿Ves el problema? El día del cliff, una montaña de tokens aterriza a la vez en manos que pueden venderlos. A eso se le llama un *choque de oferta*, y el mercado tiene que tragárselo de una sentada. Lo bueno es que estas fechas no son secretas: están escritas en la blockchain y cualquiera puede consultarlas en webs como [Token Unlocks](https://token.unlocks.app/). El mercado las vigila con lupa, y más adelante veremos la curiosa danza que se monta alrededor de ellas.

Junta las dos cosas —cuánto tiene cada uno y cuándo puede venderlo— y entiendes los incentivos de verdad. Un equipo con el 20% bloqueado cuatro años está obligado a remar: sus tokens no valen nada si el barco se hunde antes. El mismo 20% sin bloqueo ninguno es una bomba: pueden vender desde el primer día y largarse. Mismo porcentaje, comportamiento opuesto.

## El nacimiento: el día que sale al mercado

Llega el momento. El token se crea y empieza a cotizar. Ese instante tiene nombre: el *TGE*, las siglas en inglés de "evento de generación del token". Es el parto. Antes era una promesa; ahora tiene precio.

Hay varias formas de hacerlo público. En una *venta pública* o *IDO* el equipo vende tokens directamente a quien quiera comprarlos. En un *fair launch*, o lanzamiento justo, no hay venta privada previa ni descuentos para nadie: todos entran en igualdad de condiciones, como hizo Bitcoin en su día. Hay incluso mecanismos pensados para que el precio se descubra solo, sin que el equipo lo fije a dedo.

Y aquí pasa algo que conviene tener muy presente, porque ha sido la trampa de los últimos años. Recuerda los tres números del suministro: cuando un token nace, casi siempre circula muy poco —el resto está bloqueado en vesting—. Eso produce el patrón del *low float, high FDV*: poco suministro suelto, pero una valoración total enorme.

Te lo traduzco. Sale un token, circula el 5%, y con ese poco suelto el precio se dispara porque hay poca oferta. La FDV marca cifras de fantasía, diez mil millones de dólares. Todo el mundo eufórico. Pero detrás hay un 95% bloqueado que irá saliendo mes a mes durante años, presionando el precio hacia abajo sin descanso. Muchos tokens que nacieron por todo lo alto en 2024 no pararon de bajar después, no porque el proyecto fuera malo, sino porque nacieron caros y con una avalancha de oferta programada encima.

## La infancia: pagar con tokens que todavía no valen nada

Un protocolo recién nacido se enfrenta a un problema incómodo. Necesita liquidez —dinero aparcado en sus *pools* para que la gente pueda comprar y vender sin que el precio dé saltos—, pero todavía no genera ingresos con los que pagar a quien aporte ese dinero. ¿Cómo atraes capital cuando no tienes con qué remunerarlo?

La respuesta que inventó DeFi en 2020 fue tan ingeniosa como peligrosa: pagar con tokens recién impresos. Es lo que se llama [*liquidity mining*](https://academy.binance.com/es/articles/what-is-liquidity-mining), y funciona así. Tú depositas, pongamos, mil dólares en un *pool*, y el protocolo te entrega cada día un puñado de tokens nuevos como recompensa, además de la parte que te toca de las comisiones. Ese token extra dispara el rendimiento —el famoso [*yield*](https://www.coingecko.com/learn/what-is-yield-farming-in-defi)— muy por encima de lo que pagaría cualquier banco.

Funcionó. El dinero llegó a raudales, y el indicador que mide cuánto capital hay depositado, el [TVL](https://www.coingecko.com/learn/total-value-locked-tvl), se disparó en semanas en los protocolos que mejor pagaban.

Pero había una trampa en el *tipo* de dinero que llegaba. Buena parte era *capital mercenario*: liquidez sin ninguna lealtad al protocolo, que solo está ahí por la recompensa. Llegó por el *yield* y se irá por el *yield*, en cuanto otro proyecto pague más.

Y aquí empieza lo que de verdad hay que entender, porque es lo que mata protocolos. Vamos despacio.

Imagina que el protocolo emite cien tokens nuevos cada día para repartir entre quienes aportan liquidez. Esos cien tokens caen en manos de gente que, en su mayoría, no quiere el token: quiere el dólar. Así que lo vende. Todos los días.

Eso es presión vendedora constante. Si no hay suficiente gente comprando al otro lado para absorberla, el precio baja. Hasta aquí, nada raro.

Lo grave es lo que viene después. Si el precio baja, esos cien tokens diarios valen menos dólares, así que el *yield* cae. Y si el *yield* cae, el capital mercenario —que solo estaba por eso— empieza a marcharse.

¿Qué hace entonces un protocolo asustado de perder su liquidez? Emitir más tokens para volver a subir la recompensa. Pero más emisión es más oferta vendiéndose cada día, lo que hunde más el precio, lo que baja más el *yield*, lo que espanta más capital. El remedio es el veneno.

A esto se le llama una espiral [reflexiva](https://www.investopedia.com/terms/r/reflexivity.asp): el precio no se limita a reflejar la situación, la empeora, y esa situación empeorada vuelve a tirar del precio hacia abajo. Es el mismo motor que, llevado al extremo, hizo desaparecer a LUNA en unos días —pero eso lo veremos al final, cuando el token muere.

¿Y cómo se escapa de la espiral? Los protocolos que sobrevivieron a varios ciclos aprendieron a apagar el grifo poco a poco, con lo que se llama una *curva de emisión decreciente*: recompensas altas al principio, cuando hay que arrancar como sea, y cada vez más bajas a medida que el protocolo crece y empieza a tener ingresos reales con los que sustituir el subsidio. [Curve](https://curve.fi/) fue el ejemplo canónico: la emisión de su token, CRV, baja cada año siguiendo una curva fijada de antemano, de modo que nadie se lleva una sorpresa.

Hubo quien intentó resolver el problema del capital mercenario de otra forma: en vez de alquilar liquidez para siempre, comprarla. Es la idea de la *liquidez propiedad del protocolo*. El proyecto más famoso, [OlympusDAO](https://www.olympusdao.finance/), lo hizo con un mecanismo llamado *bonding*: te cambiaba tus tokens de liquidez por tokens suyos con descuento, de modo que la liquidez pasaba a ser del protocolo y no se podía marchar. La idea era brillante sobre el papel; en la práctica su modelo acabó colapsando, pero dejó una lección que muchos protocolos copiaron: la liquidez alquilada se va, la liquidez propia se queda.

Hay otro enemigo silencioso en esta fase, más sutil: la *velocidad*. Si todo el mundo recibe el token y lo vende inmediatamente, el token pasa por las manos de la gente sin que nadie lo retenga. Y un token que nadie quiere guardar no acumula valor, por mucho que se use el protocolo. Por eso tantos diseños buscan razones para que lo retengas en lugar de venderlo —y la más potente de todas es la que viene en la siguiente fase.

Una de esas razones para no vender es el *staking*: [bloquear el token](https://academy.binance.com/es/articles/what-is-staking) a cambio de una recompensa o de un derecho. Mientras está en *staking*, no se vende, así que alivia un poco la presión. Con el tiempo apareció incluso el *staking líquido*, que te da un recibo negociable por los tokens que tienes bloqueados, para que no pierdas del todo el acceso a tu dinero mientras lo tienes aparcado.

## La madurez: cuando el uso se convierte en dinero

Si el protocolo sobrevive a su infancia, llega el momento de la verdad. La pregunta que decide si un token vale algo de verdad es esta: ¿cómo se convierte el uso del protocolo en dinero para quien tiene el token? No en ilusión de que el precio suba. En dinero contante.

Hay cuatro respuestas, y un token bueno suele combinar varias. Un token malo no tiene ninguna y solo vive de la esperanza.

La primera y más limpia es **cobrar una parte de lo que el protocolo factura**. Un intercambio cobra una comisión por cada operación; un protocolo de préstamos se queda con la diferencia entre lo que paga al que deposita y lo que cobra al que pide prestado. Ese dinero puede repartirse entre quienes tienen el token. A esto se le llama *rendimiento real* —*real yield*—, y la palabra "real" es importante: es dinero de verdad que entra, no tokens nuevos impresos. Es el equivalente al dividendo de una empresa.

El interruptor que enciende ese reparto tiene nombre propio: el *fee switch*. Y que esté encendido o apagado es una decisión enorme. Uniswap, el mayor intercambio de DeFi, pasó años facturando miles de millones con el *fee switch* apagado: las comisiones iban a los proveedores de liquidez, no a los que tenían el token UNI. Tener el token no te daba ni un céntimo de lo que el protocolo ganaba. Cuándo y cómo encender ese interruptor fue uno de los grandes debates de su gobernanza.

Cuidado con un truco aquí. Si el "dividendo" te lo pagan en el propio token del protocolo, y esos tokens son recién impresos, no te están dando valor: te están dando inflación con lazo de regalo. El rendimiento de verdad es el que te llega en algo externo, como [stablecoins](https://www.coingecko.com/learn/what-are-stablecoins). La pregunta de control es siempre: ¿esto que cobro viene de dinero de fuera, o es el propio token reciclado?

La segunda respuesta es la **recompra y quema** —*buyback and burn*—. El protocolo usa parte de lo que gana para comprar su propio token en el mercado y destruirlo. Al haber menos tokens repartiéndose el mismo valor, cada uno que queda vale más. El ejemplo más conocido es [BNB](https://academy.binance.com/es/articles/what-is-bnb), que lleva años quemando tokens cada trimestre. Es elegante porque manda un mensaje simple: "prefiero devolveros valor reduciendo la oferta que repartiendo caja".

Pero tiene su trampa, igual que el dividendo. La recompra solo es sana si se paga con lo que el protocolo gana. Si se paga vaciando el cofre de la tesorería, el protocolo está gastando sus ahorros para sostener el precio artificialmente. Otra vez la misma pregunta: ¿esto sale de los ingresos o de las reservas?

La tercera respuesta es el **poder de decisión** —la gobernanza—, que es tan importante que tiene su propia fase justo después. Quédate con la idea: en un protocolo que mueve mucho dinero, decidir cómo se reparte ese dinero vale dinero.

Y la cuarta es la más sencilla y honesta: el **acceso**. Algunos tokens son simplemente llaves. Valen exactamente lo que vale aquello que abren, sin necesidad de cuentas raras ni promesas de futuro.

## El poder: la gobernanza y dónde se concentra de verdad

Aquí está la parte que no sale en los gráficos de precio pero que decide el destino del protocolo más que ninguna otra: quién manda de verdad.

La promesa de un *token de gobernanza* es bonita. Tienes tokens, votas; cuantos más tienes, más pesa tu voto; entre todos decidís el rumbo. Hay votaciones que se ejecutan solas en la blockchain en cuanto se aprueban —gobernanza *on-chain*— y otras que solo sirven para opinar y luego un equipo las ejecuta a mano —*off-chain*—. Hay un mínimo de votos que deben participar para que valga, el *quórum*. Y puedes ceder tu voto a alguien que vote por ti, lo que se llama *delegación*.

Bonito en teoría. Veamos qué pasa en la práctica, porque es más interesante.

El diseño de gobernanza más influyente de DeFi es uno que conecta de golpe cuatro cosas que hasta ahora hemos visto sueltas. Se llama [*ve-tokenomics*](https://curve.readthedocs.io/dao-vecrv.html), lo inventó Curve, y lo copió media industria. Vale la pena entenderlo porque es un mecanismo precioso, en el sentido de máquina bien engranada.

Funciona así. Para tener voto, no basta con tener el token: hay que *bloquearlo*, hasta cuatro años. Y cuanto más tiempo lo bloqueas, más poder de voto recibes —quien lo bloquea cuatro años manda cuatro veces más que quien lo bloquea uno—.

Mira lo que acaba de pasar con esa sola regla. Primero, has sacado un montón de tokens del mercado: bloqueados no se pueden vender, así que la presión de venta de la infancia baja. Segundo, has premiado a los que apuestan a largo plazo y has callado a los que solo querían entrar y salir.

Pero hay más. Esos votos no deciden cosas abstractas: deciden *hacia qué pools va la emisión de tokens nuevos*. Votar es, literalmente, decidir hacia dónde fluye el dinero recién impreso. Y en cuanto votar mueve dinero, aparece gente dispuesta a pagar por esos votos.

Así nació el *mercado de sobornos* —lo llaman así sin rubor, *bribe markets*—. En plataformas como [Votium](https://votium.app/) o [Hidden Hand](https://hiddenhand.finance/), un protocolo paga a los que tienen votos para que dirijan la emisión hacia su *pool*. No es ilegal: es transparente y voluntario. Pero es exactamente lo que cabía esperar al juntar poder de voto con dinero. Quien más gana con un resultado, paga por los votos que se lo dan.

La cosa se puso tan competitiva que se montó una guerra. Las llamadas *Curve wars*: protocolos peleándose por acumular el máximo de votos de Curve para dirigir la emisión hacia su lado. Apareció hasta un intermediario, Convex, dedicado a acumular votos de los demás para revenderlos. Una capa de poder por encima de otra capa de poder.

Y ahora la parte incómoda. En casi todos los protocolos importantes, el poder no está repartido: está concentrado. En unas pocas wallets —el equipo, los fondos que entraron pronto, los grandes delegados— suficientes para aprobar o tumbar cualquier propuesta. ¿Y de dónde viene esa concentración? De la asignación inicial, aquella tarta que se cortó al principio. El reparto de hace tres años es quien gobierna hoy. Por eso te decía que era la decisión más difícil de deshacer.

Lo agrava un detalle deprimente: casi nadie vota. En protocolos maduros, la participación suele estar entre el 5% y el 15% de los tokens, y eso en los buenos. El resto no vota porque es complicado, porque su voto no cambia nada o porque ni sigue el tema. Y la apatía no es neutral: si la mayoría no vota, el poder real se concentra todavía más en los pocos que sí lo hacen. Y los pocos que se molestan en votar suelen ser, justamente, los que tienen mucho dinero en juego.

A veces la concentración se vuelve un arma. Han existido *ataques de gobernanza* donde alguien pide prestada una montaña enorme de tokens por unos minutos —con un *flash loan*—, vota con ellos para aprobar una propuesta que le permite robar el fondo, y los devuelve. Le pasó a un protocolo llamado Beanstalk, al que vaciaron la tesorería así en una sola transacción. La gobernanza descentralizada también tiene sus agujeros.

## Los desbloqueos: el calendario que el mercado ya conoce

Volvamos a aquellas fechas de vesting que dijimos que el mercado vigilaba con lupa. Ahora toca ver la danza que se monta alrededor, porque es más astuta que un simple "sale oferta, baja el precio".

Como las fechas son públicas, el mercado no espera al día del desbloqueo: se adelanta. Semanas antes de que una montaña de tokens se libere, los que están atentos empiezan a vender, anticipando que otros venderán en la fecha. Esa expectativa hace que el precio caiga *antes* de que pase nada. Es una profecía que se cumple sola: baja porque todos creen que va a bajar.

Y aquí el giro que casi nadie espera. Si la gente ya se asustó y vendió por adelantado, cuando por fin llega el día del desbloqueo puede que la presión ya esté descontada... y el precio rebote. El miedo vendió antes de tiempo y dejó el camino despejado.

No todos los desbloqueos pesan igual, y la diferencia no está en el tamaño. Está en dos cosas.

Una es la *profundidad del mercado*: cuántos compradores hay esperando. Un desbloqueo grande en un token con muchísimo movimiento se absorbe sin despeinarse. El mismo desbloqueo en un token pequeño, con pocos compradores, hunde el precio, porque no hay suficiente gente al otro lado para comprar todo lo que se vende —y el precio se desliza, lo que se llama *slippage*—.

La otra es *a quién le llegan* esos tokens. No es lo mismo que caigan en manos de un fondo que tiene que rendir cuentas a sus inversores y necesita vender en fechas concretas, que en manos de alguien del equipo que lleva años apostando por esto y puede esperar tranquilo. Dos desbloqueos idénticos pueden tener efectos opuestos según en qué bolsillo aterricen.

## La muerte: el zombie, la mudanza y el colapso

Los tokens también mueren, y casi nunca con un anuncio. Hay tres formas de morir.

La primera es apagarse poco a poco. El protocolo deja de importar, el volumen cae a casi nada, el equipo se va, y el token sigue cotizando a un precio ridículo, sostenido solo por gente que no se molesta en vender o que espera un milagro que no llega. Se les llama *tokens zombie*: técnicamente vivos, en realidad muertos.

La segunda, y la más común, es la mudanza. El protocolo madura, lanza una versión nueva, y a veces eso obliga a cambiar de token —un *token swap*, cambiar los viejos por los nuevos—. Cuando se hace mal, la liquidez se parte en dos y los usuarios se lían. Cuando se hace bien, apenas se nota. [Uniswap](https://uniswap.org/) cambió de versión tres veces sin tocar su token: UNI sigue siendo el mismo. [MakerDAO](https://makerdao.com/) hizo lo contrario y renació entero con otro nombre, Sky, ofreciendo a sus usuarios cambiar sus tokens viejos por los nuevos, dejando los antiguos convivir sin prisa.

La mudanza enseña algo profundo: la identidad de un token no está en su nombre ni en su contrato, sino en la comunidad que lo sostiene y en la confianza de que el protocolo seguirá siendo lo que dice ser. Cuando esa confianza se rompe —por un hackeo, por un giro brusco, por la sensación de que el equipo está sacando tajada en vez de construir—, el token puede seguir cotizando meses, pero el protocolo ya ha muerto en lo que importa.

Y la tercera muerte es la espectacular: el colapso. La forma extrema se llama *espiral de la muerte*, y es exactamente la misma espiral reflexiva que vimos en la infancia, pero a toda velocidad y sin frenos. El caso que hay que conocer es [Terra y LUNA](https://www.coindesk.com/learn/the-fall-of-terra-a-timeline-of-the-meteoric-rise-and-crash-of-ust-and-luna/), en mayo de 2022, porque enseña cómo un diseño puede llevar dentro su propia bomba.

Sigámoslo despacio, que vale la pena. Terra tenía una stablecoin llamada UST, una moneda que debía valer siempre un dólar. Pero no estaba respaldada por dólares de verdad guardados en ningún sitio. Se sostenía con un truco: el protocolo prometía que siempre podrías quemar un dólar de su otro token, LUNA, para crear un UST, y al revés, quemar un UST para crear un dólar de LUNA. Mientras todo el mundo se lo creyera, el truco mantenía el dólar.

Y se lo creyeron, sobre todo porque un sitio pagaba un 20% por guardar UST, lo cual atraía dinero a montones.

Entonces, un mal día, la confianza tembló y UST empezó a valer menos de un dólar. Y el truco que lo sostenía se convirtió en su verdugo. La gente corría a quemar sus UST para sacar un dólar de LUNA —y al hacerlo, se creaban LUNA nuevos a chorro—. En cuestión de días, el número de LUNA pasó de unos pocos millones a cientos de miles de millones. Cada LUNA nuevo hundía el precio, lo que daba más miedo, lo que hacía correr a más gente a quemar UST, lo que creaba más LUNA todavía.

El mismo mecanismo que mantenía el sistema en pie lo desintegró cuando el flujo se dio la vuelta. La reflexividad, que en la infancia es un riesgo que se puede gestionar, en un diseño mal pensado es una bomba con la mecha encendida desde el primer día. El ciclo de vida de LUNA es el más corto que se puede imaginar, porque su final estaba escrito en su propio diseño.

## Lo que un token es, en realidad

Hemos seguido al token de principio a fin. Ahora podemos decir lo que es sin pedir prestadas palabras de otro sitio.

No es una acción, aunque dé voto y a veces reparta beneficios. No es una moneda, aunque sirva para pagar. No es un bono, aunque a veces pague intereses. Es las tres cosas y ninguna del todo, porque añade algo que ninguna tiene: sus reglas están escritas en código público, se ejecutan solas y cualquiera puede comprobarlas.

Lo que mejor lo define es esto: un token es una **promesa codificada**. La promesa de un protocolo sobre cómo se va a portar con quienes lo sostienen —cuánto va a emitir, cuándo, a quién y a cambio de qué—, escrita en un lenguaje que se cumple solo.

Y por eso cada fase de este recorrido era, en el fondo, una cláusula de esa promesa. El diseño promete una escasez y un uso. El reparto promete repartir el poder con justicia. El vesting promete que los de dentro reman con los de fuera. La emisión promete retirar el subsidio a tiempo. La madurez promete convertir el uso en dinero de verdad. La gobernanza promete que ese dinero lo deciden los que tienen el token, y no cuatro wallets.

El ciclo de vida de un token no es más que la historia de si esa promesa se cumplió. Un protocolo que sigue dando valor a su gente cinco años después la cumplió, por mucho que cambiara su código. Uno que cambió las reglas a escondidas, que vació la tesorería sin permiso o que dejó salir enteros a los inversores mientras los pequeños comían la caída, no la cumplió, aunque el precio subiera por el camino.

Distinguir unos de otros en tiempo real es difícil, porque el mercado los mezcla a todos en el mismo tablero. Pero ahora tienes el método: mira el diseño, el reparto, el vesting, la emisión, cómo devuelve valor, quién gobierna y qué pasa en los desbloqueos. Esas siete preguntas son la forma más fiable de saber qué promesa tienes delante —antes de que la historia ya esté escrita.
