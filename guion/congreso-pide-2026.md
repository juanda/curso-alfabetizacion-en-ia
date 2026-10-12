# Ponencia PIDE 2026 · guion oral de 45 minutos

**Título:** Usos positivos de la IA en la educación: aprender a crear para comprender<br>
**Autor:** Juan David Rodríguez García · Badajoz, 16 de octubre de 2026<br>
**Público:** comunidad educativa del V Congreso «La educación que queremos»<br>
**Idea central:** LearningML y Glass Parrot son dos entradas accesibles a la alfabetización en IA. Construir modelos sencillos ayuda después a usar la IA generativa con más criterio, eficacia y autonomía.

| Diapositivas | Bloque | Tiempo | Acumulado |
| --- | --- | ---: | ---: |
| 1–6 | La IA hoy | 6 min | 6 min |
| 7–11 | La IA en el pasado | 5 min | 11 min |
| 12–18 | Por qué alfabetizar y noción de ML | 9 min | 20 min |
| 19–23 | LearningML | 8 min | 28 min |
| 24–25 | IA generativa de texto | 4 min | 32 min |
| 26–29 | Glass Parrot | 9 min | 41 min |
| 30–31 | Cierre | 4 min | **45 min** |
| 32 | Fuentes | — | — |

## Ajustes frente al curso

- Los bloques **1, 2, 3, 5 y 8** del curso pasan a ser las secciones **1 a 5** de la ponencia.
- Del bloque 4 se conservan solo **aprender de ejemplos, entrenar, evaluar y sesgo**.
- Del bloque 7 se conservan solo **predicción del siguiente fragmento y límites de fiabilidad**.
- Se eliminan el taller del bloque 6, las tareas de plataforma y los detalles técnicos que requerían una sesión larga.
- La circular anuncia el título «Usos positivos de la Inteligencia Artificial en la Educación», por lo que la apertura y el cierre explicitan oportunidades y condiciones de buen uso.

## Preparación

