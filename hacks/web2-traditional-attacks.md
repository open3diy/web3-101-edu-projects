# Ataques Tradicionales Web2: Fundamentos de Ciberseguridad

Los ataques en sistemas Web3 y blockchain no existen en el vacío. La mayoría de vectores de ataque tradicionales que han plagado la web durante décadas siguen siendo relevantes y efectivos contra la infraestructura que soporta aplicaciones descentralizadas. Los frontends de DApps son aplicaciones web, los nodos de blockchain corren en servidores, y los usuarios interact

úan mediante navegadores y dispositivos que son susceptibles a los mismos ataques que cualquier otro sistema.

Entender estos ataques tradicionales es fundamental antes de abordar vulnerabilidades específicas de blockchain. Un protocolo DeFi puede tener smart contracts perfectamente auditados, pero si el frontend es vulnerable a XSS o el servidor backend puede ser comprometido mediante SQL injection, todo el sistema está en riesgo. La seguridad es una cadena, y el eslabón más débil determina la fortaleza total.

Este documento explora los vectores de ataque tradicionales más comunes, cómo funcionan, su impacto y las defensas disponibles. Muchos de estos ataques se adaptan y amplifican en el contexto cripto, donde las consecuencias financieras de compromiso son inmediatas e irreversibles.

## Phishing: Ingeniería social y robo de credenciales

El phishing es el vector de ataque más exitoso en toda la historia de la ciberseguridad, responsable de más brechas que todas las vulnerabilidades técnicas combinadas. Se basa en engañar a humanos para que revelen información sensible o ejecuten acciones que comprometen la seguridad. La sofisticación técnica es mínima, pero la efectividad es extraordinaria porque explota psicología humana en lugar de bugs de software.

### Funcionamiento del phishing

El phishing opera creando comunicaciones falsas que parecen provenir de fuentes legítimas y confiables. Un atacante envía correos electrónicos, mensajes o crea sitios web que imitan perfectamente las interfaces de servicios reales: bancos, empresas de tecnología, plataformas de redes sociales o, en el contexto cripto, exchanges y wallets.

El usuario objetivo recibe un mensaje urgente que demanda acción inmediata: verificar tu cuenta para evitar suspensión, confirmar una transacción sospechosa, actualizar información de seguridad o reclamar una recompensa. El mensaje incluye un enlace que lleva a un sitio web falso visualmente idéntico al real. Cuando el usuario introduce credenciales, el atacante las captura y puede acceder a la cuenta real.

La urgencia artificial es clave. Los mensajes de phishing crean presión temporal que inhibe el pensamiento crítico. "Tu cuenta será bloqueada en 24 horas" o "Detectamos actividad sospechosa, verifica inmediatamente" disparan respuestas emocionales que llevan a acciones impulsivas sin verificación cuidadosa.

### Tipos de phishing

El email phishing tradicional envía mensajes masivos a miles o millones de direcciones, esperando que un porcentaje pequeño caiga. La personalización es mínima y los mensajes suelen tener errores ortográficos, gramática pobre o detalles incorrectos que revelan su naturaleza fraudulenta a usuarios atentos.

El spear phishing es dirigido y personalizado. El atacante investiga a objetivos específicos mediante redes sociales, sitios web corporativos y fuentes públicas. Los mensajes incluyen detalles personales que generan confianza: nombres de colegas, proyectos actuales o información sobre la empresa. La tasa de éxito es significativamente mayor porque el mensaje parece legítimo y relevante.

El whaling se dirige a ejecutivos y personas con acceso privilegiado. Los mensajes pueden imitar comunicaciones internas de CEO, departamentos legales o clientes importantes. Comprometer un ejecutivo puede proporcionar acceso a sistemas críticos, información financiera sensible o autoridad para aprobar transacciones grandes.

El smishing usa SMS en lugar de email, aprovechando que los usuarios tienden a confiar más en mensajes de texto. Los vishing attacks usan llamadas telefónicas donde el atacante se hace pasar por soporte técnico, bancos o autoridades, manipulando verbalmente a las víctimas para revelar información o realizar acciones.

El clone phishing duplica emails legítimos que el usuario recibió previamente, reemplazando enlaces o adjuntos con versiones maliciosas. Como el contenido original es familiar, el usuario baja la guardia.

### Phishing en el contexto cripto

En Web3, el phishing es particularmente devastador porque las credenciales no son solo nombres de usuario y contraseñas recuperables. Las frases seed y claves privadas proporcionan acceso permanente e irrevocable a fondos. Si un usuario revela su frase seed de 12 o 24 palabras a un sitio de phishing, el atacante controla la wallet permanentemente. No hay proceso de "restablecer contraseña" o recurso a soporte técnico.

Los sitios de phishing cripto imitan exchanges, wallets y DApps perfectamente. Los atacantes registran dominios casi idénticos: `binance.com` vs `binance.cm`, `metamask.io` vs `metamask.i0`. La diferencia es imperceptible a primera vista, especialmente en móviles donde las URLs se truncan.

Los ataques de firma de transacciones engañan a usuarios para que firmen transacciones maliciosas que parecen legítimas. Una DApp falsa puede solicitar firma de una transacción que aparentemente aprueba un swap, pero en realidad es una autorización de approve que otorga al atacante permiso para gastar todos los tokens del usuario posteriormente.

### Protección contra phishing

La verificación cuidadosa de URLs es fundamental. Usuarios deben revisar manualmente cada carácter del dominio antes de introducir credenciales. Los navegadores modernos marcan sitios no HTTPS como inseguros, pero los atacantes pueden obtener certificados SSL legítimos para dominios fraudulentos, por lo que HTTPS no garantiza legitimidad.

