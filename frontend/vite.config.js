import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  logLevel: 'info',
  server: {
    host: '0.0.0.0',
    port: 5173,
    open: true,
    strictPort: true,
    watch: {
      usePolling: true,
    },
    historyApiFallback: true,
  },
});
