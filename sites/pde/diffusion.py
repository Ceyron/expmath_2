import streamlit as st

def diffusion():
    st.components.v1.iframe(
        src="http://expmath.math.nat.tu-bs.de:9001/waermeleitung",
        width=1000,
        height=430
    )

details = {
    "german": {
        "title": "Wärmeleitung in einem Stab",
        "introduction": "Some Words",
        "theory": [
            (
                "Diffusive Wärmeleitung",
                r"""
                Wärme fließt vom heißen Potential zum kalten. Das macht den
                Fluss durche ein Medium proportional zum negativen Gradienten
                des Temperaturfeldes $F \propto - \nabla u$. Dieser
                Potentialausgleich heißt Diffusion.

                Der diffusive Wärmetransport unterscheidet sich vom
                Wärmeaustausch durch Konvektion dadurch, dass keine Teilchen
                transportiert werden.

                Die dritte Form der Wärmeübertragung ist die Wärmestrahlung,
                also eine Energieübertragung durch elektromagnetische Wellen.
                """
            ),
            (
                "Vom Temperaturgradienten zum Fluss",
                r"""
                Zur quantitativen Beschreibung der Stärke des Flusses wird die
                konstitutive Gleichung benötigt. Diese enthält Informationen
                über die Beschaffenheit des Materials.

                Für ein inhomogenes anisotropes Material ist die konstitutive
                    Gleichung $I =A (\mathbf{x}) u$. Der Wärmefluss ist also
                    abhängig vom Ort $\mathbf{x}$ (inhomogen) und der Richtung
                    (anisotrop).

                Für ein inhomogenens isotropes Material ist der Wärmefluss nicht
                    richtungsabhängig, $I =a(\mathbf{x}) u$.

                Im Fall eines homogenen, isotropen Materials ist die
                    konstitutive Gleichung $I= a u$ mit $a \in \mathbb{R}.$
                """
            ),
            (
                "Die Wärmeleitungsgleichung",
                r"""
                Fließt Wärme, so ändert sich auch die Temperatur. Dieser
                Zusammenhang wird in der Kontinuitätsgleichung deutlich. Eine
                zeitliche Änderung der Temperatur wird durch die negative
                Divergenz des Wärmeflusses hervorgerufen
                $\frac{\partial}{\partial t} u = - \nabla I (t,\mathbf{x}) .$

                Zusammen mit der Kontinuitätsgleichung für den Fluss erhält man
                für ein inhomogenes, anisotropes Material die
                Wärmeleitungsgleichung $u_{,t}= \nabla \cdot ( A(\mathbf{x})
                \nabla u)$.
                """
            ),
            (
                "Bedienung der Graphik",
                r"""
                In der Graphik wird die Temperaturverteilung in einem dünnen Stab
                simuliert. Über die Regler lassen sich die Länge des Stabes, die
                Materialeigenschaften, die Temperaturverteilung zu Beginn der
                Beobachtung und die Randbedingungen steuern.
                """
            )
        ],
        "plot": diffusion,
        "questions": [
            (
                "(1) Erkundung der Graphik",
                r"""
                1. Welche physikalische Größe ist dargestellt?
                2. Beschreiben Sie kurz das zeitabhängige Lösungsverhalten.
                3. Welche Auswirkungen hat eine Verlängerung oder Verkürzung des
                   Stabs auf das Lösungsverhalten?
                4. Was verändert sich bei einer Anfangsbedingung mit der dritten
                   Eigenform anstelle der ersten?
                5. Welchen Einfluss hat die Verwendung inhomogener
                   Randbedingungen? 
                """
            ),
            (
                "(2) Fragen zum tieferen Verständnis",
                r"""
                Eine Lösung der Wärmleitungsgleichung $u_{,t}= a u_{,xx}$ mit
                homogenen Dirichlet-Randbedingungen ist $u(t,x)= e^{-a(k
                \frac{\pi}{L})^2 t} sin(\frac{\pi}{L}k x)$.

                1. Woran ist in der Formel zu erkennen, dass die höheren
                   Eigenformen schneller abklingen?
                2. Woran ist in der Formel zu erkennen, dass sich die
                    Temperaturverteilung bei längeren Stäben schneller
                    ausgleicht? 
                3. Welchen Einfluss haben inhomogene Randbedingungen auf die
                   analytische Lösung?
                """
            ),
            (
                "(3) Fragen zur eigenen Bearbeitung",
                r"""
                Lösen Sie ein Wärmeleitungsproblem mit inhomogenen
                Dirichlet-Randbedingungen. Vergleichen Sie die genutzte
                Superposition mit der statischen Lösungen aus dem Plot.
                """
            )
        ]
    }
}


if __name__ == "__main__":
    diffusion()