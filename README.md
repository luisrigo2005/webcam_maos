## Rastreamento de Mãos
### Visão Geral
Essa é uma aplicação de rastreamento de mãos desenvolvida utilizando OpenCV e o módulo HandTrackingModule do cvzone. A aplicação usa uma webcam para capturar vídeo e detectar mãos em tempo real.

## Recursos
Detecta mãos em tempo real usando uma webcam <br>
Exibe o vídeo com marcações de rastreamento de mãos <br>
Suporta até 6 mãos <br>
Confiança de detecção ajustável<br>
Opcionalmente, pode utilizar a GPU do computador para acelerar o processamento<br>

## Requisitos
OpenCV (versão 4.x ou superior)<br>
cvzone (versão 1.x ou superior)<br>
Python (versão 3.x ou superior)<br>
GPU (opcional)

## Uso
## Modo CPU
Clone o repositório e navegue até o diretório do projeto<br>
Execute o script script.py usando python script.py<br>
A aplicação começará a capturar vídeo da webcam padrão e exibirá as marcações de rastreamento de mãos<br>
Pressione 'q' para sair da aplicação<br>

## Modo GPU
Clone o repositório e navegue até o diretório do projeto<br>
Execute o script script_gpu.py usando python script_gpu.py<br>
A aplicação começará a capturar vídeo da webcam padrão e exibirá as marcações de rastreamento de mãos, utilizando a GPU do computador para acelerar o processamento<br>
Pressione 'q' para sair da aplicação

## Configuração
A aplicação usa as seguintes configurações:<br><br>

detectionCon=0.6: define a confiança de detecção para 0.6 (ajustável)<br>
maxHands=6: define o número máximo de mãos a detectar para 6 (ajustável)

## Licença
Essa aplicação é licenciada sob a Licença MIT. Veja LICENSE para detalhes.

## Autor
Luís Rigo

## Agradecimentos
Essa aplicação usa o módulo HandTrackingModule do cvzone, que é desenvolvido pelos autores do cvzone.

## Observações
Certifique-se de que a webcam esteja configurada corretamente antes de executar a aplicação.<br>
A aplicação pode ser ajustada para detectar mãos com diferentes configurações de confiança e número máximo de mãos.<br>
O modo GPU requer uma GPU compatível e pode melhorar o desempenho da aplicação em computadores com recursos limitados.<br><br>