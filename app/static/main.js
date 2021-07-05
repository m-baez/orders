function calculate_total() {
  let product = document.querySelector("#product");
  let size = document.querySelector("#size");
  let quantity = document.querySelector("#quantity");
  let advance = document.querySelector("#advance");
  let rest = document.querySelector("#rest");
  let total = document.querySelector("#total");
  const PRICE_DEFAULT = 0;

  const PRICE_CAKE = {
    Baileys: 250,
    Cheesecake: 200,
    Chocoflan: 220,
    Choconuez: 220,
    "Flan napolitano": 170,
    Kahlua: 200,
    Manjar: 180,
    Mantequilla: 150,
    Marmoleado: 200,
    Nutella: 250,
    Oreo: 250,
    Panque: 100,
    "Piña coco": 180,
    Rompope: 190,
    "Torta de fresa": 150,
    "Torta de pan": 110,
    "Torta de pan con domo": 120,
    Tropical: 200,
  };

  const PRICE_SIZE = {
    "1/4 kg": 1,
    "1/2 kg": 2,
    "3/4 kg": 3,
    "1 kg": 4,
    "1 1/4 kg": 5,
    "1 1/2kg": 6,
    "1 3/4 kg": 7,
    "2 kg": 8,
  };

  const PRICE_SELECT =
    PRICE_CAKE[product.value] * PRICE_SIZE[size.value] || PRICE_DEFAULT;

  total.value = (PRICE_SELECT * parseInt(quantity.value)).toFixed(2);
  rest.value = (total.value - advance.value).toFixed(2);
}

// hh = document.querySelector("#hola");

// hh.addEventListenner("click", () => {
//   alert(hh);
// });
