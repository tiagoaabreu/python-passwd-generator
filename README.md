# Gerador de senha com python
- Gerador de Senhas utilizando python via CLI
---

### 🎯 Objetivo
- [x]  Gerar senha colocando: numero, letras maiusculas e minusculas e pontuação.
- [ ]Dar opção ao usuario escolher a quantidade de caracteres para a senha
- [ ]Disponibilizar uma forma de exportar a senha criada, e listar as senhas(Pendente)

--- 

### 📋Funcionalidades 
Até o momento implementei flags com o argparse para poder definir o tamanho, sem colocar a flag -p/--passwd(tamanho default da geração: 8 caracteres). Tambem implementei uma verificação com if para poder delimitar o tamanho da geração, sendo o limite 30, planejo futuramente colocar o limite de caracteres para o usuario escolher.

Implementei em partes uma opção para que fosse exportada para a pasta em que se encontra o programa, um arquivo contendo a senha que foi gerada, com o nome senhas.txt, futuramente planejo implementar uma forma de adicionar numerando a senha, exemplo: Rodei 5 vezes o codigo, e as senhas estarão ordenadas por numeração, para o usuario poder lembrar ao menos qual foi a vez que a senha esta relacionada

---

## 🔑 Propostio
Esse projeto tem o proposito totalmente de aprendizado e prática com flags, geração de caracteres, e com a propria linguagem
