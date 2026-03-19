import { defineCodeRunnersSetup } from '@slidev/types'

export default defineCodeRunnersSetup(() => {
  return {
    // Whenever a ```python {monaco-run} block is executed...
    async python(code, ctx) {
      try {
        // Send the code to your local Python server
        const response = await fetch('http://localhost:8000/run', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ code })
        })

        // Return the output to the slide!
        const result = await response.json()
        return { text: result.text }

      } catch (error) {
        return { text: "Error connecting to local server. Is uvicorn running?" }
      }
    }
  }
})