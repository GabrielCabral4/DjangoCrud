/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './tarefas/templates/tarefas/*.html',
    './templates/**/*.html',  // Adiciona suporte para templates em outras pastas
    './*/templates/**/*.html',  // Suporta templates em qualquer app do Django
    './tarefas/static/tarefas/css/input.css'
  ],
  theme: {
    extend: {
      colors: {
        'primary': '#3498db',   // Azul principal
        'secondary': '#2ecc71', // Verde secundário
        'accent': '#e74c3c',    // Vermelho para ênfase
        'background': '#f4f6f7' // Fundo suave
      }
    }
  },
  plugins: [
      require('@tailwindcss/line-clamp'),
  ],
}