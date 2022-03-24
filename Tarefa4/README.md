## Tarefa 4 - Exploração dos Dados

##### Crie um vetor de características com seus dados
O vetor é composto por 79 características.
##### Utilize os rótulos das amostras como classes (é um problema binário ou multiclasse?)
    É um problema binário, no qual as amostras são classificadas entre fluxos Benignos e DDoS. Houve um tratamento no dado, sendo alterado o valor de “benign” para 0 e “ddos” para 1.
##### Inclua os rótulos como última posição do vetor de características, um por amostra, indexando como "classe"
    A inclusão do rótulo como última posição do vetor de características faz com que o vetor tenha agora 80 colunas, com o rótulo como última posição.

##### Abaixo é possível verificar o cabeçalho do vetor de características, após mudanças.

['Src Port', 'Dst Port', 'Protocol', 'Flow Duration', 'Tot Fwd Pkts', 
'Tot Bwd Pkts', 'TotLen Fwd Pkts', 'TotLen Bwd Pkts', 'Fwd Pkt Len Max', 
'Fwd Pkt Len Min', 'Fwd Pkt Len Mean', 'Fwd Pkt Len Std', 
'Bwd Pkt Len Max', 'Bwd Pkt Len Min', 'Bwd Pkt Len Mean',
'Bwd Pkt Len Std', 'Flow Byts/s', 'Flow Pkts/s', 'Flow IAT Mean', 
'Flow IAT Std', 'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Tot', 
'Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min',
'Bwd IAT Tot', 'Bwd IAT Mean', 'Bwd IAT Std', 'Bwd IAT Max', 
'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags', 'Fwd URG Flags', 
'Bwd URG Flags', 'Fwd Header Len', 'Bwd Header Len', 'Fwd Pkts/s', 
'Bwd Pkts/s', 'Pkt Len Min', 'Pkt Len Max', 'Pkt Len Mean', 'Pkt Len Std', 
'Pkt Len Var', 'FIN Flag Cnt', 'SYN Flag Cnt', 'RST Flag Cnt', 
'PSH Flag Cnt', 'ACK Flag Cnt', 'URG Flag Cnt', 'CWE Flag Count', 
'ECE Flag Cnt', 'Down/Up Ratio', 'Pkt Size Avg', 'Fwd Seg Size Avg', 
'Bwd Seg Size Avg', 'Fwd Byts/b Avg', 'Fwd Pkts/b Avg', 
'Fwd Blk Rate Avg', 'Bwd Byts/b Avg', 'Bwd Pkts/b Avg', 
'Bwd Blk Rate Avg', 'Subflow Fwd Pkts', 'Subflow Fwd Byts', 
'Subflow Bwd Pkts', 'Subflow Bwd Byts', 'Init Fwd Win Byts', 
'Init Bwd Win Byts', 'Fwd Act Data Pkts', 'Fwd Seg Size Min', 
'Active Mean', 'Active Std', 'Active Max', 'Active Min', 'Idle Mean', 
'Idle Std', 'Idle Max', 'Idle Min', 'Classe']

##### Apresente graficamente a distribuição dos seus dados por classe em um gráfico de barras (quantas amostras por classe)

(https://github.com/fequiles/CienciaDadosSeguranca/blob/main/Tarefa4/Benign_X_DDoS.png)

O dataset tem 12794627 datapoints, sendo 51% classificados como benigno e 49% classificados como DDoS, mas a quantidade de bytes para armazenar a totalidade destes dados é extremamente alta. Dessa forma, para se seguir com o projeto e também visando o treinamento de um algoritmo de aprendizado de máquina, foi realizado uma seleção aleatória de 500 amostras benignas e 500 amostras DDoS, finalizando em 50% de cada classe. A quantidade de amostras pode sofrer alterações no prosseguimento do projeto, podendo aumentar ou diminuir, mas a princípio será mantida a divisão de 50% de amostras para cada classe.