Los gestores de contraseñas ofrecen protección porque solo autorellenan credenciales en dominios exactos guardados. Si visitas un sitio de phishing, el gestor no ofrecerá las credenciales porque el dominio no coincide, alertándote del engaño.

La autenticación de dos factores (2FA) mitiga el impacto si las credenciales son comprometidas. Incluso si el atacante obtiene la contraseña, necesita el segundo factor temporal para acceso. Sin embargo, el phishing sofisticado puede capturar códigos 2FA en tiempo real mediante ataques man-in-the-middle.

Los usuarios deben acceder a sitios críticos mediante favoritos guardados o escribiendo URLs manualmente, nunca mediante enlaces en emails o mensajes. Las organizaciones legítimas raramente solicitan información sensible mediante enlaces en correos.

La educación continua es la defensa más efectiva. Los usuarios entrenados reconocen señales de phishing: urgencia artificial, errores ortográficos, remitentes sospechosos y solicitudes inusuales. Las simulaciones de phishing internas donde organizaciones envían phishing falso y monitorean quién cae permiten entrenamiento práctico.

## Denegación de Servicio: DoS y DDoS

Los ataques de denegación de servicio buscan hacer sistemas o servicios inaccesibles para usuarios legítimos mediante saturación de recursos. A diferencia de otros ataques que roban datos o comprometen sistemas, DoS simplemente interrumpe disponibilidad. El impacto puede ser devastador: sitios web caídos, servicios financieros inoperables, comunicaciones interrumpidas y reputación dañada.

### DoS: Denegación desde fuente única

Un ataque DoS tradicional proviene de una sola máquina atacante que inunda el objetivo con solicitudes hasta agotar recursos. Puede saturar ancho de banda de red, agotar CPU procesando peticiones malformadas o llenar la memoria con conexiones. El servidor dedicado a manejar tráfico malicioso no puede atender usuarios legítimos.

Los ataques DoS simples son relativamente fáciles de mitigar una vez identificados. El administrador puede bloquear la IP atacante mediante firewall, filtrar patrones de tráfico específicos o aumentar temporalmente capacidad del servidor. La naturaleza de fuente única hace la defensa directa.

### DDoS: Ataques distribuidos masivos

Los ataques DDoS distribuyen el ataque desde miles o millones de máquinas simultáneamente. Esta distribución hace la mitigación exponencialmente más difícil porque no hay una sola IP para bloquear. El tráfico proviene de direcciones legítimas comprometidas en todo el mundo, mezclado con tráfico legítimo real, dificultando distinguir atacantes de usuarios.

Las botnets de dispositivos comprometidos ejecutan ataques DDoS coordinados. Los atacantes infectan computadoras, servidores, routers domésticos y dispositivos IoT con malware que los convierte en "zombies" controlables remotamente. El operador de la botnet puede comandar millones de dispositivos para atacar simultáneamente cualquier objetivo.

### Tipos de ataques DDoS

Los ataques volumétricos saturan ancho de banda con tráfico masivo. Floods de UDP, ICMP o HTTP requests consumen toda la capacidad de red, dejando sin espacio para tráfico legítimo. Los ataques pueden alcanzar cientos de gigabits por segundo, suficiente para saturar la infraestructura de red de víctimas grandes.

Los ataques de protocolo explotan debilidades en implementaciones de protocolos de red. SYN floods abusan del handshake TCP abriendo conexiones sin completarlas, agotando la tabla de estados del servidor. Ping of death envía paquetes ICMP malformados que causan crashes en sistemas vulnerables.

Los ataques de capa de aplicación (Layer 7) operan a nivel de aplicación web, ejecutando solicitudes que parecen legítimas pero son computacionalmente costosas. Solicitar páginas que requieren queries complejos de base de datos, generar reportes pesados o procesar búsquedas elaboradas con volumen suficiente agota recursos del servidor incluso con tráfico relativamente bajo.

Los ataques de amplificación abusan de servidores que responden a solicitudes con respuestas mucho más grandes. Un atacante envía requests pequeños con IP origen falsificada (spoofing) apuntando a la víctima. Los servidores envían respuestas masivas a la víctima, amplificando el ataque. DNS, NTP y memcached son vectores comunes de amplificación.

### DDoS en el contexto blockchain

Los nodos de blockchain son objetivos para DDoS. Saturar nodos con peticiones RPC malformadas o solicitudes de datos masivas puede hacer la red más lenta o inaccesible para usuarios legítimos. Los ataques pueden dirigirse a pools de minería, validadores o nodos de infraestructura crítica.

Los frontends de DApps son especialmente vulnerables. Aunque el smart contract puede estar en blockchain descentralizada, si el frontend que los usuarios visitan está caído por DDoS, la aplicación es efectivamente inaccesible para la mayoría. Los atacantes pueden sincronizar DDoS con otros ataques, usando la interrupción como distracción.

### Mitigación de DDoS

Los servicios de protección DDoS como Cloudflare, Akamai y AWS Shield filtran tráfico malicioso antes de que llegue a la infraestructura del objetivo. Operan redes masivas distribuidas globalmente que pueden absorber y filtrar ataques incluso de magnitudes extraordinarias. El tráfico pasa por sus sistemas de filtrado que usan machine learning para distinguir peticiones legítimas de maliciosas.

El rate limiting restringe cuántas solicitudes puede hacer una dirección IP en un periodo. Si una IP excede umbrales razonables, es temporalmente bloqueada. El desafío es configurar límites que bloqueen atacantes sin afectar usuarios legítimos con uso intensivo.

Las arquitecturas de alta disponibilidad distribuyen servicios geográficamente. Si un datacenter es atacado, el tráfico se redirige a otros. La redundancia geográfica dificulta que atacantes impacten disponibilidad global.

