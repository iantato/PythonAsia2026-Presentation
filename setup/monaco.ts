import { defineMonacoSetup } from '@slidev/types'

export default defineMonacoSetup(async (monaco) => {
  // Monaco only comes with 'vs', 'vs-dark', and 'hc-black' by default.
  // To use a theme like Dracula, we must define it!
  // Here is a custom Neon theme perfectly matching your presentation's gradients.
  monaco.editor.defineTheme('neon-theme', {
    base: 'vs-dark',
    inherit: true,
    rules: [
      { token: 'comment', foreground: '6b7280', fontStyle: 'italic' },
      // Matching your neon-cool gradient (blues & purples)
      { token: 'keyword', foreground: 'c084fc' },
      { token: 'type', foreground: '8b5cf6' },
      { token: 'identifier', foreground: 'e5e7eb' },
      { token: 'function.python', foreground: '6b8cff' },
      // Matching your neon-warm gradient (oranges & yellows)
      { token: 'string', foreground: 'fbd38d' },
      { token: 'number', foreground: 'f6ad55' },
    ],
    colors: {
      'editor.background': '#00000000', // Keep it transparent for our glassmorphism slide css!
      'editor.foreground': '#e5e7eb',
      'editorLineNumber.foreground': '#4b5563',
      'editor.lineHighlightBackground': '#8b5cf61a', // Ultra-soft purple highlight
    }
  })

  // Force the theme just in case the addon ignores the return object
  monaco.editor.setTheme('neon-theme')

  return {
    theme: 'neon-theme',
    editorOptions: {
      // Behavior Customizations
      automaticLayout: true,
      scrollBeyondLastLine: false,

      // Force Monaco to render extra empty lines visually even if code is short
      // This helps pad it visually to the bottom
      padding: { top: 16, bottom: 200 },

      // Customize typography
      fontSize: 12,
      fontFamily: '"Fira Code", monospace',
      fontLigatures: true,

      // UI Customizations
      lineNumbers: 'on',       // 'on', 'off', or 'relative'
      wordWrap: 'on',          // Wrap long lines
      minimap: { enabled: false }, // Hide the tiny code map on the right
    },
  }
})