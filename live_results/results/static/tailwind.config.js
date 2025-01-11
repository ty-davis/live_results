/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    './scripts/**/*.js',
    './styles/in/*.css',
  ],
  theme: {
    extend: {
      backgroundImage: {
        'hero-pattern': "url('https://ty-davis.com/sky.webp')"
      },
      colors: {
        moseyBlue: {
          light: '#694abd',
          DEFAULT: '#370ca6',
          dark: '#240e5e',
        },
        moseyRed: {
          light: '#e66778',
          DEFAULT: '#c91a32',
          dark: '#6e0b18',
        }
      },
      keyframes: {
        shrink: {
          '0%': { width: '100%' },
          '100%': { width: '0%' },
        },
        wipeAway: {
          '0%': { opacity: '1', transform: 'translateY(0)' },
          '100%': { opacity: '0', transform: 'translateY(-100%)' },
        }
      },
      animation: {
        shrink: 'shrink 3s linear forwards',
        wipeAway: 'wipeAway 0.5s ease-in forwards',
      },
      animationDelay: {
        '3s': '3s',
      }
    },
  },
  plugins: [],
}