El blackholing redirige tráfico malicioso a un "agujero negro" donde se descarta. Cuando un ataque es detectado, las rutas de red se ajustan para que el tráfico del ataque no llegue al objetivo. Esto mitiga el ataque pero también hace el servicio inaccesible temporalmente para todos.

## Malware: Virus, Gusanos, Troyanos y Ransomware

El malware (malicious software) es cualquier software diseñado para dañar, explotar o acceder ilegítimamente a sistemas. Abarca categorías diversas con comportamientos y objetivos distintos. El malware moderno es sofisticado, persistente y difícil de detectar, operando silenciosamente mientras roba datos, instala backdoors o recluta dispositivos a botnets.

### Virus informáticos

Un virus es malware que se replica infectando archivos ejecutables legítimos. Cuando un usuario ejecuta un archivo infectado, el virus se activa, replica su código a otros archivos y ejecuta su payload malicioso. Los virus requieren acción del usuario para propagarse: ejecutar un programa, abrir un archivo adjunto o insertar un USB infectado.

Los virus clásicos operaban modificando archivos binarios, agregando su código al inicio o fin del ejecutable. Versiones modernas son polimórficas, cambiando su firma cada vez que se replican para evadir detección basada en firmas. Los virus metamórficos reescriben completamente su código manteniendo funcionalidad, haciendo cada instancia única.

Los antivirus tradicionales detectan virus mediante firmas: patrones de bytes característicos del virus. Los virus polimórficos y metamórficos evaden esto, requiriendo detección heurística que analiza comportamiento en lugar de código estático. Las soluciones modernas usan sandboxing: ejecutar archivos sospechosos en entornos aislados observando comportamiento antes de permitir ejecución real.

### Gusanos (Worms)

Los gusanos se auto-replican automáticamente sin necesidad de infectar archivos host. Explotan vulnerabilidades de red para propagarse entre sistemas, escaneando rangos de IPs buscando máquinas vulnerables y copiándose automáticamente. Esta propagación autónoma permite que un gusano infecte millones de sistemas en horas.

WannaCry, el ransomware-worm de 2017, explotó la vulnerabilidad EternalBlue en Windows para propagarse lateralmente en redes. Infectó más de 200.000 computadoras en 150 países en días, cifrando datos y demandando rescate en Bitcoin. El impacto global fue masivo: hospitales, empresas, gobiernos y usuarios individuales afectados simultáneamente.

Los gusanos modernos usan múltiples vectores de propagación: vulnerabilidades de red, emails, dispositivos USB y descargas drive-by. La combinación de vectores maximiza alcance y velocidad de infección. Los gusanos pueden llevar payloads adicionales: instalar backdoors, robar credenciales o reclutar sistemas a botnets.

La defensa primaria es parchar vulnerabilidades. Los sistemas actualizados con las últimas correcciones de seguridad son inmunes a gusanos que explotan vulnerabilidades conocidas. La segmentación de red limita propagación: si un gusano infecta una máquina en una subred aislada, no puede propagarse a redes críticas.

### Troyanos (Trojans)

Los troyanos se disfrazan de software legítimo para engañar a usuarios a instalarlos voluntariamente. Una vez ejecutados, realizan acciones maliciosas mientras aparentan funcionalidad legítima. El nombre proviene del Caballo de Troya de la mitología griega: algo aparentemente benigno que contiene una amenaza oculta.

Los troyanos no se replican automáticamente como virus o gusanos. Su distribución depende de ingeniería social: aparecer como un juego, herramienta útil, actualización de software o archivo de trabajo. Los usuarios los descargan e instalan creyendo que son legítimos.

Los banking trojans roban credenciales bancarias mediante keylogging, captura de pantalla o inyección web que modifica páginas de bancos mostradas en el navegador para capturar información. Zeus, SpyEye y más recientemente TrickBot son ejemplos de banking trojans sofisticados responsables del robo de millones.

Los Remote Access Trojans (RATs) proporcionan control remoto completo del sistema infectado. El atacante puede ver la pantalla, acceder a archivos, activar cámara y micrófono, monitorear teclado y ejecutar comandos. Las víctimas no saben que sus máquinas son controladas remotamente.

En el contexto cripto, los troyanos pueden robar claves privadas de wallets almacenadas en disco, modificar direcciones de destino en el portapapeles (clipboard hijacking) o instalar versiones falsas de wallets que envían fondos al atacante. Los usuarios instalan lo que creen son wallets legítimas pero son troyanos diseñados específicamente para robar criptomonedas.

### Ransomware: Extorsión mediante cifrado

El ransomware cifra archivos del usuario haciendo todo inaccesible y demanda pago de rescate para proporcionar la clave de descifrado. Es una de las amenazas más disruptivas y financieramente motivadas del panorama actual. Los ataques de ransomware han evolucionado de amenazas oportunistas a operaciones criminales sofisticadas dirigidas a organizaciones con capacidad de pago.

El funcionamiento típico comienza con infección inicial mediante phishing, vulnerabilidad explotada o credenciales comprometidas. Una vez dentro, el ransomware se propaga lateralmente infectando tantos sistemas como sea posible. Después establece persistencia y elimina backups para prevenir recuperación sin pago. Finalmente, cifra archivos con criptografía fuerte y muestra mensaje de rescate con instrucciones de pago en criptomonedas.

El crypto-ransomware cifra archivos específicos valiosos: documentos, fotos, bases de datos y código fuente. Los archivos del sistema operativo permanecen intactos para que la máquina pueda arrancar y mostrar el mensaje de rescate. El cifrado usa algoritmos robustos como AES, haciendo imposible descifrar sin la clave controlada por los atacantes.

El locker ransomware bloquea completamente el sistema operativo, mostrando solo la pantalla de rescate. El usuario no puede acceder a nada. Este tipo es menos común actualmente porque es más fácil de remediar: reinstalando el sistema operativo se recupera el acceso, mientras que archivos cifrados por crypto-ransomware permanecen inaccesibles.

