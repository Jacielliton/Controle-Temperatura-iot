# Plataforma de Coleta e Visualização de Dados IoT para a AMA

## Descrição

Este projeto foi desenvolvido para a AMA - Associação dos Amigos do Autista do Maranhão. O objetivo é criar uma plataforma para coletar, processar e visualizar dados de sensores IoT (temperatura e umidade) usando técnicas de Cloud Computing e Python. A aplicação ajuda a AMA a monitorar condições ambientais de suas instalações e a organizar dados socioeconômicos para melhor tomada de decisões.

## Funcionalidades

- **Coleta de Dados:** Permite a inserção manual dos valores dos sensores através de um formulário web.
- **Conexão com Arduino:** Permite conectar um Arduino para leitura de dados em tempo real, atualizando os dados automaticamente a cada 10 segundos.
- **Visualização de Dados:** Gráficos interativos mostrando as leituras dos sensores ao longo do tempo.

## Tecnologias Utilizadas

- **Flask:** Framework web em Python.
- **Pandas:** Para manipulação e análise de dados.
- **Plotly:** Para criação de gráficos interativos.
- **PySerial:** Para comunicação serial com o Arduino.
- **Threading:** Para atualização automática dos dados.
- **HTML/CSS:** Para o frontend.

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/Jacielliton/iot-ama-project.git
   cd iot-ama-project
2. Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. Instale as dependências:
pip install -r requirements.txt
Uso

4. Inicie o servidor:
python run.py

Acesse o dashboard no navegador:

Abra o navegador e vá para http://127.0.0.1:5000/
Insira novos dados:

Clique em "Adicionar Novo Dado" para inserir manualmente os dados dos sensores.
Conectar ao Arduino:
Clique em "Conectar ao Arduino" para configurar a conexão e iniciar a leitura de dados em tempo real.

###Estrutura do Projeto###

Copiar código
iot-ama-project/
├── app/
│   ├── __init__.py
│   ├── arduino.py
│   ├── routes.py
│   └── templates/
│       ├── add_data.html
│       ├── connect_arduino.html
│       └── index.html
├── data/
│   └── sensor_data.csv
├── static/
│   └── css/
│       └── style.css
├── requirements.txt
├── run.py
├── .gitattributes
├── README.md
└── LICENSE
Contribuindo
Se desejar contribuir para este projeto, siga os passos abaixo:

Faça um fork do repositório.
Crie uma nova branch (git checkout -b feature/nova-funcionalidade).
Faça commit das suas alterações (git commit -am 'Adicione nova funcionalidade').
Faça push para a branch (git push origin feature/nova-funcionalidade).
Crie um novo Pull Request.
