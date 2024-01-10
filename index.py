import time
import keyboard

def perguntar_sobre_estudos():
    print("Bot de Estudos: Olá! Como posso ajudar você nos seus estudos hoje?")
    print("1. Configurar tempo de estudo")
    print("2. Configurar tempo de pausa")
    print("3. Configurar tempo final")
    print("4. Perguntar sobre provas e conteúdo")
    print("5. Iniciar cronômetro de estudo")
    print("6. Sair")

def configurar_tempo(tipo):
    tempo = int(input(f"Digite o tempo de {tipo} em minutos: "))
    return tempo * 60  # Convertendo para segundos

def perguntar_sobre_provas():
    provas = input("Quais serão as suas provas deste semestre? ")
    conteudo = input("Qual conteúdo irá cair nelas? ")
    tempo_estudo = int(input("Quanto tempo você pretende estudar por dia? (em minutos) "))
    return provas, conteudo, tempo_estudo * 60  # Convertendo para segundos

def iniciar_cronometro(tempo_total):
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= tempo_total:
            print("Tempo de estudo concluído. Parabéns!")
            break

        print(f"Tempo estudado: {int(elapsed_time/60)} minutos", end='\r')
        time.sleep(1)

def main():
    tempo_estudo = 0
    tempo_pausa = 0
    tempo_final = 0

    while True:
        perguntar_sobre_estudos()
        opcao = input("Escolha uma opção (1-6): ")

        if opcao == '1':
            tempo_estudo = configurar_tempo("estudo")
        elif opcao == '2':
            tempo_pausa = configurar_tempo("pausa")
        elif opcao == '3':
            tempo_final = configurar_tempo("final")
        elif opcao == '4':
            provas, conteudo, tempo_estudo = perguntar_sobre_provas()
        elif opcao == '5':
            tempo_total = tempo_estudo + tempo_pausa + tempo_final
            print("Iniciando cronômetro. Pressione 'Ctrl + C' para interromper.")
            try:
                iniciar_cronometro(tempo_total)
            except KeyboardInterrupt:
                print("\nCronômetro interrompido pelo usuário.")
        elif opcao == '6':
            print("Saindo do bot de estudos. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()