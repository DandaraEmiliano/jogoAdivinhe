var numeroSecreto = 22;
var audio;

function createEmoji() {
  var emoji = document.createElement('span');
  emoji.className = 'emoji';
  emoji.textContent = '🥳🤩';
  return emoji;
}

function startEmojiRain() {
  var emojiRain = document.getElementById('emoji-rain');
  var windowWidth = window.innerWidth;

  setInterval(function () {
    var emoji = createEmoji();
    var leftPosition = Math.random() * windowWidth;
    var offset = Math.random() * 100;

    emoji.style.left = leftPosition + 'px';
    emoji.style.setProperty('--offset-x', offset + 'px');

    emoji.style.animationDuration = '2s';
    emoji.style.animationTimingFunction = 'linear';

    emoji.addEventListener('animationend', function () {
      emojiRain.removeChild(emoji);
    });

    emojiRain.appendChild(emoji);
  }, 500);
}

function verificarPalpite() {
  var palpite = parseInt(document.getElementById("palpite").value);
  var mensagem = document.getElementById("mensagem");
  var emojiRain = document.getElementById("emoji-rain");

  if (isNaN(palpite)) {
    mensagem.textContent = "Por favor, digite um número válido.";
  } else {
    if (palpite < numeroSecreto) {
      mensagem.textContent = "O número que você digitou é menor. Tente novamente!";
    } else if (palpite > numeroSecreto) {
      mensagem.textContent = "O número que você digitou é maior. Tente novamente!";
    } else {
      mensagem.textContent = "Parabéns! Você acertou!";
      emojiRain.innerHTML = '';
      startEmojiRain();

      audio = new Howl({
        src: ["assets/xuxa-parabens.mp3"],
        autoplay: true,
        loop: false,
        volume: 5.0,
        onend: function () {
        }
      });
    }
  }
}
