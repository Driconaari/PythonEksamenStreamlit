import streamlit as st

st.set_page_config(page_title="Strategier", page_icon="💰")

st.title("💡 Strategier til at blive millionær")
st.subheader("Gode vaner og smarte valg gør forskellen!")

st.info("Du behøver ikke være rig for at blive millionær – men du skal være vedholdende, tålmodig og strategisk. Her er nogle gennemprøvede måder at komme tættere på dit mål:")

# Strategier i sektioner med emojis og tydelig inddeling
strategies = {
    "📈 Øg din indkomst": [
        "Tag et deltidsjob eller begynd at freelance.",
        "Forhandl dig til en højere løn.",
        "Start en lille virksomhed eller 'side hustle'."
    ],
    "💳 Sænk dine udgifter": [
        "Lav et realistisk budget og følg det.",
        "Skær ned på abonnementer og impulskøb.",
        "Overvej billigere bolig eller transport."
    ],
    "💼 Invester smart": [
        "Start tidligt med at investere – renters rente er din ven.",
        "Spred din risiko: aktier, fonde, ejendom m.m.",
        "Geninvester dine afkast løbende."
    ],
    "📚 Lær om økonomi": [
        "Læs bøger og blogs om privatøkonomi og investering.",
        "Tag gratis kurser online – fx via Coursera eller YouTube.",
        "Følg økonomi-podcasts og eksperter."
    ],
    "🎯 Sæt mål og følg op": [
        "Definér konkrete, målbare sparemål.",
        "Brug apps eller regneark til at holde overblik.",
        "Fejr små fremskridt undervejs!"
    ]
}

for title, bullets in strategies.items():
    st.markdown(f"### {title}")
    for tip in bullets:
        st.markdown(f"- {tip}")

# Sandkasse / Eksperiment
st.divider()
st.subheader("🎮 Leg med din økonomi – Sandkasse")

st.markdown("""
Har du været inde og ændre på tallene i beregneren? Det er her, magien sker!

👉 Gå tilbage til **Millionærberegneren** og test, hvordan forskellige beløb, rentesatser og tidsrammer påvirker din vej til millionen.
""")

st.success("Tip: Det er bedre at starte småt end aldrig at komme i gang 💪")
