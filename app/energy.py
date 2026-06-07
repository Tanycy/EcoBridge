energy_scores = {
    "gemini-flash": 1,
    "gpt-4o": 10
}

def calculate_energy(model):

    return energy_scores.get(model, 0)