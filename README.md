<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Rastreamento de Mãos</h1>
    <section>
        <h2>Visão Geral</h2>
        <p>Essa é uma aplicação de rastreamento de mãos desenvolvida utilizando OpenCV e o módulo HandTrackingModule do cvzone. A aplicação usa uma webcam para capturar vídeo e detectar mãos em tempo real.</p>
    </section>
    <section>
        <h2>Recursos</h2>
        <ul>
            <li>Detecta mãos em tempo real usando uma webcam</li>
            <li>Exibe o vídeo com marcações de rastreamento de mãos</li>
            <li>Suporta até 6 mãos</li>
            <li>Confiança de detecção ajustável</li>
            <li>Opcionalmente, pode utilizar a GPU do computador para acelerar o processamento</li>
        </ul>
    </section>
    <section>
        <h2>Requisitos</h2>
        <ul>
            <li>OpenCV (versão 4.x ou superior)</li>
            <li>cvzone (versão 1.x ou superior)</li>
            <li>Python (versão 3.x ou superior)</li>
            <li>GPU (opcional)</li>
        </ul>
    </section>
    <section>
        <h2>Uso</h2>
        <h3>Modo CPU</h3>
        <ol>
            <li>Clone o repositório e navegue até o diretório do projeto</li>
            <li>Execute o script script.py usando python script.py</li>
            <li>A aplicação começará a capturar vídeo da webcam padrão e exibirá as marcações de rastreamento de mãos</li>
            <li>Pressione 'q' para sair da aplicação</li>
        </ol>
        <h3>Modo GPU</h3>
        <ol>
            <li>Clone o repositório e navegue até o diretório do projeto</li>
            <li>Execute o script script_gpu.py usando python script_gpu.py</li>
            <li>A aplicação começará a capturar vídeo da webcam padrão e exibirá as marcações de rastreamento de mãos, utilizando a GPU do computador para acelerar o processamento</li>
            <li>Pressione 'q' para sair da aplicação</li>
        </ol>
    </section>
    <section>
        <h2>Configuração</h2>
        <p>A aplicação usa as seguintes configurações:</p>
        <ul>
            <li>detectionCon=0.6: define a confiança de detecção para 0.6 (ajustável)</li>
            <li>maxHands=6: define o número máximo de mãos a detectar para 6 (ajustável)</li>
        </ul>
    </section>
    <section>
        <h2>Licença</h2>
        <p>Essa aplicação é licenciada sob a Licença MIT. Veja LICENSE para detalhes.</p>
    </section>
    <section>
        <h2>Autor</h2>
        <p>Luís Rigo</p>
    </section>
    <section>
        <h2>Agradecimentos</h2>
        <p>Essa aplicação usa o módulo HandTrackingModule do cvzone, que é desenvolvido pelos autores do cvzone.</p>
    </section>
    <section>
        <h2>Observações</h2>
        <ul>
            <li>Certifique-se de que a webcam esteja configurada corretamente antes de executar a aplicação.</li>
            <li>A aplicação pode ser ajustada para detectar mãos com diferentes configurações de confiança e número máximo de mãos.</li>
            <li>O modo GPU requer uma GPU compatível e pode melhorar o desempenho da aplicação em computadores com recursos limitados.</li>
       