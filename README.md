# 💥 Ficha Interativa - Mutantes & Malfeitores 3E

Uma ficha de personagem digital, totalmente interativa, responsiva e focada na melhor experiência de usuário para jogadores do sistema de RPG **Mutantes & Malfeitores 3ª Edição**.

Este projeto foi construído inteiramente como uma **Single-File Application** (um único arquivo HTML com CSS e JS embutidos), o que significa que ele funciona 100% offline, pode ser facilmente distribuído e não requer servidores ou banco de dados.

---

## ✨ Principais Funcionalidades

*   🎨 **Estética de História em Quadrinhos:** Visual totalmente customizado com padrão de retículas (halftone), cores fortes (amarelo, vermelho, branco), fontes estilizadas e bordas marcadas inspiradas em HQs clássicas.
*   📱 **Design Responsivo & Mobile-First:** Jogue no PC ou na mesa de bar pelo celular! O layout utiliza sistema de abas intuitivo e menus responsivos.
*   🦸 **Motor de Arquétipos (30+ Personagens Prontos):** Quer começar a jogar em 1 minuto? Carregue um dos mais de 30 templates de personagens nível 10 das franquias:
    *   *Invencível* (Invencível, Eve Atômica, Omni-Man, Battle Beast, etc.)
    *   *Marvel* (Homem-Aranha, Homem de Ferro, Hulk, Wolverine, Deadpool, etc.)
    *   *DC Comics* (Superman, Batman, Mulher-Maravilha, Flash, Lanterna Verde, etc.)
*   🧠 **Guia de Regras Dinâmico (Help Drawer):** Um painel lateral inteligente que ensina o sistema! Clique numa perícia, defesa ou poder e a gaveta desliza na tela explicando detalhadamente como usar, incluindo descrições de modificadores e o efeito da graduação.
*   💾 **Salvar e Carregar Personagem:** Toda a sua ficha pode ser exportada para um arquivo pequeno e leve em `.json`, e carregada facilmente na próxima sessão.
*   🖨️ **Impressão / PDF Inteligente:** Exclusiva aba "Ver Ficha" em formato "limpo" (somente leitura). Ao pressionar `Ctrl+P` (ou Salvar em PDF), o sistema esconde toda a interface web e botões, gerando um documento limpo e oficial para impressão.
*   🧮 **Cálculos Automáticos Básicos:** Matemática de graduações, custos e total de pontos de poder na palma da mão.

## 🚀 Como Usar

Por ser uma aplicação baseada num único arquivo, não há necessidade de instalação de dependências como Node, React, ou configuração de servidor.

1.  **Download:** Baixe o arquivo `ficha_mm3e.html` e as imagens que o acompanham (arquivos `.jpg`).
2.  **Abrir:** Dê um duplo-clique no arquivo HTML para abri-lo no seu navegador favorito (Chrome, Firefox, Safari, Edge).
3.  **Criar Personagem:** Preencha seus atributos, perícias, defesas e poderes, ou carregue um arquétipo pronto no topo da tela.
4.  **Salvar Progresso:** Ao final da sessão, clique em "📥 Baixar Progresso (JSON)" para salvar seu personagem no seu computador ou celular.
5.  **Continuar:** Na próxima sessão, clique em "📂 Carregar Arquivo (JSON)" e continue de onde parou.

## 🛠️ Arquitetura do Projeto

*   **Puro HTML/CSS/JS**: Sem bibliotecas externas.
*   **Gerenciamento de Estado**: Sistema "Data-driven". Todo formulário atualiza um objeto `state` global. Sempre que o estado muda, a função `renderAll()` redesenha a tela instantaneamente (semelhante aos conceitos do React, mas escrito de forma nativa e leve).
*   **Print Layout**: Tratativa pesada em `@media print` para desabilitar toda a interatividade e garantir que o papel impresso/PDF traga apenas a beleza da aba de leitura do personagem.

## 🤝 Contribuição

Sinta-se à vontade para realizar um *fork* deste repositório, criar *issues* ou enviar *pull requests*. Toda ajuda é bem-vinda para adicionar novos poderes, refinamentos nas calculadoras de ponto, novos heróis na lista de templates ou melhorias visuais.

## 📜 Licença

Este é um projeto não-oficial feito de fã para fãs. 
Mutantes & Malfeitores é um sistema de RPG de mesa publicado pela Green Ronin Publishing. Todos os direitos de marca registrados pertencem aos seus respectivos criadores. Personagens da Marvel, DC e Invencível pertencem às suas editoras de origem.