El doble extorsión ransomware exfiltra datos sensibles antes de cifrar. Los atacantes amenazan con publicar la información robada si no se paga el rescate. Esto presiona incluso a organizaciones con backups robustos: recuperar archivos es posible, pero la filtración de datos sensibles causa daño reputacional, legal y competitivo.

Los RaaS (Ransomware as a Service) operan como modelo de negocio criminal donde desarrolladores crean ransomware y afiliados lo distribuyen, compartiendo ganancias. Esta especialización permite que criminales sin habilidades técnicas ejecuten ataques de ransomware sofisticados usando infraestructura y herramientas proporcionadas por expertos.

Las demandas de rescate típicamente se exigen en Bitcoin, Monero u otras criptomonedas para dificultar rastreo. Los montos varían desde cientos de dólares para individuos hasta millones para corporaciones. Los atacantes ajustan demandas basándose en capacidad percibida de pago de la víctima.

La defensa primaria contra ransomware son backups offline robustos. Si los datos están respaldados en almacenamiento desconectado de la red, pueden restaurarse sin pagar. Los backups deben estar aislados porque ransomware sofisticado busca y elimina backups accesibles desde sistemas infectados.

La prevención incluye parchado regular, segmentación de red, principio de mínimos privilegios y monitoreo de comportamiento anómalo. Los EDR (Endpoint Detection and Response) detectan patrones característicos de ransomware como modificación masiva de archivos o eliminación de shadow copies.

Pagar el rescate no garantiza recuperación. Los criminales pueden no proporcionar claves funcionales, pueden demandar pagos adicionales o simplemente desaparecer con el dinero. Además, pagar financia operaciones criminales y establece precedente de que la organización pagará, convirtiéndola en objetivo futuro.

## Ataques de Inyección: SQL, Command y XSS

Los ataques de inyección explotan aplicaciones que no validan adecuadamente input de usuarios. El atacante inserta código malicioso en campos de entrada que la aplicación ejecuta sin intención, comprometiendo datos o funcionalidad. La inyección es consistentemente una de las vulnerabilidades más críticas y prevalentes en aplicaciones web.

### SQL Injection

SQL injection inserta código SQL malicioso en queries de base de datos. Las aplicaciones que concatenan input de usuarios directamente en queries SQL sin sanitización son vulnerables. El atacante puede manipular la lógica de la query para acceder, modificar o eliminar datos arbitrarios.

Un ejemplo clásico es autenticación vulnerable. Una query típica busca usuario con nombre y contraseña proporcionados: `SELECT * FROM users WHERE username='input_user' AND password='input_pass'`. Si el atacante introduce `admin'--` como username, la query se convierte en `SELECT * FROM users WHERE username='admin'--' AND password='...'`. Los dos guiones son comentario SQL, ignorando el resto. La query devuelve el usuario admin sin verificar contraseña, otorgando acceso.

Los ataques in-band SQLi retornan resultados directamente en la respuesta de la aplicación. El atacante puede extraer datos mediante UNION queries que combinan resultados de la query legítima con queries maliciosas, leyendo contenido completo de bases de datos. Las técnicas de error-based SQLi provocan errores que revelan estructura de la base de datos en mensajes de error.

Los blind SQLi no retornan datos directamente pero permiten inferir información mediante técnicas de tiempo y booleanas. Boolean-based blind SQLi hace preguntas verdadero/falso mediante queries que causan comportamiento diferente según la respuesta. Time-based blind SQLi usa funciones de espera (SLEEP, WAITFOR) para determinar respuestas: si la página tarda en cargar, la condición era verdadera.

El out-of-band SQLi usa canales diferentes para exfiltrar datos cuando la aplicación no muestra resultados de queries. El atacante puede causar que la base de datos haga peticiones DNS o HTTP a servidores controlados, incluyendo datos sensibles en los requests.

El impacto de SQL injection es devastador: bypass completo de autenticación, robo masivo de datos de usuarios, modificación o eliminación de registros, ejecución de comandos del sistema operativo si la base de datos tiene permisos elevados y compromiso total del servidor en casos severos.

La prevención fundamental son prepared statements y consultas parametrizadas. En lugar de concatenar strings, los parámetros se pasan separadamente del código SQL. El motor de base de datos trata los parámetros como datos, nunca como código ejecutable, previniendo inyección completamente. Los ORMs (Object-Relational Mappers) modernos usan prepared statements por defecto.

La validación y sanitización de input verifica que los datos del usuario cumplan formato esperado. Si un campo debe ser número, rechazar cualquier entrada que no sea numérico. Los whitelists de caracteres permitidos son más seguros que blacklists de caracteres prohibidos.

El principio de mínimos privilegios limita el impacto. Las cuentas de base de datos usadas por aplicaciones deben tener solo permisos estrictamente necesarios. Si la aplicación solo lee datos, la cuenta no debe tener permisos de escritura. Esto limita daño posible incluso si ocurre inyección.

Los Web Application Firewalls (WAF) detectan y bloquean patrones de SQL injection en peticiones HTTP. Aunque no son defensa primaria, proporcionan capa adicional contra ataques.

### Cross-Site Scripting (XSS)

XSS inyecta scripts maliciosos (típicamente JavaScript) en páginas web vistas por otros usuarios. Cuando víctimas visitan la página comprometida, el navegador ejecuta el script malicioso en contexto de la aplicación legítima, proporcionando al atacante acceso a cookies, tokens de sesión y capacidad de realizar acciones como el usuario.

