# jogoAdivinhe

# Adivinhe o Número

Um jogo simples em JavaScript e Python onde o jogador precisa adivinhar um número secreto.

## Como Jogar

1. Abra o jogo no seu navegador [clicando aqui](http://127.0.0.1:5500/src/index.html).
2. O jogo irá gerar um número secreto entre 1 e 100.
3. Digite um número no campo de entrada e clique no botão "Verificar".
4. O jogo fornecerá feedback sobre o palpite:
   - Se o número for menor que o número secreto, será exibida uma mensagem informando que o número é menor.
   - Se o número for maior que o número secreto, será exibida uma mensagem informando que o número é maior.
   - Se o número for igual ao número secreto, será exibida uma mensagem de parabéns.
5. A cada palpite, o jogo também apresentará uma animação de chuva de emojis no fundo.
6. Ao acertar o número secreto, uma música de celebração será reproduzida.

## Personalização

Você pode personalizar o jogo de acordo com suas preferências. Aqui estão algumas sugestões:

- **Intervalo de Números**: Você pode alterar o intervalo de números para tornar o jogo mais fácil ou mais difícil. Basta modificar a variável `numeroSecreto` no arquivo `script.js`.
- **Emojis**: Os emojis exibidos durante a chuva podem ser personalizados. Você pode editar a função `createEmoji()` no arquivo `script.js` para usar emojis diferentes.
- **Música**: A música de celebração pode ser substituída por outra de sua escolha. Basta substituir o arquivo de áudio `xuxa-parabens.mp3` na pasta `assets` e atualizar o caminho do arquivo no código.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novos recursos.


## Agradecimentos

- Este jogo foi desenvolvido com base em um exemplo de jogo de adivinhação em JavaScript.
- Os emojis utilizados neste jogo foram obtidos a partir da biblioteca Emoji CSS: [Emoji CSS](https://emoji-css.afeld.me/).
- A música de celebração utilizada neste jogo é "Parabéns" da Xuxa.

Sinta-se à vontade para personalizar e adaptar este jogo de acordo com suas necessidades e preferências. Divirta-se jogando e aprendendo!
