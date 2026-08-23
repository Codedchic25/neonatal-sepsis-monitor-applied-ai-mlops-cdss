"""NICU Sepsis Monitor AI - PDF Export Engine.

This module automates the generation of structural clinical documentation using ReportLab.
It dynamically embeds clinical variables, parsed AI guardrail data, and plots a localized
biomarker trend chart for historical telemetry reference.
"""

from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def draw_biomarker_chart(df_history) -> Drawing:
    """Generates a secure, native vector-based LinePlot within a ReportLab Drawing canvas.

    Prevents empty canvas generation by implementing strict data dimension fallbacks.
    """
    drawing = Drawing(450, 160)

    # Simple default message panel if telemetry contains insufficient data steps
    if df_history is None or df_history.empty or len(df_history) < 2:
        drawing.add(
            Rect(
                0,
                0,
                450,
                160,
                fillColor=colors.HexColor("#F8FAFC"),
                strokeColor=colors.HexColor("#CBD5E1"),
            )
        )
        drawing.add(
            String(
                130,
                75,
                "Insufficient tracking points to plot clearance curves.",
                fontName="Helvetica-Bold",
                fontSize=10,
                fillColor=colors.HexColor("#64748B"),
            )
        )
        return drawing

    # Format dataframe data fields explicitly for ReportLab's multi-series plot requirements [(x1,y1), (x2,y2)...]
    crp_data = []
    pct_data = []

    for idx, row in df_history.iterrows():
        # X axis can be mapped chronologically over numerical indices for clean scaling
        crp_data.append((idx, float(row["crp"])))
        pct_data.append((idx, float(row["pct"])))

    compiled_plot_data = [crp_data, pct_data]

    # Initialize professional laboratory grid line plot
    lp = LinePlot()
    lp.x = 40
    lp.y = 25
    lp.height = 110
    lp.width = 380
    lp.data = compiled_plot_data
    lp.joinedLines = 1

    # Stylize Marker 1: C-Reactive Protein (Blue Line Profile)
    lp.lines[0].strokeColor = colors.HexColor("#2563EB")
    lp.lines[0].strokeWidth = 2

    # Stylize Marker 2: Procalcitonin (Green Line Profile)
    lp.lines[1].strokeColor = colors.HexColor("#16A34A")
    lp.lines[1].strokeWidth = 2

    drawing.add(lp)
    return drawing


def generate_clinical_pdf(
    file_path, metadata, parsed_xml_data, df_history=None
) -> None:
    """Compiles local real-time clinical parameters and active AI summaries into a PDF document.

    All diagnostic tracking elements and emergency local console alert logs are fully
    documented within the generated snapshot report for strict shift audit trail compliance.
    """
    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )
    story = []
    styles = getSampleStyleSheet()

    # Custom Medical Document Typography Settings
    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=12,
    )
    section_style = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=12,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "ReportBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#334155"),
    )
    ai_box_style = ParagraphStyle(
        "AIResponseBox",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#1E293B"),
    )

    # 1. HEADER SECTION
    story.append(Paragraph("Sepsis Monitor AI - Clinical Report", title_style))
    story.append(
        Paragraph(
            f"<b>Telemetry Timestamp:</b> {metadata.get('timestamp', 'N/A')} UTC",
            body_style,
        )
    )
    story.append(
        Paragraph(
            f"<b>Authorized Practitioner Role:</b> {metadata.get('role', 'N/A')}",
            body_style,
        )
    )
    story.append(Spacer(1, 10))

    # 2. PATIENT CONTEXT PROFILE TABLE
    story.append(Paragraph("1. Initial Baseline Configuration", section_style))
    profile_data = [
        [
            Paragraph("<b>Parameter Matrix</b>", body_style),
            Paragraph("<b>Active Interface Entry</b>", body_style),
        ],
        [
            Paragraph("Gestational Profile", body_style),
            Paragraph(str(metadata.get("gestational", "N/A")), body_style),
        ],
        [
            Paragraph("Configured Patient Weight", body_style),
            Paragraph(f"{metadata.get('weight', 0.0):.2f} kg", body_style),
        ],
        [
            Paragraph("Renal Function Tracker (AKI Menu)", body_style),
            Paragraph(str(metadata.get("renal", "N/A")), body_style),
        ],
        [
            Paragraph("Kangaroo Care Interaction", body_style),
            Paragraph(str(metadata.get("kangaroo", "N/A")), body_style),
        ],
        [
            Paragraph("Music Therapy State", body_style),
            Paragraph(str(metadata.get("music", "N/A")), body_style),
        ],
    ]
    t_profile = Table(profile_data, colWidths=[220, 280])
    t_profile.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (1, 0), colors.HexColor("#F1F5F9")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ("PADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(t_profile)
    story.append(Spacer(1, 10))

    # 3. REAL-TIME SENSOR METRICS TABLE
    story.append(Paragraph("2. Active Sensor Grid Real-Time Frame", section_style))
    vitals_data = [
        [
            Paragraph(f"Heart Rate: <b>{metadata.get('hr', 0)} bpm</b>", body_style),
            Paragraph(
                f"Temperature: <b>{metadata.get('temp', 0.0)} °C</b>",
                body_style,
            ),
        ],
        [
            Paragraph(
                f"Oxygen Saturation (SpO2): <b>{metadata.get('spo2', 0)}%</b>",
                body_style,
            ),
            Paragraph(
                f"Blood Pressure (BP): <b>{metadata.get('bp', 'N/A')}</b>",
                body_style,
            ),
        ],
        [
            Paragraph(
                f"C-Reactive Protein (CRP): <b>{metadata.get('crp', 0.0)} mg/L</b>",
                body_style,
            ),
            Paragraph(
                f"Procalcitonin (PCT): <b>{metadata.get('pct', 0.0)} ng/mL</b>",
                body_style,
            ),
        ],
    ]
    t_vitals = Table(vitals_data, colWidths=[250, 250])
    t_vitals.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
                ("PADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(t_vitals)
    story.append(Spacer(1, 10))

    # 4. HISTORICAL CLEARANCE CANVA (PCR / PCT GRAPH PLOT)
    story.append(
        Paragraph(
            "3. Historical Biomarker Levels (Blue: CRP | Green: PCT)", section_style
        )
    )
    story.append(draw_biomarker_chart(df_history))
    story.append(Spacer(1, 10))

    # 5. AI GUARDRAILS INTERPOLATED RESPONSES
    story.append(
        Paragraph("4. AI Decision Support & Active Guardrail Outputs", section_style)
    )

    # Analytical Layer Block
    story.append(Paragraph("<b>[Clinical Analysis & Report Summary]</b>", body_style))
    story.append(
        Paragraph(parsed_xml_data.get("raport", "No analysis tracked."), ai_box_style)
    )
    story.append(Spacer(1, 8))

    # Medication Guidelines Block
    story.append(
        Paragraph("<b>[Individualized Medication & Dose Architecture]</b>", body_style)
    )
    story.append(
        Paragraph(
            parsed_xml_data.get("medicatie", "No protocol execution registered."),
            ai_box_style,
        )
    )
    story.append(Spacer(1, 8))

    # Family-Centered Care Summary Block
    story.append(
        Paragraph("<b>[Family-Centered Care (FCC) Co-Validation]</b>", body_style)
    )
    story.append(
        Paragraph(
            parsed_xml_data.get("fcc", "No FCC metric summary loaded."), ai_box_style
        )
    )

    # Execute document builder compilation
    doc.build(story)