El reflected XSS incluye el script malicioso en una petición (URL o formulario) que la aplicación refleja inmediatamente en la respuesta sin sanitizar. El atacante engaña a víctimas para que hagan clic en enlaces maliciosos que contienen el payload XSS. Cuando la víctima carga la URL, el servidor incluye el script en la página y el navegador lo ejecuta.

El stored XSS almacena el script malicioso en el servidor (base de datos, foro, comentarios). Cuando usuarios visualizan el contenido comprometido, el script se ejecuta automáticamente. Stored XSS es más peligroso porque afecta a todos los usuarios que ven el contenido, no solo aquellos que hagan clic en un enlace específico.

El DOM-based XSS manipula el Document Object Model del navegador mediante JavaScript. La vulnerabilidad está en código JavaScript client-side que procesa input sin sanitizar. El servidor puede estar completamente seguro, pero el código JavaScript vulnerable permite al atacante ejecutar scripts.

Los exploits XSS pueden robar cookies de sesión mediante `document.cookie`, enviándolas a servidores controlados por el atacante. Con las cookies, el atacante puede suplantar la sesión del usuario. Pueden realizar acciones como el usuario: cambiar configuración, transferir fondos, modificar datos o instalar malware adicional.

En Web3, XSS en frontends de DApps puede robar wallet addresses, manipular transacciones antes de firma o engañar a usuarios para que firmen transacciones maliciosas presentadas como legítimas. El script malicioso tiene acceso completo al contexto de la página, incluyendo objetos Web3 que interact úan con wallets.

La prevención primaria es output encoding: convertir caracteres especiales en entidades HTML antes de incluir datos de usuarios en páginas web. Los caracteres `<`, `>`, `"`, `'` y `&` se codifican como `&lt;`, `&gt;`, etc., haciendo que el navegador los muestre como texto en lugar de interpretarlos como código.

Los Content Security Policy (CSP) headers restringen qué scripts pueden ejecutarse en la página. Un CSP estricto solo permite scripts de dominios específicos o con hashes verificables, bloqueando scripts inline inyectados por XSS. Implementar CSP correctamente requiere planificación pero proporciona defensa robusta.

La sanitización de input procesa datos de usuarios para eliminar código potencialmente malicioso. Las bibliotecas de sanitización especializadas entienden contexto HTML y pueden limpiar input preservando funcionalidad legítima mientras eliminan vectores de ataque.

## Ataques Man-in-the-Middle (MITM)

Los ataques man-in-the-middle interceptan comunicaciones entre dos partes, permitiendo al atacante escuchar, modificar o inyectar mensajes sin que las partes legítimas sepan que su comunicación está comprometida. El atacante se posiciona entre víctima y servidor, retransmitiendo mensajes modificados mientras aparenta ser cada parte ante la otra.

### Técnicas MITM

El ARP spoofing en redes locales manipula tablas ARP para redirigir tráfico a través de la máquina del atacante. Address Resolution Protocol traduce direcciones IP a direcciones MAC físicas. El atacante envía respuestas ARP falsas asociando su MAC con la IP del gateway, causando que máquinas en la red envíen todo su tráfico al atacante antes de llegar al destino real.

El DNS spoofing redirige tráfico alterando respuestas DNS. Cuando un usuario consulta la IP de un dominio, el atacante proporciona una respuesta falsa apuntando a un servidor malicioso. El usuario cree estar visitando el sitio legítimo pero está conectado al servidor del atacante.

Los fake WiFi access points (Evil Twin) crean redes WiFi falsas con nombres similares a redes legítimas. Los usuarios conectándose a "Starbucks WiFi" pueden estar realmente conectados a un punto falso operado por un atacante en la misma cafetería. Todo el tráfico pasa por el atacante.

El SSL stripping degrada conexiones HTTPS a HTTP no cifrado. El atacante intercepta la petición inicial del usuario y se conecta al servidor legítimo usando HTTPS, pero sirve la página al usuario mediante HTTP sin cifrado. El navegador del usuario no muestra el candado de seguridad pero el tráfico está completamente expuesto.

### Impacto de MITM

El atacante puede escuchar todo el tráfico no cifrado: credenciales, cookies de sesión, información personal y datos sensibles transmitidos en claro. El cifrado end-to-end previene esto, pero no todos los sitios usan HTTPS correctamente.

La modificación de tráfico es más peligrosa que solo escuchar. El atacante puede alterar respuestas del servidor, inyectar malware en descargas, modificar contenido de páginas para phishing o cambiar números de cuenta en transacciones bancarias antes de que lleguen al usuario.

En cripto, MITM puede interceptar transacciones y modificar direcciones de destino. El usuario cree estar enviando fondos a una dirección legítima, pero el atacante modifica la transacción para enviarlos a su propia dirección. Sin verificación cuidadosa de la dirección final antes de firmar, el usuario puede perder fondos irreversiblemente.

### Prevención de MITM

El HTTPS con TLS proporciona cifrado y autenticación que previene MITM. El servidor presenta un certificado firmado por una autoridad certificadora confiable, verificando su identidad. El tráfico cifrado no puede ser leído ni modificado sin las claves privadas del servidor. Los usuarios deben verificar el candado de seguridad antes de introducir información sensible.

El certificate pinning en aplicaciones móviles predefine qué certificados son válidos para servicios específicos. Incluso si un atacante compromete una autoridad certificadora y obtiene certificados válidos, la aplicación rechaza conexiones con certificados no pinned.

Las VPNs cifran todo el tráfico entre dispositivo y servidor VPN, protegiendo contra MITM en redes locales comprometidas. Aunque la VPN misma es un punto de confianza, previene ataques de actores locales en WiFi públicas.

Los protocolos de verificación de integridad como DNSSEC para DNS y HSTS (HTTP Strict Transport Security) para web fuerzan uso de conexiones seguras y verificables, dificultando ataques MITM a nivel de protocolo.

