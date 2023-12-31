import openai
import config
import sys  # Importa el módulo sys para usar sys.exit()

def obtener_respuesta(pregunta, temperatura=0.7):
    try:
        openai.api_key = config.api_key

        # Agrega la pregunta del usuario a las conversaciones
        conversation = [
            {"role": "system", "content": "Eres un profesor que enseña transformar un numero entero a binario"},
            {"role": "user", "content": pregunta}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=temperatura
        )

        # Accede al contenido directamente
        respuesta = response['choices'][0]['message']['content'].strip()
        return respuesta

    except Exception as e:
        return f"Se produjo un error: {e}"

# Bucle para interactuar con el asistente
while True:
    pregunta_usuario = input("Pregunta: ")

    # Salir del bucle si el usuario ingresa "salir"
    if pregunta_usuario.lower() == "salir":
        print("Saliendo del programa...")
        sys.exit()  # Finaliza la ejecución del programa

    # Obtener y mostrar la respuesta del asistente con la temperatura predeterminada (0.7)
    respuesta_asistente = obtener_respuesta(pregunta_usuario)
    print("Respuesta del asistente:", respuesta_asistente)
    # Obtener y mostrar la respuesta del asistente con la temperatura predeterminada (0.7)
    respuesta_asistente = obtener_respuesta(pregunta_usuario)
    print("Respuesta del asistente:", respuesta_asistente)
