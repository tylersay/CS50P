from fpdf import FPDF

class PDF():
    def __init__(self):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 10, "CS50 Shirtificate", align="C")

    def shirtify(self, name):
        self._pdf.image("shirtificate.png", x=0, y=60)
        self._pdf.set_font("helvetica", "B", 30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(50,180, f"{name} took CS50")

    def save(self, name):
        self._pdf.output(f"{name}.pdf")

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.shirtify(name)
    pdf.save("shirtificate")



if __name__ == "__main__":
    main()