## Ataques de engaño y manipulación

### Bait and Switch (Cebo y cambio)

El bait and switch es técnica de engaño que usa publicidad aparentemente legítima para atraer víctimas y luego cambia el contenido por algo malicioso. Los atacantes compran espacios publicitarios legítimos en sitios web confiables, inicialmente sirviendo anuncios normales que pasan verificación. Una vez aprobados, reemplazan los anuncios con contenido malicioso que redirige a sitios de phishing o descarga malware.

La efectividad radica en aprovechar la confianza de usuarios en plataformas publicitarias conocidas. Ver un anuncio en sitio respetable reduce las defensas psicológicas del usuario. Los anuncios pueden imitar promociones reales de productos populares, actualizaciones de software urgentes o alertas de seguridad falsas.

Las técnicas incluyen cloaking donde el anuncio muestra contenido diferente a revisores humanos versus usuarios finales, fast-flux que cambia rápidamente URLs de destino para evadir blacklists y time-based switching donde el anuncio es legítimo inicialmente pero se vuelve malicioso tras cierto tiempo.

La protección incluye ad blockers que previenen carga de publicidad completamente, extensiones de navegador que verifican reputación de anuncios antes de permitir clicks, mantener software actualizado para que vulnerabilidades explotadas por malicious ads estén parcheadas y verificar URLs antes de hacer clic, especialmente en anuncios que prometen ofertas extraordinarias o alertas de seguridad urgentes.

### Cookie Theft y Session Hijacking

El robo de cookies permite a atacantes secuestrar sesiones activas de usuarios sin necesidad de credenciales. Las cookies de sesión son tokens que navegadores envían automáticamente con cada petición para mantener estado de login. Si un atacante obtiene estas cookies, puede impersonar al usuario completamente.

El cross-site scripting (XSS) es vector común para robo de cookies. Un script malicioso inyectado en página web puede acceder a `document.cookie` y enviar las cookies a servidor controlado por atacante mediante petición HTTP. Con las cookies robadas, el atacante las inyecta en su propio navegador y accede a la cuenta de la víctima.

Los ataques man-in-the-middle en redes WiFi públicas permiten interceptar cookies transmitidas sin cifrado. Aunque HTTPS cifra tráfico, configuraciones incorrectas o ataques de SSL stripping pueden degradar conexiones a HTTP donde cookies son visibles. Los network sniffing tools como Wireshark capturan fácilmente cookies en tráfico no cifrado.

El malware instalado en la máquina de la víctima puede acceder directamente a archivos de cookies almacenados por navegadores. Aunque navegadores modernos cifran cookies en disco, el malware ejecutándose bajo el contexto del usuario puede descifrarlas usando las mismas credenciales del sistema.

La protección primaria son flags HTTPOnly en cookies que previenen acceso mediante JavaScript, eliminando vector XSS. Las cookies deben marcarse Secure para transmisión solo mediante HTTPS, previniendo interceptación en tráfico no cifrado. Los tokens de sesión deben rotarse tras acciones sensibles y tener expiración corta. La autenticación multifactor agrega capa de protección: incluso si sesión es secuestrada, acciones críticas requieren verificación adicional.

### Clickjacking (UI Redressing)

El clickjacking engaña a usuarios para que hagan clic en elementos invisibles mediante capas transparentes sobre contenido legítimo. El atacante crea página con iframe invisible conteniendo sitio objetivo posicionado precisamente sobre botones o enlaces del sitio atacante. El usuario cree estar haciendo clic en contenido benigno pero realmente interactúa con sitio en el iframe oculto.

Los ejemplos de abuso incluyen activar cámara o micrófono sin consentimiento, hacer clic en botones de "me gusta" en redes sociales aumentando artificialmente engagement, transferir fondos si el iframe contiene página bancaria pre-cargada, cambiar configuraciones de privacidad a opciones menos seguras o aprobar permisos de aplicaciones sin que el usuario sea consciente.

Las técnicas sofisticadas usan opacity settings para hacer iframe casi invisible pero técnicamente presente, z-index manipulation para layering preciso de elementos, cursor positioning donde el cursor muestra estar en una posición pero el click registra en otra y responsive clickjacking que ajusta layout dinámicamente según comportamiento del usuario.

La prevención usa X-Frame-Options header configurado a DENY o SAMEORIGIN que instruye navegadores a rechazar renderizado de la página en iframes. El Content Security Policy con directiva frame-ancestors proporciona control más granular sobre qué dominios pueden embeder la página. El frame-busting JavaScript detecta si página está en iframe y "explota" fuera, aunque esta técnica es menos confiable que headers HTTP. La verificación visual de acciones críticas muestra preview de lo que el usuario está aprobando, dificultando clickjacking efectivo.

### Fake Wireless Access Points (Evil Twin)

Los fake WAP crean puntos de acceso WiFi falsos que imitan redes legítimas para interceptar tráfico de usuarios. El atacante configura access point con nombre idéntico (SSID) a red legítima en ubicación cercana. Los dispositivos de usuarios pueden conectarse automáticamente al access point falso si la señal es más fuerte, o usuarios pueden seleccionarlo manualmente creyendo que es la red real.

Una vez conectados, todo el tráfico de usuarios pasa por el access point del atacante. El atacante puede interceptar comunicaciones no cifradas, modificar tráfico en tránsito, inyectar malware en descargas, ejecutar ataques SSL stripping para degradar conexiones HTTPS a HTTP, capturar credenciales de login a servicios y realizar ataques man-in-the-middle contra cualquier comunicación.

Los lugares comunes incluyen cafeterías donde múltiples redes con nombres similares confunden a usuarios, aeropuertos con alta densidad de viajeros que buscan WiFi gratuito, hoteles donde huéspedes esperan encontrar red del establecimiento, conferencias y eventos con muchos asistentes buscando conectividad y espacios públicos con WiFi que son targets convenientes para atacantes.

