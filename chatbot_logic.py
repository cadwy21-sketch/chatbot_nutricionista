def get_bot_response(message):
    message = message.lower()
    if "hola" in message:
        return "¡Hola! Soy tu asistente de salud física y mental. ¿Cómo puedo ayudarte?"
    elif "cita" in message:
        return "Puedes agendar una cita enviando un WhatsApp al +593 999 999 999."
    elif "nutrición" in message or "alimentación" in message:
        return "Una alimentación balanceada incluye frutas, verduras, proteínas y agua."
    elif "estrés" in message or "salud mental" in message:
        return "Para mejorar tu salud mental, intenta dormir bien, hacer ejercicio y hablar con alguien."
    elif "gracias" in message:
        return "¡De nada! Estoy aquí para ayudarte."
    else:
        return "Lo siento, aún estoy aprendiendo. ¿Puedes preguntarme otra cosa?"

