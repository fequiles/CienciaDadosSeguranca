# Author: Felipe Ribeiro Quiles
# Curso: Mestrado em Cienia da Computacao
# GRR: Ainda sem, mas ja aprovado para o mestrado 

from scapy.all import *

# Variaveis utilizadas
total_packets = 0
ip_packets = 0
udp_packets = 0
tcp_packets = 0
tcp_ss = 0
udp_ss = 0
sessoes_udp_payloads = {}
sessoes_tcp_payloads = {}
lista_sessoes_udp = []
lista_sessoes_tcp = []
n_sessoes_udp = 0
n_sessoes_tcp = 0

# Leitura do Arquivo
packets = PcapReader("trace.pcap")

# Percorre os pacotes capturados na rede
for packet in packets:
    total_packets += 1
    type = packet[Ether].type
    if type == 0x0800:          # Eh IPV4?
        ip_packets += 1
        protocol = packet[IP].proto
        ip_dst = packet[IP].dst         # IPs destino e origem
        ip_src = packet[IP].src 
        if protocol == 17:              # Verifica UDP
            udp_packets += 1
            sport = packet[IP].sport    # Portas destino e origem
            dport = packet[IP].dport
            sessao = {"dst": ip_dst, "src": ip_src, "dport": dport, "sport": sport}
            sessao_inv = {"dst": ip_src, "src": ip_dst, "dport": sport, "sport": dport}
            if (sessao not in lista_sessoes_udp) and (sessao_inv not in lista_sessoes_udp):             # Verifica se nova sessao UDP no IPV4
                lista_sessoes_udp.append(sessao)
                sessoes_udp_payloads[n_sessoes_udp] = []
                sessoes_udp_payloads[n_sessoes_udp].append(packet[UDP].payload)                         #Armazena Payload
                n_sessoes_udp += 1
            else:                                                               #Sessao ja existente
                if (sessao in lista_sessoes_udp):
                    index = lista_sessoes_udp.index(sessao)
                    sessoes_udp_payloads[index].append(packet[UDP].payload)                             #Armazena Payload
                else:
                    if (sessao_inv in lista_sessoes_udp):
                        index = lista_sessoes_udp.index(sessao_inv)
                        sessoes_udp_payloads[index].append(packet[UDP].payload)                         #Armazena Payload

        if protocol == 6:               # Verifica TCP
            tcp_packets += 1
            sport = packet[IP].sport    # Portas destino e origem
            dport = packet[IP].dport
            sessao = {"dst": ip_dst, "src": ip_src, "dport": dport, "sport": sport}
            sessao_inv = {"dst": ip_src, "src": ip_dst, "dport": sport, "sport": dport}
            sessao = {"dst": ip_dst, "src": ip_src, "dport": dport, "sport": sport}
            sessao_inv = {"dst": ip_src, "src": ip_dst, "dport": sport, "sport": dport}
            if (sessao not in lista_sessoes_tcp) and (sessao_inv not in lista_sessoes_tcp):             # Verifica se nova sessao TCP no IPV4
                lista_sessoes_tcp.append(sessao)
                sessoes_tcp_payloads[n_sessoes_tcp] = []
                sessoes_tcp_payloads[n_sessoes_tcp].append(packet[TCP].payload)                         #Armazena Payload
                n_sessoes_tcp += 1
            else:                                                               #Sessao ja existente
                if (sessao in lista_sessoes_tcp):
                    index = lista_sessoes_tcp.index(sessao)
                    sessoes_tcp_payloads[index].append(packet[TCP].payload)                             #Armazena Payload
                else:
                    if (sessao_inv in lista_sessoes_tcp):
                        index = lista_sessoes_tcp.index(sessao_inv)
                        sessoes_tcp_payloads[index].append(packet[TCP].payload)                         #Armazena Payload

    if type == 0x86DD:          # Eh IPV6?
        ip_packets += 1
        protocol = packet[IPv6].nh
        ip_dst = packet[IPv6].dst       # IPs destino e origem
        ip_src = packet[IPv6].src
        if protocol == 17:              # Verifica UDP
            udp_packets += 1
            sport = packet[IPv6].sport  # Portas destino e origem
            dport = packet[IPv6].dport
            sessao = {"dst": ip_dst, "src": ip_src, "dport": dport, "sport": sport}
            sessao_inv = {"dst": ip_src, "src": ip_dst, "dport": sport, "sport": dport}
            if (sessao not in lista_sessoes_udp) and (sessao_inv not in lista_sessoes_udp):         # Verifica se nova sessao UDP no IPV6
                lista_sessoes_udp.append(sessao)
                sessoes_udp_payloads[n_sessoes_udp] = []
                sessoes_udp_payloads[n_sessoes_udp].append(packet[UDP].payload)                     #Armazena Payload
                n_sessoes_udp += 1
            else:                                                           #Sessao ja existente
                if (sessao in lista_sessoes_udp):
                    index = lista_sessoes_udp.index(sessao)
                    sessoes_udp_payloads[index].append(packet[UDP].payload)                         #Armazena Payload
                else:
                    if (sessao_inv in lista_sessoes_udp):
                        index = lista_sessoes_udp.index(sessao_inv)
                        sessoes_udp_payloads[index].append(packet[UDP].payload)                     #Armazena Payload
        if protocol == 6:               # Verifica TCP
            tcp_packets += 1
            sport = packet[IPv6].sport  # Portas destino e origem
            dport = packet[IPv6].dport
            sessao = {"dst": ip_dst, "src": ip_src, "dport": dport, "sport": sport}
            sessao_inv = {"dst": ip_src, "src": ip_dst, "dport": sport, "sport": dport}
            if (sessao not in lista_sessoes_tcp) and (sessao_inv not in lista_sessoes_tcp):         # Verifica se nova sessao TCP no IPV6
                lista_sessoes_tcp.append(sessao)
                sessoes_tcp_payloads[n_sessoes_tcp] = []
                sessoes_tcp_payloads[n_sessoes_tcp].append(packet[TCP].payload)                     #Armazena Payload
                n_sessoes_tcp += 1
            else:                                                               #Sessao ja existente 
                if (sessao in lista_sessoes_tcp):
                    index = lista_sessoes_tcp.index(sessao)
                    sessoes_tcp_payloads[index].append(packet[TCP].payload)                         #Armazena Payload
                else:
                    if (sessao_inv in lista_sessoes_tcp):
                        index = lista_sessoes_tcp.index(sessao_inv)
                        sessoes_tcp_payloads[index].append(packet[TCP].payload)                     #Armazena Payload

# Impressao dos dados
print (str(total_packets) + " pacotes no total")
print (str(ip_packets) + " pacotes IP")
print (str(tcp_packets) + " pacotes TCP")
print (str(udp_packets) + " pacotes UDP")
print (str(n_sessoes_tcp) + " sessões TCP")
print (str(n_sessoes_udp) + " sessões UDP")
print (str(total_packets - ip_packets) + " pacotes não-IP")









