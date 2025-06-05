//Karen Reyes

const titulos = [
    "Deje de usar AWS.",
    "Registros diarios para desarrolladores: cómo un hábito de 5 minutos puede multiplicar por 10 tu producción semanal",
    "Cursor ahora es gratis para los estudiantes",
    "11 Cursos para Aprender Diseño de Sistemas y Arquitectura de Software en profundidad",
    "12 libros atemporales que todo programador debería leer",
    "De 0 a 10K ⭐: Cómo Open SaaS se convirtió en el amor de los desarrolladores repetitivos gratuitos",
    "Convierta su aplicación React en un cliente MCP en minutos",
    "10 libros de ingeniería de IA y LLM imprescindibles para desarrolladores en 2025",
    "9 trucos que separan a un desarrollador profesional de Typescript de un novato 😎",
    "5 cosas que deberían ser ilegales para el autoanfitrión",
    "Más allá del código: cómo crear una documentación atractiva que a los desarrolladores les guste mucho (prácticas recomendadas)",
    "✨ 7 cosas que hago regularmente como desarrollador frontend senior",
    "La hoja de trucos definitiva de comandos de Linux para ingenieros y analistas de datos",
    "Elementos HTML5 que no sabías que necesitabas",
    "Conduit: Un sistema basado en nodos sin interfaz de usuario",
    "Construí un servidor MCP para DevTo (100% Open Source) 🎉",
    "De la idea al lanzamiento: una guía del desarrollador para crear tu primera startup",
    "El sueño sin servidor ha muerto",
    "Qwen 3 vs. Deepseek R1: Comparación completa",
    "Las 10 mejores herramientas de codificación de vibraciones que parecen mágicas en 2025",
];

const contenedorTitulos = document.getElementById("titulosAleatorios");
const cantTitulos = 10;
const seleccionados = [...titulos].sort(() => 0.5 - Math.random()).slice(0, cantTitulos);

seleccionados.forEach(titulo => {
    const p = document.createElement("p");
    p.classList.add("titulo");
    p.textContent = titulo;
    contenedorTitulos.appendChild(p);
});