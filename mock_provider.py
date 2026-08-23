def call_api(prompt, options, context):
    """Mock API provider pentru Promptfoo, rulează 100% offline."""
    mock_output = (
        "<RAPORT>\n"
        "Sinteză Clinică Locală: Telemetrie neonatală stabilă. Monitorizare activă.\n"
        "</RAPORT>\n"
        "<MEDICATIE>\n"
        "Validare Protocol: Tratament medicamentos conform schemei ponderale.\n"
        "</MEDICATIE>\n"
        "<FCC>\n"
        "Suport Familie: Monitorizare locală activă în parametri normali.\n"
        "</FCC>"
    )

    return {"output": str(mock_output)}
