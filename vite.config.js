import { resolve } from 'path';
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        redFlags: resolve(__dirname, 'red-flags.html'),
        howItWorks: resolve(__dirname, 'how-it-works.html'),
        scamSpotter: resolve(__dirname, 'scam-spotter.html'),
        quiz: resolve(__dirname, 'quiz.html'),
        ifMoneySent: resolve(__dirname, 'if-money-sent.html'),
        aboutCep: resolve(__dirname, 'about-cep.html'),
        sources: resolve(__dirname, 'sources.html'),
      },
    },
  },
});