- Comprobar LearningML y Glass Parrot en el equipo y la red del auditorio; llevar el PDF para la opción sin conexión.
- Elegir un único ejemplo curricular de LearningML para contar de forma concreta.
- Evitar presentar como certezas generales los resultados de estudios preliminares sobre efectos cognitivos; la ponencia formula una pregunta pedagógica, no una conclusión causal.
- Los incidentes de verano se documentan en [OpenAI](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), [Hugging Face](https://huggingface.co/blog/agent-intrusion-technical-timeline) y [Anthropic](https://www.anthropic.com/news/improving-alignment-security-efforts). Ocurrieron en evaluaciones de ciberseguridad con protecciones reducidas o entornos mal configurados; no fueron incidentes en centros educativos. La relación con el trabajo docente es una advertencia sobre **quién define objetivos, permisos y límites**, no una equivalencia técnica entre ambos contextos.

## Cómo leer el texto

Lo que sigue está escrito en **primera persona**, para decirlo en voz alta o adaptarlo. Las indicaciones entre corchetes son acciones para el ponente. La diapositiva 32 contiene fuentes y puede quedar visible al acabar, sin consumir tiempo oral. El plan de arriba incluye los cambios de diapositiva y una demostración breve de Glass Parrot.

# 1. La IA hoy · 6 minutos

## Diapositiva 1 · Portada

Buenas tardes. El programa anuncia una ponencia sobre los usos positivos de la inteligencia artificial en la educación. Quiero empezar afirmando algo sencillo: esos usos existen. Una herramienta que nos ayuda a preparar una explicación distinta, adaptar un texto u ofrecer práctica adicional puede ser muy valiosa. El problema es que una herramienta capaz de hacer tantas cosas también puede alterar profundamente **quién decide** qué se enseña, qué aprende el alumnado y qué papel desempeña el profesorado.

Hoy os propongo un recorrido que va de la oportunidad a la comprensión. Mi tesis es que podemos usar mejor la IA cuando conocemos, aunque sea con modelos sencillos, **cómo aprende, de qué datos depende y por qué falla**. Y la mejor manera de conocerla puede ser construirla con nuestras propias manos.

## Diapositiva 2 · La IA hoy

[Pausa breve.] Nos encontramos en un momento en que las capacidades crecen más deprisa que nuestra experiencia pedagógica con ellas. No necesitamos escoger entre entusiasmo y rechazo. Necesitamos criterios. Voy a presentar algunas posibilidades y un riesgo, y después dos experiencias de alfabetización que nos ayudan a recuperar el control: LearningML y Glass Parrot.

## Diapositiva 3 · Una herramienta de muchas caras

La IA puede escribir, traducir, resumir, generar imágenes y código, transformar voz en texto o proponer ejercicios. Como docentes, esto puede ahorrarnos trabajo mecánico. Pensemos en una profesora que prepara tres explicaciones de un mismo concepto, con ejemplos diferentes, para estudiantes que parten de lugares distintos. O en un alumno que ensaya una exposición oral y recibe observaciones inmediatas antes de presentarla a sus compañeros. Son usos que amplían las oportunidades de practicar y revisar.

Pero el verbo importante es **ayudar**. Que una respuesta llegue rápido no significa que sea correcta, apropiada para la edad o coherente con nuestro objetivo. La pregunta que debemos hacer no es solo «¿puede hacerlo la IA?», sino «¿qué aprendizaje mejora si la utilizo aquí y cómo comprobaré que ha mejorado?».

## Diapositiva 4 · Verano de 2026: los agentes cruzaron límites

Este verano hemos visto por qué importa tanto definir límites. Durante evaluaciones internas de ciberseguridad, modelos de OpenAI eludieron controles que debían aislarlos de internet y llegaron a sistemas de Hugging Face. Anthropic informó de otros incidentes en pruebas externas en los que algunos modelos accedieron a sistemas reales sin autorización. Eran **entornos de evaluación**, con salvaguardas reducidas o configuraciones defectuosas; no describen el funcionamiento habitual de un chatbot en un aula.

La enseñanza general es esta: cuando damos a un sistema **objetivos, herramientas y capacidad de actuar**, no basta con confiar en que hará lo que teníamos en mente. Debemos delimitar qué puede hacer, vigilar lo que hace y poder detenerlo. No estoy comparando un aula con una intrusión informática. Estoy señalando el mismo tipo de pregunta humana: **¿quién fija el objetivo y quién conserva el control?**

## Diapositiva 5 · Si no la dirigimos, puede dirigir la docencia

En educación esa pregunta es especialmente importante. La IA puede proponer actividades, explicar contenidos, corregir ejercicios y analizar respuestas. Si automatizamos sin deliberar, el oficio docente puede desplazarse: de diseñar experiencias de aprendizaje a **supervisar decisiones tomadas por otros**. Podemos acabar aceptando los objetivos que sugiere una plataforma, los criterios con los que clasifica al alumnado o las explicaciones que le ofrece, simplemente porque resultan cómodos.

Eso podría reducir nuestra autonomía profesional y debilitar la relación educativa. Enseñar también es reconocer a la persona que tengo delante, interpretar un silencio, provocar una pregunta, sostener el esfuerzo y construir convivencia. La amenaza no es que mañana desaparezca todo el profesorado; sería injusto presentarlo como una certeza. La amenaza es que cedamos, poco a poco y casi sin discutirlo, **las decisiones que dan sentido a nuestro trabajo**.

## Diapositiva 6 · Una IA centrada en las personas

Por eso propongo un criterio: empezar siempre por la **finalidad educativa**. Después decidir qué tarea conviene delegar, con qué datos, con qué supervisión y con qué posibilidad de corregir el resultado. Si un sistema ahorra tiempo, preguntémonos a qué dedicaremos ese tiempo. Si ofrece una explicación individual, preguntémonos qué conversación o qué actividad colectiva hace posible. Si evalúa, preguntémonos quién revisa sus errores y quién responde ante el estudiante.

Una IA centrada en las personas requiere responsabilidad, privacidad, atención a los sesgos y accesibilidad. Y requiere alfabetización. Sin una idea mínima de cómo funciona, nos costará distinguir una ayuda auténtica de una cesión de criterio.

# 2. La IA en el pasado · 5 minutos

## Diapositiva 7 · La IA en el pasado

Para explicar por qué defiendo esa alfabetización, tengo que volver unos años atrás. Antes de que los chatbots ocuparan todas las conversaciones, ya había docentes intentando llevar al aula una pregunta distinta: **¿podemos enseñar los fundamentos de la IA construyendo modelos sencillos?**

## Diapositiva 8 · 2015: todo empieza a acelerar

Esta cronología resume un cambio que se vuelve especialmente visible hacia 2015. El aprendizaje profundo mejora mucho el reconocimiento de imágenes. Después llegan hitos que reciben atención pública: AlphaGo, la arquitectura Transformer, modelos de lenguaje cada vez mayores y, en 2022, ChatGPT al alcance de millones de personas. En 2025 y 2026 se extiende el uso de agentes capaces de ejecutar acciones.

No quiero detenerme en cada fecha. La idea es que, mientras la tecnología avanzaba, el público empezó a convivir con sistemas que podían hacer cosas impresionantes sin tener necesariamente una explicación de **cómo las hacían**. En educación, eso nos planteaba un problema y una oportunidad.

## Diapositiva 9 · Docentes que se adelantaron

Hace años, un grupo de docentes e investigadores nos preguntamos si podíamos enseñar aprendizaje automático del mismo modo que Scratch había ayudado a enseñar programación: creando. De ese trabajo surgió LearningML. La idea era permitir que niñas, niños y jóvenes reunieran ejemplos, entrenaran un modelo, lo probaran y lo incorporaran a una aplicación propia.

Lo importante no era fabricar un clasificador perfecto. Era que, para conseguir que la máquina distinguiera algo, el estudiante tuviera que preguntarse qué rasgos importan, qué casos faltan y por qué el modelo se equivoca. Ahí empieza el aprendizaje. El proyecto se dio a conocer en una publicación académica en 2020, antes de que la IA generativa dominara el debate público.

## Diapositiva 10 · La IA generativa cambió el foco

Después llegaron los chatbots y las imágenes generadas a partir de texto. Era lógico que llamaran la atención: por primera vez muchísimas personas podían conversar con una IA y obtener un producto acabado en segundos. En ese nuevo paisaje, las experiencias de construir modelos pequeños parecieron menos espectaculares. «¿Para qué enseñar a entrenar un clasificador si ya tengo una máquina que escribe un ensayo?», podía preguntarse cualquiera.

Mi respuesta es que precisamente **ahora** resulta más valioso enseñar esos fundamentos. La potencia de la IA generativa no elimina la necesidad de comprenderla; la aumenta.

## Diapositiva 11 · Hoy es más importante que entonces

Usamos estos sistemas como una caja negra. Escribimos una petición y recibimos una respuesta. Cuando suena convincente, podemos olvidar que no hemos visto los datos de los que aprendió, ni sabemos siempre cómo llegó a ese resultado. Comprender los mecanismos básicos no convierte a nadie en ingeniero de IA, pero sí permite formular preguntas mejores: «¿de dónde puede venir este sesgo?», «¿qué tipo de error es probable?», «¿qué debería comprobar por mi cuenta?».

La alfabetización no tiene que esperar a que dominemos toda la matemática. Podemos empezar con modelos visibles, manipulables, lo bastante pequeños como para que el alumnado descubra por sí mismo sus posibilidades y sus límites.

# 3. Por qué alfabetizar · 9 minutos

## Diapositiva 12 · Por qué alfabetizar

Hay una razón técnica y una razón educativa. La técnica es que sin comprender al menos una parte del funcionamiento de la IA, podemos atribuirle capacidades que no ha demostrado. La educativa es que una herramienta que resuelve tareas intelectuales por nosotros puede ayudarnos a aprender o puede impedir que hagamos el esfuerzo necesario para hacerlo. Quiero detenerme en ambas.

## Diapositiva 13 · Ilusionismo estadístico

Arthur C. Clarke escribió que «cualquier tecnología suficientemente avanzada es indistinguible de la magia». Cuando leemos una respuesta clara, bien redactada y rápida, es fácil sentir que la máquina nos comprende. El efecto es parecido al de un truco de ilusionismo: vemos el resultado, pero no el mecanismo. Y cuanto mejor es el resultado, más tentador es atribuir intención, comprensión o autoridad a lo que aparece en pantalla.

La IA generativa aprende patrones de cantidades enormes de datos. Su funcionamiento es mucho más complejo que el del modelo pequeño que veremos luego, pero hay una distinción que debemos conservar: **una respuesta fluida no es una prueba de verdad**. Puede contener un dato inventado, una cita inexistente o una interpretación equivocada. Alfabetizar consiste, en parte, en levantar el telón y preguntar qué ha ocurrido detrás.

## Diapositiva 14 · La descarga cognitiva tiene dos caras

La descarga cognitiva no es nueva ni es necesariamente mala. Utilizamos papel para no memorizarlo todo, calculadoras para no hacer todas las operaciones a mano y buscadores para localizar información. Eso puede liberar tiempo para pensar mejor. Una estudiante que usa una calculadora para explorar patrones matemáticos puede llegar más lejos que si se queda atascada haciendo cuentas repetitivas.

Pero no toda descarga produce aprendizaje. Si una tarea consistía en organizar ideas y argumentar, y delego por completo ambas cosas, quizá entregue un texto mejor esta tarde mientras aprendo menos para mañana. Antes de incorporar una herramienta, propongo hacernos una pregunta sencilla: **¿qué hace ahora el estudiante que antes no podía hacer?** Si la respuesta es «comprender, comparar, crear o revisar mejor», vamos por un camino prometedor. Si la respuesta es solo «terminar antes sin pensar», conviene rediseñar la actividad.

Pensemos en una redacción. Podría pedir a un chatbot que la escriba de principio a fin. También podría escribir primero mi argumento, pedirle que señale dónde no se entiende, discutir sus objeciones y decidir cuáles acepto. En ambos casos «he usado IA», pero solo en el segundo conservo el trabajo intelectual que la actividad pretendía desarrollar. La diferencia no está en el nombre de la herramienta: está en la **secuencia de acciones** que hemos diseñado.

## Diapositiva 15 · Aprender también requiere dificultad

Seymour Papert hablaba de *hard fun*: la diversión que nace de enfrentarse a un reto difícil y significativo. Quien ha visto a un niño programar un juego sabe que puede pasar mucho tiempo corrigiendo errores sin perder el interés. El reto tiene sentido porque está construyendo algo suyo y puede ver cómo mejora.

No pretendo que hagamos el aprendizaje artificialmente arduo. Pretendo que protejamos el **esfuerzo que permite aprender**. Con la IA podemos pedirle un resultado terminado o podemos usarla dentro de un proceso en el que el estudiante formula una hipótesis, construye, prueba y corrige. En la segunda opción sigue habiendo dificultad, y esa dificultad tiene un propósito.

## Diapositiva 16 · Alfabetizar es poder crear

La imagen propone una analogía. No diríamos que una persona está alfabetizada porque puede escuchar cómo le leen un libro; también queremos que pueda leerlo, discutirlo y escribir. No basta con consultar resultados en una calculadora: necesitamos comprender los números. Y en tecnología, además de usar aplicaciones, es valioso **crear** alguna, aunque sea sencilla.

Con la IA ocurre algo parecido. Aprender a escribir buenas instrucciones puede ser útil, pero es solo una parte. Construir un pequeño modelo permite ver qué datos necesita, cómo se comporta con casos nuevos y de dónde nacen algunos de sus errores. Ese conocimiento nos da más libertad cuando después usamos sistemas mucho más potentes.

## Diapositiva 17 · Una idea básica de Machine Learning

Imaginemos que queremos reconocer cifras escritas a mano. En la programación tradicional intentamos dar a la máquina reglas: si hay un trazo aquí y otro allí, devuelve un número. Muy pronto aparecen miles de formas diferentes de escribir cada cifra. Es difícil anticiparlas todas.

El aprendizaje automático cambia la estrategia. Ofrecemos **ejemplos** y, en el aprendizaje supervisado, les añadimos la respuesta que esperamos: «esto es un tres», «esto es un ocho». Un algoritmo ajusta un modelo a partir de ellos. Luego le mostramos un ejemplo nuevo y preguntamos qué cree que es. El modelo no tiene una regla perfecta para todos los casos; ofrece una predicción basada en lo aprendido. Esta idea, ejemplos en vez de instrucciones exhaustivas, basta para entender la actividad que haremos con LearningML.

## Diapositiva 18 · Los datos enseñan y también sesgan

Hay tres momentos distintos. Primero **entrenamos**: reunimos ejemplos y sus etiquetas. Luego el sistema **aprende**: ejecutamos el algoritmo de ML, que construye un modelo a partir de esos ejemplos. Después **evaluamos** con casos que el modelo no ha visto. Si probamos solo con los mismos datos que usamos para enseñarle, podemos engañarnos: quizá los recuerde, pero no sepa generalizar.

También importa qué ejemplos elegimos. Si una clase tiene muchos casos y otra muy pocos, o si todos los ejemplos de un tipo se parecen demasiado, el modelo puede fallar de forma desigual. Esto es una lección educativa formidable. El sesgo no es una propiedad misteriosa que aparece al final; puede empezar en nuestras decisiones de **recogida, selección y etiquetado** de datos. Cuando un estudiante descubre esto entrenando su propio modelo, la palabra «sesgo» deja de ser una advertencia abstracta.

Imaginemos que entrenamos un sistema para identificar solicitudes de ayuda en textos breves y casi todos los ejemplos están escritos en el registro formal que nosotros empleamos. Si un alumno formula la misma necesidad con otras palabras, quizá el sistema no la reconozca. No es porque su necesidad sea menor: es porque nuestro conjunto de ejemplos **no representaba todas las maneras de expresarla**. Esa es una buena razón para que la evaluación incluya diversidad de casos y para que ninguna predicción sustituya automáticamente el juicio de una persona.

# 4. LearningML · 8 minutos

## Diapositiva 19 · LearningML

Aquí entra LearningML. Su utilidad en esta ponencia no reside en que sea la plataforma más potente. Reside en que permite recorrer un proceso completo y visible: proponer un problema, reunir ejemplos, entrenar, poner a prueba y construir una aplicación. Y hacerlo en un entorno pensado para aprender, que no oculta el proceso.

## Diapositiva 20 · Construir un modelo para aprender

El estudiante define clases, reúne textos o imágenes, indica a cuál pertenece cada ejemplo y entrena un modelo. Luego le presenta casos nuevos. Algunos los clasificará bien; otros, no. Esos errores son la parte más interesante. «¿Se parecía este caso a los que le enseñamos?», «¿faltaba variedad?», «¿hemos definido bien las clases?».

Después puede llevar el modelo a Scratch y darle un uso. Así se ve que la IA no es una entidad independiente que aparece en una pantalla: es **un componente dentro de una aplicación diseñada por personas**. Las personas eligen los datos, la finalidad y lo que la aplicación hará con la predicción.

Podemos narrarlo como una pequeña investigación de aula. Primer día: acordamos qué queremos reconocer y para qué serviría hacerlo. Segundo día: reunimos ejemplos y discutimos si tenemos permiso para usarlos. Tercero: entrenamos y reservamos algunos casos que nadie le ha enseñado al modelo. Cuarto día: lo ponemos a prueba, anotamos errores y volvemos a las decisiones iniciales. Si una clase funciona peor que otra, no cambiamos una palabra del *prompt* para ocultarlo: **revisamos el problema, los datos y las etiquetas**. Así, la técnica queda al servicio de una pregunta pedagógica.

## Diapositiva 21 · El aula está llena de modelos posibles

Tomemos un ejemplo de Arte. Queremos distinguir imágenes de obras impresionistas, cubistas y realistas. Para enseñar a una máquina, primero el alumnado tiene que investigar **qué rasgos caracterizan cada estilo**. Después reúne ejemplos de obras que pueda usar, los etiqueta y observa el resultado. Si todas las imágenes cubistas proceden de un único artista o tienen el mismo fondo, el modelo podría aprender el fondo o al artista en vez del estilo. Eso abre una conversación sobre qué significa realmente «aprender» una categoría.

Cuando probemos el modelo con un cuadro nuevo, no basta con celebrar un acierto. Podemos pedir al alumnado que explique por qué había elegido esa etiqueta, compararlo con la predicción y buscar casos fronterizos que nos obliguen a afinar la categoría. Un error puede revelar un problema del modelo, pero también una duda interesante sobre el contenido artístico. Ahí la IA **no reemplaza la conversación de clase**: nos proporciona un objeto común para discutir con pruebas.

La misma lógica sirve en Ciencias, Lengua o Matemáticas. Podemos clasificar especies, identificar la intención de una frase o estudiar puntos del plano. No pretendo que toda unidad didáctica termine en un modelo de IA. Propongo que, cuando construimos uno, el contenido de la materia deja de ser un decorado: **es lo que el estudiante debe comprender para seleccionar buenos ejemplos**.

## Diapositiva 22 · Aprender para enseñar

En esta imagen se ve un ciclo. Primero aprendo el tema; luego escojo y clasifico ejemplos; después entreno y evalúo; al observar fallos, vuelvo a estudiar el tema o a revisar los datos. Hay dos aprendizajes a la vez: el del modelo y el del estudiante. El modelo puede mejorar, pero lo decisivo es que la persona aprende a hacer preguntas más precisas.

Me gusta esta inversión: normalmente decimos que la máquina enseña al alumno. Aquí es el alumno quien **enseña a la máquina**, y al hacerlo descubre qué sabía de verdad y qué creía saber. El error deja de ser un fracaso que esconder y se convierte en información para la siguiente prueba.

Además, el ciclo se puede compartir. Dos grupos pueden entrenar modelos para el mismo problema y después intercambiar sus casos de prueba. Si uno de los modelos falla con imágenes que el otro sí reconoce, la conversación deja de ser «el ordenador es listo o tonto» y pasa a ser «¿qué decisiones tomó cada grupo?». Es una manera de practicar la argumentación, la revisión entre iguales y la responsabilidad sobre lo que uno construye.

## Diapositiva 23 · Del modelo a una aplicación

El último paso es construir algo que utilice el modelo. Scratch permite decidir qué hará un personaje cuando se reconozca una clase, cómo presentará un resultado y qué sucederá si la respuesta es incierta. Esto devuelve al estudiante una responsabilidad que a veces desaparece al usar IA generativa: no basta con que el modelo produzca una salida; hay que diseñar **para quién**, **para qué** y **con qué límites** se utiliza.

Aquí veo un uso positivo de la IA en la educación pública: puede unir el aprendizaje de una materia, el pensamiento computacional y el criterio crítico en una actividad en la que el alumnado crea, prueba, discute y comparte.

# Puente. IA generativa de texto · 4 minutos

## Diapositiva 24 · La IA generativa también aprende de datos

Ahora demos un salto de escala. Un modelo de lenguaje no funciona exactamente como el pequeño clasificador que acabamos de imaginar. Durante su entrenamiento aprende patrones de grandes colecciones de texto y, al generar, calcula qué fragmentos son probables a continuación del contexto que tiene delante. Repite ese proceso paso a paso, construyendo una respuesta.

No es un simple teclado predictivo ampliado; esa comparación sirve para entrar en el tema, pero los modelos actuales captan relaciones mucho más complejas. Tampoco debemos concluir que «solo predice, luego nunca puede razonar». Lo que sí podemos afirmar con seguridad es que **producir una secuencia plausible no garantiza que sus afirmaciones sean verdaderas**. Esa diferencia importa mucho cuando lo usamos para preparar clases, aprender o evaluar.

Fijémonos en lo que ocurre al empezar una respuesta. Nuestra petición proporciona un contexto: una pregunta, un nivel educativo, quizá un texto que queremos revisar. El modelo propone una continuación; la continuación pasa a formar parte del contexto para elegir la siguiente. Ese proceso permite escribir páginas coherentes, pero no añade por sí solo una comprobación externa de cada afirmación. Si pido una referencia bibliográfica, la forma de una cita puede resultar muy familiar para el modelo incluso cuando el artículo concreto **no existe**. Por eso la verificación debe formar parte de nuestra tarea, no añadirse solo cuando algo nos suena raro.

## Diapositiva 25 · Qué conviene comprobar

Si le pedimos una fecha, una referencia o una explicación, debemos verificar lo que sostiene. Puede inventar fuentes, mezclar datos o reproducir sesgos presentes en sus materiales de entrenamiento. Puede sonar seguro y, sin embargo, no haber entendido el propósito educativo de la tarea. Por eso la revisión humana debe ir más allá de corregir una errata: consiste en comprobar hechos, adecuación, derechos y consecuencias.

Un buen uso no se reduce a escribir una petición muy detallada. También exige saber **qué no pedirle**, qué información no introducir, qué parte revisar con especial cuidado y en qué momento conviene que el estudiante haga el trabajo sin esa ayuda.

# 5. Glass Parrot · 9 minutos

## Diapositiva 26 · Glass Parrot

La segunda herramienta que quiero mostrar es Glass Parrot, creada por Elena Tomás Vela. Si LearningML permite construir modelos que clasifican, Glass Parrot permite construir un **modelo de lenguaje pequeño y transparente**. De nuevo, el objetivo no es competir con los sistemas comerciales. Es hacer visible una idea que, a gran escala, suele quedar oculta detrás de una respuesta sorprendente.

## Diapositiva 27 · Un loro de cristal

El nombre es muy expresivo. Loro, porque genera a partir de lo que ha visto; de cristal, porque podemos observar sus datos y sus probabilidades. Le damos un conjunto pequeño de frases, lo entrenamos y vemos qué palabras considera posibles después de un comienzo. Como el corpus lo hemos elegido nosotros, podemos modificarlo y observar cómo cambia el resultado.

Eso ofrece una experiencia que una explicación teórica difícilmente sustituye. Podemos provocar repeticiones, introducir ejemplos desequilibrados o hacer una pregunta para la que no hay información. El alumnado ve que el sistema no saca las respuestas de una verdad interior: **depende de lo que le hemos dado y de cómo combina sus posibilidades**.

## Diapositiva 28 · ¿Qué palabra viene después?

Miremos esta imagen. Si en los ejemplos aparecen «el gato duerme» y «el gato come», después de «el gato» hay dos continuaciones observadas. En este pequeño corpus, ambas aparecen una vez: cincuenta por ciento para «duerme» y cincuenta por ciento para «come». El modelo cuenta secuencias de palabras, llamadas *n-gramas*, y utiliza esos recuentos para elegir qué añadir.

[Demostración opcional, **2–3 minutos**, incluida en el tiempo del bloque.] Si la herramienta está preparada, cargo unas frases, entreno y miro la lista de palabras posibles tras «el gato». Añado varias frases que terminan con «duerme» y vuelvo a observar. Pregunto al auditorio: «¿Ha aprendido una verdad sobre los gatos o hemos cambiado la distribución de sus datos?». No hace falta que el público interactúe ni generar un párrafo largo. Queremos ver **cómo se mueve una probabilidad**.

Para que el experimento sea limpio, preparo un corpus muy corto: «el gato duerme», «el gato come», «el perro duerme». Primero invito a anticipar qué dos palabras pueden seguir a «el gato». Después de mostrar el reparto, añado «el gato duerme» dos o tres veces y pregunto hacia dónde se inclinará la predicción. Este pequeño momento de **anticipar, observar y explicar** es más valioso que recorrer todas las opciones de la interfaz. Quien asiste no necesita conocer los menús; necesita comprobar que una decisión sobre los datos cambia el comportamiento del modelo.

[Sin conexión.] Señalo los dos recuadros de la imagen, explico el reparto inicial y digo en voz alta qué pasaría si añadiera tres veces «el gato duerme». La idea pedagógica es la misma y no depende de que funcione la web.

## Diapositiva 29 · Lo pequeño aclara lo grande

Glass Parrot cuenta apariciones en un corpus pequeño. Un LLM moderno utiliza una red neuronal entrenada a otra escala y puede aprovechar relaciones que un simple n-grama no captura. Sería engañoso decir que son lo mismo. Pero compararlos permite formular preguntas valiosas sobre ambos: ¿qué datos han visto?, ¿qué contexto están utilizando?, ¿qué opciones consideran?, ¿cómo se elige la siguiente parte de la respuesta?

La herramienta pequeña sirve como un mapa. Un mapa no reproduce cada árbol de un territorio, pero nos ayuda a orientarnos. Y al mirar también lo que el mapa **no explica**, evitamos convertir una analogía didáctica en una explicación total de la IA generativa.

Si un estudiante sale de esta experiencia diciendo «ahora sé exactamente cómo funciona un gran modelo de lenguaje», le hemos enseñado mal. Espero algo más humilde y más útil: que se pregunte de dónde vienen los datos, qué significa una predicción probable y por qué una respuesta convincente puede requerir comprobación. Un buen modelo didáctico abre preguntas mejores; no clausura la investigación.

# Cierre · 4 minutos

## Diapositiva 30 · Primero comprender; después usar mejor

Estamos llegando al final. Os he propuesto una secuencia. Con LearningML, el alumnado construye un modelo y descubre el peso de los datos, los errores y los sesgos. Con Glass Parrot, construye un modelo de lenguaje pequeño y observa contexto y probabilidades. Con esa experiencia, puede acercarse a la IA generativa con preguntas más afinadas y con más capacidad de verificar lo que recibe.

No digo que cada docente tenga que enseñar redes neuronales ni que cada estudiante deba programar antes de usar una herramienta. Digo que **hacer visible lo esencial** cambia nuestra relación con ella. Nos permite aprovechar sus ventajas sin entregar por inercia el pensamiento, la responsabilidad o la decisión pedagógica.

## Diapositiva 31 · La educación que queremos

La pregunta con la que abrí era qué educación queremos construir con la IA. Mi respuesta es una educación en la que esta tecnología nos ayude a explicar mejor, a practicar más, a crear cosas nuevas y a ampliar oportunidades, pero en la que el profesorado conserve su juicio profesional y el alumnado siga siendo protagonista de su aprendizaje.

Si una herramienta hace una tarea en segundos, aprovechemos esa capacidad para dedicar más tiempo a lo que importa: **preguntar, comprender, contrastar, acompañar y crear**. Pero decidamos nosotros qué merece ser delegado y qué merece seguir siendo una experiencia humana y formativa.

[Pausa.] Antes de usar mejor la IA, necesitamos comprenderla. Y una manera poderosa de comprenderla es **construir**. Muchas gracias.

## Diapositiva 32 · Fuentes y recursos

[No hace falta leer esta diapositiva. Déjala visible durante las preguntas o al cerrar.] Fuentes para consultar y ampliar:

- **Contexto del acto:** circular del V Congreso Internacional «La educación que queremos» (PIDE, 2026), incluida en este proyecto.
- **Incidente de julio:** [OpenAI, *The Hugging Face incident and the road ahead*](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) y [cronología técnica de Hugging Face](https://huggingface.co/blog/agent-intrusion-technical-timeline).
- **Otros incidentes de evaluación:** [Anthropic, *Improving our alignment and security practices*](https://www.anthropic.com/news/improving-alignment-security-efforts). Se citan como incidentes de ciberseguridad, no como casos educativos.
- **Alfabetización y construcción de modelos:** [LearningML](https://learningml.org/) y Rodríguez-García, J. D. y cols. (2020), [artículo en *RED*](https://doi.org/10.6018/red.410121).
- **Modelo de lenguaje didáctico:** [Glass Parrot](https://glass-parrot.vercel.app/), de Elena Tomás Vela.
- **Construccionismo:** Papert, S. (1980), *Mindstorms*. Basic Books.
- **Cita de la diapositiva 13:** tercera ley de Arthur C. Clarke, recogida por la [Arthur C. Clarke Foundation](https://clarkefoundation.org/arthur-c-clarke-biography/). La formulación en español es una traducción.

© 2026 Juan David Rodríguez García · CC BY-NC 4.0.
