/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
      padding: {
        content: "50px",
      },
    },
  },
  plugins: [],
};
