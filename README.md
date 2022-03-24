# CienciaDadosSeguranca
Repositório criado para armazenar tarefas e projetos realizados na disciplina de Ciência de dados para Segurança

## Tarefa 1
Crie um script que leia o arquivo capturado (pcap) e analise os dados dos pacotes

## Tarefa 3

Gerar um scatterplot do dataset escolhido e analisar os resultados. Além de analisar o dataset escolhido.
O dataset se mostrou muito grande (Travando meu pc :( ). Dessa forma, houve uma diminuição no número de amostras para 
Informações obtidas:

##### Quantidade de amostras
O dataset é composto por 12794627 datapoints
Cada datapoint corresponde a um fluxo (ida e volta)

**OBS:** Para a geração do scatterplot foi utilizado um dataset parcial de 100 mil amostras.

##### Classificação
Os datapoints são classificados em :
- Benigno (49%)
- DDoS (51%)

**OBS:** Para a geração do scatterplot foi utilizado um dataset tinha 50% de amostras de ddos e 50% de amostras benignas

##### Características
Os datapoints são compostos de 84 características, sendo elas:
| NOME | DESCRIÇÃO |
| ------ | ------ |
| FlowID | Identificador do fluxo |
| SRC IP | IP de Origem |
| SRC Port * | Porta de Origem |
| DST IP | IP de Destino |
| DST Port  * | Porta de Destino |
| Protocolo | Protocolo utilizado |
| Timestamp | Marca Temporal |
| fl_dur * |	Flow duration |
| tot_fw_pk * |	Total packets in the forward direction |
| tot_bw_pk * |	Total packets in the backward direction |
| tot_l_fw_pkt |	Total size of packet in forward direction |
| tot_l_bw_pkt |	Total size of packet in backward direction |
| fw_pkt_l_max |	Maximum size of packet in forward direction |
| fw_pkt_l_min |	Minimum size of packet in forward direction |
| fw_pkt_l_avg |	Average size of packet in forward direction |
| fw_pkt_l_std |	Standard deviation size of packet in forward direction |
| Bw_pkt_l_max |	Maximum size of packet in backward direction |
| Bw_pkt_l_min |	Minimum size of packet in backward direction|
| Bw_pkt_l_avg |	Mean size of packet in backward direction|
| Bw_pkt_l_std |	Standard deviation size of packet in backward direction|
| fl_byt_s * |	flow byte rate that is number of packets transferred per second|
| fl_pkt_s * |	flow packets rate that is number of packets transferred per second|
| fl_iat_avg |	Average time between two flows|
| fl_iat_std |	Standard deviation time two flows|
| fl_iat_max |	Maximum time between two flows|
| fl_iat_min |	Minimum time between two flows|
| fw_iat_tot |	Total time between two packets sent in the forward direction|
| fw_iat_avg |	Mean time between two packets sent in the forward direction|
| fw_iat_std |	Standard deviation time between two packets sent in the forward direction|
| fw_iat_max |	Maximum time between two packets sent in the forward direction|
| fw_iat_min |	Minimum time between two packets sent in the forward direction|
| bw_iat_tot |	Total time between two packets sent in the backward direction||
| bw_iat_avg |	Mean time between two packets sent in the backward direction|
| bw_iat_std |	Standard deviation time between two packets sent in the backward direction||
| bw_iat_max |	Maximum time between two packets sent in the backward direction|
| bw_iat_min |	Minimum time between two packets sent in the backward direction|
| fw_psh_flag |	Number of times the PSH flag was set in packets travelling in the forward direction (0 for UDP)|
| bw_psh_flag |	Number of times the PSH flag was set in packets travelling in the backward direction (0 for UDP)|
| fw_urg_flag |	Number of times the URG flag was set in packets travelling in the forward direction (0 for UDP)|
| bw_urg_flag |	Number of times the URG flag was set in packets travelling in the backward direction (0 for UDP)|
| fw_hdr_len |	Total bytes used for headers in the forward direction|
| bw_hdr_len |	Total bytes used for headers in the forward direction|
| fw_pkt_s * |	Number of forward packets per second|
| bw_pkt_s *	|Number of backward packets per second|
| pkt_len_min | 	Minimum length of a flow|
| pkt_len_max |	Maximum length of a flow|
| pkt_len_avg |	Mean length of a flow|
| pkt_len_std |	Standard deviation length of a flow|
| pkt_len_va |	Minimum inter-arrival time of packet|
| fin_cnt |	Number of packets with FIN|
| syn_cnt |	Number of packets with SYN|
| rst_cnt |	Number of packets with RST|
| pst_cnt |	Number of packets with PUSH|
| ack_cnt |	Number of packets with ACK|
| urg_cnt |	Number of packets with URG|
| cwe_cnt |	Number of packets with CWE|
| ece_cnt |	Number of packets with ECE|
| down_up_ratio |	Download and upload ratio|
| pkt_size_avg * | 	Average size of packet|
| fw_seg_avg |	Average size observed in the forward direction|
| bw_seg_avg |	Average size observed in the backward direction|
| fw_byt_blk_avg |	Average number of bytes bulk rate in the forward direction|
| fw_pkt_blk_avg |	Average number of packets bulk rate in the forward direction|
| fw_blk_rate_avg |	Average number of bulk rate in the forward direction|
| bw_byt_blk_avg |	Average number of bytes bulk rate in the backward direction|
| bw_pkt_blk_avg |	Average number of packets bulk rate in the backward direction|
| bw_blk_rate_avg |	Average number of bulk rate in the backward direction|
| subfl_fw_pk |	The average number of packets in a sub flow in the forward direction|
| subfl_fw_byt 	| The average number of bytes in a sub flow in the forward direction|
| subfl_bw_pkt |	The average number of packets in a sub flow in the backward direction|
| subfl_bw_byt | 	The average number of bytes in a sub flow in the backward direction|
| fw_win_byt |	Number of bytes sent in initial window in the forward direction|
| bw_win_byt |	# of bytes sent in initial window in the backward direction|
| Fw_act_pkt |	# of packets with at least 1 byte of TCP data payload in the forward direction|
| fw_seg_min |	Minimum segment size observed in the forward direction|
| atv_avg |	Mean time a flow was active before becoming idle|
| atv_std |	Standard deviation time a flow was active before becoming idle|
| atv_max |	Maximum time a flow was active before becoming idle|
| atv_min |	Minimum time a flow was active before becoming idle|
| idl_avg |	Mean time a flow was idle before becoming active|
| idl_std |	Standard deviation time a flow was idle before becoming active|
| idl_max |	Maximum time a flow was idle before becoming active|
| idl_min |	Minimum time a flow was idle before becoming active|
| label * | Classificação |

**OBS:** *Características que fizeram parte do scatterplot 

##### Distinguiveis?
Não, os dados não se mostraram distinguíveis entre si quando se compara pela classe dos mesmos

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

[Benign X DDoS](https://github.com/fequiles/CienciaDadosSeguranca/blob/main/Tarefa4/Benign_X_DDoS.png)
O dataset tem 12794627 datapoints, sendo 51% classificados como benigno e 49% classificados como DDoS, mas a quantidade de bytes para armazenar a totalidade destes dados é extremamente alta. Dessa forma, para se seguir com o projeto e também visando o treinamento de um algoritmo de aprendizado de máquina, foi realizado uma seleção aleatória de 500 amostras benignas e 500 amostras DDoS, finalizando em 50% de cada classe. A quantidade de amostras pode sofrer alterações no prosseguimento do projeto, podendo aumentar ou diminuir, mas a princípio será mantida a divisão de 50% de amostras para cada classe.