La protección requiere usar VPN siempre en redes públicas para cifrar todo el tráfico independiente de si el access point es confiable. Verificar con personal del establecimiento el nombre exacto de la red legítima antes de conectarse. Desactivar conexión automática a redes WiFi para prevenir que dispositivos se conecten sin consentimiento. Verificar que conexiones a servicios importantes usan HTTPS válido antes de introducir credenciales. Usar datos móviles para transacciones importantes en lugar de WiFi pública cuando sea posible. Mantener firewall activado para bloquear accesos no solicitados desde la red local.

### Keyloggers

Los keyloggers registran todas las pulsaciones de teclado, capturando contraseñas, mensajes privados, números de tarjetas de crédito y cualquier información escrita. Operan completamente ocultos del usuario, transmitiendo datos capturados a atacantes remotamente o almacenándolos localmente para posterior exfiltración.

Los software keyloggers se instalan como malware mediante phishing, drive-by downloads o explotación de vulnerabilidades. Una vez instalados, se ejecutan en background con privilegios de sistema, interceptando pulsaciones antes de que lleguen a aplicaciones. Los keyloggers sofisticados son rootkits que operan a nivel de kernel, haciéndolos extremadamente difíciles de detectar.

Los hardware keyloggers son dispositivos físicos insertados entre teclado y computadora, típicamente conectores USB pequeños que pasan desapercibidos. Capturan pulsaciones sin necesidad de software, siendo inmunes a antivirus. Requieren acceso físico para instalación y posterior recuperación del dispositivo con datos capturados.

Los keyloggers basados en API interceptan llamadas a funciones de sistema operativo que manejan input de teclado. Los JavaScript keyloggers ejecutan en navegadores mediante XSS, capturando solo input en páginas web específicas. Los keyloggers de formularios capturan datos antes de transmisión, incluso si formularios usan JavaScript para ofuscar.

La información capturada incluye contraseñas y PINs ingresados en cualquier aplicación, credenciales bancarias y financieras, números de tarjetas de crédito y CVV codes, mensajes privados en chats y emails, frases seed de wallets cripto que controlan millones en activos.

La protección incluye software antimalware actualizado que detecta keyloggers conocidos mediante firmas y heurísticas de comportamiento. Mantener sistema operativo y aplicaciones parcheadas para cerrar vulnerabilidades explotadas para instalación. Usar gestores de contraseñas que autorellenan credenciales sin pulsaciones de teclado. Implementar autenticación de dos factores para que contraseñas capturadas solas sean insuficientes. Usar teclados virtuales en pantalla para transacciones críticas, aunque keyloggers sofisticados pueden capturar pantalla. Hardware wallets para cripto que nunca exponen claves privadas al sistema potencialmente comprometido. Inspección física periódica de puertos USB buscando dispositivos no autorizados.

### Eavesdropping (Escucha clandestina)

El eavesdropping intercepta pasivamente comunicaciones de red sin modificar el tráfico. A diferencia de ataques activos, el atacante simplemente escucha, capturando datos transmitidos sin alertar a las partes comunicándose. La naturaleza pasiva hace la detección extremadamente difícil.

El packet sniffing en redes WiFi abiertas captura todo el tráfico visible en el medio compartido. Los access points no cifrados transmiten datos en claro que cualquiera en rango puede capturar con herramientas como Wireshark. Incluso en redes con WPA2, atacantes que conocen la contraseña pueden descifrar tráfico capturado.

Los man-in-the-middle activos también incluyen componentes de eavesdropping, pero el atacante intercepta y retransmite tráfico en lugar de solo capturarlo pasivamente. El atacante se posiciona en el camino de comunicación, viendo todo sin que las partes sepan de su presencia.

La interceptación de comunicaciones móviles usa IMSI catchers (Stingray devices) que se hacen pasar por torres celulares legítimas. Los teléfonos conectan al dispositivo del atacante, permitiendo interceptar llamadas, SMS y datos. Estas técnicas son usadas por agencias gubernamentales pero también disponibles para actores criminales con recursos.

La información objetivo incluye credenciales de acceso transmitidas sin cifrado, cookies de sesión que permiten secuestro, comunicaciones privadas en emails y chats, datos financieros en transacciones no protegidas y transacciones cripto donde detalles de billeteras o cantidades pueden revelarse.

La protección fundamental es cifrado end-to-end que hace el contenido ilegible para interceptores. HTTPS para navegación web con verificación de certificados válidos. VPNs que cifran todo el tráfico de red incluyendo metadata. Aplicaciones de mensajería con cifrado E2E como Signal. Verificar que conexiones WiFi usan WPA3 o mínimo WPA2 con contraseñas fuertes. Evitar redes WiFi públicas sin protección para actividades sensibles. Usar PGP/GPG para cifrado de emails que contienen información crítica.

### Waterhole Attacks

Los waterhole attacks comprometen sitios web frecuentados por víctimas objetivo en lugar de atacar directamente a las víctimas. Como predadores que acechan en abrevaderos donde presas vienen a beber, los atacantes infectan sitios que saben que sus objetivos visitan regularmente, esperando pacientemente la infección.

El atacante primero perfila víctimas objetivo identificando qué sitios web visitan frecuentemente mediante reconocimiento de red, análisis de logs si tiene acceso limitado o inteligencia de fuentes públicas. Una vez identificados sitios objetivo, el atacante busca vulnerabilidades en esos sitios específicos para comprometer sus servidores.

