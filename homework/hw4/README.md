# HW4: Seznámení se se zvolenou pokročilou iterativní metodou na problému batohu

## Záměna základu exponenciály uvnitř shouldAcceptByProbability

Vyzkoušeno na základech 2 a 10.
S větším (10) exponentem byla chybovost vyšší. 

Důvodem je, že s rostoucím základem je větší chybě (tedy větší hodnotě exponentu) nižší pravděpodobnost splnění následující podmínky: 

    random.random() < (2 ** (- optimalCriteriaDistance / self.currentTemp))
    random.random() < (10 ** (- optimalCriteriaDistance / self.currentTemp))
    
Díky tomu docházelo méně častěji k přijetí zhoršení stavu a tedy k uváznutí v lokálním optimu.