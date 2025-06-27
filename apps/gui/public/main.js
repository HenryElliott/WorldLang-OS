let currentDeck = [];
let currentIndex = 0;

document.getElementById('language-select').addEventListener('change', async (e) => {
  const lang = e.target.value;
  const res = await fetch(`decks/${lang}.json`);
  currentDeck = await res.json();
  currentIndex = 0;
  nextCard();
});

function showAnswer() {
  document.getElementById("card-back").innerText = currentDeck[currentIndex].back;
}

function nextCard() {
  if (!currentDeck.length) return;
  currentIndex = (currentIndex + 1) % currentDeck.length;
  document.getElementById("card-front").innerText = currentDeck[currentIndex].front;
  document.getElementById("card-back").innerText = "";
}