Las fases incluyen compromiso del sitio legítimo mediante explotación de vulnerabilidades en CMS, plugins desactualizados o credenciales débiles de administrador. Inyección de código malicioso en páginas del sitio comprometido, típicamente JavaScript que detecta visitantes objetivo y sirve exploits. Infección selectiva donde el malware solo se activa para visitantes que coincidan con perfil objetivo, evitando detección masiva. Explotación de visitantes objetivo mediante exploits de navegador, drive-by downloads o redirecciones a sitios de phishing.

Los ejemplos de uso incluyen ataques APT (Advanced Persistent Threat) por grupos patrocinados por estados dirigidos a organizaciones específicas o sectores industriales completos. Espionaje corporativo donde competidores comprometen foros o recursos visitados por empleados de empresas objetivo. Campañas de estado-nación que comprometen sitios de noticias locales, foros de comunidades específicas o recursos de industrias de interés estratégico.

La protección incluye mantener navegadores y plugins actualizados con últimos parches de seguridad. Usar extensiones de seguridad como NoScript que bloquean JavaScript de sitios no confiados por defecto. Mantener soluciones antimalware y EDR actualizadas que detecten comportamientos maliciosos. Implementar network segmentation donde máquinas comprometidas no pueden acceder a sistemas críticos. Monitoreo de comportamiento anómalo en endpoints que pueda indicar infección. Threat intelligence que alerta sobre sitios comprometidos conocidos para bloquearlos proactivamente.

### DNS Spoofing y Cache Poisoning

El DNS spoofing falsifica respuestas DNS para redirigir usuarios a sitios maliciosos cuando intentan acceder a dominios legítimos. El atacante intercepta consultas DNS o contamina cachés DNS, proporcionando direcciones IP incorrectas que apuntan a servidores controlados por el atacante.

El DNS cache poisoning contamina cachés de servidores DNS con información falsa que persiste hasta que el TTL (Time To Live) expira. El atacante envía respuestas DNS falsas con autoridad aparente, engañando a resolvers DNS para almacenar mappings incorrectos. Una vez contaminado, el servidor DNS proporciona información maliciosa a todos los clientes que consultan esos dominios durante la duración del cache.

El funcionamiento típico incluye al atacante interceptando consulta DNS antes de que llegue al servidor legítimo o prediciendo transaction IDs de queries DNS para inyectar respuestas falsas. El servidor DNS acepta la respuesta falsa creyendo que proviene del nameserver autoritativo. Usuarios consultando ese dominio reciben IP maliciosa y son redirigidos a sitio del atacante. El atacante opera sitio falso que imita el legítimo para phishing, malware distribution o interceptación de credenciales.

Los usos maliciosos incluyen phishing sofisticado donde víctimas escriben URLs correctas pero son redirigidas a sitios falsos perfectamente replicados. Malware distribution donde descargas de software legítimo son reemplazadas con versiones troyanizadas. Censura o bloqueo de sitios implementado por adversarios mediante envenenamiento selectivo de resolvers DNS. Business email compromise donde emails corporativos son redirigidos a servidores del atacante.

La protección usa DNSSEC (DNS Security Extensions) que firma criptográficamente respuestas DNS permitiendo verificar autenticidad. DNS sobre HTTPS (DoH) o DNS sobre TLS (DoT) que cifran queries DNS previniendo interceptación y manipulación. Usar resolvers DNS de confianza como Google (8.8.8.8), Cloudflare (1.1.1.1) o Quad9 (9.9.9.9) que implementan seguridad robusta. Caché DNS con TTL corto para limitar duración de información contaminada. Monitoreo de cambios inesperados en resoluciones DNS que puedan indicar compromiso.

### Password Cracking y Key Derivation Functions

El password cracking recupera contraseñas desde hashes almacenados o mediante fuerza bruta contra sistemas de autenticación. Los atacantes que obtienen dumps de bases de datos con hashes de contraseñas usan técnicas computacionales para revertir los hashes a texto plano.

Los métodos incluyen offline cracking sobre hashes robados donde atacantes prueban millones de contraseñas por segundo sin límites de rate. Online cracking contra sistemas live limitado por throttling pero puede tener éxito con credenciales débiles. Dictionary attacks probando palabras de diccionarios y contraseñas comunes conocidas de brechas previas. Rainbow tables con hashes precomputados para contraseñas comunes permitiendo lookups instantáneos. Distributed cracking usando poder computacional distribuido en múltiples máquinas o GPUs para velocidad masiva.

Las Key Derivation Functions (KDF) protegen contraseñas aplicando hashing repetitivo computacionalmente costoso. Las funciones como Argon2, bcrypt y PBKDF2 están diseñadas para ser lentas deliberadamente, haciendo cracking impráctico incluso con hardware especializado. El uso de salt aleatorio único por usuario previene rainbow tables y fuerza cracking individual por hash.

La protección requiere usar KDF modernos (Argon2 recommended, bcrypt acceptable) nunca hashes simples como MD5 o SHA-1 para contraseñas. Implementar salt aleatorio único para cada contraseña almacenada. Configurar work factors altos que balance seguridad contra performance de login legítimo. Requerir contraseñas largas y complejas que resisten dictionary attacks. Implementar autenticación multifactor como segunda línea de defensa. Monitorear intentos de login fallidos indicando brute force attempts. Rotación periódica de contraseñas críticas especialmente tras posibles brechas.

## Referencias y recursos adicionales

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/): Vulnerabilidades web más críticas
- [MITRE ATT&CK](https://attack.mitre.org/): Framework de tácticas y técnicas de adversarios
- [SANS Top 25 Software Errors](https://www.sans.org/top25-software-errors/): Errores de programación más peligrosos
- [CWE Common Weakness Enumeration](https://cwe.mitre.org/): Catálogo de debilidades de software
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework): Estándares de gestión de riesgo
- [Krebs on Security](https://krebsonsecurity.com/): Análisis de incidentes y tendencias de seguridad

---
