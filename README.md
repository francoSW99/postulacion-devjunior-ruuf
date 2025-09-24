 ## Postulación Tarea para Dev Junior - Ruuf

### 🎯 Objetivo

El objetivo de este ejercicio fue desarrollar un algoritmo para determinar la cantidad máxima de paneles solares que pueden caber dentro de un techo.

---
### 📝 Mi Solución

Para resolver este problema, desarrollé una función en Python que evalua distintas formas de posicionar los paneles en el techo, encontrando la solución óptima que maximiza la cantidad de paneles en este. El algoritmo sigue estos pasos:

1.  **Validación Inicial:** La función primero comprueba un caso crítico: si el panel es más grande que el techo en ambas orientaciones posibles es imposible que quepan, por lo que retorna 0.
2.  **Calcular cuantos paneles caben con la misma orientación:** el algoritmo calcula la cantidad de paneles que cabrían si se llenara todo el techo con una sola orientación:
    * **Orientación Vertical:** Calcula cuántos paneles caben si todos se colocan "de pie".
    * **Orientación Horizontal:** Calcula cuántos caben si todos se colocan "acostados".
    * Se almacena el máximo de estas dos estrategias como el resultado base final hasta el momento, evaluando si conviene posicionarlos veritcal u horizontalmente.

3.  **Estrategia de Combinación (Recursiva):** Es posible que la solución más óptima sea combinar las dos orientaciones para maximizar la cantidad de paneles en el techo, por lo tanto se combinan estos dos estilos:
    * **Corte Vertical:** Simula un corte vertical en el techo del tamaño del ancho de un panel. Luego, la función se llama a sí misma para calcular la mejor forma de llenar los dos rectángulos sobrantes(nuevamente de manera verticial o sino de manera horizontal).
    * **Corte Horizontal:** Repite el proceso, pero con un corte horizontal.
    * La función compara los resultados de estas combinaciones con el resultado base y devuelve el máximo valor encontrado.

---
### 🤔 ¿Como llegué a la solución?

* **Supuesto:** Se asume que los paneles no se pueden cortar. Deben colocarse como unidades enteras.
* **Primer algoritmo y primer problema:** Inicialmente, desarrollé un algoritmo simple que solo probaba las dos orientaciones principales. Al analizar los casos de prueba, noté que para el Test 2 (paneles 1x2 en un techo 3x5), este enfoque calculaba 6, mientras que el resultado óptimo era 7.
* **Solución:** Descubrí que la solución óptima para el Test 2 requería una combinación de orientaciones. Para resolver esto, implementé una estrategia recursiva que estudia la mejor opción de "cortes" en el techo para encontrar la maxima cantidad de paneles. Esta decisión hizo que el algoritmo fuera más robusto y capaz de resolver todos los casos de prueba correctamente.
