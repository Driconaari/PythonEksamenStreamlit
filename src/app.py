import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.calculations import calculate_years_to_millionaire, suggest_investment_options

def calculate_savings_over_time(current, monthly, rate, years):
    """Returner en liste med opsparingens udvikling år for år."""
    savings = []
    total = current
    for year in range(1, years + 1):
        for _ in range(12):
            total = total * (1 + rate / 100 / 12) + monthly
        savings.append(total)
    return savings

def show_about_page():
    st.title("Hvad er renter, renters rente og hvordan udnytter du det?")
    st.markdown("""
**Rente** er det beløb, du får for at have penge stående på en konto eller investeret.  
**Renters rente** betyder, at du får rente af både dine egne penge og de renter, du tidligere har fået.  
Det gør, at din opsparing vokser hurtigere over tid!

### Eksempel på renters rente
Hvis du investerer 10.000 kr. med 7% i årlig rente, har du efter 10 år:
- Uden renters rente: 10.000 kr. + (10 x 700 kr.) = 17.000 kr.
- Med renters rente: ca. 19.672 kr.

Jo længere tid og jo højere rente, jo større effekt!

### Sådan udnytter du renters rente:
- **Start tidligt:** Jo før du starter, jo mere vokser din opsparing.
- **Invester regelmæssigt:** Små beløb hver måned gør en stor forskel over tid.
- **Geninvester renter:** Lad renterne blive investeret, så de også vokser.
- **Undgå at hæve penge:** Hver gang du hæver, mister du fremtidig vækst.

---
**Tip:** Brug grafen i denne app til at se, hvor meget renters rente betyder for din opsparing!
""")

def main():
    # Sidebar navigation
    page = st.sidebar.radio(
        "Vælg side / Choose page",
        ("Millionærberegner", "Om renter og opsparing")
    )

    if page == "Om renter og opsparing":
        show_about_page()
        return

    # Millionærberegneren
    lang = st.sidebar.selectbox("Sprog / Language", ["Dansk", "English"])
    currency = st.sidebar.selectbox("Valuta / Currency", ["DKK", "USD", "EUR"])
    currency_symbol = {"DKK": "kr", "USD": "$", "EUR": "€"}[currency]

    texts = {
        "Dansk": {
            "title": "Millionærberegner",
            "header": "Find ud af, hvornår du bliver millionær",
            "current": f"Indtast dine nuværende opsparing ({currency_symbol}):",
            "monthly": f"Indtast dit månedlige investeringsbeløb ({currency_symbol}):",
            "rate": "Forventet årlig rente (%):",
            "years": "Hvor mange år vil du simulere?:",
            "calc": "Beregn",
            "result": "Du bliver millionær om cirka {years} år.",
            "sooner": "For at nå dit mål hurtigere, overvej disse muligheder:",
            "ontrack": "Du er på rette vej til at blive millionær inden for din ønskede tidsramme!",
            "download": "Download opsparingsplan (CSV)",
            "graph": "Udvikling af opsparing over tid"
        },
        "English": {
            "title": "Millionaire Calculator",
            "header": "Determine When You'll Become a Millionaire",
            "current": f"Enter your current savings ({currency_symbol}):",
            "monthly": f"Enter your monthly investment ({currency_symbol}):",
            "rate": "Expected annual return rate (%):",
            "years": "How many years do you want to simulate?:",
            "calc": "Calculate",
            "result": "You will become a millionaire in approximately {years} years.",
            "sooner": "To reach your goal sooner, consider the following options:",
            "ontrack": "You're on track to become a millionaire within your desired timeline!",
            "download": "Download savings plan (CSV)",
            "graph": "Savings growth over time"
        }
    }
    t = texts[lang]

    st.title(t["title"])
    st.header(t["header"])

    # Initialiser session state hvis nødvendigt
    for key, default in [
        ("current_savings", 100_000),
        ("monthly_investment", 5_000),
        ("annual_return_rate", 7.0)
    ]:
        if key not in st.session_state:
            st.session_state[key] = default

    # Vælg input-metode
    input_method = st.radio(
        "Vælg hvordan du vil indtaste værdier / Choose input method",
        ("Slider", "Manuelt indtastet / Manual input"),
        horizontal=True
    )

    col1, col2 = st.columns(2)
    if input_method == "Slider":
        with col1:
            current_savings = st.slider(
                t["current"], 0, 2_000_000, int(st.session_state.current_savings), 10_000, key="current_savings_slider"
            )
            monthly_investment = st.slider(
                t["monthly"], 0, 50_000, int(st.session_state.monthly_investment), 500, key="monthly_investment_slider"
            )
            annual_return_rate = st.slider(
                t["rate"], 0.0, 20.0, float(st.session_state.annual_return_rate), 0.1, key="annual_return_rate_slider"
            )
        # Opdater session_state så inputfelter følger slideren
        st.session_state.current_savings = current_savings
        st.session_state.monthly_investment = monthly_investment
        st.session_state.annual_return_rate = annual_return_rate
    else:
        with col2:
            current_savings = st.number_input(
                t["current"], min_value=0.0, value=float(st.session_state.current_savings), step=100.0, key="current_savings_input"
            )
            monthly_investment = st.number_input(
                t["monthly"], min_value=0.0, value=float(st.session_state.monthly_investment), step=100.0, key="monthly_investment_input"
            )
            annual_return_rate = st.number_input(
                t["rate"], min_value=0.0, value=float(st.session_state.annual_return_rate), step=0.1, key="annual_return_rate_input"
            )
        # Opdater session_state så sliders følger inputfelterne
        st.session_state.current_savings = current_savings
        st.session_state.monthly_investment = monthly_investment
        st.session_state.annual_return_rate = annual_return_rate

    years_to_simulate = st.slider(t["years"], 1, 50, 30, 1)

    if st.button(t["calc"]):
        years_needed = calculate_years_to_millionaire(current_savings, monthly_investment, annual_return_rate)
        st.success(t["result"].format(years=years_needed))

        # Graf over opsparing
        savings = calculate_savings_over_time(current_savings, monthly_investment, annual_return_rate, years_to_simulate)
        df = pd.DataFrame({
            "År": list(range(1, years_to_simulate + 1)),
            "Opsparing": savings
        })
        fig, ax = plt.subplots()
        ax.plot(df["År"], df["Opsparing"], label="Opsparing")
        ax.axhline(1_000_000, color="red", linestyle="--", label="1 million")
        ax.set_xlabel("År")
        ax.set_ylabel(f"Opsparing ({currency_symbol})")
        ax.set_title(t["graph"])
        ax.legend()
        st.pyplot(fig)

        # Download-knap
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label=t["download"],
            data=csv,
            file_name="opsparing.csv",
            mime="text/csv"
        )

        # Ekstra info
        total_interest = savings[-1] - (current_savings + monthly_investment * 12 * years_to_simulate)
        st.info(f"Efter {years_to_simulate} år har du {savings[-1]:,.0f} {currency_symbol}. Renter har bidraget med {total_interest:,.0f} {currency_symbol}.")

        # Forslag hvis man ikke når målet hurtigt nok
        if years_needed > years_to_simulate:
            st.warning(t["sooner"])
            options = suggest_investment_options(current_savings, monthly_investment, years_to_simulate)
            for option in options:
                st.write(f"- {option}")
        else:
            st.success(t["ontrack"])

if __name__ == "__main__":
    main()