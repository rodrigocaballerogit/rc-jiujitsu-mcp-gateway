from datetime import datetime

PROFESSORS: dict[str, dict] = {
    "zurdo": {
        "name":  "Alejandro Zurdo",
        "phone": "524428242114",
        "gym":   "Zurdos MMA",
        "city":  "Querétaro",
    },
    "nestor": {
        "name":  "Néstor Aguirre",
        "phone": "524421458290",
        "gym":   "Dracarys Jiu Jitsu Club",
        "city":  "Irapuato",
    },
    "ramon": {
        "name":  "Ramón Jiménez",
        "phone": None,
        "gym":   "RC Jiu Jitsu Querétaro",
        "city":  "Querétaro",
    },
}


def send_whatsapp(professor_key: str, message: str, to: str = "") -> dict:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prof = PROFESSORS.get(professor_key)

    if prof is None:
        return {"ok": False, "error": f"Profesor '{professor_key}' no encontrado"}

    if prof["phone"] is None:
        print(f"\n[{ts}] WhatsApp PENDIENTE — {prof['name']} no tiene número configurado aún")
        return {"ok": True, "simulated": True, "note": "Número pendiente, lead guardado"}

    print(f"\n[{ts}] -- WhatsApp SIMULADO ---------------------------")
    print(f"  Para:    {prof['name']} (+{prof['phone']})")
    print(f"  Mensaje:\n{message}")
    print(f"---------------------------------------------------\n")

    return {"ok": True, "simulated": True, "to": prof["phone"], "professor": prof["name"]}


def build_message(lead_name: str, lead_phone: str, lead_city: str, professor_key: str) -> str:
    prof = PROFESSORS.get(professor_key, {})
    return (
        f"*Nuevo lead — RC Jiu Jitsu*\n\n"
        f"Nombre: {lead_name}\n"
        f"Teléfono: {lead_phone}\n"
        f"Ciudad: {lead_city}\n\n"
        f"Quiere una clase de prueba en {prof.get('gym', '')}."
    )
