

# Stable Diffusion Checkpoint Merge (GUI)

Um aplicativo com interface gráfica (GUI) para mesclar checkpoints do **Stable Diffusion**. Suporta os formatos `.ckpt` e `.safetensors`, permitindo criar modelos personalizados combinando pesos de diferentes checkpoints.

## Recursos

- **Interface gráfica amigável**: Sem necessidade de comandos complexos.
- **Compatibilidade**: Suporte para arquivos `.ckpt` e `.safetensors`.
- **Log em tempo real**: Acompanhe o processo detalhadamente.
- **Barra de progresso**: Feedback visual do andamento.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados no seu sistema:

- **Python 3.8 ou superior**
- Bibliotecas Python necessárias:
  - `torch`
  - `safetensors`
  - `tkinter` (normalmente já incluído com o Python)

### Instalação das dependências

Antes de usar o aplicativo, instale as bibliotecas necessárias com o comando:

```bash
pip install torch safetensors
```

---

## Como Usar

1. **Clone este repositório** ou baixe os arquivos.

   ```bash
   git clone https://github.com/Drifer97/stable-diffusion-checkpoint-merge.git
   cd stable-diffusion-checkpoint-merge
   ```

2. **Execute o script**:

   ```bash
   python checkpoint_merge.py
   ```

3. **Interface Gráfica**:
   - **Checkpoint 1**: Clique em "Selecionar" e escolha o primeiro arquivo `.ckpt` ou `.safetensors`.
   - **Checkpoint 2**: Clique em "Selecionar" e escolha o segundo arquivo `.ckpt` ou `.safetensors`.
   - **Salvar Como**: Escolha o local para salvar o novo arquivo mesclado.
   - Clique em **"Mesclar"**.

4. Acompanhe o progresso pela barra e mensagens de log.

5. Após a conclusão, o arquivo mesclado estará salvo no local especificado.

---

## Exemplos de Uso

### Exemplo de combinação
- Checkpoint 1: `model1.ckpt`
- Checkpoint 2: `model2.safetensors`
- Arquivo gerado: `merged_model.ckpt`

Este processo cria um novo modelo com 50% dos pesos de cada checkpoint.

---

## Problemas Comuns

1. **"Invalid load key"**  
   - Certifique-se de que os arquivos fornecidos são checkpoints válidos no formato `.ckpt` ou `.safetensors`.

2. **Erro durante a mesclagem**  
   - Pode ocorrer se os arquivos estiverem corrompidos ou forem incompatíveis. Verifique os arquivos.

---

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou tiver ideias para melhorias, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
---

## Créditos

Criado por **Drifer97**.

